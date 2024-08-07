# K-Means Image Compression

This repository contains a Python implementation of the K-Means clustering algorithm for image compression. The script reduces the number of colors in an image by clustering similar colors and replacing them with the centroid of the cluster.

## How It Works

1. **Image Loading**: The script reads an input image and converts it into a numpy array.
2. **K-Means Clustering**: It applies the K-Means algorithm to the image data to cluster pixels into `k` clusters.
3. **Image Compression**: Each pixel in the image is then replaced with the centroid of its cluster, resulting in a compressed image with `k` colors.

## Prerequisites

- Python 3.x
- `numpy` library
- `Pillow` library
- `matplotlib` library

You can install the required libraries using:

```bash
pip install numpy Pillow matplotlib
```
## Usage

```bash
python kmeans_image_compression.py <path_to_image> <k>
```
- <path_to_image>: Path to the input image file.
- <k>: Number of colors to reduce the image to.


## Example 

```bash
python kmeans_image_compression.py image.jpg 16
```
This command will read image.jpg, compress it to 16 colors, and save the result as image-16.png in the same directory.

## Implementation Deta

The K-Means algorithm implementation involves:

- Initializing centroids by randomly selecting k pixels from the image.
- Iteratively updating pixel labels and centroids until convergence or a maximum of 100 iterations.
- Converting the clustered pixel data back to an image and saving it.

## File Structure 

- `kmeans_image_compression.py`: Main script for image compression using K-Means.

## Notes

- Ensure the input image path is valid.
- The `k` value should be a positive integer.
- The compressed image will be saved in the same directory as the input image with the format `<original_filename>-<k>.png`.

## License

This project is licensed under the MIT License.