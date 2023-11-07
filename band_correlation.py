import numpy as np
import rasterio

# Open the input raster file
input_file = "red_edge_bands.tif"
with rasterio.open(input_file) as src:
    # Read all bands from the raster as a 3D NumPy array
    hyperspectral_data = src.read()

# Reshape the data to 2D (rows are pixels, columns are bands)
num_pixels = hyperspectral_data.shape[1] * hyperspectral_data.shape[2]
data = hyperspectral_data.reshape(hyperspectral_data.shape[0], num_pixels).T

# Calculate the correlation matrix between bands
correlation_matrix = np.corrcoef(data, rowvar=False)

# Find the band with the highest mean correlation
mean_correlations = np.mean(correlation_matrix, axis=1)
highest_correlation_band = (
    np.argmax(mean_correlations) + 1
)  # Add 1 to get the original band number

# Extract the band with the highest correlation
band_to_save = hyperspectral_data[
    highest_correlation_band - 1
]  # Subtract 1 to get the 0-based index

# Multiply the extracted band by 0.0001
band_to_save *= 0.0001

# Save the extracted band to a new raster file
output_file = "red_edge_highest_correlation_band.tif"
with rasterio.open(
    output_file,
    "w",
    driver="GTiff",
    width=src.width,
    height=src.height,
    count=1,
    dtype=src.dtypes[0],
    crs=src.crs,
    transform=src.transform,
) as dst:
    dst.write(band_to_save, 1)

print(
    f"Band with the highest correlation (Band {highest_correlation_band}) saved to:",
    output_file,
)
