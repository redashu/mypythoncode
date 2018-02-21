
# coding: utf-8

# In[3]:


#!/usr/bin/python3
from sklearn import tree
import numpy as np


# In[11]:


features=np.loadtxt("tryfootball.txt")
print(features)
k=features.reshape(10,160000)
print(features.shape)
print(k.shape)


# In[12]:


label=[]
for i in range(1,11):
    label.append([i])
print(label)


# In[14]:


clf=tree.DecisionTreeClassifier()
trained=clf.fit(k,label)


# In[18]:


remove=k[8]
training_data=np.delete(k,remove,axis=0)
training_target=np.delete(k,remove)


# In[19]:


print(trained.predict([remove]))


# In[ ]:




