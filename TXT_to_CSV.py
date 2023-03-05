#!/usr/bin/env python
# coding: utf-8

# ## Importing Modules

# In[1]:


import re
import csv
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Setting up files

# In[ ]:


source = 'Feb2023.TXT'


# ## Reading Files

# In[ ]:


file = open(source, 'r',  encoding="utf-8")


# In[ ]:


read = file.readlines()


# In[ ]:


no_header = read[8:]


# In[ ]:


no_header


# In[ ]:





# ## Cleaning function

# In[ ]:


def clean(line):
    
    purg = line.split('  ')
    
    while '' in purg:
        purg.remove('')
        
    ','.join(purg)
        
    return purg


# In[ ]:


write_to_file = []


# In[ ]:


for line in no_header:
    
    write_to_file.append(clean(line))


# In[ ]:


write_to_file


# ## Writing new CSV file

# In[ ]:


with open("Feb2023_v2.csv", "w", encoding='Utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(write_to_file)


# ## Loading new CSV file

# In[2]:


df = pd.read_csv('Feb2023_v2.csv',sep=',',encoding='Utf-8', engine='python')


# In[6]:


df.head()


# In[13]:


df[df['Tender'] == r'CHA-\w+\r\n'].value_counts()


# In[4]:


df.drop('Unnamed: 0', axis=1, inplace=True)


# ## Preparing file

# In[ ]:


mapper = ({0:'Invoice_#',
           1:'Clerk',
           2:'SKU',
           3:'Name',
           4:'Quantity',
           5:'Net_Price',
           6:'Total_Sale',
           7:'COGS',
           8:'Profit',
           9:'Margin',
           10:'Tender'})


# In[ ]:


df = df.rename(columns=mapper)


# ## Correcting 'Tender' info

# In[ ]:


df = df.replace(['DBC\r\n'], 'Debit')
df = df.replace(['VIS\r\n'], 'Visa')
df = df.replace(['MAS\r\n'], 'Mastercard')
df = df.replace(['CAS\r\n'], 'Cash')


# In[ ]:


df.info()


# In[ ]:


df = df.dropna()


# In[ ]:


## boolseries = (df['SKU'] != 'EF5') & (df['SKU'] != 'EF4') & (df['SKU'] != 'EF3') & (df['SKU'] != 'EF2') & (df['SKU'] != 'EF1') & (df['SKU'] != '/H') & (df['SKU'] != 'DELIVERY')
## (df['SKU'] != 'EF5') & (df['SKU'] != 'EF4') & (df['SKU'] != 'EF3') & (df['SKU'] != 'EF2') & (df['SKU'] != 'EF1')


# ## Saving new CSV

# In[ ]:


df.to_csv(path_or_buf='Feb2023_v2.csv')


# In[ ]:


cleandf[cleandf['SKU'] == 'DELIVERY']


# In[ ]:


df[df['SKU'] == '/H']


# In[ ]:


cleandf = cleandf[~(cleandf['SKU'] == 'WARNING.')]


# In[ ]:


cleandf.info()


# In[ ]:


cleandf.plot.hexbin(x='Total_Sale', y='Profit',gridsize=15)


# In[ ]:


bysku = cleandf.groupby('SKU').Total_Sale.aggregate(np.sum)


# In[ ]:


cleandf[['SKU','Profit']].value_counts()


# In[ ]:





# In[29]:


rank = df.groupby(['SKU'])['Total_Sale'].sum()


# In[30]:


rank


# In[67]:


rank.sort_values(ascending=False)[0:21]


# In[47]:


rank.sort_values(ascending=False)[0:11].plot.pie()


# In[41]:


rank


# In[48]:





# In[62]:


sns.distplot(test(['SKU']),bins=30)


# In[55]:


df.groupby(['SKU'])


# In[61]:


test = df.groupby(['SKU']).sum()


# In[63]:


test


# In[ ]:




