# Implementing ANNs with TensorFlow - Homework 06

## Assignment: CIFAR-10 Classification (Part II)

We used five optimisation techniques in order to find out whether and how much they improve our training results compared to the base model.
Note that we only use a subset of the training examples, so our results might not be as good as with the full dataset.

Our base model achieves slightly under 60% accuracy on the test data.

### 1) Data Augmentation

We augment the data by adding random transformations to the images in the form of horizontal rotations. These transformations aim to improve the generalisation
of the model by diversifying the training data.

We used the augmented data with our base model, but could not see improvements in the test loss. At the same time, the accuracy of the model dropped noticeably. 

### 2) L2 kernel regularization

The L2 kernel regularizer applies a penalty in the form of `loss = l2 * reduce_sum(square(x))` to the loss function, and hereby to the weights of the layers.
This is an effort to reduce overfitting to the training data and improve generalization on unseen data.

### 3) Glorot Normal kernel initializer

The Glorot Normal kernel initializer helps us to achieve a better initialization of the weights. In this case, the weights will be randomly initialized with
a mean of zero and a variance depending on the number of input and output units of the weight tensor. Diverse weight values at the start of the training are
supposed to prevent the introduction of symmetries in the weights of a layer.

### 4) Dropout

This technique is a measure against overfitting which randomly sets some inputs to a layer to 0 during the training stage. Meanwhile, the other inputs are 
scaled up such that the sum over all inputs remains unchanged. Naturally, this forces rearrangements to the structure of the weights of a layer, reducing
overfitting as a result.

We set the frequence of the dropout to 0.1 in our respective test model, and use dropout layers between the Conv2D layers. We could observe a reduction in training
and test loss, while also recording a slight improvement regarding the accuracy.

### 5) Batch normalization

Batch normalization aims to extinguish vanishing or exploding gradients, which would severely impact the training process in a negative manner. It normalizes the
activations to each layer, so they roughly follow a standard normal distribution.

As a test, we introduced two batch-norm layers between Conv2D layers of our base model. This model had the "best" accuracy (still low) of the tested models.
