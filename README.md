# Dubrico_2ECE-A - PA #3 (V2)

# PROBLEM 1

  **Using the dataframe cars, load the .csv file using pandas and it must display the first and last five rows of the resulting cars**
  
  import pandas as pd # Imports Pandas Library

  # a.) Load the corresponding .csv file into a data frame named cars using pandas
  cars = pd.read_csv('cars.csv') # Loads the CSV file into a DataFrame
  
  cars # Displays the 'cars.csv' file

 # b.) Display the first five and last five rows of the resulting cars.
  print("First five rows of the DataFrame:") # Prints the output
  
  cars.head() # Displays the first five rows of the dataframe
  
  print("Last five rows of the DataFrame:") # Prints the output
  
  cars.tail() # Displays the last five rows of the dataframe


# PROBLEM 2

 **Using the dataframe cars in the previous problem, it must extract the following information using subsetting, splicing, and indexing**
  
  import pandas as pd # Imports Pandas Library
  cars = pd.read_csv('cars.csv') # Load the CSV file into a DataFrame
  cars # Displays the 'cars.csv' file

  **a.) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.**
  
  cars.iloc[:5, 1::2] # Selects every second column starting from the first index

  **b.) Display the row that contains the ‘Model’ of ‘Mazda RX4’.**
  
  cars.loc[cars['Model']=='Mazda RX4'] # locates the value with Mazda RX4 as the Model

  **c.) Determine how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?**
  
  cars.loc[cars['Model']=='Camaro Z28', ['Model', 'cyl']] # locates the value with Camaro Z28 as the Model and displays the columns Model cyl

  **d.) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**
  
  cars_models = ['Mazda RX4 Wag',
                'Ford Pantera L',
                'Honda Civic'] # Makes a list of the car models
  
  cars.loc[cars['Model'].isin(cars_models), ['Model', 'cyl', 'gear']] # .isin is used to filter the DataFrame for these specific models

  --VERSION 2--
