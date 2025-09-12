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

# Exercise 2

def to_binary(n):
    '''
    Function to find binary representation
    of the input n.

    Parameters:
    n (int): The integer you want converted
    to binary.

    Return value:
    A string containing the binary
    version of the input "n".
    '''
    # For these two special cases, the function will
    # return n because the binary representation of
    # 0 and 1 are themselves.
    if n == 0:
        return "0"
    elif n == 1:
        return "1"

    # Otherwise, the function will perform recursion
    # which builds up the string containing the binary
    # number in each step.
    else:
        return to_binary(n // 2) + str(n % 2)
