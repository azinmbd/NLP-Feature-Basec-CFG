#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


tokens = "Kim chased Lee".split()


# In[3]:


kim = {'CAT': 'NP', 'ORTH':'Kim', 'REF': 'k'}


# In[4]:


lee = {'CAT': 'NP', 'ORTH':'Lee', 'REF': 'l'}


# In[5]:


chase = {'CAT': 'V', 'ORTH':'chased', 'REL': 'chase'}


# In[8]:


def lex(word):
    for fs in [kim, lee, chase]:
        if fs['ORTH'] == word:
            return fs


# In[9]:


subj, verb, obj = lex(tokens[0]), lex(tokens[1]), lex(tokens[2])


# In[10]:


chase['AGT'] = 'sbj'


# In[11]:


chase['PAT'] = 'obj'


# In[12]:


verb['AGT'] = subj['REF']


# In[13]:


verb['PAT'] = obj['REF']


# In[14]:


for k in ['ORTH', 'REL', 'AGT', 'PAT']:
    print("%-5s => %s" % (k, verb[k]))


# In[ ]:




