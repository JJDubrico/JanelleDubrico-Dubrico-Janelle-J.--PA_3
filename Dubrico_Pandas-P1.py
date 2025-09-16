#!/usr/bin/env python
# coding: utf-8

# **PROBLEM 1**

# In[29]:


import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')
cars


# In[30]:


# Display the first five rows
print("First five rows of the DataFrame:")
cars.head()


# In[31]:


# Display the last five rows
print("Last five rows of the DataFrame:")
cars.tail()

