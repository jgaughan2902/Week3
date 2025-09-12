import seaborn as sns
import pandas as pd

# Exercise 1

def fib(n):
    '''
    Function to find the value of the nth
    element in the Fibonacci series.

    Parameters:
    n (int): The element you want in the
    Fibonacci series.

    Return value:
    An integer representing the nth
    element in the Fibonacci series. 
    '''
    if n == 0 or n == 1:

        # This will return 0 or 1 for the first two elements
        return n
    
    else:

        # Otherwise the function will perform recursion until
        # it returns the correct value.
        return fib(n-1) + fib(n-2)
