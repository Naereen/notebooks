#!/usr/bin/env python
# coding: utf-8

# # Débugguer du code Python depuis Notebook Jupyter

# ## Avec `pdb` ou `ipdb`
# 
# - <https://docs.python.org/3/library/pdb.html>
# - <https://pypi.org/project/ipdb/>

# In[8]:


get_ipython().run_line_magic('debug', '')

def print_endline(i: int) -> None:
    print(1.0 / i)

def main() -> None:
    for i in range(10, -10, -1):
        print_endline(i)o

main()


# ## Avec PixieDebugger - nouveau!
# 
# - <https://pixiedust.github.io/pixiedust/1-1-8.html>
# - <https://medium.com/codait/the-visual-python-debugger-for-jupyter-notebooks-youve-always-wanted-761713babc62>
# 

# In[11]:


import pixiedust


# In[10]:


pixiedust.optOut()


# In[ ]:


get_ipython().run_cell_magic('pixie_debugger', '', '\ndef print_endline(i: int) -> None:\n    print(1.0 / i)\n\ndef main() -> None:\n    for i in range(10, -10, -1):\n        print_endline(i)\n\nmain()')


# **Ca ne marche pas chez moi, ça affiche des codes couleurs ANSI non interprétés (16/02/2021).**

# ## Avec le nouveau débuggueur visuel de Jupyter Lab - new!
# 
# TODO!
# 
# - <https://github.com/jupyterlab/debugger>
# - See <https://blog.jupyter.org/a-visual-debugger-for-jupyter-914e61716559>
# - And <https://stackoverflow.com/a/61120586/5889533>

# In[14]:


def print_endline(i: int) -> None:
    print(1.0 / i)

def main() -> None:
    for i in range(10, -10, -1):
        print_endline(i)

main()


# ## Conclusion
# 
# C'est cool !
