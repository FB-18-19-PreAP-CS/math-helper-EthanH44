from math import *
    

  
def slope(x1,y1,x2,y2):
    ''' Finds how much x increases/decreases and y
        increases/decreases as a line advancess
        
        >>> slope(0,0,1,1)
        '1.0'
        >>> slope(3,4,5,2)
        '-1.0'
        >>> slope(6,2,6,5)
        Traceback (most recent call last):
            ...
        ValueError: Denominator cannot equal 0; undefined
        >>> slope(5,8,3,0) 
        '4.0'
        >>> slope(-2,3,10,-8)
        '-0.9'
    
    ''' 
    y = y1-y2
    x = x1-x2
    if x == 0:
        raise ValueError("Denominator cannot equal 0; undefined")
    slope = y/x
    return f'{slope:.1f}'

def pythag(a,b):
    ''' With given two sides of a triangle you will be
        able to find the length of the third side
        
        >>> pythag(7,24)
        '25.0'
        >>> pythag(3,4)
        '5.0'
        >>> pythag(8,15)
        '17.0'
        >>> pythag(6,18)
        '19.0'
        >>> pythag(4,12)
        '12.6'
        
    '''
    c = (a**2)+(b**2)
    c = sqrt(c)
    
    return f'{c:.1f}'

def arith_last(a1,n,d):
    ''' Gives the nth term in a sequence that is
        arithmetic(addition)
        
        >>> arith_last(2,15,3)
        44
        >>> arith_last(3,12,8)
        91
        >>> arith_last(1,20,3.5)
        67.5
        >>> arith_last(3.75,17,2.5)
        43.75
        >>> arith_last(-23, -7, 3.5)
        -51.0
    '''
    an = a1 + ((n-1)*d)
    return an

def geo_last(a1,n,r):
    ''' Gives the nth term in a sequence that is
        geometric(multiplication)
    
        >>> geo_last(4,5,3)
        324
        >>> geo_last(6,6,3.5)
        3151.3125
        >>> geo_last(-3,4,6)
        -648
        >>> geo_last(3,-3,8)
        0.000732421875
        >>> geo_last(-4,3,-6)
        -144
    '''
    an = a1*(r**(n-1))
    return an

 


    


def main():
    print("Hello welcome to Ethan's Math Helper")
    print("In this math helper you can use the following functions:")
    while True:
        print("a. Slope")
        print("b. Pythagorean Theorem")
        print("c. Arithmetic Last Sequence")
        print("d. Geometric Last Sequence")
        print("e. Quit")
        func = input("Which function would you like to use: ")
        if func == "a":
            x1 = input("What is the x value of your first coordinate: ")
            y1 = input("What is the y value of your first coordinate: ")
            x2 = input("What is the x value of your second coordinate: ")
            y2 = input("What is the y value o fyour second coordinate: ")
            slope(x1,y1,x2,y2)
        if func == "e":
            break
    print("Thank you for using Ethan's Math Helper")
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
