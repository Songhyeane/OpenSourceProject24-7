import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../resource/image2.png')

med_val = np.median(img)
lower = int(max(0, 0.7* med_val))
upper = int(min(255,1.3 * med_val))
edges = cv2.Canny(image=img, threshold1=lower , threshold2=upper)

blurred_img = cv2.blur(img,ksize=(5,5))

edges = cv2.Canny(image=blurred_img, threshold1=lower , threshold2=upper-50)

edges = cv2.resize(edges, dsize=(200, 200), interpolation=cv2.INTER_AREA)

print(edges.nonzero())

plt.imshow(edges)

plt.show()

np.savetxt('test.txt', edges, fmt = '%2d', delimiter = ',', header='test')

edges[edges != 0] = 1

np.savetxt('test_1.txt', edges, fmt = '%2d', delimiter = ',', header='test')






def get_outline(filepass) :
    img = cv2.imread('../resource/img.png')

    med_val = np.median(img)

    lower = int(max(0, 0.7 * med_val))
    upper = int(min(255, 1.3 * med_val))

    blurred_img = cv2.blur(img, ksize=(5, 5))

    edges = cv2.Canny(image=blurred_img, threshold1=0, threshold2=upper + 50)

    edges = cv2.resize(edges, dsize=(200, 200), interpolation=cv2.INTER_AREA)

    return edges