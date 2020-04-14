from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import tensorflow as tf

# Download mnist data and slit into train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train[0].shape)

# Reshape data to fit the model
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

# One-shot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print(y_train[0])

# Create model
model = Sequential()

# Add model layers
model.add(Conv2D(64, kernel_size=3, activation="relu", input_shape=(28, 28, 1)))
model.add(Conv2D(32, kernel_size=3, activation="relu"))
model.add(Flatten())
model.add(Dense(10, activation="softmax"))

# Compile model using accuracy to measure model performance
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=3)
