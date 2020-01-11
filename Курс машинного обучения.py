#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')


# In[6]:


df.head()


# In[7]:


print(df.shape)


# In[8]:


print(df.columns)


# In[9]:


print(df.info())


# In[11]:


df.describe()


# In[12]:


df.describe(include=['object', 'bool'])


# In[14]:


df['User_Count'].value_counts()


# In[15]:


df['NA_Sales'].value_counts(normalize=True)


# In[17]:


df.sort_values(by='Global_Sales', 
        ascending=False).head()


# In[19]:


df['User_Count'].mean()


# In[24]:


df[df['User_Count'] == 1].mean()


# In[25]:


df.loc[0:5, 'Platform':'Genre']


# In[27]:


df['User_Count'].mean()


# In[28]:


df[df['User_Count'] == 1].mean()


# In[29]:


df[(df['User_Count'] == 0) & (df['Platform'] == 'No')]['Genre'].max()


# In[31]:


d = {'No' : False, 'Yes' : True}
df['Year_of_Release'] = df['Year_of_Release'].map(d)
df.head()


# In[33]:


columns_to_show = ['NA_Sales', 'EU_Sales', 'JP_Sales']

df.groupby(['User_Count'])[columns_to_show].describe(percentiles=[])


# In[34]:


pd.crosstab(df['User_Count'], df['Global_Sales'])


# In[35]:


total_calls = df['NA_Sales'] + df['EU_Sales'] +                   df['JP_Sales'] + df['Other_Sales']
df.insert(loc=len(df.columns), column='Global sales', value=total_calls) 
df.head()


# In[36]:


df = df.drop(['NA_Sales', 'Other_Sales'], axis=1) 

df.drop([1, 2]).head()


# In[ ]:




