#!/usr/bin/env python
# coding: utf-8

# 1.Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving
# average of the given sequence is defined as follows:
# The moving average sequence has n-k+1 elements as shown below.

# In[22]:


from collections import deque
import itertools

def moving_average(iterable, n=3):
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable) 
    # create an iterable object from input argument
    d = deque(itertools.islice(it, n-1))  
    # create deque object by slicing iterable
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

# example on how to use it
for i in  moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




