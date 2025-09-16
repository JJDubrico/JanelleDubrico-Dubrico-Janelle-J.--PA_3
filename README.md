# JanelleDubrico-Dubrico-Janelle-J.--PA_3

# PROBLEM 1

  **To open the Pandas library, use the import convention:**
  
  import pandas as pd

  **a.) To read the file, use the pd.read_csv function:**
  
  cars = pd.read_csv('cars.csv') # Load the CSV file into a DataFrame
  cars

 **b.1) Using the .head(), display the first five rows**
 print("First five rows of the DataFrame:")
 cars.head()

 **b.2) Using the .tail(), display the last five rows**
 print("Last five rows of the DataFrame:")
 cars.tail()


# PROBLEM 2

  *To open the Pandas library, use the import convention:**
  
  import pandas as pd

  **To read the file, use the pd.read_csv function:**
  
  cars = pd.read_csv('cars.csv') # Load the CSV file into a DataFrame
  cars

  **a.) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.**
  **Using the .iloc:** 
  cars.iloc[:5, 1::2] # 1::2 selects every second column starting from the first index

  **b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.**
  **Using the .loc:**
  cars.loc[cars['Model']=='Mazda RX4'] # filters the DataFrame to return only the relevant row

  **c.) Determine how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?**
  **Using the .loc:**
  cars.loc[cars['Model']=='Camaro Z28', ['Model', 'cyl']]

  **d.) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**
  cars_models = ['Mazda RX4 Wag',
                'Ford Pantera L',
                'Honda Civic']
  cars.loc[cars['Model'].isin(cars_models), ['Model', 'cyl', 'gear']] # .isin is used to filter the DataFrame for these specific models
