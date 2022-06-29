import tensorflow as tf
from tensorflow import keras

import numpy as np

print(tf.__version__)


model = keras.Sequential()
model.add(keras.layers.Dense(4, activation='sigmoid'))
model.add(keras.layers.Dense(4, activation='sigmoid'))



model.compile(optimizer='adam', #'sgd'
              loss='binary_crossentropy',
              metrics=['accuracy'])
x=[[0,0],[0,1],[1,0],[1,1]]
y=[[0],[1],[1],[0]]

model.fit(x, y, batch_size=32, epochs=10)
