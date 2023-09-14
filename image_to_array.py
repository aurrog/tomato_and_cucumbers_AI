from PIL import Image
import numpy as np


img = Image.open('../Cucumber/Image_1.jpg')
img = img.resize((90, 90))
img = img.convert('L')
# img.show()
arr = np.asarray(img, dtype='uint8')
print(arr.shape)