#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:09:01 2022

@author: Audiorunner13
"""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

# trees_steward_counts = pd.DataFrame()

url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json'
tree = pd.read_json(url)

# print(tree.head(10))

# tree.describe()

num_rows = tree.shape[0]

# print(num_rows)
# print(tree.steward[0])

tree = tree.replace(np.nan, '', regex=True)

# v_steward_4 = '4orMore'
# v_steward_34 = '3or4'
# v_steward_12 = '1or2'
# v_steward_N = 'None'
# v_health_g = 'Good'
# v_health_f = 'Fair'
# v_health_p = 'Poor'
# v_count = 425

# v_h4_g_cnt = 0
# v_h34_g_cnt = 0
# v_h12_g_cnt = 0
# v_hN_g_cnt = 0

# v_h4_f_cnt = 0
# v_h34_f_cnt = 0
# v_h12_f_cnt = 0
# v_hN_f_cnt = 0

# v_h4_p_cnt = 0
# v_h34_p_cnt = 0
# v_h12_p_cnt = 0
# v_hN_p_cnt = 0

# i = 0
        
# while i in range(0,num_rows):    
#     if trees.steward[i] == v_steward_N:
#         if trees.health[i] == v_health_g:
#             v_hN_g_cnt += 1
#         elif trees.health[i] == v_health_f:
#             v_hN_f_cnt += 1
#         elif trees.health[i] == v_health_p:
#             v_hN_p_cnt += 1
#         i = i + 1
#     elif trees.steward[i] == v_steward_4:
#         if trees.health[i] == v_health_g:
#             v_h4_g_cnt += 1
#         elif trees.health[i] == v_health_f:
#             v_h4_f_cnt += 1
#         elif trees.health[i] == v_health_p:
#             v_h4_p_cnt += 1
#         i = i + 1
#     elif trees.steward[i] == v_steward_34:
#         if trees.health[i] == v_health_g:
#             v_h34_g_cnt += 1
#         elif trees.health[i] == v_health_f:
#             v_h34_f_cnt += 1
#         elif trees.health[i] == v_health_p:
#             v_h34_p_cnt += 1
#         i = i + 1
#     elif trees.steward[i] == v_steward_12:
#         if trees.health[i] == v_health_g:
#             v_h12_g_cnt += 1
#         elif trees.health[i] == v_health_f:
#             v_h12_f_cnt += 1
#         elif trees.health[i] == v_health_p:
#             v_h12_p_cnt += 1
#         i = i + 1
#     else:
#         i += 1

# n = 1
# while n in range(1,13):
#     if n == 1:
#         new_row = {'steward' : v_steward_N, 'health':v_health_g, 'count':v_hN_g_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 2:
#         new_row = {'steward' : v_steward_N, 'health':v_health_f, 'count':v_hN_f_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 3:
#         new_row = {'steward' : v_steward_N, 'health':v_health_p, 'count':v_hN_p_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 4:
#         new_row = {'steward' : v_steward_4, 'health':v_health_g, 'count':v_h4_g_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 5:
#         new_row = {'steward' : v_steward_4, 'health':v_health_f, 'count':v_h4_f_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 6:
#         new_row = {'steward' : v_steward_4, 'health':v_health_p, 'count':v_h4_p_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 7:
#         new_row = {'steward' : v_steward_34, 'health':v_health_g, 'count':v_h34_g_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 8:
#         new_row = {'steward' : v_steward_34, 'health':v_health_p, 'count':v_h34_p_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 9:
#         new_row = {'steward' : v_steward_34, 'health':v_health_f, 'count':v_h34_f_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 10:
#         new_row = {'steward' : v_steward_12, 'health':v_health_g, 'count':v_h12_g_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 11:
#         new_row = {'steward' : v_steward_12, 'health':v_health_p, 'count':v_h12_p_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
#     elif n == 12:
#         new_row = {'steward' : v_steward_12, 'health':v_health_f, 'count':v_h12_f_cnt}
#         trees_steward_counts = trees_steward_counts.append(new_row, ignore_index=True)
#         n += 1
        
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# fig_q1 = px.scatter(tree, x="steward", y="health",
#                   color="tree_id", hover_name="boroname",
#                   log_x=True, size_max=60)

fig_q1 = px.bar(tree, x="health", y="steward", color="spc_common", barmode="group")
# fig_q2 = px.bar(trees_steward_counts, x="health", y="count", color="steward", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='graph-q1',
        figure=fig_q1
    )
    # ,
    
    # dcc.Graph(
    #     id='graph-q2',
    #     figure=fig_q2
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)

