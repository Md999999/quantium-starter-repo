from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# 1. Load the data
df = pd.read_csv('./formatted_data.csv')

# 2. Sort the data by date
# This ensures the line moves chronologically from left to right
df = df.sort_values(by="date")

# 3. Create the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Trend (Pre and Post Price Increase)",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# 4. Define the layout
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'fontFamily': 'sans-serif'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 5. Run the app (Updated for modern Dash)
if __name__ == '__main__':
    app.run(debug=True)