from math import *
    

  
def slope(x1,y1,x2,y2):
    ''' Finds how much x increases/decreases and y
        increases/decreases as a line advances ''' 
    y = y1-y2
    x = x1-x2
    slope = y/x
    return slope

def Pythag(a,b):
    ''' With given two sides of a triangle you will be
        able to find the length of the third side '''
    c = (a**2)+(b**2)
    c = sqrt(c)
    return c

def Arithmetic_last(a1,n,d):
    ''' Gives the nth term in a sequence that is
        arithmetic(addition) '''
    an = a1 + ((n-1)*d)
    return an

def Geo_last(a1,n,r):
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
    main()
