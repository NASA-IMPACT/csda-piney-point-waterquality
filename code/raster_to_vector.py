import rasterio
from rasterio.features import shapes
from shapely.geometry import shape
import geopandas as gpd

# Load the raster image
raster_path = "BB_severity_aoi2.tif"
with rasterio.open(raster_path) as src:
    raster_array = src.read(1)  # Assuming a single-band raster
    raster_crs = src.crs  # Get the CRS (projection) of the raster

    # Generate shapes and transform
    shapes = list(shapes(raster_array, transform=src.transform))
    polygons = [shape(s) for s, v in shapes if v == 1]

# Create a GeoDataFrame from the polygons
gdf = gpd.GeoDataFrame({"geometry": polygons}, crs=raster_crs)

# Define the output shapefile path
output_shapefile = "BBextracted_aoi2.shp"

# Save the GeoDataFrame as a shapefile with the same CRS as the raster
gdf.to_file(output_shapefile)
