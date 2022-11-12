#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


V =[22,55,7,9]


# In[4]:


V


# In[5]:


V[-1]


# In[7]:


V[0]


# # Multindexação

# In[12]:


import pandas as pd


# In[13]:


arrays = [[1,1,2,2], ['red','blue','red','blue']]


# In[14]:


pd.MultiIndex.from_arrays(arrays, names=('number','color'))


# # Multindexação do produto Cartesiano

# In[15]:


numbers = [0,1,2]
colors = ['green','purple']


# In[17]:


pd.MultiIndex.from_product([numbers,colors],
                          names=['number','color'])


# In[ ]:




