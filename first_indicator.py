
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello from Flask!'



import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css", dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],suppress_callback_exceptions=True, title="Food & Nutrition Dashboard")


# importing all the sheets
province = pd.read_excel("./data/Children_nutrition_status_ZDHS.xlsx", sheet_name = 'province')
national_by_gender = pd.read_excel("./data/Children_nutrition_status_ZDHS.xlsx", sheet_name = 'national_gender')
residence = pd.read_excel("./data/Children_nutrition_status_ZDHS.xlsx", sheet_name = 'national_residence')



# nav header
dashboard_header = html.Div(
    id="header",
    children=[
        dbc.NavbarSimple(
            children=[
                # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
                html.Div(
                    children=[
                        html.H3(
                            id="header_text",
                            children="FOOD & NUTRITION COUNCIL DASHBOARD",
                            style={'color': '#ffffff', 'display': 'inline-block', 'textAlign': 'center'}
                        )
                    ]
                ),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("OPTIONS", header=True),
                        dbc.DropdownMenuItem("Change Password", href="#"),
                        dbc.DropdownMenuItem("Settings", href="#"),
                        dbc.DropdownMenuItem("FNC Logout", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Options",
                ),
            ],
            # brand="FOOD & NUTRITION COUNCIL DASHBOARD",
            brand_href="#",
            color="dark",
            dark=True,
            sticky="top",
            className="font-weight-bold"
        )],
)


# my tabs
def my_tabs():
    return (
        html.Div(
            id="my_tab",
            children=[
                dbc.Tabs(
                    [
                        dbc.Tab(label="Children Nutrition Status", tab_id="tab_1"),
                        dbc.Tab(label="Food Insecurity Score", tab_id="tab_2"),
                        dbc.Tab(label="Livestock Ownership", tab_id="tab_3"),
                    ],
                    className="",
                    id="tabs",
                    active_tab="tab_1",
                ),
                html.Div(id="tab-content", className="p-4"),
            ]
        )
    )


###########################################

# first tab
def first_tab():
    return (dbc.CardBody(
        children=[
            # first row with dropdown
            dbc.Row(
                className="top_outer_second_row",
                children=[
                    #column with dropdown lists
                    dbc.Col(
                        className="col-md-12",
                        children=[
                            html.Div(
                                className="dropdown_single_row",
                                children=[
                                    # row for the dropdowns
                                    dbc.Row([
                                        # dropdown 1
                                        dbc.Col(
                                            children=[
                                                dcc.Dropdown(
                                                    id='residence_mulnutrition_type',
                                                    multi=False,
                                                    clearable=False,
                                                    value="Wasting",
                                                    placeholder='mulnutrition type',
                                                    options=[{'label': i, 'value': i} for i in
                                                             list(residence.mulnutrition_type.unique())],

                                                ),
                                            ],
                                            id="mydropdown",
                                            className="col-md-3",
                                        ),

                                        # dropdown 2
                                        dbc.Col(
                                            children=[

                                                dcc.Dropdown(
                                                    id='residence_year',
                                                    multi=False,
                                                    clearable=False,
                                                    value=1994,
                                                    placeholder='Select Year',
                                                    options=[{'label': i, 'value': i} for i in list(residence.year.unique())],

                                                )
                                            ],
                                            id="mydropdown",
                                            className="col-md-3"
                                        ),
                                    ],
                                        justify="center",
                                    ),

                                ],
                            )
                        ]
                    )]),


            #############################
            #second row is here
            dbc.Row(
                id="top_outer_row",
                children=[
                    # first column with consumption by meals
                    dbc.Col(
                        className="col-md-6",
                        children=[
                            html.Div(
                                className="with_padding_top",
                                children=[
                                    dbc.Col(dcc.Graph(id='residence_bar_graph'),)
                                ],
                            )
                        ],
                       
                    ),
                    # second column with food consumption score
                    dbc.Col(
                        className="col-md-6",
                        children=[
                            html.Div(
                                className="with_padding_top",
                                children=[
                                    dbc.Col(dcc.Graph(id='residence_pie_chart'),)
                                ],
                            )
                        ],
                       
                    ),

                ]
            ),

            html.Hr(),

            ################################
            #third row
            dbc.Row(
                className="top_outer_second_row",
                children=[
                    #column with dropdown lists
                    dbc.Col(
                        className="col-md-12",
                        children=[
                            html.Div(
                                className="dropdown_single_row",
                                children=[
                                    # row for the dropdowns
                                    dbc.Row([
                                        # dropdown 1
                                        dbc.Col(
                                            children=[
                                                dcc.Dropdown(
                                                    id='gender_mulnutrition_type',
                                                    multi=False,
                                                    clearable=False,
                                                    value="Wasting",
                                                    placeholder='mulnutrition type',
                                                    options=[{'label': i, 'value': i} for i in
                                                             list(national_by_gender.mulnutrition_type.unique())],

                                                ),
                                            ],
                                            id="mydropdown",
                                            className="col-md-3",
                                        ),

                                        # dropdown 2
                                        dbc.Col(
                                            children=[

                                                dcc.Dropdown(
                                                    id='gender_year',
                                                    multi=False,
                                                    clearable=False,
                                                    value=1994,
                                                    placeholder='Select Year',
                                                    options=[{'label': i, 'value': i} for i in list(national_by_gender.year.unique())],

                                                )
                                            ],
                                            id="mydropdown",
                                            className="col-md-3"
                                        ),
                                    ],
                                        justify="center",
                                    ),

                                ],
                            )
                        ]
                    )]),


            #############################
            #fouth row is here
            dbc.Row(
                id="top_outer_row",
                children=[
                    # first column with consumption by meals
                    dbc.Col(
                        className="col-md-6",
                        children=[
                            html.Div(
                                className="with_padding_top",
                                children=[
                                    dbc.Col(dcc.Graph(id='national_by_gender_bar_graph'),)
                                ],
                            )
                        ],
                       
                    ),
                    # second column with food consumption score
                    dbc.Col(
                        className="col-md-6",
                        children=[
                            html.Div(
                                className="with_padding_top",
                                children=[
                                    dbc.Col(dcc.Graph(id='national_by_gender_pie_chart'),)
                                ],
                            )
                        ],
                        
                    ),

                ]
            ),

            html.Hr(),
            #########
            #Provincial and national Trends
            dbc.Row(
                className="top_outer_second_row",
                children=[
                    #column with dropdown lists
                    dbc.Col(
                        className="col-md-12",
                        children=[
                            html.Div(
                                className="dropdown_single_row",
                                children=[
                                    # row for the dropdowns
                                    dbc.Row([
                                        # dropdown 1
                                        dbc.Col(
                                            children=[
                                                dcc.Dropdown(
                                                    id='province_nutrition',
                                                    multi=False,
                                                    clearable=True,
                                                    value="Masvingo",
                                                    placeholder='Select Province',
                                                    options=[{'label': i, 'value': i} for i in
                                                             list(province.province.unique())],

                                                ),
                                            ],
                                            id="mydropdown",
                                            className="col-md-3",
                                        ),

                                    ],
                                        justify="center",
                                    ),
                                    #################
                                    #Second Row
                                    dbc.Row([
                                        # dropdown 1
                                        dbc.Col(
                                                className="col-md-6",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            # row for the dropdowns

                                                            # the graph
                                                            dbc.Col(dcc.Graph(id='national_nurtition_Trends')),

                                                        ]
                                                    )
                                                ]
                                            ),

                                        # dropdown 2
                                        dbc.Col(
                                                className="col-md-6",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            # row for the dropdowns

                                                            # the graph
                                                            # html.Div(id='national_nurtition_Trends_text'),
                                                            dcc.Markdown(id='national_nurtition_Trends_text')

                                                        ]
                                                    )
                                                ]
                                            ),
                                    ],
                                        justify="center",
                                    ),

                                ],
                            )
                        ]
                    )]),

            ##########
            html.Hr(),
            #####################################
            #row

            dbc.Row(
                className="top_outer_second_row",
                children=[
                    #column with dropdown lists
                    dbc.Col(
                        className="col-md-12",
                        children=[
                            html.Div(
                                className="dropdown_single_row",
                                children=[
                                    # row for the dropdowns
                                    dbc.Row([
                                        # dropdown 1
                                        dbc.Col(
                                            children=[
                                                dcc.Dropdown(
                                                    id='province_mulnutrition_type',
                                                    multi=False,
                                                    clearable=False,
                                                    value="Wasting",
                                                    placeholder='mulnutrition type',
                                                    options=[{'label': i, 'value': i} for i in
                                                             list(province.mulnutrition_type.unique())],

                                                ),
                                            ],
                                            id="mydropdown",
                                            className="col-md-3",
                                        ),

                                        # dropdown 2
                                        dbc.Col(
                                            children=[

                                                dcc.Dropdown(
                                                    id='province_year',
                                                    multi=False,
                                                    clearable=False,
                                                    value=1994,
                                                    placeholder='Select Year',
                                                    options=[{'label': i, 'value': i} for i in list(province.year.unique())],

                                                )
                                            ],
                                            id="mydropdown",
                                            className="col-md-3"
                                        ),
                                    ],
                                        justify="center",
                                    ),

                                ],
                            )
                        ]
                    )]),


            #############################
            #second row is here
            dbc.Row(
                id="top_outer_row",
                children=[
                    # first column with consumption by meals
                    dbc.Col(
                        className="col-md-6",
                        children=[
                            html.Div(
                                className="with_padding_top",
                                children=[
                                    dbc.Col(dcc.Graph(id='mulnutrition_by_province'),)
                                ],
                            )
                        ],
                        
                    ),
                    # second column with food consumption score
                    dbc.Col(
                            className="col-md-6",
                            children=[
                                html.Div(
                                    children=[
                                        # row for the dropdowns

                                        # the graph
                                        # html.Div(id='national_nurtition_Trends_text'),
                                        dcc.Markdown(id='mulnutrition_by_province_summary')

                                    ]
                                )
                            ]
                        ),

                ]
            ),

        ]
    )
    )



# app layout
app.layout = html.Div(
    children=[
        dashboard_header,
        my_tabs(),
    ],
)


@app.callback(
    Output('residence_bar_graph', 'figure'),
    Input('residence_mulnutrition_type', 'value')
)
def national_residence_bar_graph(residence_mulnutrition_type):
    if residence_mulnutrition_type == None:
        residence_mulnutrition_type = 'Wasting'
    residence['mulnutrition_type'] = residence['mulnutrition_type'].str.strip()
    residence['residence'] = residence['residence'].str.strip()
    df = residence[residence['mulnutrition_type']==residence_mulnutrition_type] 
    fig = px.bar(df, x = 'year', y = 'prevalence_rate', color = 'residence',
                 text=df['prevalence_rate'].apply(lambda x: '{0:1.0f}%'.format(x)),
               color_discrete_map={ 'Rural': 'rgb(239, 85, 59)', 'Urban':'rgb(99, 110, 250)'},
                 template= 'simple_white'
                )

    fig.update_layout(
        title = {
            'text' : f"<b>Urban and Rural {residence_mulnutrition_type} Analysis</b>",
            'y' : 0.93,
            'x': 0.43,
            'xanchor': 'center',
            'yanchor': 'top'
                },
        titlefont={'family': 'Oswald',
                        'color': 'rgb(0,0,0)',
                        'size': 16},


        xaxis=  {
            'title': '<b>Year</b>',
            'tickangle': 35,
            'color':'rgb(0, 0, 0)',
            'showticklabels': True,
            'type': 'category',
            'fixedrange': True,
    #         'showline':True,
            'linecolor':'rgb(0, 0, 0)',
            'showgrid':False,
            'linewidth':1.5,
        'ticks':'outside',
        'tickfont':dict(
            family='Arial',
            size=12,
            color='rgb(0, 0, 0)'
            )
                },

        yaxis= {
            'title': '<b>Prevalence rate</b>',
            'color':'rgb(0, 0, 0)',
            'fixedrange': True,
            'linecolor':'rgb(0, 0, 0)',
            'showgrid':True,
            'linewidth':1.5,
            'ticks':'outside',
            'tickfont':dict(
                family='Arial',
                size=12,
                color='rgb(0, 0, 0)'
                )        
                },

        legend=dict(
            title = '',
            bgcolor='rgb(255,255,255)',
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color='rgb(0, 0, 0)'
                )
            ),
        title_font_color = 'rgb(0, 0, 0)',

        barmode = 'group',
        autosize = True,
        width = 700,
        height = 450)
    fig.update_traces(
            hovertemplate='Year: %{x} <br>prevalence: %{y}',
            textfont=dict( color="White" )
    )


    return fig


############################################################
# household_graph


@app.callback(
    Output('residence_pie_chart', 'figure'),
    Input('residence_mulnutrition_type', 'value'),
    Input('residence_year', 'value')
)
def residence_pie_chart( residence_mulnutrition_type, residence_year):
    if residence_year < 2010:
        residence_year = 2010
    if residence_mulnutrition_type == None:
        residence_mulnutrition_type = 'Wasting'
    residence['mulnutrition_type'] = residence['mulnutrition_type'].str.strip()
    residence['residence'] = residence['residence'].str.strip()
    df = residence[residence['mulnutrition_type']==residence_mulnutrition_type]
    df1 = df[df['year']== residence_year]
    fig = px.pie(df1, values='prevalence_rate', names='residence', color='residence',
                color_discrete_map={ 'Rural': 'rgb(239, 85, 59)', 'Urban':'rgb(99, 110, 250)'}
                     )

    fig.update_layout(
        title={
                'text' : f"<b>{str(residence_year)} Urban and Rural {residence_mulnutrition_type} Prevalence Rate Analysis.</b>",
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
        titlefont={'family': 'Oswald',
                        'color': 'rgb(0,0,0)',
                        'size': 16},

         # hovermode='x',
        
        autosize = True,
        width = 700,
        height = 450,
 
        legend=dict(
                     bgcolor='rgba(255, 255, 255, 0)',
                     traceorder="normal",
                     font=dict(
                          family="sans-serif",
                          size=12,
                          color='#000000')),

                     uniformtext_minsize=12,
                     uniformtext_mode='hide'
                 )
    fig.update_traces(
            # hovertemplate='Year: %{x} <br>prevalence: %{y}',
            textfont_color="white",
            )
    return fig

#By Gender Graphs
@app.callback(
    Output('national_by_gender_bar_graph', 'figure'),
    Input('gender_mulnutrition_type', 'value'),
)
def national_by_gender_bar_graph(gender_mulnutrition_type):
    if gender_mulnutrition_type == None:
        gender_mulnutrition_type = 'Wasting'
    national_by_gender['mulnutrition_type'] = national_by_gender['mulnutrition_type'].str.strip()
    national_by_gender['gender'] = national_by_gender['gender'].str.strip()
    df = national_by_gender[national_by_gender['mulnutrition_type']==gender_mulnutrition_type.strip()]
    fig = px.line(df, x = 'year', y = 'prevalence_rate', color = 'gender',
                 text=df['prevalence_rate'].apply(lambda x: '{0:1.0f}%'.format(x)),
                 template= 'simple_white',
                 color_discrete_map={ 
                    'female': 'rgb(239, 85, 59)', 
                    'male':'rgb(99, 110, 250)'
                    }

                )

    fig.update_layout(
        title = {
            'text' : f"<b>Urban and Rural {gender_mulnutrition_type} Trends</b>",
            'y' : 0.93,
            'x': 0.43,
            'xanchor': 'center',
            'yanchor': 'top'
                },
        titlefont={'family': 'Oswald',
                        'color': 'rgb(0,0,0)',
                        'size': 16},


        xaxis=  {
            'title': '<b>Year</b>',
            'tickangle': 35,
            'color':'rgb(0,0,0)',
            'showticklabels': True,
            'type': 'category',
            'fixedrange': True,
    #         'showline':True,
            'color':'rgb(0,0,0)',
            'linewidth':1.5,
        'ticks':'outside',
        'tickfont':dict(
            family='Arial',
            size=12,
            color='rgb(0,0,0)',
            )
                },

        yaxis= {
            'title': '<b>Prevalence rate</b>',
            'color':'rgb(0,0,0)',
            'fixedrange': True,
            'linecolor':'rgb(0,0,0)',
            'showgrid':True,
            'linewidth':1.5,
            'ticks':'outside',
            'tickfont':dict(
                family='Arial',
                size=12,
                color='rgb(0,0,0)'
                )        
                },

        legend=dict(
            title = '',
            bgcolor='rgba(255, 255, 255, 0)',
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color='rgb(0,0,0)'
                )
            ),
        title_font_color = 'rgb(0,0,0)',

        barmode = 'group',
        autosize = True,
        width = 700,
        height = 450
        )
    #update hover
    fig.update_traces(
            hovertemplate='Year: %{x} <br>prevalence: %{y}',
            textfont=dict( color="White")
            )

    return fig

#pie chart
@app.callback(
    Output('national_by_gender_pie_chart', 'figure'),
    Input('gender_mulnutrition_type', 'value'),
    Input('gender_year', 'value')
)
def national_by_gender_pie_chart( gender_mulnutrition_type, gender_year):
    if gender_year == None:
        gender_year = 1994
    if gender_mulnutrition_type == None:
        gender_mulnutrition_type = 'Wasting'
    national_by_gender['mulnutrition_type'] = national_by_gender['mulnutrition_type'].str.strip()
    national_by_gender['gender'] = national_by_gender['gender'].str.strip()
    df = national_by_gender[national_by_gender['mulnutrition_type']==gender_mulnutrition_type.strip()]
    df1 = df[df['year']== gender_year]
    fig = px.pie(df1, values='prevalence_rate', names='gender', color = 'gender',
                     title='wasting',
                     color_discrete_map={ 
                    'female': 'rgb(239, 85, 59)', 
                    'male':'rgb(99, 110, 250)'}
                     )

    fig.update_layout(
        title={
                'text' : f"<b>{str(gender_year)} Gender {gender_mulnutrition_type} Prevalence Rate Analysis.</b>",
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
        titlefont={'family': 'Oswald',
                        'color': 'rgb(0,0,0)',
                        'size': 16},

        autosize = True,
        width = 700,
        height = 450,
 
        legend=dict(
                 bgcolor='rgba(255, 255, 255, 0)',
                 traceorder="normal",
                 font=dict(
                      family="sans-serif",
                      size=12,
                      color='#000000')),

                 # legend_title_font_color='rgb(0,0,0)',
                 uniformtext_minsize=12,
                 uniformtext_mode='hide'

                 )
    fig.update_traces(
            textfont_color="white",
            )
    return fig

###############################################################    Province     ###################################
#Trends by Province 
@app.callback(
    Output('national_nurtition_Trends', 'figure'),
    Input('province_nutrition', 'value'),
)
def national_nurtition_Trends( province_nutrition):
    if province_nutrition == None:
        province_nutrition = 'Manicaland'
    province['province'] = province['province'].str.strip()
    province['mulnutrition_type'] = province['mulnutrition_type'].str.strip()
    df = province[province['province']== province_nutrition.strip()]
#     df = df[df['mulnutrition_type']== province_mulnutrition_type]
    fig = px.line(df, x = 'year', y = 'prevalence_rate', color = 'mulnutrition_type',
                 text=df['prevalence_rate'].apply(lambda x: '{0:1.0f}%'.format(x)),
                 template= 'simple_white',
                 color_discrete_map={ 
                    'Wasting': 'rgb(228, 26, 28)', 
                    'Underweight':'rgb(55, 126, 184)',
                     'Overweight': 'rgb(77, 175, 74)', 
                    'Stunting':'rgb(255, 127, 0)',
                     
                    }

                )

    fig.update_layout(
        title = {
            'text' : f"<b>{province_nutrition} Children Mulnutrition Trends</b>",
            'y' : 0.93,
            'x': 0.43,
            'xanchor': 'center',
            'yanchor': 'top'
                },
        titlefont={'family': 'Oswald',
                        'color': 'rgb(0,0,0)',
                        'size': 16},


        xaxis=  {
            'title': '<b>Year</b>',
            'tickangle': 35,
            'color':'rgb(0,0,0)',
            'showticklabels': True,
            'type': 'category',
            'fixedrange': True,
    #         'showline':True,
            'color':'rgb(0,0,0)',
            'linewidth':1.5,
        'ticks':'outside',
        'tickfont':dict(
            family='Arial',
            size=12,
            color='rgb(0,0,0)',
            )
                },

        yaxis= {
            'title': '<b>Prevalence rate</b>',
            'color':'rgb(0,0,0)',
            'fixedrange': True,
            'linecolor':'rgb(0,0,0)',
            'showgrid':True,
            'linewidth':1.5,
            'ticks':'outside',
            'tickfont':dict(
                family='Arial',
                size=12,
                color='rgb(0,0,0)'
                )        
                },

        legend=dict(
            title = '',
            bgcolor='rgba(255, 255, 255, 0)',
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color='rgb(0,0,0)'
                )
            ),
        title_font_color = 'rgb(0,0,0)',

        barmode = 'group',
#         showlegend=False,
        autosize = True,
        width = 700,
        height = 450
        )
    #update hover
    fig.update_traces(
            hovertemplate='Year: %{x} <br>prevalence: %{y}%',
            textfont=dict( color="Black"),
            textposition='top center',
#             mode="lines+markers",
            )

    return fig
####Trends summary information
@app.callback(
    Output('national_nurtition_Trends_text', 'children'),
    Input('province_nutrition', 'value'))
def national_nurtition_Trends_text(province_nutrition):
    return f'You have selected {province_nutrition} and can add explanation of information shown on the graph'



##Bar Graph
@app.callback(
    Output('mulnutrition_by_province', 'figure'),
    Input('province_mulnutrition_type', 'value'),
    Input('province_year', 'value')
)
def mulnutrition_by_province(province_mulnutrition_type, province_year):
    if province_mulnutrition_type == None:
        province_mulnutrition_type = 'Wasting'
    if province_year == None:
        province_year = 1994
    province['province'] = province['province'].str.strip()
    province['mulnutrition_type'] = province['mulnutrition_type'].str.strip()
    df = province[province['mulnutrition_type']==province_mulnutrition_type]
    df1 = df[df['year']==province_year]
    fig = px.bar(df1, x = 'province', y = 'prevalence_rate', color = 'province',
                 text=df1['prevalence_rate'].apply(lambda x: '{0:1.0f}%'.format(x)),
                 template= 'simple_white',
#                color_discrete_map={
#                     'Urban': 'rgb(255,69,0)',
#                     'Rural': 'rgb(255,255,102)',
#                     }
                )

    fig.update_layout(
        title = {
            'text' : f"<b>{province_year} {province_mulnutrition_type} Prevalence Rate comparison</b>",
            'y' : 0.93,
            'x': 0.43,
            'xanchor': 'center',
            'yanchor': 'top'
                },


        xaxis=  {
            'title': '<b>Province</b>',
            'tickangle': 35,
            'color':'rgb(0,0,0)',
            'showticklabels': True,
            'type': 'category',
            'fixedrange': True,
    #         'showline':True,
            'linecolor':'rgb(0,0,0)',
            'showgrid':False,
            'linewidth':1.5,
        'ticks':'outside',
        'tickfont':dict(
            family='Arial',
#             size=12,
            color='rgb(0,0,0)'
            )
                },

        yaxis= {
            'title': '<b>Prevalence rate</b>',
            'color':'rgb(0,0,0)',
            'fixedrange': True,
            'linecolor':'rgb(0,0,0)',
            'showgrid':True,
            'linewidth':1.5,
            'ticks':'outside',
            'tickfont':dict(
                family='Arial',
                size=12,
                color='rgb(0,0,0)'
                )        
                },

        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color='rgb(0,0,0)'
                )
            ),
        title_font_color = 'rgb(0,0,0)',

#         barmode = 'group',
        autosize = True,
        width = 700,
        height = 450)
        #update hover
    fig.update_traces(
            hovertemplate='Year: %{x} <br>prevalence: %{y}',
            textfont=dict( color="White")
            )
    return fig

#Bar Graph Summary
@app.callback(
    Output('mulnutrition_by_province_summary', 'figure'),
    Input('province_mulnutrition_type', 'value'),
    Input('province_year', 'value')
)
def mulnutrition_by_province_summary(province_mulnutrition_type, province_year):
    province = pd.read_excel("./data/Children_nutrition_status_ZDHS.xlsx", sheet_name = 'province')
    if province_mulnutrition_type == None:
        province_mulnutrition_type = 'Wasting'
    if province_year == None:
        province_year = 1994
    province['province'] = province['province'].str.strip()
    province['mulnutrition_type'] = province['mulnutrition_type'].str.strip()
    df = province[province['mulnutrition_type']==province_mulnutrition_type]
    df1 = df[df['year']==province_year]
    high =df1[df1['prevalence_rate']==df1['prevalence_rate'].max()].values.tolist()[0]
    province = high[0]
    prevalence_rate = high[2]

    return 'hello_world'
    # f'{province} have the worst prevalence_rate ({prevalence_rate}%) of children under {province_mulnutrition_type} in the Year {province_year}'



# tabs switch case
@app.callback(Output("tab-content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab_1":
        return first_tab()
    elif at == "tab_2":
        return food_insecurity_tab
    elif at == "tab_3":
        return livestock_ownership_tab


if __name__ == '__main__':
    app.run_server(debug=True, port= 8051)

