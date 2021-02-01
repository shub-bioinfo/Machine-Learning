
#This is the basic program to run the NN with two layes: one hidden and one output layer.

# Import required libraries :
import numpy as np# Define input features :
input_features = np.array([[1,7,3],[2,8,4],[3,9,3],[4,6,5],[5,4,5],[6,4,5],[7,6,1],[8,5,3],
                           [1,4,2],[2,5,3],[3,4,8],[4,3,1],[5,1,2],[6,6,3],[7,1,9],[8,3,2]])
print (input_features.shape)
print (input_features)# Define target output :
target_output = np.array([[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,]])# Reshaping our target output into vector :
target_output = target_output.reshape(16,1)
print(target_output.shape)
print (target_output)

# Define weights :
# 6 for hidden layer
# 3 for output layer
# 9 total
weight_hidden = np.array([[0.1,0.2,0.3,0.7],[0.4,0.5,0.6,0.4],[0.1,0.2,0.1,0.3]])
weight_output = np.array([[0.7],[0.8],[0.9],[0.2]])

# Learning Rate :
lr = 0.05

# Sigmoid function :
def sigmoid(x):
   return 1/(1+np.exp(-x))

# Derivative of sigmoid function :
def sigmoid_der(x):
   return sigmoid(x)*(1-sigmoid(x))

file =open("error2.dat", 'w')

for epoch in range(200000):

 # Input for hidden layer :
   input_hidden = np.dot(input_features, weight_hidden)
 
 # Output from hidden layer :
   output_hidden = sigmoid(input_hidden)
 
 # Input for output layer :
   input_op = np.dot(output_hidden, weight_output)
 
 # Output from output layer :
   output_op = sigmoid(input_op)

#==========================================================
 # Phase1
 
 # Calculating Mean Squared Error :
   error_out = ((1 / 2) * (np.power((output_op  - target_output), 2)))
   error_final = error_out.sum()
   file.write("%d % 9.8f \n" % (epoch, error_final))

 
 # Derivatives for phase 1 :
   derror_douto = output_op - target_output
   douto_dino = sigmoid_der(input_op) 
   dino_dwo = output_hidden
   derror_dwo = np.dot(dino_dwo.T, derror_douto * douto_dino)

#===========================================================
 # Phase 2 
 # derror_w1 = derror_douth * douth_dinh * dinh_dw1
 # derror_douth = derror_dino * dino_outh
 
 # Derivatives for phase 2 :
   derror_dino = derror_douto * douto_dino
   dino_douth = weight_output
   derror_douth = np.dot(derror_dino , dino_douth.T)
   douth_dinh = sigmoid_der(input_hidden) 
   dinh_dwh = input_features
   derror_wh = np.dot(dinh_dwh.T, douth_dinh * derror_douth)# Update Weights
   weight_hidden -= lr * derror_wh
   weight_output -= lr * derror_dwo

print("\n#-------------------------------------------------\n" )
print("\nModified weights for hidden layer.\n" )
print(weight_hidden)
print("\nModified weights for output layer.\n" )
print(weight_output)
print("\n#-------------------------------------------------\n" )

print("\nderror_douto " )
print( derror_douto )
print( derror_douto.shape )
print("\ndino_dwo " )
print( douto_dino )
print( douto_dino.shape )
print("\ndno_dwo " )
print( dino_dwo )
print( dino_dwo.shape )
print("\nderror_dwo " )
print( derror_dwo )
print( derror_dwo.shape )
print("\nderror_dino = derror_douto * douto_dino") 
print( derror_dino )
print( derror_dino.shape )
print("\nweight outpout: dino_douth")
print( dino_douth ) 
print( dino_douth.shape ) 
print("\n derror_douth = np.dot(derror_dino , dino_douth.T) ") 
print( derror_douth )
print( derror_douth.shape )
print("\ndouth_dinh")
print(douth_dinh)
print("\ndinh_dwh")
print(dinh_dwh)
print("\nderror_wh")
print(derror_wh)



print("\nInput features " )
print( input_features)
print("\nInput for Hidden layer " )
print( input_hidden)
print("\nOutput for hidden layer "  )
print( output_hidden)
