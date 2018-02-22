import keras
import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation,Dense

training_data = np.array([[0,0], [0,1], [1, 0], [1, 1]])

target_data = np.array([[0], [1], [1], [0]])

model = Sequential()

model.add(Dense(25, input_dim = 2, activation = "relu"))

model.add(Dense(1))

model.compile(loss = "mean_squared_error")
model.fit(training_data, target_data, epoch = 500) !!backsize, how will it change over time
model.ealuate(training-data, target_data)

print(model.predict(np.array([[0,0]])))