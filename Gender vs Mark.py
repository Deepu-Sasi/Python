#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[5]:


os.chdir('C:\\Users\\user\\OneDrive\\Desktop\\deepu')


# In[6]:


os.getcwd()


# In[10]:


import matplotlib.pyplot as plt
from pandas import *
df= read_csv("AllDetails.csv")
x=df['Mark'].tolist()
y=df['Gender'].tolist()
plt.plot(x,y)    
plt.xlabel("Mark")
plt.ylabel("Gender")
plt.grid()
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(x,y,color='r')
ax.set_xlabel('Mark')
ax.set_ylabel('Gender')
plt.show()


# In[8]:


df


# In[11]:


ko=df.loc[df['Gender']=='f']


# In[12]:


ko


# In[13]:


ko
q=ko['Mark'].tolist()
w=ko['Gender'].tolist()
u=0
s=0
for i in q:
    u=u+i
for i in w:
    s=s+1
print("Total mark of female students:" +str(u) )
print("Total number of female students:" +str(s))
avg_f=u/s
print("Average mark of female students :" +str(avg_f))


# In[14]:


nm=df.loc[df['Gender']=='m']


# In[15]:


nm


# In[16]:


nm
l=nm['Mark'].tolist()
g=nm['Gender'].tolist()
p=0
a=0
for j in l:
    p=p+j
for t in g:
    a=a+1    
print(p)
print(a)
print("Total mark of male students:" +str(p) )
print("Total number of male students:" +str(a))
avg_m=p/a
print("Average mark of male students :" +str(avg_m))


# In[17]:


if avg_f > avg_m:
    print('Female students have greater average score')
else :
    print('Males students have greater average score')


# In[ ]:




