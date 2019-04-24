from datawrangling.geomunging import g2
from pprint import pprint
from folium import LayerControl, Map, FeatureGroup
from folium.plugins import HeatMap

# create map object
m = Map(tiles='openstreetmap',min_zoom=7, max_zoom=17, zoom_start=7,\
         min_lat=40, max_lat=48,min_lon=-114, max_lon=-128, \
         max_bounds=True)
fg = FeatureGroup('Heat Map')
# add list of coordinates to map object
fg.add_child(HeatMap(list(zip(g2.lat.values, g2.lon.values))))
m.add_child(fg)
LayerControl().add_to(m)
m.save(r'templates\g2eventheat.html')