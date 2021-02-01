#This is the test code to check the neuron2 weights

import numpy as np
input_features=[3 , 8, 7]

weight_hidden =[[ 0.0195378,   0.64192783,  0.51226266,  1.11792818],
                [-0.34186876, -0.75103503, -0.09507995,  0.79968335],
                [-0.22615683, -0.49195619, -0.07006987,  0.54533509]]
weight_output =[[-7.86273392], [ 2.3996796 ], [ 4.53925934], [-3.47506371]]




# Sigmoid function :
def sigmoid(x):
   return 1/(1+np.exp(-x))


 # Input for hidden layer :
input_hidden = np.dot(input_features, weight_hidden)
 
 # Output from hidden layer :
output_hidden = sigmoid(input_hidden)
 
 # Input for output layer :
input_op = np.dot(output_hidden, weight_output)
 
 # Output from output layer :
output_op = sigmoid(input_op)

print(output_op)



