import numpy as np
import matplotlib.pyplot as plt

def get_function(x):
    return eval(f)

def definite_integral(f, x0, x1, N, toDisplay=True):
    """ Approximates the definite integral of f(x)dx between lower limit x0
    and upper limit x1.
    Args:
    f: function that is DEFINED within the given range
    x0: lower limit of definite integral
    x1: upper limit of definite integral
    """
    X = np.arange(x0, x1, 0.1)
    Y = f(X)
    f_max = max(Y)
    f_min = min(0, min(Y))

    def determine_below_and_above_points(X, Y):
        """ Determines the positive and negative points that are within the function plot
         and x axis, and the points that are outside of the function plot and x axis.
        Args:
        X: Random x values to evaluate in given function.
        Y: Random y values to compare with function evaluation results with given x values.
        """
        positives, negatives, outs = (list() for i in range(3))
        for i in range(len(X)):
            x = f(X[i]) ; y = Y[i]
            if x <= 0 and y <= 0 and y >= x:
                negatives.append(i)
            elif x > 0 and y > 0 and y < x:
                positives.append(i)
            else:
                outs.append(i)
        return np.asarray(positives), np.asarray(negatives), np.asarray(outs)

    # Generating random x values between x0 and x1 to evaluate in given function.
    random_Xs = x0 + np.random.random(N) * (x1 - x0)

    # Generating random y values between f_min and f_max to compare with the results from the function evaluation.
    random_Ys = f_min + np.random.random(N) * (f_max - f_min)

    # Determine the indices of the points above, below and outside of the function plot.
    positive_indices, negative_indices, outside_indices = determine_below_and_above_points(random_Xs, random_Ys)

    # Result of the integral
    result = (f_max - f_min) * (x1 - x0) * len(positive_indices) / N - ((f_max - f_min) * (x1 - x0) * len(negative_indices) / N)
    
    if toDisplay:
        # Displaying the results of random choices
        posivites, negatives, outs = (None for i in range(3))
        plot_tuple, desc_tuple = (None for i in range(2))
        plt.plot(X, Y, color="red")
        if positive_indices.size > 0:
            positives = plt.scatter(random_Xs[positive_indices], random_Ys[positive_indices], color="green")
            plot_tuple = (positives,) ; desc_tuple = ("Positive vls.",)
            
        if negative_indices.size > 0:
            negatives = plt.scatter(random_Xs[negative_indices], random_Ys[negative_indices], color="yellow")
            plot_tuple = (*plot_tuple, negatives) ; desc_tuple = (*desc_tuple, "Negative vls.")
            
        if outside_indices.size > 0:
            outs = plt.scatter(random_Xs[outside_indices], random_Ys[outside_indices], color="blue")
            plot_tuple = (*plot_tuple, outs) ; desc_tuple = (*desc_tuple, "Points outside")
            
        plt.legend(plot_tuple, desc_tuple, loc="lower right", ncol=3, fontsize=10)
        print("Number of points outside the function plot:", len(outside_indices))
        print("Rectangle area:", (f_max - f_min) * (x1 - x0))
        print("Value of the function:", result)
    return result

#########################--DEFINITE INTEGRAL--#################################
def integral():
#   Asking user for input
    global f
    f = input('Enter the function to integrate: ')
    lower_limit = float(input('Enter the lower limit: '))
    upper_limit = float(input('Enter the upper limit: '))
    
    result = definite_integral(get_function, lower_limit, upper_limit, 100000)
    print(result)
    
#########################--MEAN VALUE OF A FUNCTION--##########################
def function_mean():
#   Asking user for input
    global f
    f = input('Enter the function to integrate: ')
    lower_limit = float(input('Enter the lower limit: '))
    upper_limit = float(input('Enter the upper limit: '))
    result = (1/(upper_limit-lower_limit)) * definite_integral(get_function, lower_limit, upper_limit, 100000)
    print(result)

#########################--COMPUTING ln(x) VALUE--#############################
def ln():
#   Asking user for input
    x = float(input('Enter x for ln(x): '))
    global f
    f = "1/x"
    if x > 0 and x < 1:
        result = definite_integral(get_function, x, 1, 100000, False)
    else :
        result = definite_integral(get_function, 1, x, 100000, False)
    print(result)

#########################--COMPUTING logy(x) VALUE--###########################
def logy():  
#   Asking user for input
    base = float(input('Enter base (y) value for logy(x): '))
    x = float(input("Enter value for x: "))
    global f
    f = "1/x"
    result = definite_integral(get_function, 1, x, 100000, False) / definite_integral(get_function, 1, base, 100000, False)
    print("log" + str(base) + "(" + str(x) + ") = " + str(result))

#########################--COMPUTING exp(x) VALUE--############################
def exp():
#   Asking user for input
    x = float(input("Enter the value of x for exp(x): "))
    global f
    f = "np.exp(x)"
    result = definite_integral(get_function, 0, x, 100000, False) + 1
    print("exp(x) =", str(result))

#########################--COMPUTING x**y VALUE--##############################
def power():
#   Asking user for input
    x = float(input('Enter base value for x**y: '))
    y = float(input('Enter exponent value for x**y: '))
    bothInt = round(x) == x and round(y) == y
    global f
    f = "1/x"
    exponent = y * definite_integral(get_function, 1, x, 1000000, False)
    f = "np.e**x"
    result = definite_integral(get_function, 0, exponent, 1000000, False) + 1
    if bothInt: result = int(round(result))
    print(result)

#integral()
#function_mean()
ln()
#logy()
#exp()
#power()
