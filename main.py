from keras.datasets import mnist
import numpy

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
	return fit_model

def validate(fit_model):
	text = fit_model.history
	accuracy = text['accuracy'][2]
	accuracy = accuracy * 100
	accuracy = int(accuracy)
	accuracy = str(accuracy)
	f= open("accuracy.txt","w+")
	f.write(accuracy)
	f.close()
	print(accuracy)
	return accuracy

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
neurons = 10
from keras.layers import Dense
fit_model=train_model(neurons)
accuracy = validate(fit_model)


while int(accuracy) < 90 :
	print("Model trained successfully but accuracy is less than 95%")
	fit_model=train_model(neurons+10)
	accuracy=validate(fit_model)

print("Code run successfully ")




