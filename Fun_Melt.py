#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[10]:


df = pd.DataFrame({'A': {0:'a',1:'b',2:'c'},
                   'B': {0 : 1, 1 : 3, 2 : 5},
                   'C': {0 : 2, 1 : 4, 2 : 6}})


# In[11]:


df


# # fundir colunas com Melt

# In[12]:


pd.melt(df, id_vars=["A"],value_vars=["B"])


# In[13]:


pd.melt(df, id_vars=["A"],value_vars=["B","C"])


# In[19]:


pd.melt(df, id_vars=["A"],value_vars=["B","C"],var_name="Varteste", value_name='Nome do Valor')


# 
