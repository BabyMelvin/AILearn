import numpy as np
import matplotlib.pyplot as plt
from isort.profiles import plone
from matplotlib.lines import lineStyles
from scipy.ndimage import label

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()

# show image
from matplotlib.image import imread
img = imread('chatgpt.jpg')
# plt.imshow(img)

plt.show()

