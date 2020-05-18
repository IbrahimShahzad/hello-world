""" This file is an implementation file for a example calculator """

def add(x,y):
  """ Returns sum of function x and y """  
  return x + y
  
def pow(x,y):
  """returns the value of x to the power of y(x^y)"""
  res = 1 
  for _ in range(y):
    res *= x
    
def subtract(x,y):
  """ Returns difference of function x and y """  
  return x - y    

