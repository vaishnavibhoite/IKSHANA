import cv2
import os
from keras.preprocessing.image import img_to_array


class load:
    def __init__(self):
        self.x_data=[]
        self.y_data=[]
    # def __init__(self, width, height, channels, paths):
    #     self.width = width
    #     self.height = height
    #     self.channels = channels
    #     self.paths = paths
    #     self.data = []
    #     self.labels = []

    def imgload(self):
        # i = -1
        path = 'WRITE PATH'
        ori = os.listdir(path)
        for i in ori:
            img = cv2.imread(path+'/'+i, 1)
            img = cv2.resize(img, (256, 256))
            self.x_data.append(img_to_array(img))
            # print(orig+'/'+i)
            img = cv2.imread('FOLDER NAME'+'/'+i.split('.')[0]+".png", 1)
            img = cv2.Canny(img, 100, 150)
            img = cv2.dilate(img, None, iterations=5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.resize(img, (256, 256))
            # print(seg+'/'+i)
            self.y_data.append(img_to_array(img))
            # self.x_data.append(img_to_array(img))
            # self.x_data.append(img_to_array(img_noise))

        return self.x_data, self.y_data
        # for folder in self.paths:
        #     i = i+1
            
        #     path = str(folder[0])
        #     folder = os.listdir(path)
            
        #     for file in folder:
        #         # print(file+" "+str(i))
        #         img = cv2.imread(path+'/'+file, -1)
                
        #         img = cv2.resize(img, (self.width, self.height))
        #         img = img_to_array(img)
        #         self.data.append(img)
        #         self.labels.append(i)
                
        # return self.data, self.labels