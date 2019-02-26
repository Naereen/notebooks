
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Demonstration-of-running-a-Jupyter-notebook-with-sudo-rights" data-toc-modified-id="Demonstration-of-running-a-Jupyter-notebook-with-sudo-rights-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Demonstration of running a Jupyter notebook with sudo rights</a></div><div class="lev2 toc-item"><a href="#Without-sudo-rights" data-toc-modified-id="Without-sudo-rights-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Without sudo rights</a></div><div class="lev2 toc-item"><a href="#With-sudo-rights" data-toc-modified-id="With-sudo-rights-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>With sudo rights</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Demonstration of running a Jupyter notebook with sudo rights

# ## Without sudo rights
# 
# The next cells were first ran when Jupyter was not running with sudo rights.

# In[5]:


get_ipython().system('apt update')


# In[6]:


get_ipython().system('sudo apt update')


# As we see here, using `sudo ...` asks for a password, but it doesn't work from Jupyter.

# ## With sudo rights
# The next cells were then ran when Jupyter was running with sudo rights.

# In[6]:


get_ipython().system('apt update')


# It works!

# ## Conclusion
# 
# It works!
