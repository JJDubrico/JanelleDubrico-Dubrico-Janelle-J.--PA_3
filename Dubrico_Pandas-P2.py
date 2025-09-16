#!/usr/bin/env python
# coding: utf-8

# **PROBLEM 2**

# In[23]:


import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')
cars


# In[24]:


#Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars.iloc[:5, 1::2]


# In[25]:


#Display the row that contains the ‘Model’ of ‘Mazda RX4’.
cars.loc[cars['Model']=='Mazda RX4']


# In[26]:


#How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
cars.loc[cars['Model']=='Camaro Z28', ['Model', 'cyl']]


# In[27]:


#Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

cars_models = ['Mazda RX4 Wag',
              'Ford Pantera L',
              'Honda Civic']
cars.loc[cars['Model'].isin(cars_models), ['Model', 'cyl', 'gear']]

