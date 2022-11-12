#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


datas = pd.date_range(start='20190101',periods=12)


# In[4]:


datas


# In[5]:


Pessoa = ['George','Victor','Lucas']


# In[6]:


#choice = escolha
np.random.choice(Pessoa)


# In[9]:


Nome =[]
Gasto =[]
for i in range(12):
    Nome.append(np.random.choice(Pessoa))
    Gasto.append(np.round(np.random.rand()*100,2))
Nome


# In[10]:


Gasto


# In[13]:


df = pd.DataFrame({'Dia': datas,'Nome':Nome,'Gasto':Gasto})


# In[14]:


df


# # Ordena com pivot

# In[17]:


df.pivot(index="Dia",columns="Nome",values="Gasto")

