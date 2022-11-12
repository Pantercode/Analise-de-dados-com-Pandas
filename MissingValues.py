#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[7]:


datas = pd.date_range('20190101',periods=60,freq="D")

df = pd.DataFrame(np.random.randn(60,5), index=datas, columns=list("ABCDE"))


# In[8]:


df.head(3)


# In[9]:


df["F"] = df.A[df.A>0]


# In[10]:


df.head


# # Copia dados

# In[11]:


df2 = df.copy()


# In[12]:


df3 = df.copy()


# # Apagar todos os dados NAN

# In[16]:


df2.dropna().shape


# # Preencher os Dados faltantes

# In[ ]:


df3.F.fillna(np.mean(df3.A))


# In[17]:


df3.F.fillna(np.mean(df3.A))


# In[18]:


df4 = df.copy()


# In[19]:


df4.fillna(value=7777)


# In[ ]:




