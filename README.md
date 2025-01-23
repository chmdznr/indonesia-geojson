# Indonesia GeoJSON Boundaries

This repository provides ready-made GeoJSON files for Indonesia's administrative boundaries based on the latest administrative divisions (2022/2023 with 38 provinces). The data is sourced from official administrative boundary shapefiles and converted to GeoJSON format for easier use in web mapping applications.

## 🔥 Quick Download

> **[⬇️ Download Ready-to-Use GeoJSON Files from Google Drive](https://drive.google.com/drive/folders/10gEi4mIriMoL2p6kzlncPXkScw2uZiDW?usp=sharing)**

⚠️ **Important Notes**: 
- The GeoJSON files are quite large (>2GB) due to the detailed boundary information they contain
- If you don't need the full dataset, consider using the province-level boundaries which are smaller in size
- The files are regularly updated to reflect the latest administrative changes

## Data Source

The original shapefile data is sourced from [Indonesia Geospasial](https://www.indonesia-geospasial.com/2023/05/download-shapefile-batas-administrasi.html), which provides up-to-date administrative boundaries reflecting the latest changes in Indonesia's territorial divisions.

## Repository Contents

This repository includes Python scripts for working with the geographical data:

1. `simple_shp_to_geojson.py`: A conversion script that:
   - Converts the original shapefile (.shp) to GeoJSON format
   - Creates two output files:
     - Full administrative boundaries (villages/kelurahan level)
     - Province-only boundaries (created using dissolve operation)
   - Includes validation steps to ensure the generated GeoJSON files are valid

2. `plot_geojson.py`: A visualization script that provides two methods to view the GeoJSON data:
   - Static visualization using GeoPandas and Matplotlib
   - Interactive web map using Folium (outputs an HTML file)

## Requirements

The Python scripts require several dependencies which can be installed using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Visualizing GeoJSON Data

To visualize the GeoJSON file using the provided script:

```bash
python plot_geojson.py
```

This will:
1. Create a static plot showing the administrative boundaries
2. Generate an interactive HTML map that you can open in your web browser

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the MIT License. However, please note that the underlying geographical data may have its own licensing terms.

## Acknowledgments

- Original shapefile data: [Indonesia Geospasial](https://www.indonesia-geospasial.com/)
- Thanks to the open-source community for the tools that made this possible (GeoPandas, Folium, etc.)
