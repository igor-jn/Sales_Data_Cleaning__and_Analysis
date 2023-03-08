#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import csv
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[67]:


df = pd.read_csv('newdata.CSV',encoding='Utf-8',engine='python')
df.dropna(inplace=True)


# In[68]:


df.head()


# In[29]:


df[['Item #', 'Sales','Profit','Margin','Net Sold']]


# In[35]:


topten = df.sort_values('Sales',ascending=False).head(10)


# In[65]:


sns.countplot(data=topten, y=topten['Sales'])


# In[44]:


sns.distplot(topten['Sales'],bins=15)


# In[47]:


topten = topten[['Item #','Sales','Profit','Margin']]


# In[48]:


topten


# In[61]:


sns.barplot(x='Sales',y='Item #',data=topten,palette='crest', orient='h')


# ## 248 Detailing

# In[100]:


df248 = pd.read_csv('248s_feb2023.csv',sep=',',header=None,encoding='Utf-8', engine='python')
df248


# In[101]:


df248.dropna(inplace=True)


# In[102]:


mapper = ({0:'Invoice',
           1:'customer#',
           2:'invoicedate',
           3:'qty',
           4:'UOM',
           5:'netprice',
           6:'Total',
           7:'COGS',
           8:'Profit',
           9:'Margin'})


# In[103]:


df248 = df248.rename(columns=mapper)


# In[ ]:





# In[90]:


df248.invoicedate = pd.to_datetime(df248.invoicedate)


# In[128]:


byday = df248.set_index('day')


# In[144]:


sns.countplot(y=byday['day'],data=byday,palette='crest',orient='h')


# In[132]:


df248['day'] = df248.invoicedate.apply(lambda x: getday(x))


# In[121]:


def getday(date):
    
    work = date.split('/')
    
    return work[1]        


# In[119]:


work = df248.invoicedate[0].split('/')


# In[120]:


work


# In[ ]:





# In[135]:


byday['day'] = byday.invoicedate.apply(lambda x: getday(x))


# In[ ]:





# In[ ]:




