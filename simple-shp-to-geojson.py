# %% main import
import geopandas as gpd

# %% load SHP
shp = gpd.read_file("Batas_Wilayah_KelurahanDesa_10K_AR.shp")

# %% view first 5 rows
shp.head()

# %% view summary
shp.info()

# %% view column
shp.columns

# %% view geometry type
shp.geometry.type

# %% convert to geojson
shp.to_file("Batas_Wilayah_KelurahanDesa_10K_AR.geojson", driver="GeoJSON")

# %% validate geojson
import json

with open("Batas_Wilayah_KelurahanDesa_10K_AR.geojson") as f:
    json.load(f)

# %% take the province boundary only
prov_shp = shp.dissolve(by="WADMPR", as_index=True)
prov_shp = prov_shp.reset_index()

# %% convert to geojson
prov_shp.to_file("Batas_Wilayah_KelurahanDesa_10K_AR_prov.geojson", driver="GeoJSON")

# %% validate geojson
with open("Batas_Wilayah_KelurahanDesa_10K_AR_prov.geojson") as f:
    json.load(f)

# %%
