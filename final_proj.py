

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


print( readFile( 'income.py' ) )
