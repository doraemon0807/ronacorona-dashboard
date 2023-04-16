from dash import html


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                className="table-head",
                children=[
                    html.Tr(
                        className="table-head__row",
                        children=[
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ],
                    )
                ],
            ),
            html.Tbody(
                className="table-body",
                children=[
                    html.Tr(
                        className="table-body__row",
                        children=[html.Td(column_value) for column_value in value],
                    )
                    for value in df.values
                ],
            ),
        ]
    )
