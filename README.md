# **Codebase for deriving spectral indices from hyperspectral satellite imagery**

## **Description**

### **Raster mask**

### **Image merge**

### **Band extraction**

### **Band correlation**

### **Spectral indices**

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
