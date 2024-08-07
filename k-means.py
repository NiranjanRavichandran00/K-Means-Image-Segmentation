from matplotlib import pyplot as io
import numpy as np
from PIL import Image
import sys
import os

def kmeans(X, k):

    # Pick random points as centroids
    
    #Get all indexes in image
    indices  = []
    for i in range(X.shape[0]):
        indices.append(i)
    
    #Shuffle the list of indexes
    np.random.shuffle(indices)

    #Pick k indexes and get their value in image
    centroids = X[indices[:k]]

    labels = np.zeros(X.shape[0])
    count = 0

    #Stop at 100 iterations if not converged
    while count < 100:

        distances_squared = np.zeros((X.shape[0], k))

        for i in range(X.shape[0]): 
            for j in range(k):  
                distances_squared[i, j] = np.sum((X[i] - centroids[j]) ** 2)
 
        new_labels = np.argmin(distances_squared, axis=1)

        # Check for convergence
        if np.array_equal(new_labels, labels):
            break

        labels = new_labels

        centroids = np.zeros((k, X.shape[1]))

        #Iterate through cluster 
        for i in range(k):
            update_cluster = []
            for j in range(X.shape[0]):
                if labels[j] == i:
                    update_cluster.append(X[j])

            update_cluster = np.array(update_cluster)

            if len(update_cluster) > 0:
                centroids[i] = np.mean(update_cluster, axis=0)

        centroids = np.array(centroids)
        count = count + 1

    return centroids.astype(np.uint8), labels


# Some Basic input validation
if not os.path.exists(sys.argv[1]):
    print("Input Image File path Invalid/Does not exist, Try again")
    sys.exit(0)

flag = True
try:
    int(sys.argv[2])
except ValueError:
    flag = False

if not flag:
    print("Please enter a valid integer for k-value")
    sys.exit(0)

directory = os.path.dirname(sys.argv[1])
filename, file_extension = os.path.splitext(os.path.basename(sys.argv[1]))

# Image to array
img1 = io.imread(sys.argv[1]) 

# Apply K-Means algorithm on image array 
final_centroids, cluster_labels = kmeans(img1.reshape((-1, 3)), int(sys.argv[2])) 
array = final_centroids[cluster_labels].reshape(img1.shape)

#Array to image file
img2 = Image.fromarray(array)
img2.save(f'{directory}/{filename}-{sys.argv[2]}.png')