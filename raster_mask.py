import rasterio
import numpy as np

# Open DESIS spectral image file
spectral_file_path = (
    "DESIS-HSI-L2A-DT0707652640_011-20220404T193259-V0220-SPECTRAL_IMAGE.tif"
)
with rasterio.open(spectral_file_path) as spectral_dataset:
    # Read the quality image file
    quality_file_path = (
        "DESIS-HSI-L2A-DT0707652640_011-20220404T193259-V0220-QL_QUALITY-2.tif"
    )
    with rasterio.open(quality_file_path) as quality_dataset:
        # Read the quality image bands you want to use as masks
        mask_bands = [3, 6]  # Use bands 1, 3, and 6 as masks
        mask_data = np.stack([quality_dataset.read(band) for band in mask_bands])

        # Define thresholds for each mask band
        threshold_band3 = 1  # Threshold value for mask band 3
        threshold_band6 = 1  # Threshold value for mask band 6

        # Create masks based on each mask band and threshold
        mask_band3 = mask_data[0] == threshold_band3
        mask_band6 = mask_data[1] == threshold_band6

        # Combine masks using logical operations (e.g., AND, OR)
        combined_mask = np.logical_or.reduce((mask_band3, mask_band6))

        # Open spectral dataset again and read its data
        spectral_data = spectral_dataset.read()

        # Convert spectral_data to a floating-point data type
        spectral_data = spectral_data.astype(np.float32)

        # Replace the specific "no data" value (-32768) with np.nan
        spectral_data[spectral_data == -32768] = np.nan

        # Apply the combined mask to the spectral data
        masked_spectral_data = np.where(combined_mask, np.nan, spectral_data)

        # Calculate the bounding box of the valid data
        rows, cols = np.where(~combined_mask)
        min_row, max_row = min(rows), max(rows) + 1
        min_col, max_col = min(cols), max(cols) + 1

        # Get the valid data area as a window
        window = rasterio.windows.Window(
            min_col, min_row, max_col - min_col, max_row - min_row
        )

        # Create output file metadata based on the valid data window
        masked_metadata = spectral_dataset.meta
        masked_metadata.update(
            dtype=rasterio.float32,
            nodata=np.nan,
            width=window.width,
            height=window.height,
            transform=spectral_dataset.window_transform(window),
        )

        # Output file path
        output_file_path = "apr2022_spectral2.tif"

        # Save the masked spectral data (without black border) and no specific no data value as a new GeoTIFF file
        with rasterio.open(output_file_path, "w", **masked_metadata) as masked_dataset:
            masked_dataset.write(
                masked_spectral_data[
                    :,
                    window.row_off : window.row_off + window.height,
                    window.col_off : window.col_off + window.width,
                ]
            )
