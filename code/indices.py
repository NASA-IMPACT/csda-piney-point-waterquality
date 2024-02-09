import rasterio
import numpy

green_band_file = "green_highest_correlation_band.tif"
red_band_file = "red_highest_correlation_band.tif"
red_edge_band_file = "red_edge_highest_correlation_band.tif"
nir_band_file = "nir_highest_correlation_band.tif"

# Open each band file separately
green_dataset = rasterio.open(green_band_file)
red_dataset = rasterio.open(red_band_file)
red_edge_dataset = rasterio.open(red_edge_band_file)
nir_dataset = rasterio.open(nir_band_file)

# Read each band as a numpy array
green_band = green_dataset.read(1)
red_band = red_dataset.read(1)
red_edge_band = red_edge_dataset.read(1)
nir_band = nir_dataset.read(1)

numpy.seterr(divide="ignore", invalid="ignore")

# Calculate indices
# Normalized Difference Vegetation Index
ndvi = (nir_band.astype(float) - red_band.astype(float)) / (
    nir_band.astype(float) + red_band.astype(float)
)
# Normalized Difference Water Index
ndwi = (green_band.astype(float) - nir_band.astype(float)) / (
    green_band.astype(float) + nir_band.astype(float)
)
# Normalized Difference Green Red Index
ngrdi = (green_band.astype(float) - red_band.astype(float)) / (
    green_band.astype(float) + red_band.astype(float)
)
# Normalized Difference Red Edge Index
ndre3 = (nir_band.astype(float) - red_edge_band.astype(float)) / (
    nir_band.astype(float) + red_edge_band.astype(float)
)
# Normalized Difference Index 4/5
nd145 = (red_band.astype(float) - red_edge_band.astype(float)) / (
    red_band.astype(float) + red_edge_band.astype(float)
)

# Prepare metadata for the new rasters (using any of the input band datasets as a reference)
profile = red_dataset.profile
profile.update(dtype=rasterio.float32, count=1, compress="lzw", nodata=0)

# Define the output file paths for the new rasters
output_ndvi_file = "ndvi.tif"
output_ndwi_file = "ndwi.tif"
output_ngrdi_file = "ngrdi.tif"
output_ndre3_file = "ndre3.tif"
output_nd145_file = "nd145.tif"

# Write the NDVI array to a new raster file
with rasterio.open(output_ndvi_file, "w", **profile) as dst:
    dst.write(ndvi, 1)

# Write the NDWI array to a new raster file
with rasterio.open(output_ndwi_file, "w", **profile) as dst:
    dst.write(ndwi, 1)

# Write the NGRDI array to a new raster file
with rasterio.open(output_ngrdi_file, "w", **profile) as dst:
    dst.write(ngrdi, 1)

# Write the NDRE3 array to a new raster file
with rasterio.open(output_ndre3_file, "w", **profile) as dst:
    dst.write(ndre3, 1)

# Write the ND145 array to a new raster file
with rasterio.open(output_nd145_file, "w", **profile) as dst:
    dst.write(nd145, 1)

# Close all opened datasets
red_dataset.close()
red_edge_dataset.close()
green_dataset.close()
nir_dataset.close()
