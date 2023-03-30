#!/usr/bin/env python
# coding: utf-8

# # Relatorio de Analise III

# ## Imoveis Residenciais

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[4]:


dados.head(10)


# In[6]:


list(dados['Tipo'].drop_duplicates())


# In[7]:


residencial = ['Quitinete',
'Casa',
'Conjunto Comercial/Sala',
'Apartamento',
'Casa de Condomínio',
'Prédio Inteiro',
'Flat',
'Loja/Salão',
'Galpão/Depósito/Armazém',
'Casa Comercial',
'Casa de Vila',
'Terreno Padrão',
'Box/Garagem',
'Loft'
'Loja Shopping/ Ct Comercial',
'Chácara',
'Loteamento/Condomínio',
'Sítio',
'Pousada/Chalé',
'Studio',
'Hotel',
'Indústria']


# In[8]:


residencial = ['Quitinete', 
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']


# In[9]:


residencial


# In[10]:


dados.head(10)


# In[12]:


selecao = dados['Tipo'].isin(residencial)
selecao


# In[13]:


dados_residencial = dados[selecao]


# In[14]:


dados_residencial


# In[15]:


list(dados_residencial['Tipo'].drop_duplicates())


# In[16]:


dados_residencial.shape[0]


# In[17]:


dados.shape[0]


# In[18]:


dados_residencial.index = range(dados_residencial.shape[0])


# In[19]:


dados_residencial


# ## Exportando a Base de Dados

# In[20]:


dados_residencial.to_csv('dados/aluguel_residencial.csv', sep =';')


# In[21]:


dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep =';')


# In[22]:


dados_residencial_2


# In[23]:


dados_residencial.to_csv('dados/aluguel_residencial.csv', sep =';', index= False)


# In[24]:


dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep =';')


# In[25]:


dados_residencial_2


# In[ ]:




