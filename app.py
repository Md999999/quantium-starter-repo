from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

#Load and sort data
df = pd.read_csv('./formatted_data.csv')
df = df.sort_values(by="date")

app = Dash(__name__)

#Styling
COLORS = {
    'background': '#f9f9f9',
    'text': '#2c3e50',
    'header_bg': '#ffffff',
    'accent': '#e74c3c'
}

#App Layout
app.layout = html.Div(style={'backgroundColor': COLORS['background'], 'padding': '20px'}, children=[

    # Styled Header
    html.Div(style={'backgroundColor': COLORS['header_bg'], 'padding': '20px', 'borderRadius': '10px',
                    'boxShadow': '0 4px 6px rgba(0,0,0,0.1)', 'marginBottom': '20px'}, children=[
        html.H1(
            children='Pink Morsel Sales Insights',
            style={'textAlign': 'center', 'color': COLORS['text'], 'fontFamily': 'Arial, sans-serif'}
        ),
    ]),

    # Radio Buttons
    html.Div(style={'textAlign': 'center', 'marginBottom': '30px', 'fontFamily': 'Arial, sans-serif'}, children=[
        html.Label("Filter by Region:", style={'fontWeight': 'bold', 'fontSize': '18px', 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            labelStyle={'marginRight': '15px', 'cursor': 'pointer'}
        ),
    ]),

    # The Graph Container
    html.Div(style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px',
                    'boxShadow': '0 4px 6px rgba(0,0,0,0.05)'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])


#Interactivity
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    #Filter logic
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    #Create the chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Trend: {selected_region.capitalize()}",
        template="plotly_white",
        color_discrete_sequence=[COLORS['accent']]
    )

    #Maintain the price increase reference point
    fig.add_vline(x="2021-01-15", line_width=2, line_dash="dash", line_color="#34495e")

    fig.update_layout(
        font_family="Arial",
        title_font_size=22,
        xaxis_title="Date",
        yaxis_title="Total Sales ($)"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)