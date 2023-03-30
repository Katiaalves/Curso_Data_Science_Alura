#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd


# # Series

# In[44]:


data = [1,2,3,4,5]


# In[45]:


s= pd.Series(data)


# In[46]:


s


# In[47]:


index = ['linha' + str(i) for i in range(5)]


# In[48]:


index


# In[49]:


s= pd.Series(data = data, index = index)


# In[50]:


s


# In[51]:


data = {'linha' + str(i) : i + 1 for  i in range(5)}


# In[52]:


data


# In[53]:


s = pd.Series(data)


# In[54]:


s


# In[55]:


s1 = s +2
s


# In[56]:


s2 = s +s1
s2


# # DataFrame

# In[57]:


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]


# In[58]:


data


# In[59]:


df1 = pd.DataFrame(data = data)


# In[60]:


df1


# In[61]:


index = ['linha' +  str(i ) for i in range(3)]


# In[62]:


index


# In[63]:


df1 = pd.DataFrame(data = data, index = index)


# In[64]:


df1


# In[65]:


columns = ['Coluna' + str(i) for i in range(3)]


# In[66]:


columns


# In[67]:


df1 = pd.DataFrame(data = data, index = index, columns = columns)


# In[68]:


df1


# In[69]:


data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}


# In[70]:


data


# In[71]:


df2 = pd.DataFrame(data)


# In[72]:


df2


# In[73]:


data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]


# In[74]:


data


# In[75]:


df3 = pd.DataFrame(data = data, index = index, columns = columns)


# In[76]:


df3


# In[77]:


df1[df1 > 0] = 'A'


# In[78]:


df1


# In[79]:


df2[df2 > 0] = 'B'


# In[80]:


df2


# In[81]:


df3[df3 > 0] = 'C'


# In[82]:


df3


# In[83]:


df4 = pd.concat([df1, df2, df3])
df4


# In[84]:


df4 = pd.concat([df1, df2, df3], axis = 1)
df4


# In[ ]:




