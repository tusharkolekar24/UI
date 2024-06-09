import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('update.csv')

year_list = list(df['Year'].unique())

font_awesome1 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
font_awesome2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/regular.min.css'
font_awesome3 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'

meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}]
external_stylesheets = [font_awesome1, font_awesome2, font_awesome3, meta_tags] #['assets/s1.css','assets/style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    # 1st Row Details
    html.Div([
    html.Div([
        html.H5('Movie Data Analyser', className='title_text')
    ],className="title_container twelve columns")
    ],className='row flex_display'),

    #2nd Row Detail
    html.Div([
    #1nd Column Detail
    html.Div([
    html.P(dcc.Markdown(
                    """
                    **Below table** shows gross sales **values** for each genre category and percentage of share for 
                    each genre category in **each year**.
                    """
                ),style={'line-height': '1', 'font-size': '17px',
                      'text-align': 'justify', 'margin-bottom': '20px'}),

    html.Div(id='calculations'),

    dcc.Graph(id='bar_graph',
                      config={'displayModeBar': 'hover'},
                      className='bar_graph_border')    

    ],className='create_container six columns',style={'margin-top':'10px','margin-bottom':'10px','width':'58%'}),


    #2rd Column Detail
    html.Div([
    
    html.Div([
            html.P('Year:', className='fix_label', style={'color': 'black',
                                                          # 'margin-top': '15px'
                                                          }),
            dcc.Slider(id='select_years',
                        min=year_list[0],
                        max=year_list[-1],
                        value=year_list[6],
                        step=1,
                        included=False,
                        updatemode='drag',
                        tooltip={'always_visible': True},
                        marks={str(yrs): str(yrs) for yrs in range(year_list[0], year_list[-1], 2)},
                        className='slider_component'),
    
    ],className='container_slider'),

    dcc.Graph(id='pie_graph',
            config={'displayModeBar': 'hover'},
            className='pie_graph_border'),

    html.P(dcc.Markdown(
                """
                Percentage **share** of each **rated category** in each **year**.
                """
            ), style={'line-height': '1', 'font-size': '17px',
                      'text-align': 'justify', 'margin-top': '30px'}),

    html.Div([
                html.Div(id='text1',
                         className='text_container'),
                html.Div(id='text2',
                         className='text_container1'),
                html.Div(id='text3',
                         className='text_container1'),
                html.Div(id='text4',
                         className='text_container1'),
                html.Div(id='text5',
                         className='text_container2')
            ], className='container_text_border')

    ],className='create_container six columns',style={'margin-top':'10px','margin-bottom':'10px','margin-left':'10px','width':'60%'},
    )

    ],className='row flex_display')



], className='mainContainer',style={"display": "flex","flex-direction": "column"})

@app.callback(Output('calculations', 'children'),
              [Input('select_years', 'value')])
def display_data(select_years):
    df1 = df.groupby(['genre', 'Year'])['total_gross'].sum().reset_index()
    df2 = df1[(df1['genre'] == 'Musical') & (df1['Year'] == select_years)]['total_gross'].sum()
    df3 = df1['total_gross'].sum()
    df4 = (df2 / df3) * 100

    df5 = df1[(df1['genre'] == 'Comedy') & (df1['Year'] == select_years)]['total_gross'].sum()
    df6 = (df5 / df3) * 100

    df7 = df1[(df1['genre'] == 'Adventure') & (df1['Year'] == select_years)]['total_gross'].sum()
    df8 = (df7 / df3) * 100

    df9 = df1[(df1['genre'] == 'Romantic Comedy') & (df1['Year'] == select_years)]['total_gross'].sum()
    df10 = (df9 / df3) * 100

    df11 = df1[(df1['genre'] == 'Western') & (df1['Year'] == select_years)]['total_gross'].sum()
    df12 = (df11 / df3) * 100

    df13 = df1[(df1['genre'] == 'Action') & (df1['Year'] == select_years)]['total_gross'].sum()
    df14 = (df13 / df3) * 100

    df15 = df1[(df1['genre'] == 'Drama') & (df1['Year'] == select_years)]['total_gross'].sum()
    df16 = (df15 / df3) * 100

    df17 = df1[(df1['genre'] == 'Thriller/Suspense') & (df1['Year'] == select_years)]['total_gross'].sum()
    df18 = (df17 / df3) * 100

    df19 = df1[(df1['genre'] == 'Black Comedy') & (df1['Year'] == select_years)]['total_gross'].sum()
    df20 = (df19 / df3) * 100

    df21 = df1[(df1['genre'] == 'Documentary') & (df1['Year'] == select_years)]['total_gross'].sum()
    df22 = (df21 / df3) * 100

    df23 = df1[(df1['genre'] == 'Horror') & (df1['Year'] == select_years)]['total_gross'].sum()
    df24 = (df23 / df3) * 100

    df25 = df1[(df1['genre'] == 'Concert/Performance') & (df1['Year'] == select_years)]['total_gross'].sum()
    df26 = (df25 / df3) * 100

    return [
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th('Genre'),
                    html.Th('Symbol'),
                    html.Th('Gross Sales ($):' + ' ' + '{0:.0f}'.format(select_years)),
                    html.Th('% Share:' + ' ' + '{0:.0f}'.format(select_years))
                ], className='header_hover')
            ]),
            html.Tbody([
                html.Tr([
                    html.Td('Musical'),
                    html.Td(html.I(className='fa-solid fa-music', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df2)),
                    html.Td('{0:,.2f}%'.format(df4))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Comedy'),
                    html.Td(html.I(className='fa-solid fa-masks-theater', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df5)),
                    html.Td('{0:,.2f}%'.format(df6))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Adventure'),
                    html.Td(html.I(className='fa-brands fa-space-awesome', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df7)),
                    html.Td('{0:,.2f}%'.format(df8))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Romantic Comedy'),
                    html.Td(html.I(className='fa-solid fa-masks-theater', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df9)),
                    html.Td('{0:,.2f}%'.format(df10))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Western'),
                    html.Td(html.I(className='fa-solid fa-hat-cowboy', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df11)),
                    html.Td('{0:,.2f}%'.format(df12))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Action'),
                    html.Td(html.I(className='fa-solid fa-person', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df13)),
                    html.Td('{0:,.2f}%'.format(df14))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Drama'),
                    html.Td(html.I(className='fa-solid fa-house-chimney-crack', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df15)),
                    html.Td('{0:,.2f}%'.format(df16))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Thriller/Suspense'),
                    html.Td(html.I(className='fa-solid fa-skull', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df17)),
                    html.Td('{0:,.2f}%'.format(df18))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Black Comedy'),
                    html.Td(html.I(className='fa-solid fa-masks-theater', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df19)),
                    html.Td('{0:,.2f}%'.format(df20))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Documentary'),
                    html.Td(html.I(className='fa-solid fa-book', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df21)),
                    html.Td('{0:,.2f}%'.format(df22))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Horror'),
                    html.Td(html.I(className='fa-solid fa-skull', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df23)),
                    html.Td('{0:,.2f}%'.format(df24))
                ], className='hover_only_row'),
                html.Tr([
                    html.Td('Concert/Performance'),
                    html.Td(html.I(className='fa-solid fa-user', style={'font-size': '150%'})),
                    html.Td('{0:,.0f}'.format(df25)),
                    html.Td('{0:,.2f}%'.format(df26))
                ], className='hover_only_row'),
            ])
        ], className='table_style')
    ]

@app.callback(Output('bar_graph', 'figure'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    df1 = df.groupby(['genre', 'Year'])['total_gross'].sum().reset_index()
    df2 = df1[df1['Year'] == select_years]

    return {
        'data': [
            go.Bar(
                x=df2['genre'],
                y=df2['total_gross'],
                text=df2['total_gross'],
                texttemplate='%{text:,.2s}',
                textposition='outside',
                marker=dict(color='#38D56F'),
                textfont=dict(
                    family="sans-serif",
                    size=12,
                    color='black'),

                hoverinfo='text',
                hovertext=
                '<b>Year</b>: ' + df2['Year'].astype(str) + '<br>' +
                '<b>Gross Sales</b>: $' + [f'{x:,.0f}' for x in df2['total_gross']] + '<br>'

            )],

        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Gross Sales ($) in' + ' ' + str((select_years)),

                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'black',
                'size': 17},
            hovermode='closest',
            margin=dict(t=30, r=70),
            xaxis=dict(showline=True,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='black')

                       ),

            yaxis=dict(title='<b>Gross Sales ($)</b>',
                       visible=True,
                       color='black',
                       showline=False,
                       showgrid=True,
                       )
        )

    }

@app.callback(Output('pie_graph', 'figure'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    df1 = df.groupby(['mpaa_rating', 'Year'])['total_gross'].sum().reset_index()
    df2 = df1[df1['Year'] == select_years]

    return {
        'data': [go.Pie(
            labels=df2['mpaa_rating'],
            values=df2['total_gross'],
            hoverinfo='label+value+percent',
            textinfo='label+value',
            textfont=dict(size=13),
            texttemplate='%{label}: %{value:,.0f}<br>(%{percent})',
            textposition='auto',
            rotation=160
        )],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Sales by rating in' + ' ' + str(select_years),

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'rgb(50, 50, 50)',
                'size': 15},
            hovermode='x',
            legend={
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'xanchor': 'center',
                'yanchor': 'bottom',
                'x': 0.5,
                'y': -0.2
            }

        )
    }

@app.callback(Output('text1', 'children'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    g = df[(df['mpaa_rating'] == 'G') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g = df[(df['mpaa_rating'] == 'PG') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g13 = df[(df['mpaa_rating'] == 'PG-13') & (df['Year'] == select_years)]['mpaa_rating'].count()
    r = df[(df['mpaa_rating'] == 'R') & (df['Year'] == select_years)]['mpaa_rating'].count()
    not_rated = df[(df['mpaa_rating'] == 'Not Rated') & (df['Year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + p_g + p_g13 + r + not_rated
    g_per = (g / total_rated) * 100

    return [
        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td('G:', className='style1'),
                    html.Td('{0:.2f}%'.format(g_per) + ' ' + 'share in' + ' ' + str(select_years),
                            className='style2')
                ])
            ])
        ], className='box_style')
    ]

@app.callback(Output('text2', 'children'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    g = df[(df['mpaa_rating'] == 'G') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g = df[(df['mpaa_rating'] == 'PG') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g13 = df[(df['mpaa_rating'] == 'PG-13') & (df['Year'] == select_years)]['mpaa_rating'].count()
    r = df[(df['mpaa_rating'] == 'R') & (df['Year'] == select_years)]['mpaa_rating'].count()
    not_rated = df[(df['mpaa_rating'] == 'Not Rated') & (df['Year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + p_g + p_g13 + r + not_rated
    p_g_per = (p_g / total_rated) * 100

    return [
        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td('PG:', className='style1'),
                    html.Td('{0:.2f}%'.format(p_g_per) + ' ' + 'share in' + ' ' + str(select_years),
                            className='style2')
                ])
            ])
        ], className='box_style')
    ]


@app.callback(Output('text3', 'children'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    g = df[(df['mpaa_rating'] == 'G') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g = df[(df['mpaa_rating'] == 'PG') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g13 = df[(df['mpaa_rating'] == 'PG-13') & (df['Year'] == select_years)]['mpaa_rating'].count()
    r = df[(df['mpaa_rating'] == 'R') & (df['Year'] == select_years)]['mpaa_rating'].count()
    not_rated = df[(df['mpaa_rating'] == 'Not Rated') & (df['Year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + p_g + p_g13 + r + not_rated
    p_g13_per = (p_g13 / total_rated) * 100

    return [
        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td('PG-13:', className='style1'),
                    html.Td('{0:.2f}%'.format(p_g13_per) + ' ' + 'share in' + ' ' + str(select_years),
                            className='style2')
                ])
            ])
        ], className='box_style')
    ]


@app.callback(Output('text4', 'children'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    g = df[(df['mpaa_rating'] == 'G') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g = df[(df['mpaa_rating'] == 'PG') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g13 = df[(df['mpaa_rating'] == 'PG-13') & (df['Year'] == select_years)]['mpaa_rating'].count()
    r = df[(df['mpaa_rating'] == 'R') & (df['Year'] == select_years)]['mpaa_rating'].count()
    not_rated = df[(df['mpaa_rating'] == 'Not Rated') & (df['Year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + p_g + p_g13 + r + not_rated
    r_per = (r / total_rated) * 100

    return [
        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td('R:', className='style1'),
                    html.Td('{0:.2f}%'.format(r_per) + ' ' + 'share in' + ' ' + str(select_years),
                            className='style2')
                ])
            ])
        ], className='box_style')
    ]


@app.callback(Output('text5', 'children'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    g = df[(df['mpaa_rating'] == 'G') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g = df[(df['mpaa_rating'] == 'PG') & (df['Year'] == select_years)]['mpaa_rating'].count()
    p_g13 = df[(df['mpaa_rating'] == 'PG-13') & (df['Year'] == select_years)]['mpaa_rating'].count()
    r = df[(df['mpaa_rating'] == 'R') & (df['Year'] == select_years)]['mpaa_rating'].count()
    not_rated = df[(df['mpaa_rating'] == 'Not Rated') & (df['Year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + p_g + p_g13 + r + not_rated
    not_rated_per = (not_rated / total_rated) * 100

    return [
        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td('Not Rated:', className='style1'),
                    html.Td('{0:.2f}%'.format(not_rated_per) + ' ' + 'share in' + ' ' + str(select_years),
                            className='style2')
                ])
            ])
        ], className='box_style')
    ]

if __name__ == '__main__':
    app.run_server(debug=True)