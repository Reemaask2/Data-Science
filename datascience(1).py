#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from IPython import display 
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('Obesity levels Data.csv')
df.head()


# In[9]:


df.info()


# In[10]:


df.describe()


# In[17]:


pip install seaborn 


# In[18]:


import seaborn as sns 
numerical_attributes = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE']

# Plot box plots for numerical attributes
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[numerical_attributes])
plt.title('Box plots of Numerical Attributes')
plt.xlabel('Attributes')
plt.ylabel('Values')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# In[ ]:


plt.figure(figsize=(12, 8))
numerical_attributes_for_bar = ['Age', 'Weight]
for i, col in enumerate(numerical_attributes_for_bar, 1):
    plt.subplot(3, 3, i)
    df[col].plot(kind='bar', color='skyblue')
    plt.title(col)
    plt.xlabel('')
    plt.ylabel('Value')
plt.tight_layout()
plt.show()


# In[ ]:


df.isnull()


# In[16]:


df.nunique()


# In[5]:


categorical_columns = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS', 'NObeyesdad']
for col in categorical_columns:
    print(f"Unique values in {col}: {df[col].unique()}")


# In[ ]:




