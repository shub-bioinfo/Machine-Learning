import numpy as np

# Define the true probability distribution
p_true = np.array([2/5, 3/5])

# Define the Bernoulli approximation
p_approx = np.array([0.5])

#To get the true entropy
#H(P) = - P(0) * log2(P(0)) - P(1) * log2(P(1))
H_true = - (2/5) * np.log2(2/5) - (3/5) * np.log2(3/5) 


# Define the objective function to minimize
def kl_divergence(p):
    return p_true[0] * np.log2(p_true[0] / p) + p_true[1] * np.log2(p_true[1] / (1-p))

# Define the gradient of the objective function
def kl_gradient(p):
    return -(p_true[0] / p) + (p_true[1] / (1-p))

# Use gradient descent to optimize the approximation
learning_rate = 0.1
num_iterations = 1000
for i in range(num_iterations):
    gradient = kl_gradient(p_approx)
    p_approx -= learning_rate * gradient

# Calculate the estimated entropy
p1 = p_approx[0]
p0 = 1 - p1
h_approx = - p0 * np.log2(p0) - p1 * np.log2(p1)
print("True entropy:", H_true)
print("Variational entropy:", h_approx)
