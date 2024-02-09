import rasterio

# Open the input raster file
input_file = "june_2022_16bit.tif"
with rasterio.open(input_file) as src:
    # Read all bands from the raster as a 3D NumPy array
    raster_data = src.read()

    # Identify the indices of the specific bands you want to extract
    extracted_bands = [
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
    ]

    # Create a new array to store the extracted bands
    extracted_bands = raster_data[extracted_bands]

# Save the extracted bands to a new raster file
output_file = "red_edge_bands.tif"
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
