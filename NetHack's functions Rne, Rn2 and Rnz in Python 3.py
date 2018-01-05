
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#NetHack's-functions-Rne,-Rn2-and-Rnz-in-Python-3" data-toc-modified-id="NetHack's-functions-Rne,-Rn2-and-Rnz-in-Python-3-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>NetHack's functions Rne, Rn2 and Rnz in Python 3</a></div><div class="lev2 toc-item"><a href="#Rn2-distribution" data-toc-modified-id="Rn2-distribution-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span><code>Rn2</code> distribution</a></div><div class="lev2 toc-item"><a href="#Rne-distribution" data-toc-modified-id="Rne-distribution-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span><code>Rne</code> distribution</a></div><div class="lev2 toc-item"><a href="#Rnz-distribution" data-toc-modified-id="Rnz-distribution-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span><code>Rnz</code> distribution</a></div><div class="lev2 toc-item"><a href="#Examples" data-toc-modified-id="Examples-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Examples</a></div><div class="lev3 toc-item"><a href="#For-x=350" data-toc-modified-id="For-x=350-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>For <code>x=350</code></a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></div>

# # NetHack's functions Rne, Rn2 and Rnz in Python 3
# 
# I liked [this blog post](https://eev.ee/blog/2018/01/02/random-with-care/#beware-gauss) by [Eevee](https://eev.ee/blog/).
# He wrote about interesting things regarding random distributions, and linked to [this page](https://nethackwiki.com/wiki/Rnz) which describes a weird distribution implemented as `Rnz` in the [NetHack](https://www.nethack.org/) game.
# 
# > Note: I never heard of any of those before today.
# 
# I wanted to implement and experiment with the `Rnz` distribution myself.
# Its code ([see here](https://nethackwiki.com/wiki/Source:NetHack_3.6.0/src/rnd.c#rnz)) uses two other distributions, `Rne` and `Rn2`.

# In[41]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -p numpy,matplotlib')


# In[39]:


import random
import numpy as np
import matplotlib.pyplot as plt


# ## `Rn2` distribution
# 
# [The `Rn2` distribution](https://nethackwiki.com/wiki/Rn2) is simply an integer uniform distribution, between $0$ and $x-1$.

# In[19]:


def rn2(x):
    return random.randint(0, x-1)


# In[20]:


np.asarray([rn2(10) for _ in range(100)])


# Testing for `rn2(x) == 0` gives a $1/x$ probability :

# In[32]:


from collections import Counter


# In[35]:


Counter([rn2(10) == 0 for _ in range(100)])


# In[36]:


Counter([rn2(10) == 0 for _ in range(1000)])


# In[37]:


Counter([rn2(10) == 0 for _ in range(10000)])


# ## `Rne` distribution
# 
# [The `Rne` distribution]() is a truncated geometric distribution.

# In[88]:


def rne(x, truncation=5):
    truncation = max(truncation, 1)
    tmp = 1
    while tmp < truncation and rn2(x) == 0:
        tmp += 1
    return tmp


# > In the NetHack game, the player's experience is used as default value of the `truncation` parameter...

# In[89]:


np.asarray([rne(3) for _ in range(50)])


# In[90]:


plt.hist(np.asarray([rne(3) for _ in range(10000)]), bins=5)


# In[91]:


np.asarray([rne(4, truncation=10) for _ in range(50)])


# In[92]:


plt.hist(np.asarray([rne(4, truncation=10) for _ in range(10000)]), bins=10)


# Let's check what [this page](https://nethackwiki.com/wiki/Rnz#Probability_density_function) says about `rne(4)`:
# 
# > The rne(4) call returns an integer from 1 to 5, with the following probabilities:
# >
# > |Number| Probability |
# > |:-----|------------:|
# > | 1 | 3/4 |
# > | 2 | 3/16 |
# > | 3 | 3/64 |
# > | 4 | 3/256 |
# > | 5 | 1/256 | 

# In[96]:


ref_table = {1: 3/4, 2: 3/16, 3: 3/64, 4: 3/256, 5: 1/256}
ref_table


# In[99]:


N = 100000
table = Counter([rne(4, truncation=5) for _ in range(N)])
for k in table:
    table[k] /= N
table = dict(table)
table


# In[111]:


rel_diff = lambda x, y: abs(x - y) / x
for k in ref_table:
    x, y = ref_table[k], table[k]
    r = rel_diff(x, y)
    print(f"For k={k}: relative difference is {r:.3g} between {x:.3g} (expectation) and {y:.3g} (with N={N} samples).")


# > Seems true !

# ## `Rnz` distribution
# 
# It's not too hard to write.

# In[112]:


def rnz(i, truncation=10):
    x = i
    tmp = 1000
    tmp += rn2(1000)
    tmp *= rne(4, truncation=truncation)
    flip = rn2(2)
    if flip:
        x *= tmp
        x /= 1000
    else:
        x *= 1000
        x /= tmp
    return int(x)


# ## Examples

# In[113]:


np.asarray([rnz(3) for _ in range(100)])


# In[114]:


np.asarray([rnz(3, truncation=10) for _ in range(100)])


# ### For `x=350`

# In[115]:


np.asarray([rnz(350) for _ in range(100)])


# In[122]:


_ = plt.hist(np.asarray([rnz(350) for _ in range(100000)]), bins=200)


# In[78]:


np.asarray([rnz(350, truncation=10) for _ in range(100)])


# In[120]:


_ = plt.hist(np.asarray([rnz(350, truncation=10) for _ in range(10000)]), bins=200)


# ## Conclusion
# That's it, not so interesting but I wanted to write this.
