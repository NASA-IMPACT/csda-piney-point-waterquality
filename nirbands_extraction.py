import rasterio

# Open the input raster file
input_file = "june_2022_16bit.tif"
with rasterio.open(input_file) as src:
    # Read all bands from the raster as a 3D NumPy array
    raster_data = src.read()

    # Identify the indices of the specific bands you want to extract
    extracted_bands = [
        130,
        131,
        132,
        133,
        134,
        135,
        136,
        137,
        138,
        139,
        140,
        141,
        142,
        143,
        144,
        145,
        146,
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        154,
        154,
        155,
        156,
        166,
        167,
        168,
        169,
        170,
        171,
        172,
        173,
        174,
        175,
        176,
        177,
        178,
        179,
        180,
        181,
        182,
        183,
        184,
        185,
        186,
        187,
        188,
        189,
        190,
        191,
        192,
        193,
        194,
        195,
        196,
        197,
        198,
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        209,
        210,
        211,
        212,
        213,
        214,
        215,
        216,
        217,
        218,
        219,
        220,
        221,
        222,
        223,
        224,
        225,
        226,
        227,
        228,
        229,
        230,
        231,
        232,
        233,
        234,
    ]

    # Create a new array to store the extracted bands
    extracted_bands = raster_data[extracted_bands]

# Save the extracted bands to a new raster file
output_file = "nir_bands.tif"
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
