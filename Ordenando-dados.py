#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[8]:


df = pd.DataFrame({'Col1':['A','A','B',np.nan,'D','C'],'Col2':[2,1,9,8,7,4],'Col3':[0,1,9,4,2,3]})


# In[9]:


df


# # Ordenar valores

# In[14]:


df.sort_values(by="Col1")#Uma coluna


# In[15]:


df.sort_values(by="Col3")


# # Ordenando Multiplas colunas

# In[17]:


df.sort_values(by=["Col1","Col3"])


# # Ordenando de forma Asc

# In[18]:


df.sort_values(by=["Col3"],ascending=False)#TRUE


# In[ ]:




