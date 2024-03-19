import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import pandas as pd

# create app object
app = Dash(__name__)
# read data
df = pd.read_table('Data for graphing test.txt')
# get column names for checkbox
columns = df.columns.to_list()
for col in ['A', 'B']:
    columns.remove(col)

# define the layout of the app
app.layout = html.Div([
    html.H4('TITLE'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=columns,
        value=[columns[0]],
        inline=True
    ),
    # add more items here for inputting file path or sliders etc.
])


# function that gets called to update the dashboard any time a user interacts
@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"),
    # add input here for sliders etc.
    )
def update_line_chart(checked):
    # uncomment below to read each time if you want to input file via the dashboard
    # df = pd.read_table('Data for graphing test.txt')
    
    # TODO: extract and plot the columns shown
    fig = px.line(df, x='A', y=checked[-1])  # option for color= arg here
    return fig


app.run_server(debug=True)
