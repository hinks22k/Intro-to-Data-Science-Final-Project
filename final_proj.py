import requests
from math import sqrt
from functools import reduce

def readFile( fileName ):
    """
    reads the file and returns the contents in a string
    """
    file = open( fileName, 'r' )
    line = file.readline()
    while line:
        print( line )
        line = file.readline()
    file.close()

def mean( lst ):
    """
    mean takes a single argument, a list of numbers, \
    and returns the mean value for the numbers in that list.
    """
    return( sum( lst ) / len( lst ) )

# may be wrong
def variance( lst ):
    """
    variance takes a list of numbers and returns the \
    population variance within that list.
    """
    meanOfList = mean( lst )
    # subtracts num in list from average and squares it
    # places that number into a new list
    sumOfDifferences = map( lambda x: ( x - meanOfList ) ** 2, lst )
    return mean( list( sumOfDifferences ) )

def standard_deviation( lst ):
    return sqrt( variance( lst ) )

def myMin( lst ):
    """
    myMin takes a list of numbers as its argument and \
    returns the minimum value in the list.
    """
    # Using reduce and the < sign to return the min value
    return reduce( lambda x,y: x if x < y else y, lst)

def myMax( lst ):
    """
    myMax takes a list of numbers as its argument and \
    returns the maximum value in the list.
    """
    # Using reduce and the > sign to return the max value
    return reduce( lambda x,y: x if x > y else y, lst)

def filterOutMinMax( lst ):
    """
    filterOutMinMax takes a single list of numbers as its only argument. \
    filterOutMinMax should return a list that has the same elements as \
    the original list except for the original’s min and max values.
    """
    minOfList = myMin( lst )
    maxOfList = myMax( lst )
    # filter out the min and max values of the list
    return list( filter( lambda x: x != minOfList and x != maxOfList, lst ) )
