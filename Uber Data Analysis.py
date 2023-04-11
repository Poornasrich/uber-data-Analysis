#!/usr/bin/env python
# coding: utf-8

# ### About Dataset
# 
# Geography: USA, Sri Lanka and Pakistan
# 
# Time period: January - December 2016
# 
# Unit of analysis: Drives
# 
# Total Drives: 1,155
# 
# Total Miles: 12,204
# 
# Dataset: The dataset contains Start Date, End Date, Start Location, End Location, Miles Driven and Purpose of drive (Business, Personal, Meals, Errands, Meetings, Customer Support etc.)

# In[1]:


#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read csv
df=pd.read_csv('C:\\Users\\cvchy\\Downloads\\My Uber Drives - 2016.csv')


# ## Understanding the Data
# 
# we need to understand the data for the data cleaning process. Here we use Pandas, Numpy, Matplotlib and seaborn for visulaization

# In[3]:


# printing first five rows
df.head()


# In[4]:


#printing null values
df.isnull().sum()


# In[5]:


#information of the dataset
df.info()


# In[6]:


#printing columns 
df.columns


# In[7]:


#data types of the columns in the dataset
df.dtypes


# In[8]:


#print last 5 rows 
df.tail()


# ### we can see that last row doesn't have any detailed information so we can remove it

# In[9]:


# Remove uncessary data
uber_df = df[:-1]


# In[10]:


uber_df


# In[11]:


uber_df.dtypes


# In[12]:


import datetime


# In[13]:


uber_df['START_DATE*']=  pd.to_datetime(uber_df['START_DATE*'], infer_datetime_format=True)


# In[14]:


uber_df['END_DATE*']=  pd.to_datetime(uber_df['END_DATE*'], infer_datetime_format=True)


# In[ ]:





# In[15]:


uber_df.dtypes


# #### Data type of the startdate and enddate has been changed into datetime

# # visualization

# ### visualization helps to understand the problem and get insights through graphs. We use matplotlib and searborn to do visualization
# 

# In[16]:


# plot number of trip at each category
x = uber_df['CATEGORY*'].value_counts().plot(kind='bar')


# Here we can see that business category are of more than 1000 and personal is of 50
# 

# In[17]:


#visualizing the hours in start_date column with the help of bar graph
hours = uber_df['START_DATE*'].dt.hour.value_counts()

hours.plot(kind='bar',color='orange',figsize=(10,5))

plt.xlabel('Hours')
plt.ylabel('Trips')
plt.title('Number of trips per hour')


# Here we visualized the number of trips per hour. Most of the drivers spent 15 hours to make 100 trips in a day.

# In[18]:


#visualizing the month in end_date coulmn with the help of bar graph
MONTH = uber_df['END_DATE*'].dt.month.value_counts()

MONTH.plot(kind='bar',color='blue',figsize=(10,5))
plt.xlabel('Hours')
plt.ylabel('Trips')
plt.title('Number of trips per Month')


# We visualized the month data in a end_date to know number of trips made by drivers in a month. Here we can see that for 12 months they made 145 trips.

# In[19]:


#visualization of purpose column using bar graph
purpose = uber_df['PURPOSE*'].value_counts()
purpose.plot(kind='bar',figsize=(10,5),color='green')


# Here we visualized that the purpose of using uber services is for attending Meeting(185),Meal/Entertain(152) and least purpose is of commute(2)

# In[20]:


#visulaizing the Miles columns using histogram
miles = uber_df['MILES*'].value_counts()
miles.plot(kind='hist',figsize=(10,5),color='black')


# In[ ]:





# In[21]:


purpose = uber_df['PURPOSE*'].value_counts()
purpose.plot(kind='hist',figsize=(10,5),color='green')


# In[ ]:





# In[22]:


#calculating the exact time(minutes) travelled by the uber driver 
minutes=[]
uber_df['Duration_Minutes'] = uber_df['END_DATE*'] - uber_df['START_DATE*']
uber_df['Duration_Minutes']
for i in uber_df['Duration_Minutes']:
    minutes.append(i.seconds / 60) 

uber_df['Duration_Minutes'] = minutes


# In[23]:


uber_df['Duration_Minutes']


# In[24]:


#calculation of speed of a trip by uber drivers

#calculation of hours as per the minutes travelled
uber_df['Duration_hours'] = uber_df['Duration_Minutes'] / 60 
uber_df['Speed_KM'] = uber_df['MILES*'] / uber_df['Duration_hours'] 
uber_df['Speed_KM']


# In[25]:


uber_df.isnull().sum()


# Here we can see null values in purpose column. But we can't replace or delete them without the expert domain suggestion.

# # What is the average length of the trip?

# In[26]:


# calucationg the average miles travelled
uber_df['MILES*'].mean() 


# # Average number of rides per week or per month?

# In[27]:


# calculating the average rides per month
MONTH.mean()


# In[28]:


# calculating the average rides per week

week=MONTH/4
week
week.mean()


# # Percentage of business vs personal ?

# In[29]:


#calculating the percentage of the category column
(uber_df['CATEGORY*'].value_counts() / len(uber_df))*100


# Here we can see that the most of the uber services is used for the business category i.e.,93% and the least used for the personal category i.e.,6%.

# In[30]:


#printing uber_df file

uber_df


# Now the Dataset is ready for the Model building.
