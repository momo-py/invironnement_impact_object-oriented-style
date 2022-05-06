
def approxEqual(X, Y, RelativeEpsilon, AbsoluteEspilon):
  
  
  absX = abs(X)
  absY = abs(Y)
  absdiff = abs(X-Y)
  if (X == Y):
    # Shortcut, handles infinities and the case where both X and Y are exactly 0
    return True
  elif absdiff <= AbsoluteEspilon:
    # The idea of relative difference breaks down near zero.
    # Near zero, it is better to use the absolute difference.
    return True
  else:
    # Use relative error
    largest = max(absX, absY) # if X or Y is exactly 0, we divide by the other one
    return ((absdiff / largest) < RelativeEpsilon)


def approxEqualVect(V1, V2, RelativeEpsilon, AbsoluteEspilon):
  
  
  if len(V1) != len(V2):
    return False
  OK = True
  for i in range(len(V1)):
    if not approxEqual(V1[i], V2[i], RelativeEpsilon, AbsoluteEspilon):
      OK = False
      break
  return OK


def strInput(Message, ValidStrings):
 
  
  while True:  
      mystring = input(Message)
      mystring = mystring.strip()
      if mystring in ValidStrings:
        break
      else:
        print('Please type one of the following values:', ", ".join(ValidStrings))
  return mystring
  


def intInput(Message):
  
  
  while True:
    try:  
      myint = int(input(Message))
      break
    except ValueError as e:
      print('Input error:', str(e))
      print('Please try again!')
  return myint


def floatInput(Message):
 
  
  
  while True:
    try:  
      myfloat = float(input(Message))
      break
    except ValueError as e:
      print('Input error:', str(e))
      print('Please try again!')
  return myfloat
  
  
  
  
  
