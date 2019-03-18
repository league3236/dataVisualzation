from datetime import datetime
import time
import pymongo

import plotly 
plotly.tools.set_credentials_file(username='ID', api_key='API_KEY')

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from pandas import DataFrame as df
import numpy as np

gate_df = pd.read_csv("gate_time_re.csv")
# gate_df = gate_df.sort_values(["TIME"], ascending=[True])
# gate_df = gate_df.reset_index(drop=True)
gate_df.head()

in_bins =  -1*gate_df['IN']
out_bins =  gate_df['OUT']

y = gate_df['TIME']

trace1 = {
  "x": out_bins, 
  "y": y, 
  "hoverinfo": "x+y+name", 
  "marker": {
    "color": "rgb(94, 160, 191)", 
    "line": {"width": 1}
  }, 
  "name": "OUT", 
  "orientation": "h", 
  "selectedpoints": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], 
  "type": "bar", 
  "uid": "d730b32a-f2e6-4d25-ae58-d194a1cdb5c1", 
  "xsrc": "league3236:36:563d29", 
  "ysrc": "league3236:36:694748"
}
trace2 = {
  "x": in_bins, 
  "y": y, 
  "hoverinfo": "text+y+name", 
  "marker": {
    "color": "rgb(25, 74, 191)", 
    "line": {
      "color": "rgb(64, 142, 204)", 
      "width": 1
    }
  }, 
  "name": "IN", 
  "orientation": "h", 
  "selectedpoints": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], 
#   "text": [386, 460, 657, 1182, 1782, 2295, 2187, 561, 635, 863.0, 808.0, 880.0, 893.0, 570.0, 359.0, 271.0, 322.0, 307.0, 319.0, 372.0, 334.0, 284.0, 238.0, 146.0, 122.0, 198.0, 384.0, 744.0, 1346.0, 1884.0, 2841.0, 1209.0, 591.0, 389.0, 361.0, 444.0, 664.0, 552.0, 351.0, 305.0, 276.0, 305.0, 354.0, 345.0, 321.0, 315.0, 382.0, 320.0, 328.0, 455.0, 779.0, 618.0, 643.0, 577.0, 484.0, 448.0, 460.0, 387.0, 410.0, 359.0, 248.0, 181.0, 127.0, 200.0, 246.0, 199.0, 177.0, 122.0, 90.0, 89.0, 62.0, 61.0, 82.0],
  "text": -1 * in_bins.astype('int'),
  "textsrc": "league3236:36:2e793c", 
  "type": "bar", 
  "uid": "21c5540c-07ed-423d-841a-2c08a4d24a70", 
  "xsrc": "league3236:36:602d43", 
  "ysrc": "league3236:36:694748"
}
data = go.Data([trace1, trace2])
layout = {
  "autosize": True, 
  "bargap": 0, 
  "barmode": "overlay", 
  "dragmode": "select", 
  "font": {
    "family": "Roboto", 
    "size": 21
  }, 
  "hoverlabel": {"font": {"size": 13}}, 
  "margin": {
    "t": 74, 
    "b": 71
  }, 
  "paper_bgcolor": "rgb(250, 250, 250)", 
  "plot_bgcolor": "rgb(255, 255, 255)", 
  "title": {"text": "<b>로비 Gate 입/출입자</b>"}, 
  "xaxis": {
    "automargin": False, 
    "autorange": True, 
    "range": [-3134.6666666666665, 2738.6666666666665], 
    "showticklabels": True, 
#     "tickmode": "auto", 
    "ticks": "", 
    "ticktext": [3500, 3000, 1500, 500, 0, 500, 1000, 1500, 3000, 3500], 
    "tickvals": [-3500, -3000, -1500, -500, 0, 500, 1000, 1500, 3000, 3500], 
    "title": {"text": "입/출 인원"}, 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-0.5, 72.5], 
    "title": {"text": "시간"}, 
    "type": "category"
  }
}

py.iplot(dict(data=data, layout=layout), filename='bar_pyramid') 
