# %% main import
import json
import geopandas as gpd
from shapely.geometry import shape
import matplotlib.pyplot as plt
import folium
import os

# %% verify geopandas
print(gpd.__version__)

# %% main functions
def plot_with_geopandas(geojson_file):
    with open(geojson_file, 'r') as f:
        geojson_data = json.load(f)
    
    features = []
    for feature in geojson_data['features']:
        geometry = shape(feature['geometry'])
        properties = feature['properties']
        features.append({'geometry': geometry, 'properties': properties})
    
    gdf = gpd.GeoDataFrame(features, crs="EPSG:4326")  # Add CRS parameter
    
    fig, ax = plt.subplots(figsize=(15, 10))
    gdf.plot(ax=ax, edgecolor='black', facecolor='none')
    plt.title('Indonesia Administrative Boundaries')
    plt.show()

def plot_with_folium(geojson_file):
    gdf = gpd.read_file(geojson_file, driver='GeoJSON')
        
    # Simplify geometries to reduce size
    gdf['geometry'] = gdf['geometry'].simplify(tolerance=0.01)
    
    # Calculate center
    center_lat = gdf.geometry.centroid.y.mean()
    center_lon = gdf.geometry.centroid.x.mean()
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
    
    # Convert to smaller GeoJSON
    geo_data = gdf.to_json()
    
    folium.GeoJson(
        geo_data,
        name='Indonesia Boundaries',
        style_function=lambda x: {
            'fillColor': 'transparent',
            'color': 'blue',
            'weight': 1
        }
    ).add_to(m)
    
    m.save('indonesia_map.html')

# %% main execution
if __name__ == "__main__":
    # File path
    geojson_file = "Batas_Wilayah_KelurahanDesa_10K_AR_prov.geojson"
    
    print("Plotting with GeoPandas...")
    plot_with_geopandas(geojson_file)
    
    print("Creating interactive map with Folium...")
    plot_with_folium(geojson_file)
    print("Interactive map saved as 'indonesia_map.html'")

# %%