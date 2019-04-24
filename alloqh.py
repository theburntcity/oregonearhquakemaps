from datawrangling.geomunging import oqh
from pprint import pprint
from folium import LayerControl, Map, FeatureGroup
from folium.plugins import HeatMap

# create map object
m = Map(tiles='openstreetmap',min_zoom=7, max_zoom=14, zoom_start=7,\
         min_lat=40, max_lat=48,min_lon=-114, max_lon=-128, \
         max_bounds=True)
fg = FeatureGroup('Heat Map')
# add a list of coordinates to the map object
fg.add_child(HeatMap(list(zip(oqh.lat.values, oqh.lon.values))))
m.add_child(fg)
LayerControl().add_to(m)
m.save(r'templates\alleventheat.html')