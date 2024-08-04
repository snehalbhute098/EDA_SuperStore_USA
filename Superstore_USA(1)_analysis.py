#!/usr/bin/env python
# coding: utf-8

# # EDA on superstore analysis using python 

# In[43]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Import of dataset 

# In[2]:


dataset=pd.read_excel('Superstore_USA.xlsx')


# # View of data

# In[3]:


dataset


# In[4]:


dataset.head()


# In[5]:


dataset.info()


# In[6]:


dataset.describe()


# In[7]:


dataset.shape


# In[8]:


dataset.size


# In[41]:


## Top 2 of the data


# In[9]:


dataset.head(2)


# In[ ]:


## columns of data


# In[10]:


dataset.columns


# # Missing value analysis

# In[11]:


dataset.isnull().sum()


# # fill with mean(), median()

# In[12]:


dataset['Product Base Margin'].fillna(dataset['Product Base Margin'].mean(),inplace=True)


# In[14]:


dataset.isnull().sum()


# In[42]:


#univariate analysis


# In[15]:


dataset.shape


# # Order priority

# In[16]:


dataset['Order Priority'].value_counts()


# In[17]:


dataset['Order Priority'].unique()


# In[18]:


dataset['Order Priority']=dataset['Order Priority'].replace('Critical ','Critical')


# In[19]:


dataset['Order Priority'].value_counts()


# In[21]:


import matplotlib.pyplot as plt


# In[22]:


plt.figure(figsize=(5,4))
sns.countplot(x='Order Priority', data=dataset)
plt.title('Count of Order Priority')
plt.savefig('Count of Order Priority')
plt.show()


# # Ship mode

# In[24]:


dataset['Ship Mode'].value_counts()


# In[25]:


x=dataset['Ship Mode'].value_counts().index
y=dataset['Ship Mode'].value_counts().values


# In[26]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")
plt.legend(loc=3)
plt.title('Type of Ship Mode')
plt.savefig('Type of Ship Mode')
plt.show()


# In[ ]:


# bivariate analysis


# # Product category and shipping mode

# In[27]:


plt.figure(figsize=(10,4))
sns.countplot(x="Ship Mode",data=dataset, hue='Product Category')
plt.show()


# # Customer segment

# In[28]:


plt.figure(figsize=(6,4))
sns.countplot(x='Customer Segment', data= dataset)
plt.show()


# In[29]:


plt.figure(figsize=(6,4))
sns.countplot(x='Product Category', data= dataset)
plt.show()


# # Product category

# In[30]:


plt.figure(figsize=(10,6))
sns.countplot(x='Product Category', data= dataset[dataset['Product Category']=='Office Supplies'],hue='Product Sub-Category')
plt.show()


# # Order Year

# In[34]:


dataset['Order Date'].value_counts()


# In[32]:


dataset['Order Year']=dataset['Order Date'].dt.year


# In[33]:


dataset['Order Date']


# In[35]:


dataset.info()


# In[36]:


dataset['Order Year'].value_counts()


# # Count of orders with years

# In[37]:


plt.figure(figsize=(6,4))
sns.countplot(x='Order Year', data= dataset)
plt.show()


# # product category Vs profit analysis

# In[38]:


sns.barplot(x="Product Category",y="Profit", data=dataset,estimator='sum')
plt.show()


# # Top 5 states with top sales

# In[39]:


dataset['State or Province'].value_counts()[:5]


# # Product base margin on the category

# In[40]:


plt.figure(figsize=(6,4))
sns.barplot(x='Product Category', y='Product Base Margin',data=dataset,estimator='sum')
plt.show()


# In[ ]:




