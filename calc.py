""" This file is an implementation file for a example calculator """

def add(x,y):
  """ Returns sum of function x and y """  
  return x + y
  
def pow(x,y):
  """returns the value of x to the power of y(x^y)"""
  res = 1 
  for _ in range(y):
    res *= x

def multiply (x, y):
  """ Returns the multiple of x and y """
  return x*y

def divide(x,y):
  """ Divides number x by number y"""
  if (y == 0):
        if(x == 0):
            print("Result is undefined")
        else:
            print("Can not divide by zero")
    else:
        result = x/y
        print("X divided by Y = ", result)

def input_num():
    print("Enter two numbers")
    x = int(input("X: "))
    y = int(input("Y: "))
    return x,y

if __name__ == '__main__':
    print("Calculator\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Area of Circle")
    option = int(input("Enter index of function, you want to calculate: "))
       
    if (option == 1):
        x,y = input_num()
        add(x,y)
    #elif (option == 2):
        # subtract
    elif (option == 3):
        x,y = input_num()
        multiply(x,y)
    elif (option == 4):
        x,y  = input_num()
        divide(x,y)
    elif (option == 5):
        x,y = input_num()
        pow(x,y)
    #elif (option == 6):
        # area of circle
    else:
        print("Invalid input")


