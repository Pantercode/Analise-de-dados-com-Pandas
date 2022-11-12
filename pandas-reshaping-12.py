#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# # Reshaping Reformualar os dados

# In[3]:


datas = pd.date_range('20200101',periods=6)

df1 = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A','Var_B','Var_C','Var_D'])


# In[4]:


df


# In[5]:


df.T


# In[6]:


dft = df.T


# In[7]:


df.shape


# In[13]:


df.values


# In[14]:


v =df


# In[16]:


v.reshape((4,12))


# In[ ]:




