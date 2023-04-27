import numpy as np

def gradient_descent(x,y):

# This is according to the linear regression function -> ax + b = for only one feature(x)
    a_curr = b_curr = 0
    iterations = 10
    n = len(x)
    learning_rate = 0.02

    for i in range(iterations):
# The linear regression function
        y_predicted = a_curr * x + b_curr

# The loss function for the linear regression
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

# Calculate the Gradient by derivative the both targeted values (a,b)
        ad = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)

# Calculate the Gradient Descent by updating targeted values according to the loss function results
        a_curr = a_curr - learning_rate * ad
        b_curr = b_curr - learning_rate * bd

        print ("m {}, b {}, cost {} iteration {}".format(a_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)