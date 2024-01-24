#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

# Given code
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

# Q1: Difference in data types
print(type(list_))
print(type(array_list))
##yes they both have different datatype as list_ can have different datatype i.e string in this case.
##while array_list is numpy array and have fixed datatypes.


# In[3]:


# Q2: Data type of each element
print("Data types of elements in list_:")
for element in list_:
    print(type(element))

print("Data types of elements in array_list:")
for element in array_list:
    print(type(element))


# In[7]:


# Q3: Difference in data types after updating array_list
array_list = np.array(object=list_, dtype=int)
print("Data types of elements in updated array_list:")
for element in array_list:
    print(type(element))


# In[12]:


#Q4: finding the shape and size
num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)
np.shape(num_array)


# In[11]:


np.size(num_array)


# In[18]:


#Q5 creating a numpy array 3*3 contaning zeroes .
arr1=np.zeros((3,3))


# In[19]:


arr1


# In[20]:


#Q6 creating an identity matrix of (5*5) using numpy function
arr2 = np.eye(5)


# In[21]:


arr2


# In[ ]:




