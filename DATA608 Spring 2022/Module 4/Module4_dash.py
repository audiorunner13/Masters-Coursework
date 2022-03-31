#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:18:18 2022

@author: Audiorunner13
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

trees_steward_counts = pd.DataFrame()

url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json'
tree = pd.read_json(url)

tree_df = tree[["boroname","steward","spc_common","health"]]

tree_df['count'] = 1

df2 = tree_df.groupby(['boroname','spc_common','health'])[["count"]].sum().reset_index()

# tree_df['tree_total'] = 1

# df2_final = tree_df.groupby(['boroname'])[["tree_total"]].sum().reset_index()

# print(df2_final.head(50))

df3 = tree_df.groupby(['steward','health'])[["count"]].sum().reset_index()

# print(df3.head(50))

app = Dash(__name__)

fig_q1 = px.bar(df2, x="health", y="count", color="spc_common", hover_name="boroname", barmode="group")

fig_q2 = px.bar(df3, x="health", y="count", color="steward", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Data 0608 - Knowledge and Visual Analytics'),
    html.H2(children='Module 4 Assignment: New York City Tree Census'),

    html.Div(children='''
        Question 1: What proportion of trees are in good, fair, or poor health according to the ‘health’ variable?
    '''),
    html.Div(children='''
        Answer:  While I could not figure out how to include the total count of trees by borough to calculate the
        proportion, one can see from the visual that most trees are in Good condition and a small percentage are in
        poor condition.
    '''),

    dcc.Graph(
        id='graph-q1',
        figure=fig_q1
    ),
    
    html.Div(children='''
        Question 2: Are stewards (steward activity measured by the ‘steward’ variable) having an impact on the health of trees?
    '''),
    html.Div(children='''
        Answer:  One can see that steward activity does not have any impact on the health of trees.  The majority of trees with
        a steward on "None" are in good and fair condition.
    '''),
    
    dcc.Graph(
        id='graph-q2',
        figure=fig_q2
    )  
])

if __name__ == '__main__':
    app.run_server(debug=True)