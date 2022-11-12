#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Cadastro da loja a
cadastro_a = {'Id': ['AA2930','BB4563','CC2139','DE2521','GT3462','HH1158'],
            'Nome':  ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
            'Idade': [20,35,40,54,30,27],
            'CEP': ['00092-029','11111-111','22222-888','00000-999','88888-111','77777-666']
           }

cadastro_a = pd.DataFrame(cadastro_a, columns = ['Id','Nome','Idade','CEP'])
cadastro_a


# In[3]:


# Cadastro da loja b
cadastro_b = {'Id': ['CC9999','EF4488','DD9999','GT3462','HH1158'],
            'Nome':  ['Marcos', 'Patricia', 'Ericka', 'Ricardo', 'Maria'],
            'Idade': [19,30,22,30,27],
            'CEP': ['00092-029','11111-111','11111-888','88888-111','77777-666']
           }
 
cadastro_b = pd.DataFrame(cadastro_b, columns = ['Id','Nome','Idade','CEP'])
cadastro_b


# In[4]:


# Registro de compras de todas unidades
compras = {'Id': ['AA2930','EF4488','CC2139','EF4488','CC9999','AA2930','HH1158','HH1158'],
            'Data':  ['2019-01-01','2019-01-30','2019-01-30','2019-02-01','2019-02-20','2019-03-15','2019-04-01','2019-04-10'],
            'Valor': [200,100,40,150,300,25,50,500]
           }
 
compras = pd.DataFrame(compras, columns = ['Id','Data','Valor'])

compras


# #Fazendo LEfTJOIN

# In[6]:


pd.merge(cadastro_a, compras ,how='left',on='Id')


# In[8]:


pd.merge(compras,cadastro_b, how='left',on='Id')


# In[11]:


esquerda = pd.merge(cadastro_b,compras, how='left',on='Id')


# In[12]:


esquerda


# #AGRUPANDO id, e o nome somando os valores gastos

# In[13]:


esquerda.groupby(['Id','Nome'])['Valor'].sum()


# In[ ]:




