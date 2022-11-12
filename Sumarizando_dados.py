#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[11]:


datas = pd.date_range('20200101',periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=datas, columns=['VAR_A','VAR_B','VAR_C','VAR_D'])


# In[13]:


df2 = pd.DataFrame({'A':1.,
                            'B': pd.Timestamp('20130102'),
                            'C': pd.Series(1, index=list(range(4)),dtype='float32'),
                            'D': np.array([3] * 4,dtype='int32'),
                            'E': pd.Categorical(["test","train","test","train"]),
                            'F': 'Python'})


# In[14]:


df


# # Sumariza o tamanho do df 

# In[15]:


df.shape


# # Informa o type de informações contidas no df

# In[16]:


df.dtypes


# In[17]:


df2.shape


# In[18]:


df2.dtypes


# In[19]:


#Float64 armazena um a quantidade maior de numeros de ponto flutuante
#float32 armazena uma quantidade menor


# # Sumarizando

# In[20]:


df.describe() #feito somente a dados numericos


# In[21]:


df2.describe()


# # Imposição de valores adicionado uma coluna a mais

# In[22]:


df1 = df.reindex(index=datas[0:4],columns=list(df.columns)+['VAR_E'])


# In[23]:


df1


# In[25]:


df1.loc[datas[0]:datas[1],"VAR_E"] = 77


# In[26]:


df1


# In[27]:


df1.dtypes


# In[28]:


df1.describe()


# In[ ]:




