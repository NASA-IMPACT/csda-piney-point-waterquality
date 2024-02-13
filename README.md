# **Codebase for deriving spectral indices from hyperspectral satellite imagery**

## **Description**


### **Raster mask**
This code will use the DESIS quality image to remove unwanted pixels such as those containing clouds, shadows, haze, etc. 

### **Image merge**
Two or images will be merged together to create a mosaic image. 

### **Band extraction**
Hyperspectral imagery contains many bands within a specific spectral range. For example, there may be 15 bands that are within the blue spectrum. Therefore, sometimes it is necessary to extract specific bands.

### **Band correlation**
As noted above, hyperspectral imagery may contain many bands within a specific spectral range. Once these are extracted, it may be necessary to determine which band(s) to use. There are many techniques to do this. This code will extract the band having the highest correlation out of all the input bands. 

### **Spectral indices**
Spectral indices are calculated based on specific bands. This code will calculate the Normalized Difference Chorophyll Index (NDCI), the Normalized Difference Vegetation Index (NDVI), the Normalized Difference Water Index (NDWI), the Normalized Difference Green/Red Index (NDGRI), the Normalized Difference Red Edge Index (NDRE), and the Normalized DIfference 4.5 Index (ND145).   

### **Regression model**


### **Example results using water quality monitoring**

A case study was conducted to evaluate measuring chlorophyll a (chl-a) using DESIS hyperspectral imagery and in situ water quality measurements. A significant waste water leak occurred at the Piney Point phosporous plant in Tampa Bay, FL from March to April 2021. The contaminants that were released, phosporous and nitrogen, are known to cause harmful algal blooms. A high concentration of chl-a serves as a useful tool to detect algal blooms. Six spectral indices were calculated including the normalized difference chlorophyll index (NDCI), the normalized difference vegetation index (NDVI, the normalized difference water index (NDWI), 
the normalized difference red edge index (NDRE), the normalized difference green/red index (NDGRI), and normalized difference 4.5 index (ND145). A multivariant linear regression model was calculated using all six spectral indices and the in situ chl-a measurements. Chl-a maps were created by applying the regression equation to each pixel in the satellite data. 

<p align="center">
<img width="340" alt="fig5" src="https://github.com/NASA-IMPACT/csda-piney-point-waterquality/assets/56319064/92d40f4a-c792-45db-8858-f7b5b5336a33">
</p>
<p>
  <em>Chl-a maps created using the multivariant regression equation. Values extracted using a threshold value of 4 ug/L. Includes copyrighted material of Teledyne Brown Engineering, Inc. © Teledyne Brown Engineering, Inc. 2023. All rights reserved. </em>
</p>
