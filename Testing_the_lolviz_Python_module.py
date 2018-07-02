
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Testing-lolviz" data-toc-modified-id="Testing-lolviz-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Testing <a href="https://github.com/parrt/lolviz" target="_blank">lolviz</a></a></div><div class="lev2 toc-item"><a href="#Testing-naively" data-toc-modified-id="Testing-naively-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Testing naively</a></div><div class="lev2 toc-item"><a href="#Testing-from-within-a-Jupyter-notebook" data-toc-modified-id="Testing-from-within-a-Jupyter-notebook-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Testing from within a Jupyter notebook</a></div><div class="lev3 toc-item"><a href="#List" data-toc-modified-id="List-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>List</a></div><div class="lev3 toc-item"><a href="#List-of-lists" data-toc-modified-id="List-of-lists-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>List of lists</a></div><div class="lev3 toc-item"><a href="#List-of-lists-of-lists???" data-toc-modified-id="List-of-lists-of-lists???-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>List of lists of lists???</a></div><div class="lev3 toc-item"><a href="#Tree" data-toc-modified-id="Tree-124"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Tree</a></div><div class="lev3 toc-item"><a href="#Objects" data-toc-modified-id="Objects-125"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Objects</a></div><div class="lev3 toc-item"><a href="#Calls" data-toc-modified-id="Calls-126"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>Calls</a></div><div class="lev3 toc-item"><a href="#String" data-toc-modified-id="String-127"><span class="toc-item-num">1.2.7&nbsp;&nbsp;</span>String</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Testing [lolviz](https://github.com/parrt/lolviz)
# 
# I liked how the [lolviz](https://github.com/parrt/lolviz) module looked like. Let's try it!

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -p lolviz')


# In[3]:


from lolviz import *


# ## Testing naively

# In[4]:


data = ['hi', 'mom', {3, 4}, {"parrt": "user"}]
g = listviz(data)
print(g.source) # if you want to see the graphviz source
g.view() # render and show graphviz.files.Source object


# It opened a window showing me this image:
# 
# <img src="data/Testing_the_lolviz_Python_module_1.png" width=55%>

# ## Testing from within a Jupyter notebook
# 
# I test here all [the features of lolviz](https://github.com/parrt/lolviz#functionality) :

# ### List

# In[13]:


squares = [ i**2 for i in range(10) ]


# In[14]:


squares


# In[15]:


listviz(squares)


# ### List of lists

# In[16]:


n, m = 3, 4
example_matrix = [[0 if i != j else 1 for i in range(n)] for j in range(m)]


# In[17]:


example_matrix


# In[18]:


lolviz(example_matrix)


# ### List of lists of lists???

# In[22]:


n, m, o = 2, 3, 4
example_3D_matrix = [[[
    1 if i < j < k else 0
    for i in range(n)]
    for j in range(m)]
    for k in range(o)]


# In[23]:


example_3D_matrix


# In[25]:


lolviz(example_3D_matrix)


# It works, even if it is not as pretty.

# ### Tree
# Only for binary trees, apparently. Let's try with a dictionary that looks like a binary tree:

# In[26]:


anakin = {
    "name": "Anakin Skywalker",
    "son": {
        "name": "Luke Skywalker",
    },
    "daughter": {
        "name": "Leia Skywalker",
    },
}


# In[27]:


from pprint import pprint
pprint(anakin)


# In[42]:


treeviz(anakin, leftfield='son', rightfield='daugther')


# It doesn't work out of the box for dictionaries, sadly.
# 
# Let's check another example:

# In[67]:


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
root = Tree('parrt',
            Tree('mary',
                 Tree('jim',
                      Tree('srinivasan'),
                      Tree('april'))),
            Tree('xue',None,Tree('mike')))

treeviz(root)


# ### Objects

# In[48]:


objviz(anakin)


# In[49]:


objviz(anakin.values())


# In[50]:


objviz(anakin.items())


# For complex numbers for instance?

# In[74]:


z = 1+4j


# In[75]:


print(z)


# In[77]:


objviz(z)


# OK, this fails.

# ### Calls

# In[55]:


def factorial(n):
    if n < 0: return 0
    elif n == 0: return 1
    else: return n * factorial(n - 1)


# In[57]:


for n in range(12):
    print(f"{n}! = {factorial(n)}")


# And now with some visualization:

# In[ ]:


from IPython.display import display


# In[72]:


def factorial2(n):
    display(callsviz(varnames=["n"]))
    if n < 0: return 0
    elif n == 0: return 1
    else: return n * factorial2(n - 1)


# In[73]:


n = 4
print(f"{n}! = {factorial2(n)}")


# We really see the "call stack" as the system keeps track of the nested calls. I like that! 👌

# ### String

# In[8]:


import string
string.hexdigits


# In[9]:


strviz(string.hexdigits)


# ## Conclusion
# That's it. See [this other example](https://github.com/parrt/lolviz/blob/master/examples.ipynb) for more.
