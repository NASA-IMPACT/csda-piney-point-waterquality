# **Codebase for deriving spectral indices from hyperspectral satellite imagery**

## **Description**
This repository provides Python scripts that can be utilized to process multispectral and hyperspectral satellite imagery. The scripts were based on processing DESIS hyperspectral imagery but may be applicable to other data sets. The tasks including raster masking, merging, band extraction, band correlation, and calculating spectral indices. 

The DESIS scene IDs are provided in the folder "DESIS_scene_ids." All of the scripts are found in the "code" folder.  

### **Raster mask**
This code will use the DESIS quality image to remove unwanted pixels such as those containing clouds, shadows, haze, etc. 

#### **Running Raster maks**

To run raster_mask.py, user must change three arguments.

* spectral_file_path: this is the hyperspectral image GeoTIFF.
* quality_file_path: this is the quality image file (GeoTIFF).
* output_file_path: what to name the output file.

`python raster_mask.py`

#### **Running Merge**

### **Image merge**
Two or images will be merged together to create a mosaic image. 

Three arguments must be changed to run merge.py.

* folder_path: the path to the folder containing images to merge. Must be GeoTIFFs.
* merged_path: this is the output filename.

  `python merged.py`

### **Band extraction**
Hyperspectral imagery contains many bands within a specific spectral range. For example, there may be 15 bands that are within the blue spectrum. Therefore, sometimes it is necessary to extract specific bands.

#### **Running Band extraction**

Two arguments must be changed to run _extraction.py (blue_extraction.py, green_extraction.py, red_extraction.py, rededge_extraction.py, and nir_extraction.py).

* input_file: name of the input hyperspectral image (must be GeoTIFF).
* output_file: the desired output filename.

  `python red_extraction.py`

### **Band correlation**
As noted above, hyperspectral imagery may contain many bands within a specific spectral range. Once these are extracted, it may be necessary to determine which band(s) to use. There are many techniques to do this. This code will extract the band having the highest correlation out of all the input bands. 

#### **Running Band correlation**

To run band_correlation.py, user must change two arguments.

* input_file: name of the input file containing the desired bands.
* output_file: this is the output filename.

  `python band_correlation.py`

### **Spectral indices**
Spectral indices are calculated based on specific bands. This code will calculate the Normalized Difference Chorophyll Index (NDCI), the Normalized Difference Vegetation Index (NDVI), the Normalized Difference Water Index (NDWI), the Normalized Difference Green/Red Index (NDGRI), the Normalized Difference Red Edge Index (NDRE), and the Normalized DIfference 4.5 Index (ND145).   

Four arugments need to be changed to run the indice.py.

* green_band_file: this is the input green band.
* red_band_file: this is the input red band.
* red_edge_band_file: this is the input to the red edge band.
* nir_band_file: this is the input to the NIR band.

  `python indices.py`

### **Example results using water quality monitoring**

A case study was conducted to evaluate measuring chlorophyll a (chl-a) using DESIS hyperspectral imagery and in situ water quality measurements. A significant waste water leak occurred at the Piney Point phosporous plant in Tampa Bay, FL from March to April 2021. The contaminants that were released, phosporous and nitrogen, are known to cause harmful algal blooms. A high concentration of chl-a serves as a useful tool to detect algal blooms. Six spectral indices were calculated including the normalized difference chlorophyll index (NDCI), the normalized difference vegetation index (NDVI, the normalized difference water index (NDWI), 
the normalized difference red edge index (NDRE), the normalized difference green/red index (NDGRI), and normalized difference 4.5 index (ND145). A multivariant linear regression model was calculated using all six spectral indices and the in situ chl-a measurements. Chl-a maps were created by applying the regression equation to each pixel in the satellite data. 

<p align="center">
<img width="340" alt="fig5" src="https://github.com/NASA-IMPACT/csda-piney-point-waterquality/assets/56319064/92d40f4a-c792-45db-8858-f7b5b5336a33">
</p>
<p>
  <em>Chl-a maps created using the multivariant regression equation. Values extracted using a threshold value of 4 ug/L. Includes copyrighted material of Teledyne Brown Engineering, Inc. © Teledyne Brown Engineering, Inc. 2023. All rights reserved. </em>
</p>
