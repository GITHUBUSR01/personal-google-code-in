import geopandas as gpd
import os
import matplotlib.pyplot as plt

os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/toronto_files/shape')
base_file = gpd.read_file('landuse.shp')
base_file.head()
base = base_file.plot(color='yellow', edgecolor='gray', facecolor='blue')

tor_files_list = ['buildings.shp', 'places.shp', 'railways.shp', 'natural.shp', 'waterways.shp']
tor_colors = ['orange', 'yellow', 'red', 'green', 'lightblue']
edge_color = 'gray'
cur_path = os.path.dirname(__file__)

def maps_of_tor(files, colors):
    for x in range(len(files)):
        os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/toronto_files/shape')
        z = gpd.read_file(f'{files[x]}')
        z.plot(ax=base, color=colors[x], edgecolor=edge_color, label=tor_files_list[x])

maps_of_tor(tor_files_list, tor_colors)

plt.show()
