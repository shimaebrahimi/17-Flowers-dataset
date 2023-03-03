#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import h5py
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier


# In[5]:


x=h5py.File(os.path.join('data','X.h5'),'r')['features']


# In[6]:


y=h5py.File(os.path.join('data','y.h5'),'r')['targets']


# In[7]:


x_train,x_test,y_train,y_test=train_test_split(np.array(x),np.array(y),random_state=13)


# In[8]:


rfc=RandomForestClassifier(n_estimators=1000)
rfc.fit(x_train,y_train)


# In[9]:


y_pred=rfc.predict(x_test)


# In[10]:


print(classification_report(y_test,y_pred))


# In[11]:


rfc.score(x_test,y_test)


# In[12]:


from catboost import CatBoostClassifier


# In[13]:


cc=CatBoostClassifier(iterations=500,learning_rate=0.05,depth=6,eval_metric='Accuracy',verbose=10)


# In[14]:


cc.fit(x_train,y_train,eval_set=(x_test,y_test))


# In[ ]:




