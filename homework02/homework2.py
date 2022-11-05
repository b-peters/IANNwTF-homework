import numpy as np

# An array of inputs between 0 and 1
x = np.random.random_sample(100)

# Initializes an empty array of targets
t = np.empty(0)

# An array of targets
for i in x:
    values = i**3-i**2
    t = np.append(t, values)

class Layer:
    """A class for any given layer of the MLP."""  

    def __init__(self, n_units, input_units):
        """
        A method that specifies layer attributes.
        """
        # the number of units in the layer
        self.n_units = n_units
        # the number of units in the preceding layer
        self.input_units = input_units
        self.bias_vector = np.zeros(shape=(1, n_units))
        self.weight_matrix = np.random.uniform(low = -10, high = 10, size=(input_units, n_units))
        self.layer_input = None
        self.layer_preactivation = None
        self.layer_activation = None
    
    def forward_step(self, input):
        """
        A method that takes one unit as an input and returns each unit's activation as an output.
        """
        output = ((input @ self.weight_matrix) + self.bias_vector)
        # applies ReLU to the preactivation
        np.place(output, output <= 0, 0)
        return np.reshape(output, -1)

# Creates an instance of an example object of the Layer class
Layer1 = Layer(n_units = 10, input_units = 100)

print(Layer.forward_step(Layer1, x))

   # def backward_step(self):

