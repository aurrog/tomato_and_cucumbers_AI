from PIL import Image
import numpy as np
import os

img = Image.open('Cucumber/Image_1.jpg')
img = img.resize((90, 90))
img = img.convert('L')
# img.show()
arr = np.asarray(img, dtype='uint8')
print(arr.shape)
# Заппустить в цикл и сохранить сброку массивов в json
path = 'Tomato'
for root, dirs, files in os.walk(path):
    for filename in files:
        print(path+'/'+filename)
