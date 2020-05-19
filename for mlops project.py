from keras.datasets import mnist
import numpy
dataset = mnist.load_data("mymnist.data")
train, test = dataset
train_X , train_y = train
test_X , test_y = test
import matplotlib.pyplot as plt
test_X = test_X.reshape(-1 , 28*28)
train_X = train_X.reshape(-1 ,  28*28)
test_X = test_X.astype("float32")
train_X = train_X.astype("float32")
from keras.utils.np_utils import to_categorical
test_y = to_categorical(test_y)
train_y = to_categorical(train_y)
from keras.models import Sequential
model = Sequential()
from keras.layers import Dense
train_model(70)
model.save("number detection model.pk1")
text = fit_model.history
accuracy = text['accuracy'][2]
accuracy = accuracy * 100
accuracy = int(accuracy)
accuracy = str(accuracy)
f= open("accuracy.txt","w+")
f.write(accuracy)
f.close()
print(accuracy)
print("Code run successfully ")




def train_model(neurons) : 
	model.add(Dense(units = neurons , input_dim = 28*28 , activation = 'relu'))
	model.summary()
	model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))
	model.summary()
	model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
	model.summary()
	model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
	model.summary()
	from keras.optimizers import Adam
	model.compile( optimizer= "Adam" , loss='categorical_crossentropy', 
	             metrics=['accuracy'] )
	fit_model = model.fit(train_X ,  train_y , epochs = 3)
if accuracy < 98 