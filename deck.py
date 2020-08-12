#!/usr/bin/env python
# coding: utf-8

# In[1]:
from collections import deque
# In[2]:
deck = deque('aeiou')
# In[3]:
print(deck)
# In[4]:
deck.append('b')
# In[5]:
deck
# In[7]:
deck.append('cd')
# In[8]:
deck
# In[9]:
deck.pop()
# In[11]:
deck.popleft()
# In[12]:
deck
# In[13]:
deck.appendleft('a')
# In[14]:
deck
# In[15]:
deck[0]
# In[16]:
deck[-1]
# In[25]:
list(deck)
# In[29]:
deck.reverse()
# In[32]:
print(deck)
# In[ ]:
