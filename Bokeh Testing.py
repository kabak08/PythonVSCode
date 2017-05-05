import pandas as pd
import os

url = "https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/12cb3883-56f5-47de-afa5-3b1cf61b257b/download/crime.csv"

data = pd.read_csv(url)
len(data) #shows us we have 161,127 rows of data
data.head #shows us the top few rows of our data
names = data.columns.values #shows us the column names
list(names)

#finding the shooting data
shootings = data[data['SHOOTING'] == 'Y']
data = shootings

from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson




geo_source = GeoJSONDataSource(geojson=geojson)

p = figure(toolbar_location = "above", plot_width = 600, plot_height = 300)
p.circle(x='x', y='y', alpha=0.9, source=geo_source)
output_file("geojson.html")
show(p)




#Map data ©2017 Google
#Terms of Use
#Report a map error
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=42.3601, lng=-71.0589, map_type="roadmap", zoom=13)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, plot_width = 1000, plot_height = 600)
plot.title.text = "Boston"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyB1IR_MczcjRvimyTR7wmD8aQgpKbUUBjA"

source = ColumnDataSource(
    data=dict(
        lat=data["Lat"],
        lon=data["Long"],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
#Map data ©2017 Google
#Terms of Use
#Report a map error
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool)
circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)