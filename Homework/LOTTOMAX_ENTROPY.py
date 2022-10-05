#!/usr/bin/env python
# coding: utf-8

# # Pipeline
# 
# Understanding the Business Problem > Exploratory Analysis > Data Mining > Entropy Calculation > Information Entropy Calculation
# 

# In[36]:


# Loading csv
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import os 
import pandas as pd


# In[37]:


data = pd.read_csv('C:/Users/vinic/Downloads/LOTTOMAX.csv')


# In[38]:


data.head()


# In[39]:


data.shape


# In[40]:


data.describe()


# In[41]:


data.groupby('NUMBER DRAWN 1').size()


# In[42]:


data = data.drop(columns=['DRAW NUMBER','SEQUENCE NUMBER'])
data_clean = data

colums = ['NUMBER DRAWN 1', 'NUMBER DRAWN 2', 'NUMBER DRAWN 3', 'NUMBER DRAWN 4',       'NUMBER DRAWN 5', 'NUMBER DRAWN 6', 'NUMBER DRAWN 7']


# In[43]:


data_clean.corr(method = 'pearson')


# In[44]:


from scipy.stats import entropy
from math import log2
from matplotlib import pyplot


# entropy for a random number from 1 to 7 draw
probs = [1/49, 1/48, 1/47, 1/46, 1/45, 1/44, 1/43, 1/42]
e = entropy(probs, base=49) 


# In[45]:


print('entropy: %.3f bits' % e)


# In[46]:


dists = [[p, 1.0 - p] for p in probs]

# calculate entropy for each distribution
ents = [entropy(d) for d in dists]

pyplot.plot(probs, ents, marker='.')
pyplot.title('Probability Distribution vs Entropy')
pyplot.xticks(probs, [str(d) for d in dists])
pyplot.xlabel('Probability Distribution')
pyplot.ylabel('Entropy (bits)')
pyplot.show()


# ## The formula for the Information Entropy looks like this

# <center><h2>$\displaystyle S = - k \sum_{i=1}^{W} p(i) \log p(i)$</h2></center>

# In[47]:


list = []
for col in colums:
  list.extend(data[col].values.tolist())

result_list = pd.Series(list)
e = entropy(result_list.value_counts(), base=49)


# In[48]:


print('entropy: %.3f bits' % e)


# <h3>With that result we can say that it's extremely difficult to fit an accurate ML model to predict results on lottery.<h3>

# In[ ]:




