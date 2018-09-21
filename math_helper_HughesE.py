from math import *
    

  
def slope(x1,y1,x2,y2):
    ''' Finds how much x increases/decreases and y
        increases/decreases as a line advancess
        
        >>> slope(0,0,1,1)
        1.0
        >>> slope(3,4,5,2)
        -1.0
        >>> slope(6,2,6,5)
        'Undefined'
        >>> slope(5,8,3,0) 
        4.0
        
    
    ''' 
    y = y1-y2
    x = x1-x2
    if x == 0:
        return "Undefined"
    slope = y/x
    return slope

def pythag(a,b):
    ''' With given two sides of a triangle you will be
        able to find the length of the third side
        
        >>> pythag(7,24)
        25.0
        
        >>> pythag(-3,4)
        Error?
        
    '''
    c = (a**2)+(b**2)
    c = sqrt(c)
    return c

def arith_last(a1,n,d):
    ''' Gives the nth term in a sequence that is
        arithmetic(addition)
        
        >>> arith_last(2,15,3)
        44
        
        >>> arith_last(1,-10,12)
        Error?
        
        
    '''
    an = a1 + ((n-1)*d)
    return an

def geo_last(a1,n,r):
    ''' Gives the nth term in a sequence that is
        geometric(multiplication)
    
        >>> geo_last(4,5,3)
        324
    
        >>> geo_last(2,-8,3)
        Error?
    
    '''
    an = a1*(r**(n-1))
    return an

 


    


def main():
    return

if __name__ == "__main__":
    #main()
    import doctest
    doctest.testmod()
