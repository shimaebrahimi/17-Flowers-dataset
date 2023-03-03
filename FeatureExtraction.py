#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import pandas as pd
import cv2
import os
import h5py
import mahotas
import pickle


# In[2]:


train_labels = [i for i in os.listdir('flwfolder3/jpg') if '.txt' not in i] 
train_labels


# In[3]:


train_labels.sort()


# In[4]:


train_labels


# In[5]:


X = []
y = []
for label in train_labels:
    dir = os.path.join('flwfolder2/jpg', label)
    current_label = label
    print('Current Folder: ' + current_label)
    for x in range(1, 81):
        print('Current Image: ' + str(x))
        file = os.path.join(dir, str(x) + '.jpg')
        image = cv2.imread(file)
        try:
            image = cv2.resize(image,(500,500))
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
            cv2.normalize(hist, hist)
            histogram_features = hist.flatten()
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            hue_features = cv2.HuMoments(cv2.moments(image_gray)).flatten()
            haralick_features = mahotas.features.haralick(image_gray).mean(axis=0)
            current_features = np.hstack([histogram_features, hue_features, haralick_features])
            X.append(current_features)
            y.append(current_label)
        except:
            break


# In[ ]:


np.shape(X)


# In[ ]:


np.shape(y)


# In[ ]:


le = LabelEncoder()
y = le.fit_transform(y)


# In[ ]:


y


# In[ ]:


mms = MinMaxScaler()
X = mms.fit_transform(X)


# In[ ]:


X


# In[ ]:


h5_X = h5py.File('data/X.h5', 'w')
h5_X.create_dataset('features', data=np.array(X))


# In[ ]:


h5_y = h5py.File('data/y.h5', 'w')
h5_y.create_dataset('targets', data=np.array(y))


# In[ ]:


h5_X.close()
h5_y.close()


# In[ ]:


with open('data/le.h5', 'wb') as f:
    pickle.dump(le, f)


# In[ ]:


with open('data/mms.h5', 'wb') as f:
    pickle.dump(mms, f)


# In[ ]:




