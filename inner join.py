#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[ ]:





# In[3]:


# Cadastro da loja a
cadastro_a = {'Id': ['AA2930','BB4563','CC2139','DE2521','GT3462','HH1158'],
            'Nome':  ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
            'Idade': [20,35,40,54,30,27],
            'CEP': ['00092-029','11111-111','22222-888','00000-999','88888-111','77777-666']
           }

cadastro_a = pd.DataFrame(cadastro_a, columns = ['Id','Nome','Idade','CEP'])
cadastro_a


# In[4]:


# Cadastro da loja b
cadastro_b = {'Id': ['CC9999','EF4488','DD9999','GT3462','HH1158'],
            'Nome':  ['Marcos', 'Patricia', 'Ericka', 'Ricardo', 'Maria'],
            'Idade': [19,30,22,30,27],
            'CEP': ['00092-029','11111-111','11111-888','88888-111','77777-666']
           }
 
cadastro_b = pd.DataFrame(cadastro_b, columns = ['Id','Nome','Idade','CEP'])
cadastro_b


# In[5]:


# Registro de compras de todas unidades
compras = {'Id': ['AA2930','EF4488','CC2139','EF4488','CC9999','AA2930','HH1158','HH1158'],
            'Data':  ['2019-01-01','2019-01-30','2019-01-30','2019-02-01','2019-02-20','2019-03-15','2019-04-01','2019-04-10'],
            'Valor': [200,100,40,150,300,25,50,500]
           }
 
compras = pd.DataFrame(compras, columns = ['Id','Data','Valor'])

compras


# #Fazendo um fulljoin

# In[9]:


lojas = pd.concat([cadastro_a,cadastro_b],ignore_index=True)


# In[11]:


lojas.drop_duplicates()


# In[12]:


lojas


# #Apagando duplicatas por seção

# In[16]:


clientes_unicos = lojas.drop_duplicates(subset="Id")


# In[17]:


clientes_unicos.sample(5)


# In[ ]:




