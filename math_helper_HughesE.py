from math import *
    

  
def slope(x1,y1,x2,y2):
    ''' Finds how much x increases/decreases and y
        increases/decreases as a line advancess
        
        >>> slope(0,0,1,1)
        1.0
    
        
    
    ''' 
    y = y1-y2
    x = x1-x2
    if x == 0:
        return "False, 0 for denominator is undefined"
    slope = y/x
    return slope

def pythag(a,b):
    ''' With given two sides of a triangle you will be
        able to find the length of the third side '''
    c = (a**2)+(b**2)
    c = sqrt(c)
    return c

def arithmetic_last(a1,n,d):
    ''' Gives the nth term in a sequence that is
        arithmetic(addition) '''
    an = a1 + ((n-1)*d)
    return an

def geo_last(a1,n,r):
    ''' Gives the nth term in a sequence that is
        geometric(multiplication) '''
    an = a1*(r**(n-1))
    return an


    
    
def add(x,y):
    a = x+y
    print(a)

def main():
    return

if __name__ == "__main__":
    #main()
    import doctest
    doctest.testmod()
