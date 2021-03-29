#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[5]:


df=pd.read_csv("C:/Users/hamid/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/PaAgreement.csv")


# In[6]:


df


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.head()


# In[10]:


df[5:8]


# In[11]:


df.tail()


# In[12]:


df.info()


# In[13]:


df.describe()


# In[15]:


df["Cotienent"].unique()


# In[16]:


df["Cotienent"].value_counts()


# In[18]:


df[df["Cotienent"]=="Asia"]


# In[20]:



df["Amount of CFC in m3"].value_counts().plot()


# In[21]:


df["Amount of CFC in m3"].value_counts().plot(kind="bar", figsize=(8,8))
plt.xlabel("CFC in m3")
plt.ylabel("count")
plt.show()


# In[24]:


df["Amount of CFC in m3"].value_counts().plot(kind="pie", figsize=(10,10))
plt.show()


# In[25]:


sns.heatmap(df.corr(),square=True)


# In[ ]:




