from dash import Dash, html, dcc
import plotly.express as px

from data import countries_df, totals_df
from builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    size_max=40,
    template="plotly_dark",
    hover_name="Country_Region",
    title="Confirmed Case by Country",
    hover_data={
        "Confirmed": ":,",
        "Recovered": ":,",
        "Deaths": ":,",
        "Country_Region": False,
    },
    color="Confirmed",
    color_continuous_scale=px.colors.sequential.Oryel,
    locations="Country_Region",
    locationmode="country names",
)

bubble_map.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    coloraxis_colorbar=dict(xanchor="left", x=0),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    geo={
        "bgcolor": "rgba(0,0,0,0)",
        "landcolor": "rgba(0,0,0,0.4)",
        "lakecolor": "rgba(0,0,0,0)",
    },
)

bubble_map.update_traces(
    fillcolor="rgba(0,0,0,0)",
)


bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    hover_data={"count": ":,"},
    labels={"condition": "Condition", "count": "Count", "color": "Condition"},
)

bars_graph.update_traces(marker_color=["#54a0ff", "#ee5253", "#1dd1a1"])

bars_graph.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "rgb(38, 50, 56)",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            className="main-title",
            children=[html.H1("COVID-19 Dashboard")],
        ),
        html.Div(
            className="container-1",
            children=[
                html.Div(children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            className="container-2",
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
