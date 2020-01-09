import geopandas as gpd
import os
import matplotlib.pyplot as plt

os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/france_files/shape')
base_file = gpd.read_file('landuse.shp')
base_file.head()
base = base_file.plot(color='yellow', edgecolor='gray', facecolor='blue')



cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

france_files_list = ['buildings.shp', 'places.shp', 'railways.shp', 'natural.shp', 'waterways.shp']
france_colors = ['orange', 'yellow', 'gray', 'gray', 'green', 'lightblue']
edge_color = 'black'
cur_path = os.path.dirname(__file__)

def maps_of_france(files, colors):
    for x in range(len(files)):
        os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/france_files/shape')
        z = gpd.read_file(f'{files[x]}')
        z.plot(ax=base, color=colors[x], edgecolor=edge_color)

maps_of_france(france_files_list, france_colors)

plt.show()
