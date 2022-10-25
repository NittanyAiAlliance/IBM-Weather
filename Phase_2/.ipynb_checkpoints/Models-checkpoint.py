from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Activation, Permute, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, Conv3D
from tensorflow.keras.layers import SeparableConv2D, DepthwiseConv2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import SpatialDropout2D
from tensorflow.keras.regularizers import l1_l2
from tensorflow.keras.layers import Input, Flatten
from tensorflow.keras.constraints import max_norm
from tensorflow.keras import backend as K
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame as df


def OneFeatCNNModel(months, latNum, lonNum,
             dropoutRate = 0.5, spatialKernelShape = (5,5), 
             C1 = 4, S1 = 4, norm_rate = 0.25, dropoutType = 'Dropout'):
    dropoutType = Dropout
    input1   = Input(shape = (latNum, lonNum, months))

    ##################################################################
    block1 = MaxPooling2D((4, 4), padding='valid',strides = (4,4))(input1)
    block1 = Conv2D(filters = 4, kernel_size = spatialKernelShape, padding = 'same',strides = (1,1),
                                   input_shape = (latNum, lonNum, months),
                                   use_bias = False)(input1)
    block1 = Conv2D(filters = C1, kernel_size = (1,1))(block1)
    block1 = Activation('leaky_relu')(block1)
    block1 = AveragePooling2D((4, 4),padding='same',strides = (4,4))(block1)
        
    block2 = SeparableConv2D(S1, (4,4),
                                   use_bias = True, padding = 'valid')(block1)
    block2       = Activation('leaky_relu')(block2)
    flatten = Flatten()(block2)
    
    dense1 = Dense(10,activation = 'leaky_relu')(flatten)
    dense2 = Dense(1, activation = 'linear')(dense1)
    
    return Model(inputs=input1, outputs=dense2)