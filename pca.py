import numpy as np
import pandas as pd
import rasterio
import rasterio.plot
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xml.dom import minidom

# input image
image1_ = "wadley_after.tif"
# output image
output_filename = "test.tif"
# number of components
num_comp = 3
# pca to save to tif
pca_comp = 1
# output for eigenvalues
eigenvalues_table = "eigenvalues.csv"
# output for eigenvectors
eigenvectors_table = "eigenvectors_table.csv"


def main(
    image1_, output_filename, num_comp, pca_comp, eigenvalues_table, eigenvectors_table
):
    image1 = rasterio.open(image1_)

    # Enter the number of principal components
    num_comp = num_comp
    # Enter the component to save to geotiff (note need to add loop to save all components)
    pca_comp = pca_comp

    band_list = []
    band_numbers = []
    for band_num in range(1, image1.count + 1):
        band_after = image1.read(band_num)
        band_list.append(band_after)
        band_numbers.append(band_num)

    arr_st = np.stack(band_list)

    # Preprocessing to capture image shapes
    x = np.moveaxis(arr_st, 0, -1)
    x1 = x.shape[0]
    x2 = x.shape[1]
    x_reshape = x.reshape(-1, x.shape[-1])

    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(x_reshape)

    # Calculate principal components
    pca = PCA(n_components=num_comp)
    data = pca.fit_transform(X_scaled)

    # Get the eigenvalues
    var = pca.explained_variance_
    var2 = pca.explained_variance_ratio_

    # Extract eigenvectors
    eigenvectors = pca.components_

    # Create DataFrame for eigenvectors and eigenvalues
    column_names = ["pca{}".format(i) for i in range(1, num_comp + 1)]
    eigenvectors_df = pd.DataFrame(eigenvectors.T, columns=column_names)
    eigenvectors_df["Band"] = band_numbers
    eigenvectors_df.to_csv(eigenvectors_table, index=False)

    eigenvalues_df = pd.DataFrame(
        {
            "Component": column_names,
            "Eigenvalues": var,
            "Explained Variance Ratio": var2,
        }
    )
    # eigenvalues_table = eigenvectors_table.replace(".csv", "_eigenvalues.csv")
    eigenvalues_df.to_csv(eigenvalues_table, index=False)

    # Get the desired PCA component
    component = data[:, pca_comp - 1]
    comp_reshape = component.reshape(x1, x2)

    # Get metadata information for output file
    kwargs = image1.meta
    kwargs.update(dtype=rasterio.float32, count=1)

    # Write output file
    with rasterio.open(output_filename, "w", **kwargs) as dst:
        dst.write_band(1, comp_reshape.astype(rasterio.float32))


if __name__ == "__main__":
    (
        image1_,
        output_filename,
        num_comp,
        pca_comp,
        eigenvalues_table,
        eigenvectors_table,
    )
    main(
        image1_,
        output_filename,
        num_comp,
        pca_comp,
        eigenvalues_table,
        eigenvectors_table,
    )
