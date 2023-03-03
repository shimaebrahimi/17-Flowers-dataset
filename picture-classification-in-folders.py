#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

url = 'https://www.robots.ox.ac.uk/~vgg/data/flowers/17/17flowers.tgz'
target_path = 'file.tgz'

response = requests.get(url, stream=True)
with open(target_path, 'wb') as f:
    f.write(response.raw.read())


# In[12]:


import tarfile


# In[13]:


import os


# In[3]:


os.stat('file.tgz')


# In[4]:


tar=tarfile.open('file.tgz')
tar.extractall('flwfolder3')
tar.close


# In[5]:


import glob


# In[7]:


image_path=sorted(glob.glob('flwfolder3/jpg/*.jpg'))


# In[8]:


image_path


# In[9]:


class_names=['Buttercup','Colts’Foot','Daffodil','Daisy','Dandelion','Fritillary','Iris','Pansy','Sunflower','Windflower','Snowdrop','LilyValley','Bluebell','Crocus','Tigerlily','Tulip','Cowslip']


# In[11]:


l=0
i=0
j=80
for p in range(1,18):
    os.makedirs('flwfolder3/jpg/' + class_names[l])
    cpath='flwfolder3/jpg/' + class_names[l] + '/'
    for index,imgpath in enumerate(image_path[i:j],start=1):
        original=imgpath
#         i_p=imgpath.split('/')
        f_n=str(index)+'.jpg'
        os.rename(original,cpath+f_n)
       
        
    i+=80
    l+=1
    j+=80
        
    


# In[ ]:




