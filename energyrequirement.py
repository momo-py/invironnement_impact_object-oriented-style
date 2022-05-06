###########
# Imports #
###########

# External librairies

import os.path


# Local modules

import myutils

########################
# Function definitions #
########################


def basalMetabolicRate(Gender, BodyWeight, Height, Age):
 
 
 
  if Gender != 'F' and Gender != 'M':
    raise ValueError('Gender should be either F or M.')
  if Age < 18:
    raise ValueError('This program is currently designed for adult food requirements, sorry.')
  if BodyWeight < 0:
    raise ValueError('Body weight should be a positive number.')
  if Height < 0:
    raise ValueError('Height should be a positive integer.')
  BMR = 10*BodyWeight + 6.25*Height - 5.0*Age
  if Gender == 'F':
    BMR -= 161
  elif Gender == 'M':
    BMR += 5
  return BMR


def dailyEnergyRequirement(Gender, BodyWeight, Height, Age, PhysicalActivityLevel):
  
  
  
  if PhysicalActivityLevel == 'sedentary':
    PAL = 1.4
  elif PhysicalActivityLevel == 'light':
    PAL = 1.6
  elif PhysicalActivityLevel == 'moderate':
    PAL = 1.75
  elif PhysicalActivityLevel == 'intense':
    PAL = 1.9
  elif PhysicalActivityLevel == 'very intense':
    PAL = 2.1
  else:
    raise ValueError('Physical activity level should be one of "sedentary", "light", "moderate", "intense", "very intense"')
  result = PAL*basalMetabolicRate(Gender, BodyWeight, Height, Age)
  return result


def askUserPhysiologicalParameters():
  
  
  
  
  gender =         myutils.strInput('Gender (M for male, F for female): ', ['M', 'F'])
  age =            myutils.intInput('Age                              : ')
  body_weight =  myutils.floatInput('Body weight (kg)                 : ')
  height =         myutils.intInput('Height (cm)                      : ')
  physical_activity_level = myutils.strInput('Physical activity level (sedentary, light, moderate, intense, very intense)? ', ['sedentary', 'light', 'moderate', 'intense', 'very intense'])
  return (gender, age, body_weight, height, physical_activity_level)


def setUserPhysiologicalParameters():
  
  
  
  physiol_params_file_name = 'physiological_parameters.txt'
  if os.path.isfile(physiol_params_file_name):
    yes_or_no = input('Would you like to re-use the physiological parameters of the last execution? (Y/n)? ')
    if yes_or_no.lower() == 'n':   
      (gender, age, body_weight, height, physical_activity_level) = askUserPhysiologicalParameters() 
    else:
      physiol_params_file = open(physiol_params_file_name,'r')
      line = physiol_params_file.readline()
      gender = line.split()[0]
      line = physiol_params_file.readline()
      age = int(line.split()[0])
      line = physiol_params_file.readline()
      body_weight = float(line.split()[0])
      line = physiol_params_file.readline()
      height = int(line.split()[0])
      line = physiol_params_file.readline()
      physical_activity_level  = line.split()[0]
      physiol_params_file.close()  
      print('Gender                  : {0:>5} '.format(gender))
      print('Age                     : {0:>5} years'.format(age))
      print('Body weight             : {0:5.1f} kg'.format(body_weight))
      print('Height                  : {0:>5} cm'.format(height))
      print('Physical activity level : {0}'.format(physical_activity_level))
  else:
    (gender, age, body_weight, height, physical_activity_level) = askUserPhysiologicalParameters()
  
  physiol_params_file = open(physiol_params_file_name,'w')
  physiol_params_file.write(gender + '\n')
  physiol_params_file.write(str(age) + '\n')
  physiol_params_file.write(str(body_weight) + '\n')
  physiol_params_file.write(str(height) + '\n')
  physiol_params_file.write(physical_activity_level + '\n')
  physiol_params_file.close()   
  
  return (gender, age, body_weight, height, physical_activity_level)




################
# Main program #
################


if __name__ == "__main__":
  # The program below (unit tests) will be run only if the Python interpreter is launched with energyrequirement.py as an argument,
  # not if this file is included as a module in another main program.

  abseps = 1e-15
  releps = 1e-6

  ####################################
  # Unit tests of basalMetabolicRate #
  ####################################

  print("Unit tests of basalMetabolicRate:")

  try:
    print(basalMetabolicRate('X', 60, 165, 40))
  except ValueError as e:
    # code that must be executed if the try clause raises an exception
    print(True) # throwing a ValueError exception is the correct and expected behavior here (wrong Gender)
  else:
    # code that must be executed if the try clause does not raise an exception
    print(False)

  try:
    print(basalMetabolicRate('F', 60, 165, 15))
  except ValueError as e:
    # code that must be executed if the try clause raises an exception
    print(True) # throwing a ValueError exception is the correct and expected behavior here (Age < 18)
  else:
    # code that must be executed if the try clause does not raise an exception
    print(False)

  try:
    print(basalMetabolicRate('F', -6, 165, 40))
  except ValueError as e:
    # code that must be executed if the try clause raises an exception
    print(True) # throwing a ValueError exception is the correct and expected behavior here (BodyWeight < 0)
  else:
    # code that must be executed if the try clause does not raise an exception
    print(False)


  try:
    print(basalMetabolicRate('F', 60, -165, 40))
  except ValueError as e:
    # code that must be executed if the try clause raises an exception
    print(True) # throwing a ValueError exception is the correct and expected behavior here (Height < 0)
  else:
    # code that must be executed if the try clause does not raise an exception
    print(False)

  print(myutils.approxEqual(basalMetabolicRate('F', 60, 165, 40), 1270.25, releps, abseps))
  print(myutils.approxEqual(basalMetabolicRate('M', 60, 165, 40), 1436.25, releps, abseps))



  ########################################
  # Unit tests of dailyEnergyRequirement #
  ########################################

  print("Unit tests of dailyEnergyRequirement:")

  try:
    print(dailyEnergyRequirement('F', 60, 165, 40, 'lalala'))
  except ValueError as e:
    # code that must be executed if the try clause raises an exception
    print(True) # throwing a ValueError exception is the correct and expected behavior here (invalid value for PhysicalActivityLevel)
  else:
    # code that must be executed if the try clause does not raise an exception
    print(False)

  print(myutils.approxEqual(dailyEnergyRequirement('F', 60, 165, 40, 'light'), 2032.4, releps, abseps))

