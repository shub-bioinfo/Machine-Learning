#Neural network for 1 neuron.
# Import required libraries:
import numpy as np

# Define input features:
input_features = np.array([[0,1],[0,0],[1,0],[1,1]])
print (input_features.shape)
print (input_features)

# Define target output:
target_output = np.array([[1,0,1,1]])

# Reshaping our target output into vector:
target_output = target_output.reshape(4,1)
print(target_output.shape)
print (target_output)

# Define weights:
weights = np.array([[0.2],[0.3]])
print(weights.shape)
print (weights)

# Bias weight:
bias = 0.5

# Learning Rate:
lr = 0.05

file =open("error1.dat", 'w')

# Sigmoid function:
def sigmoid(x):
   return 1/(1+np.exp(-x))

# Derivative of sigmoid function:
def sigmoid_der(x):
   return sigmoid(x)*(1-sigmoid(x))

  # Main logic for neural network:
   # Running our code 10000 times:
for epoch in range(20000):
   inputs = input_features

   #Feedforward input:
   in_o = np.dot(inputs, weights) + bias 

   #Feedforward output:
   out_o = sigmoid(in_o) 
   #Backpropogation#Calculating error
   error = out_o - target_output

   #Going with the formula:
   x = error.sum()
   print("This is the erro\n")
   print(x)
   file.write("%d % 9.8f \n"% (epoch, x))

   #Calculating derivative:
   derror_douto = error
   douto_dino = sigmoid_der(out_o)#Multiplying individual derivatives:
   deriv = derror_douto * douto_dino #Multiplying with the 3rd individual derivative:
   
#Finding the transpose of input_features:
   inputs = input_features.T
   deriv_final = np.dot(inputs,deriv)#Updating the weights values:
   weights -= lr * deriv_final #Updating the bias weight value:
   print("This is the weights")
   print(weights)
   for i in deriv:
      bias -= lr * i 

#Check the final values for weight and biasprint (weights)



