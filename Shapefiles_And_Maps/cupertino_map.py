import geopandas as gpd
import os
import matplotlib.pyplot as plt

os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/cupertino_files/shape')
base_file = gpd.read_file('landuse.shp')
base_file.head()
base = base_file.plot(color='yellow', edgecolor='gray', facecolor='blue')

cupertino_files_list = ['buildings.shp', 'places.shp', 'railways.shp', 'natural.shp', 'waterways.shp']
cupertino_colors = ['orange', 'yellow', 'red', 'green', 'lightblue']
edge_color = 'gray'
cur_path = os.path.dirname(__file__)

def maps_of_cupertino(files, colors):
    for x in range(len(files)):
        os.chdir('/Users/kumarfamily/Desktop/Programming/Code_in_with_google/Shapefiles_And_Maps_shp/cupertino_files/shape')
        z = gpd.read_file(f'{files[x]}')
        z.plot(ax=base, color=colors[x], edgecolor=edge_color, label=cupertino_files_list[x])

maps_of_cupertino(cupertino_files_list, cupertino_colors)

plt.show()
