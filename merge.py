import os
import rasterio
from rasterio.merge import merge

with rasterio.Env(CHECK_DISK_FREE_SPACE=False):
    # Path to folder
    folder_path = "/Users/brad/Downloads/SmallSats/Science_Applications/forest_disturbance/boulder/feb2023"

    # Get a list of all GeoTIFF files within the folder
    file_paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith(".tif")
    ]

    # Open the GeoTIFF files and read their metadata
    src_files = [rasterio.open(fp) for fp in file_paths]

    # Merge the GeoTIFF files
    mosaic, out_trans = merge(src_files)

    # Get the metadata of the first GeoTIFF
    out_meta = src_files[0].meta.copy()

    # Update the metadata with the mosaic's dimensions and transformation
    out_meta.update(
        {
            "driver": "GTiff",
            "height": mosaic.shape[1],
            "width": mosaic.shape[2],
            "transform": out_trans,
        }
    )

    # Save the merged GeoTIFF
    merged_path = "feb2023_merged.tif"
    with rasterio.open(merged_path, "w", **out_meta) as dest:
        dest.write(mosaic)
