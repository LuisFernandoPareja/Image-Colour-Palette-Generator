from sklearn.cluster import KMeans
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def gen_color_palette(img):
    # READ IMAGE AND CONVERT TO BGR
    img = cv.imread('static/assets/OnePunchMan.jpg')
    dim = (int(img.shape[1]*0.5), int(img.shape[0]*0.5))
    img = cv.resize(img, dim)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # RESHAPE IMG FOR TRAINING
    reshaped_img = img.reshape(-1, 3)

    clt = KMeans(n_clusters=5)
    clt.fit(reshaped_img)

    # GET THE PALETTE
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clt.cluster_centers_.shape[0]
    for idx, centers in enumerate(clt.cluster_centers_):
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers

    print(clt.cluster_centers_)
    # SHOW IMAGE WITH PALETTE
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img)
    ax[1].imshow(palette)
    ax[0].axis('off')  # hide the axis
    ax[1].axis('off')
    f.tight_layout()

    # plt.show()

    palette_list = []
    for color_pixel in range(len(clt.cluster_centers_)):
        palette_list.append(clt.cluster_centers_[color_pixel])

    return palette_list

# cv.waitKey(0)
