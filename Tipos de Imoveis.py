#!/usr/bin/env python
# coding: utf-8

# # Relatorio de Analise II

# ## Tipo de Imoveis

# In[2]:


import pandas as pd


# In[5]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[6]:


dados.head(10)


# In[7]:


dados['Tipo']


# In[8]:


dados.Tipo


# In[9]:


tipo_de_imovel = dados['Tipo']


# In[10]:


type(tipo_de_imovel)


# In[11]:


tipo_de_imovel.drop_duplicates()


# In[12]:


tipo_de_imovel


# In[14]:


tipo_de_imovel.drop_duplicates(inplace = True)


# In[15]:


tipo_de_imovel


# ## Organizando Visualização

# In[16]:


tipo_de_imovel = pd.DataFrame(tipo_de_imovel)


# In[17]:


tipo_de_imovel


# In[18]:


tipo_de_imovel.index


# In[19]:


tipo_de_imovel.shape[0]


# In[20]:


range(tipo_de_imovel.shape[0])


# In[21]:


for i in range(tipo_de_imovel.shape[0]):
    print(i)


# In[22]:


tipo_de_imovel.index = range(tipo_de_imovel.shape[0])


# In[23]:


tipo_de_imovel


# In[ ]:




