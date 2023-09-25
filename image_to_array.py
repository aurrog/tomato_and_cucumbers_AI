from PIL import Image
import numpy as np
import os
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# img = Image.open('Cucumber/Image_1.jpg')
# img = img.resize((90, 90))
# img = img.convert('L')
# # img.show()
# arr = np.asarray(img, dtype='uint8')
# print(arr.shape)
# # Заппустить в цикл и сохранить сброку массивов в json
path = 'Tomato'
array_main = []
for root, dirs, files in os.walk(path):
    for filename in files:
        # print(path+'/'+filename)
        file = path+'/'+filename
        img = Image.open(file)
        img = img.resize((90, 90))
        img = img.convert('L')
        # array_main = np.append(array_main, np.asarray(img, dtype='uint8'))
        array_main.append(np.asarray(img, dtype='uint8'))

# print(array_main.shape)
with open('DATA.json', 'w') as f:
    json.dump(array_main, f, cls=NumpyEncoder)
#
#
#

# import numpy as np
# # a = np.ndarray([])
# # # print(a)
# # # print(a.shape)
# # a = np.append(a, [[0, 1, 2], [0, 0, 0], [2, 2, 2]])
# # print(a.shape)
# # print(a)
# a = [
#     [[0, 1],
#     [1, 0]],
#     [[3, 4],
#      [5, 6]]
# ]
# b = np.array(a)
# print(b.shape)
# for i in b:
#     print(i)