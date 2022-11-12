#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame({'A':1.,
                            'B': pd.Timestamp('20130102'),
                            'C': pd.Series(1, index=list(range(4)),dtype='float32'),
                            'D': np.array([3] * 4,dtype='int32'),
                            'E': pd.Categorical(["test","train","test","train"]),
                            'F': 'Python',
                            'G': [2,2,4,4],
                            'H':[np.nan,2,4,np.nan]})


# # Conferi se existe dados repetidos

# In[6]:


df.nunique(axis=1,dropna=False)


# In[7]:


df.nunique(axis=0,dropna=True)


# In[8]:


df


# # Remove duplicatas

# In[13]:


df.drop_duplicates(subset="G",keep='first') # ou last


# In[ ]:




