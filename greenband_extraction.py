import rasterio

# Open the input raster file
input_file = "june_2022_16bit.tif"
with rasterio.open(input_file) as src:
    # Read all bands from the raster as a 3D NumPy array
    raster_data = src.read()

    # Identify the indices of the specific bands you want to extract
    extracted_bands = [
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
    ]

    # Create a new array to store the extracted bands
    extracted_bands = raster_data[extracted_bands]

# Save the extracted bands to a new raster file
output_file = "green_bands.tif"
with rasterio.open(
    output_file,
    "w",
    driver="GTiff",
    width=src.width,
    height=src.height,
    count=len(extracted_bands),
    dtype=src.dtypes[0],
    crs=src.crs,
    transform=src.transform,
) as dst:
    dst.write(extracted_bands)

print("Extracted bands saved to:", output_file)
