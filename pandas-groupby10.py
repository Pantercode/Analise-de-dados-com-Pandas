#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df = pd.DataFrame({"A" : ['Verdadeiro','falso','verdadeiro','falso','verdadeiro','falso','verdadeiro','falso'],
                   
                   "B" : ['um','um','dois','tres','dois','dois','um','tres'],
                   "C" : np.random.randn(8),
                   "D" : np.random.randn(8)})


# In[6]:


df


# #Agrupando e somando

# In[7]:


df.groupby(['A']).sum()


# #Agrupando e fazendo media

# In[8]:


df.groupby(['A']).mean()


# In[10]:


df.groupby(['B']).sum()


# In[11]:


df.groupby(['A','B']).sum()


# In[ ]:




