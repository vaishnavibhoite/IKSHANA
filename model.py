import os
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as keras


class Models:
    def init(self, w, h, c):
        self.w = w
        self.h = h
        self.c = c

    def arch1(self):
        inp = Input(shape=(self.w, self.h, self.c))
        enc = Conv2D(64, (3, 3), padding='same')(inp)
        enc = BatchNormalization()(enc)
        enc = LeakyReLU(alpha=0.1)(enc)
        enc = MaxPooling2D(pool_size=(2, 2))(enc)
        enc = Conv2D(32, (3, 3), padding='same')(enc)
        enc = LeakyReLU(alpha=0.1)(enc)
        enc = BatchNormalization()(enc)
        

        dec = Conv2D(8, (3, 3), padding='same')(enc)
        dec = LeakyReLU(alpha=0.1)(dec)
        dec = UpSampling2D((2, 2))(dec)
        dec = Conv2D(16, (3, 3), padding='same')(dec)
        dec = LeakyReLU(alpha=0.1)(dec)
        dec = UpSampling2D((2, 2))(dec)
       
        final = Conv2D(3, (3, 3), padding='same', activation='sigmoid')(dec)
        auto = Model(inp, final)
        return auto

    
    def arch2(self,input_size = (256,256,3)):
        inputs = Input(input_size)
        conv1 = Conv2D(8, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(inputs)
        conv1 = Conv2D(8, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv1)
        pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
        conv2 = Conv2D(16, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool1)
        conv2 = Conv2D(16, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv2)
        pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
        conv3 = Conv2D(32, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool2)
        conv3 = Conv2D(32, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv3)
        pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
        conv4 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool3)
        conv4 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv4)
        drop4 = Dropout(0.5)(conv4)
        pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

       

        conv10 = Conv2D(3, 1, activation='sigmoid')(conv9)

        model = Model(input=inputs, output=conv10)
        model.summary()
        return model
