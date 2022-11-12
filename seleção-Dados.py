#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


datas = pd.date_range('20180101',periods=600,freq="D")
df = pd.DataFrame(np.random.randn(600,5),index= datas, columns= list("ABCDE"))


# In[7]:


df


# In[8]:


df.head(2)


# # Selecionando colunas

# In[9]:


df["D"]


# In[10]:


df["B"].head()


# # Selecionando algumas linhas

# In[11]:


df[1:4]


# # Selecionando todasa as linhas de algumas colunas

# In[16]:


df.loc[:,["A","D","E"]]


# # selecção de Datas

# In[18]:


df.loc['20180301':'20180917',['A','E']].head(4)


# # Seleção Part2

# # ILOC

# In[20]:


df.iloc[1]


# # Selecionando duas colunas

# In[23]:


df.iloc[1:4,1:3]


# # Selecionando indices e linhas

# In[24]:


df.iloc[[1,5,6],[0,3]]


# # Selecão de todas a colunas d linha tal

# In[29]:


df.iloc[1:3, ]


# # Seleção de Dados de forma Booleana

# In[30]:


df.A


# In[31]:


df.C


# # Filtrando tudo com logica

# In[32]:


df[df.A>0]


# In[33]:


df[df>0]


# In[ ]:




