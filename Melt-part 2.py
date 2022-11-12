#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[39]:


data = {
    'Localização':['CidadeA','CidadeB'],
    'Temperatura':['Prevista','Atual'],
    'Set-2019':[30,32],
    'Out-2019':[45,43],
    'Nov-2019':[24,22]}


# In[40]:


print(data)


# # converte pra colunas

# In[41]:


#df = pd.DataFrame(data,columns=['Localização','Temperatura','Set-2019','Out-2019','Nov-2019'])
#print(df)


# In[44]:


#df = pd.melt(df,id_vars=["Localização","Temperatura"], var_name="Date",value_name='Value')
#print(df)


# # Mudando nome dos df

# In[43]:


df = pd.melt(df,id_vars=["Localização"], var_name="Date",value_name='Value')
print(df)


# In[ ]:




