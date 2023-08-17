#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get this figure: fig = py.get_figure("https://plotly.com/~chelsea_lyn/5245/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~chelsea_lyn/5245/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Pie Chart Subplot Example", fileopt="extend")

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "name": "Starry Night", 
  "type": "pie", 
  "domain": {
    "x": [0, 0.52], 
    "y": [0, 0.49]
  }, 
  "marker": {"colors": ["rgb(56, 75, 126)", "rgb(18, 36, 37)", "rgb(34, 53, 101)", "rgb(36, 55, 57)", "rgb(6, 4, 4)"]}, 
  "textinfo": "none", 
  "hoverinfo": "label+percent+name", 
  "labels": ["1st", "2nd", "3rd", "4th", "5th"], 
  "values": [38, 27, 18, 10, 7]
}
trace2 = {
  "name": "Sunflowers", 
  "type": "pie", 
  "domain": {
    "x": [0.48, 1], 
    "y": [0, 0.49]
  }, 
  "marker": {"colors": ["rgb(177, 127, 38)", "rgb(205, 152, 36)", "rgb(99, 79, 37)", "rgb(129, 180, 179)", "rgb(124, 103, 37)"]}, 
  "textinfo": "none", 
  "hoverinfo": "label+percent+name", 
  "labels": ["1st", "2nd", "3rd", "4th", "5th"], 
  "values": [28, 26, 21, 15, 10]
}
trace3 = {
  "name": "Irises", 
  "type": "pie", 
  "domain": {
    "x": [0, 0.52], 
    "y": [0.51, 1]
  }, 
  "marker": {"colors": ["rgb(33, 75, 99)", "rgb(79, 129, 102)", "rgb(151, 179, 100)", "rgb(175, 49, 35)", "rgb(36, 73, 147)"]}, 
  "textinfo": "none", 
  "hoverinfo": "label+percent+name", 
  "labels": ["1st", "2nd", "3rd", "4th", "5th"], 
  "values": [38, 19, 16, 14, 13]
}
trace4 = {
  "name": "The Night Café", 
  "type": "pie", 
  "domain": {
    "x": [0.48, 1], 
    "y": [0.51, 1]
  }, 
  "marker": {"colors": ["rgb(146, 123, 21)", "rgb(177, 180, 34)", "rgb(206, 206, 40)", "rgb(175, 51, 21)", "rgb(35, 36, 21)"]}, 
  "textinfo": "none", 
  "hoverinfo": "label+percent+name", 
  "labels": ["1st", "2nd", "3rd", "4th", "5th"], 
  "values": [31, 24, 19, 18, 8]
}
data = Data([trace1, trace2, trace3, trace4])
layout = {
  "title": "Van Gogh: 5 Most Prominent Colors Shown Proportionally", 
  "showlegend": False
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

