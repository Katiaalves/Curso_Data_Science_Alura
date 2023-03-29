#!/usr/bin/env python
# coding: utf-8

# # Relatorio de Analise I

# ## Importando a Base de Dados

# In[1]:


import pandas as pd


# In[11]:


#importando 
pd.read_csv('dados/aluguel.csv', sep=';')


# In[4]:


dados = pd.read_csv('dados/aluguel.csv', sep =';')


# In[5]:


dados


# In[6]:


type(dados)


# In[7]:


dados.info()


# In[10]:


dados.head(10)


# # Informações Gerais sobre a Base de Dados

# In[12]:


dados.dtypes


# In[13]:


pd.DataFrame(dados.dtypes)


# # Especificando tipos de dados

# In[14]:


pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])


# In[15]:


tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])


# In[16]:


tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados


# In[17]:


dados.shape


# In[18]:


print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0], dados.shape[1]))


# In[ ]:




