from math import *
from time import *

  
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
    if x1 == x2 and y1 == y2:
        raise ValueError("Cannot find slope of identical points; no slope")
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

def heron(a,b,c):
    '''Gives the area of triangle when gives three side lengths

        >>> heron(1,4,8)




    '''
    
    s = (a+b+c)/2
    added = a + b
    if added < c:
        print('Not a valid input')
    if added >= c:
        area = int(sqrt((s)*(s-a)*(s-b)*(s-c)))
        return area

 


    


def main():
    print("Hello welcome to Ethan's Math Helper")
    print("In this math helper you can use the following functions:")
    while True:
        print("A. Slope")
        print("B. Pythagorean Theorem (Solving for Hypotneuse)")
        print("C. Arithmetic Last Sequence")
        print("D. Geometric Last Sequence")
        print("E. Heron's Formula")
        func = input("Which function would you like to use: ")
        if func == "a" or func == "A":
            x1 = float(input("What is the x value of your first coordinate: "))
            y1 = float(input("What is the y value of your first coordinate: "))
            x2 = float(input("What is the x value of your second coordinate: "))
            y2 = float(input("What is the y value of your second coordinate: "))
            print('The slope is {}'.format(slope(x1,y1,x2,y2)))
        elif func == "b" or func == "B":
            s1 = float(input("What is the value of the first side: "))
            s2 = float(input("What is the falue of the second side: "))
            print('The third side is equal to {}'.format(pythag(s1,s2)))
        elif func == "c" or func == "C":
            a1 = float(input("What is the first term in the sequence: "))
            n = float(input("What term are you looking for: "))
            d = float(input("What is the common difference of the sequence: "))
            print('The term you are looking for is {}'.format(arith_last(a1,n,d)))
        elif func == "d" or func == "D":
            a1 = float(input("What is the first term in the sequence: "))
            n = float(input("What is the term you are looking for: "))
            r = float(input("What is the common rate of the sequence: "))
            print("The term you are looking for is {}".format(geo_last(a1,n,r)))
        elif func == "e" or func == "E":
            a = float(input("What is the length of the first side of the triangle: "))
            b = float(input("What is the length of the second side of the triangle: "))
            c = float(input("What is the length of the third side of the trangle: "))
            print("The area of the triangle is {}".format(heron(a,b,c)))
        else:
            print ('not a valid input')
        yn = input("Would you like to use Ethan's Math Helper again? y/n: ")
        if yn == 'n' or yn == 'N':
            break
        elif yn == 'y' or yn == 'Y':
            continue
        else:
            break
        
        
    print("Thank you for using Ethan's Math Helper")
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
