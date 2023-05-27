

import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Downloads\Untitled spreadsheet - Sheet1 (3).csv")
df
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Lakshadweep','Haryana'], multi=True,
                  options=[{'label': x, 'value': x} for x in
                          df.State.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,)
    ])
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.State.isin(country_chosen)]
    fig = px.bar(data_frame=dff, x='State', y='Population', color='State',
                  # custom_data=['country', 'continent', 'lifeExp', 'pop']
                  )
    fig.update_traces(mode='lines+markers')
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.Year == 1952]
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='Ratio', names='State',
                      title='Population for 1952')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.State.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.State == hov_year]
        fig2 = px.pie(data_frame=dff2, values='Ratio', names='State', title=f'Population for: {hov_year}')
        return fig2


if __name__ == '__main__':
    app.run_server()    






# import dash  # use Dash version 1.16.0 or higher for this app to work
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Output, Input
# import plotly.express as px

# df = px.data.gapminder()
# df
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True,
#                   options=[{'label': x, 'value': x} for x in
#                           df.country.unique()]),
#     html.Div([
#         dcc.Graph(id='pie-graph', figure={}),
#         dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,)
#     ])
# ])

# @app.callback(
#     Output(component_id='my-graph', component_property='figure'),
#     Input(component_id='dpdn2', component_property='value'),
# )
# def update_graph(country_chosen):
#     dff = df[df.country.isin(country_chosen)]
#     fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country',
#                   custom_data=['country', 'continent', 'lifeExp', 'pop'])
#     fig.update_traces(mode='lines+markers')
#     return fig


# # Dash version 1.16.0 or higher
# @app.callback(
#     Output(component_id='pie-graph', component_property='figure'),
#     Input(component_id='my-graph', component_property='hoverData'),
#     Input(component_id='my-graph', component_property='clickData'),
#     Input(component_id='my-graph', component_property='selectedData'),
#     Input(component_id='dpdn2', component_property='value')
# )
# def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
#     if hov_data is None:
#         dff2 = df[df.country.isin(country_chosen)]
#         dff2 = dff2[dff2.Year == 1952]
#         print(dff2)
#         fig2 = px.pie(data_frame=dff2, values='Ratio', names='State',
#                       title='Population for 1952')
#         return fig2
#     else:
#         print(f'hover data: {hov_data}')
#         # print(hov_data['points'][0]['customdata'][0])
#         # print(f'click data: {clk_data}')
#         # print(f'selected data: {slct_data}')
#         dff2 = df[df.State.isin(country_chosen)]
#         hov_year = hov_data['points'][0]['x']
#         dff2 = dff2[dff2.State == hov_year]
#         fig2 = px.pie(data_frame=dff2, values='Ratio', names='State', title=f'Population for: {hov_year}')
#         return fig2


# if __name__ == '__main__':
#     app.run_server()    




# import dash  # use Dash version 1.16.0 or higher for this app to work
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Output, Input
# import plotly.express as px

# df = px.data.gapminder()
# df
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True,
#                   options=[{'label': x, 'value': x} for x in
#                           df.country.unique()]),
#     html.Div([
#         dcc.Graph(id='pie-graph', figure={}),
#         dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,)
#     ])
# ])

# @app.callback(
#     Output(component_id='my-graph', component_property='figure'),
#     Input(component_id='dpdn2', component_property='value'),
# )
# def update_graph(country_chosen):
#     dff = df[df.country.isin(country_chosen)]
#     fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country',
#                   custom_data=['country', 'continent', 'lifeExp', 'pop'])
#     fig.update_traces(mode='lines+markers')
#     return fig


# # Dash version 1.16.0 or higher
# @app.callback(
#     Output(component_id='pie-graph', component_property='figure'),
#     Input(component_id='my-graph', component_property='hoverData'),
#     Input(component_id='my-graph', component_property='clickData'),
#     Input(component_id='my-graph', component_property='selectedData'),
#     Input(component_id='dpdn2', component_property='value')
# )
# def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
#     if hov_data is None:
#         dff2 = df[df.country.isin(country_chosen)]
#         dff2 = dff2[dff2.Year == 1952]
#         print(dff2)
#         fig2 = px.pie(data_frame=dff2, values='Ratio', names='State',
#                       title='Population for 1952')
#         return fig2
#     else:
#         print(f'hover data: {hov_data}')
#         # print(hov_data['points'][0]['customdata'][0])
#         # print(f'click data: {clk_data}')
#         # print(f'selected data: {slct_data}')
#         dff2 = df[df.State.isin(country_chosen)]
#         hov_year = hov_data['points'][0]['x']
#         dff2 = dff2[dff2.State == hov_year]
#         fig2 = px.pie(data_frame=dff2, values='Ratio', names='State', title=f'Population for: {hov_year}')
#         return fig2


# if __name__ == '__main__':
#     app.run_server()    
    



