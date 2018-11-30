import matplotlib.pyplot as plt
import seaborn as sns

import skimage, skimage.io, skimage.color, skimage.transform, skimage.filters

im = skimage.io.imread('Scottish_Fold.jpg')
im = skimage.color.rgb2gray(im)
# import ipdb; ipdb.set_trace()
im = skimage.transform.rescale(im, .25)
im = skimage.filters.laplace(im, ksize=10)

plt.imshow(im, cmap='gray')
plt.show()
# skimage.io.imsave('img/early/cat_log.jpg', im)