# K-Means Image Compression

This repository contains a Python implementation of the K-Means clustering algorithm for image compression. The script reduces the number of colors in an image by clustering similar colors and replacing them with the centroid of the cluster.

## Compressed Image 

### 2 Colors 

![fruits-2](https://github.com/user-attachments/assets/1e243dd5-df75-49bc-842e-18a3d9b8c91a)

### 3 Colors 

![fruits-3](https://github.com/user-attachments/assets/167bd1bb-d159-45e0-a412-5f385b443f96)

### 5 Colors 

![fruits-5](https://github.com/user-attachments/assets/d6867792-1810-417b-9639-f33fe332d94e)

### 10 Colors 

![fruits-10](https://github.com/user-attachments/assets/8f292d25-7d43-4d37-88e5-e5a3acd96083)

### 20 Colors 

![fruits-20](https://github.com/user-attachments/assets/1d1b9d7b-d731-4f7f-aa61-0a8b22b2fd2e)

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
