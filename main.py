###########
# Imports #
###########

# External librairies

import os.path

# Local modules

import usermodule
import nutritionDBmodule
import envDBmodule
import myutils
from datetime import date
from random import sample
import calendar


########################
# Function definitions #
########################



random.sample(Meals)
 cal = calendar.Calendar()
 for x in cal.itermonthdates(2022, 5)



################
# Main program #
################

"""if __name__ == "__main__":

  user = usermodule.User() 
  user.setPhysiologicalParameters()
  daily_energy_req = user.dailyEnergyRequirement()
  print('Your daily energy requirement is', daily_energy_req, 'kcal.')
  print('The breakfast should bring', 0.2*daily_energy_req, 'kcal.')
  print('The lunch and dinner should each bring', 0.4*daily_energy_req, 'kcal.')

  print('Importing nutritional data... ', end='')
  nutrDB = nutritionDBmodule.NutritionDatabase('poore2018/TableS1_augmented_with_FAO_data.xlsx')
  assert(nutrDB.isComplete())
  assert(nutrDB.isConsistent())
  print('done')

  user.setExtraQuantities(nutrDB)
  all_valid_meals_with_quantities = nutrDB.enumerateAllPossibleMealsWithQuantities(0.4*daily_energy_req, user.extra_qty_dict)

  print('Importing environmental data... ', end='')
  envDB = envDBmodule.EnvironmentalDatabase('poore2018/DataS2.xlsx')
  assert(envDB.isConsistentWith(nutrDB))
  print('done')

  all_valid_meals_with_quantities.computeAllEnvironmentalImpacts(envDB)
  
  print('Here are the distributions of environmental impacts for all nutritionnally valid meals.')  
  all_valid_meals_with_quantities.drawEnvironmentalImpactHistograms()
  user.setEnvironmentalThresholds()

  my_meals = all_valid_meals_with_quantities.environmentFriendlyMeals(user.env_thresholds)
  print(len(my_meals), 'meals are compatible with the environmental impact thresholds.')
  result_file_name = 'meals.txt'  
  my_meals.saveToFile(result_file_name)
  print(len(my_meals), 'meals written to file', result_file_name, '.') 
  
  """
