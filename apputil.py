import seaborn as sns
import pandas as pd
import numpy as np

# Exercise 1

def fibonacci(n):
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
        return fibonacci(n-1) + fibonacci(n-2)

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

# Exercise 3

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Part 1: 
# Return a list of all column names, sorted such that
# the first column has the least missing values, and the last
# column has the most missing values.

switch_to_NaN = df_bellevue['gender'].loc[~df_bellevue['gender'].isin(['m', 'w'])].unique()
df_bellevue['gender'] = df_bellevue['gender'].replace(switch_to_NaN, np.nan)

def task_1():
    '''
    Function to provide user with a list of columns
    with amount of missing values in each column in
    ascending order.

    Parameters:
    No input parameters

    Return value:
    A list containing all column names sorted in
    ascending order based on how many missing
    values they have.
    '''
    # Per instructions, anything in the 'gender' column that isn't
    # a 'm' or 'w' is being treated as a missing value.
    switch_to_NaN = df_bellevue['gender'].loc[~df_bellevue['gender'].isin(['m', 'w'])].unique()
    df_bellevue['gender'] = df_bellevue['gender'].replace(switch_to_NaN, np.nan)

    # Finding the amount of null values in each column and sorting
    # the values and their respective column names into ascending
    # order.
    null_values = df_bellevue.isna().sum()
    sorted = null_values.sort_values(ascending = True)

    # Returning a sorted list of the column names only.
    return list(sorted.index)

# Part 2:
# Return a data frame with two columns:
# The year (for each year in the data), year
# The total number of entries (immigrant admissions) for
# each year, total_admissions

def task_2():
    '''
    Function to provide user with a data frame
    containing the count of admissions for
    each year

    Parameters:
    No input parameters

    Return value:
    A data frame containing the counts of
    admissions for each year in the original
    data frame.
    '''
    # Ensure the dates are in the right format and make sure
    # anything that doesn't comply with the format is dropped.
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors = 'coerce')
    df_bellevue.dropna(subset = ['date_in'], inplace = True)

    # Extract the year from the 'date_in' column.
    df_bellevue['year'] = df_bellevue['date_in'].dt.year

    # Group years together and count them up.
    entries_per_year = df_bellevue.groupby('year').size()
    entries_per_yeardf = entries_per_year.reset_index(name = 'total_admissions')

    return(entries_per_yeardf)

def task_3():
    '''
    Function to provide a series with the
    average age for each gender.

    Parameters:
    No input parameters

    Return value:
    A series containing the average age for
    both genders in the data frame.
    '''
    # Group the dataset by the gender variable.
    grouped_gender = df_bellevue.groupby('gender')

    # Get a series of the age of each group
    # and find the average of each group(gender).
    gender_series = grouped_gender['age'].mean()

    return gender_series

def task_4():
    '''
    Function to provide a list with the 5 most
    common professions from most to least.

    Parameters:
    No input parameters

    Return value:
    A list containing the names of the 5 most
    common professions by count in descending order.
    '''
    # Find the value counts of the profession column
    profession_counts = df_bellevue['profession'].value_counts()

    # Find the top 5 professions by count
    profession_list = profession_counts.index.tolist()[1:6]
    return profession_list
