#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


df=pd.read_csv("C:/Users/hamid/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/PaAgreement.csv")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df[5:8]


# In[8]:


df.tail()


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df["Cotienent"].unique()


# In[12]:


df["Cotienent"].value_counts()


# In[13]:


df[df["Cotienent"]=="Asia"]


# In[14]:


df["Amount of CFC in m3"].value_counts().plot()


# In[15]:


df["Amount of CFC in m3"].value_counts().plot(kind="bar", figsize=(8,8))
plt.xlabel("CFC in m3")
plt.ylabel("count")
plt.show()


# In[16]:


df["Amount of CFC in m3"].value_counts().plot(kind="pie", figsize=(10,10))
plt.show()


# In[17]:


sns.heatmap(df.corr(),square=True)


# In[ ]:




