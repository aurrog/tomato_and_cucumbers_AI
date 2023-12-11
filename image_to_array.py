# from PIL import Image
# import numpy as np
# import os
# import json
#
# class NumpyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return json.JSONEncoder.default(self, obj)
#
# # img = Image.open('Cucumber/Image_1.jpg')
# # img = img.resize((90, 90))
# # img = img.convert('L')
# # # img.show()
# # arr = np.asarray(img, dtype='uint8')
# # print(arr.shape)
# # # Заппустить в цикл и сохранить сброку массивов в json
# #TOMATO ----- 0
# #CUCUMBER --- 1
# array_y = np.array([])
# path = 'Tomato'
# array_main = []
# for root, dirs, files in os.walk(path):
#     for filename in files:
#         # print(path+'/'+filename)
#         file = path+'/'+filename
#         img = Image.open(file)
#         img = img.resize((90, 90))
#         img = img.convert('L')
#         # array_main = np.append(array_main, np.asarray(img, dtype='uint8'))
#         array_main.append(np.asarray(img, dtype='uint8'))
#         array_y = np.append(array_y, 0)
#
# path2='Cucumber'
# for root, dirs, files in os.walk(path2):
#     for filename in files:
#         # print(path+'/'+filename)
#         file = path2+'/'+filename
#         img = Image.open(file)
#         img = img.resize((90, 90))
#         img = img.convert('L')
#         # array_main = np.append(array_main, np.asarray(img, dtype='uint8'))
#         array_main.append(np.asarray(img, dtype='uint8'))
#         array_y = np.append(array_y, 1)
#
import os
from PIL import Image
#
# path1 = 'Cucumber/'
# new_path = 'cucumber_short/'
# for root, dirs, files in os.walk(path1):
#     for filename in files:
#         file = path1+filename
#         img = Image.open(file).resize((90, 90)).convert('L')
#         save_path = new_path+filename
#         img.save(save_path)


# a = r'C:/Users/aurrog/PycharmProjects/tomato_and_cucumbers_AI/tomato_and_cucumbers_AI/cucumber_short/'
for root, dirs, files in os.walk('cucumber_short/'):
    print(files)