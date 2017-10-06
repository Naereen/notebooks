
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Short-study-of-the-Lempel-Ziv-complexity" data-toc-modified-id="Short-study-of-the-Lempel-Ziv-complexity-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Short study of the Lempel-Ziv complexity</a></div><div class="lev2 toc-item"><a href="#Short-definition" data-toc-modified-id="Short-definition-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Short definition</a></div><div class="lev2 toc-item"><a href="#Python-implementation" data-toc-modified-id="Python-implementation-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Python implementation</a></div><div class="lev2 toc-item"><a href="#Tests-(1/2)" data-toc-modified-id="Tests-(1/2)-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Tests (1/2)</a></div><div class="lev2 toc-item"><a href="#Cython-implementation" data-toc-modified-id="Cython-implementation-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Cython implementation</a></div><div class="lev2 toc-item"><a href="#Numba-implementation" data-toc-modified-id="Numba-implementation-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Numba implementation</a></div><div class="lev2 toc-item"><a href="#Tests-(2/2)" data-toc-modified-id="Tests-(2/2)-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Tests (2/2)</a></div><div class="lev2 toc-item"><a href="#Benchmarks" data-toc-modified-id="Benchmarks-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Benchmarks</a></div><div class="lev2 toc-item"><a href="#Complexity-?" data-toc-modified-id="Complexity-?-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Complexity ?</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev2 toc-item"><a href="#(Experimental)-Julia-implementation" data-toc-modified-id="(Experimental)-Julia-implementation-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>(Experimental) <a href="http://julialang.org" target="_blank">Julia</a> implementation</a></div><div class="lev2 toc-item"><a href="#Ending-notes" data-toc-modified-id="Ending-notes-111"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Ending notes</a></div>

# # Short study of the Lempel-Ziv complexity
# 
# In this short [Jupyter notebook](https://www.Jupyter.org/) aims at defining and explaining the [Lempel-Ziv complexity](https://en.wikipedia.org/wiki/Lempel-Ziv_complexity).
# 
# [I](http://perso.crans.org/besson/) will give examples, and benchmarks of different implementations.
# 
# - **Reference:** Abraham Lempel and Jacob Ziv, *« On the Complexity of Finite Sequences »*, IEEE Trans. on Information Theory, January 1976, p. 75–81, vol. 22, n°1.

# ----
# ## Short definition
# The Lempel-Ziv complexity is defined as the number of different substrings encountered as the stream is viewed from begining to the end.
# 
# As an example:
# 
# ```python
# >>> s = '1001111011000010'
# >>> lempel_ziv_complexity(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010
# 6
# ```
# 
# Marking in the different substrings, this sequence $s$ has complexity $\mathrm{Lempel}$-$\mathrm{Ziv}(s) = 6$ because $s = 1001111011000010 = 1 / 0 / 01 / 1110 / 1100 / 0010$.
# 
# - See the page https://en.wikipedia.org/wiki/Lempel-Ziv_complexity for more details.

# Other examples:
# 
# ```python
# >>> lempel_ziv_complexity('1010101010101010')  # 1 / 0 / 10
# 3
# >>> lempel_ziv_complexity('1001111011000010000010')  # 1 / 0 / 01 / 1110 / 1100 / 0010 / 000 / 010
# 7
# >>> lempel_ziv_complexity('100111101100001000001010')  # 1 / 0 / 01 / 1110 / 1100 / 0010 / 000 / 010 / 10
# 8
# ```

# ----
# ## Python implementation

# In[1]:


def lempel_ziv_complexity(binary_sequence):
    """Lempel-Ziv complexity for a binary sequence, in simple Python code."""
    u, v, w = 0, 1, 1
    v_max = 1
    length = len(binary_sequence)
    complexity = 1
    while True:
        if binary_sequence[u + v - 1] == binary_sequence[w + v - 1]:
            v += 1
            if w + v >= length:
                complexity += 1
                break
        else:
            if v > v_max:
                v_max = v
            u += 1
            if u == w:
                complexity += 1
                w += v_max
                if w > length:
                    break
                else:
                    u = 0
                    v = 1
                    v_max = 1
            else:
                v = 1
    return complexity


# ----
# ## Tests (1/2)

# In[2]:


s = '1001111011000010'
lempel_ziv_complexity(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010


# In[3]:


get_ipython().run_line_magic('timeit', 'lempel_ziv_complexity(s)')


# In[4]:


lempel_ziv_complexity('1010101010101010')  # 1 / 0 / 10


# In[5]:


lempel_ziv_complexity('1001111011000010000010')  # 1 / 0 / 01 / 1110


# In[6]:


lempel_ziv_complexity('100111101100001000001010')  # 1 / 0 / 01 / 1110 / 1100 / 0010 / 000 / 010 / 10


# In[7]:


get_ipython().run_line_magic('timeit', "lempel_ziv_complexity('100111101100001000001010')")


# We can start to see that the time complexity of this function seems to grow exponentially as the complexity grows.

# ----
# ## Cython implementation
# As [this blog post](https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/) explains it, we can easily try to use [Cython](http://Cython.org/) in a notebook cell.
# 
# > See [the Cython documentation](http://docs.cython.org/en/latest/src/quickstart/build.html#using-the-jupyter-notebook) for more information.

# In[7]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[8]:


get_ipython().run_cell_magic('cython', '', 'from __future__ import division\nimport cython\n\nctypedef unsigned int DTYPE_t\n\n@cython.boundscheck(False) # turn off bounds-checking for entire function, quicker but less safe\ndef lempel_ziv_complexity_cython(str binary_sequence not None):\n    """Lempel-Ziv complexity for a binary sequence, in simple Cython code (C extension)."""\n    cdef DTYPE_t u = 0\n    cdef DTYPE_t v = 1\n    cdef DTYPE_t w = 1\n    cdef DTYPE_t v_max = 1\n    cdef DTYPE_t length = len(binary_sequence)\n    cdef DTYPE_t complexity = 1\n    # that was the only needed part, typing statically all the variables\n    while True:\n        if binary_sequence[u + v - 1] == binary_sequence[w + v - 1]:\n            v += 1\n            if w + v >= length:\n                complexity += 1\n                break\n        else:\n            if v > v_max:\n                v_max = v\n            u += 1\n            if u == w:\n                complexity += 1\n                w += v_max\n                if w > length:\n                    break\n                else:\n                    u = 0\n                    v = 1\n                    v_max = 1\n            else:\n                v = 1\n    return complexity')


# Let try it!

# In[9]:


s = '1001111011000010'
lempel_ziv_complexity_cython(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010


# In[10]:


get_ipython().run_line_magic('timeit', 'lempel_ziv_complexity_cython(s)')


# In[12]:


lempel_ziv_complexity_cython('1010101010101010')  # 1 / 0 / 10


# In[13]:


lempel_ziv_complexity_cython('1001111011000010000010')  # 1 / 0 / 01 / 1110


# In[14]:


lempel_ziv_complexity_cython('100111101100001000001010')  # 1 / 0 / 01 / 1110 / 1100 / 0010 / 000 / 010 / 10


# In[15]:


get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_cython('100111101100001000001010')")


# > $\implies$ Yay! It seems faster indeed!

# ----
# ## Numba implementation
# As [this blog post](https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/) explains it, we can also try to use [Numba](http://Numba.PyData.org/) in a notebook cell.

# In[87]:


from numba import jit


# In[94]:


@jit("int32(boolean[:])")
def lempel_ziv_complexity_numba_x(binary_sequence):
    """Lempel-Ziv complexity for a binary sequence, in Python code using numba.jit() for automatic speedup (hopefully)."""
    u, v, w = 0, 1, 1
    v_max = 1
    length = len(binary_sequence)
    complexity = 1
    while True:
        if binary_sequence[u + v - 1] == binary_sequence[w + v - 1]:
            v += 1
            if w + v >= length:
                complexity += 1
                break
        else:
            if v > v_max:
                v_max = v
            u += 1
            if u == w:
                complexity += 1
                w += v_max
                if w > length:
                    break
                else:
                    u = 0
                    v = 1
                    v_max = 1
            else:
                v = 1
    return complexity

def str_to_numpy(s):
    """str to np.array of bool"""
    return np.array([int(i) for i in s], dtype=np.bool)

def lempel_ziv_complexity_numba(s):
    return lempel_ziv_complexity_numba_x(str_to_numpy(s))


# Let try it!

# In[95]:


str_to_numpy(s)


# In[96]:


s = '1001111011000010'
lempel_ziv_complexity_numba(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010


# In[97]:


get_ipython().run_line_magic('timeit', 'lempel_ziv_complexity_numba(s)')


# In[98]:


lempel_ziv_complexity_numba('1010101010101010')  # 1 / 0 / 10


# In[99]:


lempel_ziv_complexity_numba('1001111011000010000010')  # 1 / 0 / 01 / 1110


# In[100]:


lempel_ziv_complexity_numba('100111101100001000001010')  # 1 / 0 / 01 / 1110 / 1100 / 0010 / 000 / 010 / 10


# In[101]:


get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_numba('100111101100001000001010')")


# > $\implies$ Well... It doesn't seem that much faster from the naive Python code.
# > We specified the signature when calling [`@numba.jit`](http://numba.pydata.org/numba-doc/latest/user/jit.html), and used the more appropriate data structure (string is probably the smaller, numpy array are probably faster).
# > But even these tricks didn't help that much.
# 
# > I tested, and without specifying the signature, the fastest approach is using string, compared to using lists or numpy arrays.
# > Note that the [`@jit`](http://numba.pydata.org/numba-doc/latest/user/jit.html)-powered function is compiled at runtime when first being called, so the signature used for the *first* call is determining the signature used by the compile function

# ----
# ## Tests (2/2)
# 
# To test more robustly, let us generate some (uniformly) random binary sequences.

# In[57]:


from numpy.random import binomial

def bernoulli(p, size=1):
    """One or more samples from a Bernoulli of probability p."""
    return binomial(1, p, size)


# In[25]:


bernoulli(0.5, 20)


# That's probably not optimal, but we can generate a string with:

# In[26]:


''.join(str(i) for i in bernoulli(0.5, 20))


# In[58]:


def random_binary_sequence(n, p=0.5):
    """Uniform random binary sequence of size n, with rate of 0/1 being p."""
    return ''.join(str(i) for i in bernoulli(p, n))


# In[60]:


random_binary_sequence(50)
random_binary_sequence(50, p=0.1)
random_binary_sequence(50, p=0.25)
random_binary_sequence(50, p=0.5)
random_binary_sequence(50, p=0.75)
random_binary_sequence(50, p=0.9)


# And so, this function can test to check that the three implementations (naive, Cython-powered, Numba-powered) always give the same result.

# In[29]:


def tests_3_functions(n, p=0.5, debug=True):
    s = random_binary_sequence(n, p=p)
    c1 = lempel_ziv_complexity(s)
    if debug:
        print("Sequence s = {} ==> complexity C = {}".format(s, c1))
    c2 = lempel_ziv_complexity_cython(s)
    c3 = lempel_ziv_complexity_numba(s)
    assert c1 == c2 == c3, "Error: the sequence {} gave different values of the Lempel-Ziv complexity from 3 functions ({}, {}, {})...".format(s, c1, c2, c3)
    return c1


# In[30]:


tests_3_functions(5)


# In[31]:


tests_3_functions(20)


# In[32]:


tests_3_functions(50)


# In[33]:


tests_3_functions(500)


# In[34]:


tests_3_functions(5000)


# ----
# ## Benchmarks
# 
# On two example of strings (binary sequences), we can compare our three implementation.

# In[102]:


get_ipython().run_line_magic('timeit', "lempel_ziv_complexity('100111101100001000001010')")
get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_cython('100111101100001000001010')")
get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_numba('100111101100001000001010')")


# In[103]:


get_ipython().run_line_magic('timeit', "lempel_ziv_complexity('10011110110000100000101000100100101010010111111011001111111110101001010110101010')")
get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_cython('10011110110000100000101000100100101010010111111011001111111110101001010110101010')")
get_ipython().run_line_magic('timeit', "lempel_ziv_complexity_numba('10011110110000100000101000100100101010010111111011001111111110101001010110101010')")


# Let check the time used by all the three functions, for longer and longer sequences:

# In[104]:


get_ipython().run_line_magic('timeit', 'tests_3_functions(10, debug=False)')
get_ipython().run_line_magic('timeit', 'tests_3_functions(20, debug=False)')
get_ipython().run_line_magic('timeit', 'tests_3_functions(40, debug=False)')
get_ipython().run_line_magic('timeit', 'tests_3_functions(80, debug=False)')
get_ipython().run_line_magic('timeit', 'tests_3_functions(160, debug=False)')
get_ipython().run_line_magic('timeit', 'tests_3_functions(320, debug=False)')


# In[105]:


def test_cython(n):
    s = random_binary_sequence(n)
    c = lempel_ziv_complexity_cython(s)
    return c


# In[39]:


get_ipython().run_line_magic('timeit', 'test_cython(10)')
get_ipython().run_line_magic('timeit', 'test_cython(20)')
get_ipython().run_line_magic('timeit', 'test_cython(40)')
get_ipython().run_line_magic('timeit', 'test_cython(80)')
get_ipython().run_line_magic('timeit', 'test_cython(160)')
get_ipython().run_line_magic('timeit', 'test_cython(320)')


# In[40]:


get_ipython().run_line_magic('timeit', 'test_cython(640)')
get_ipython().run_line_magic('timeit', 'test_cython(1280)')
get_ipython().run_line_magic('timeit', 'test_cython(2560)')
get_ipython().run_line_magic('timeit', 'test_cython(5120)')


# In[41]:


get_ipython().run_line_magic('timeit', 'test_cython(10240)')
get_ipython().run_line_magic('timeit', 'test_cython(20480)')


# ----
# ## Complexity ?
# $\implies$ The function `lempel_ziv_complexity_cython` seems to be indeed (almost) linear in $n$, the length of the binary sequence $S$.
# 
# But let check more precisely, as it could also have a complexity of $\mathcal{O}(n \log n)$.

# In[42]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(context="notebook", style="darkgrid", palette="hls", font="sans-serif", font_scale=1.4)


# It's durty, but let us capture manually the times given by the experiments above.

# In[43]:


x = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
y = [18, 30, 55, 107, 205, 471, 977, 2270, 5970, 17300, 56600, 185000]


# In[44]:


plt.figure()
plt.plot(x, y, 'o-')
plt.xlabel("Length $n$ of the binary sequence $S$")
plt.ylabel(r"Time in $\mu\;\mathrm{s}$")
plt.title("Time complexity of Lempel-Ziv complexity")
plt.show()


# In[45]:


plt.figure()
plt.semilogx(x, y, 'o-')
plt.xlabel("Length $n$ of the binary sequence $S$")
plt.ylabel(r"Time in $\mu\;\mathrm{s}$")
plt.title("Time complexity of Lempel-Ziv complexity, semilogx scale")
plt.show()


# In[46]:


plt.figure()
plt.semilogy(x, y, 'o-')
plt.xlabel("Length $n$ of the binary sequence $S$")
plt.ylabel(r"Time in $\mu\;\mathrm{s}$")
plt.title("Time complexity of Lempel-Ziv complexity, semilogy scale")
plt.show()


# In[47]:


plt.figure()
plt.loglog(x, y, 'o-')
plt.xlabel("Length $n$ of the binary sequence $S$")
plt.ylabel(r"Time in $\mu\;\mathrm{s}$")
plt.title("Time complexity of Lempel-Ziv complexity, loglog scale")
plt.show()


# It is linear in $\log\log$ scale, so indeed the algorithm seems to have a linear complexity.
# 
# To sum-up, for a sequence $S$ of length $n$, it takes $\mathcal{O}(n)$ basic operations to compute its Lempel-Ziv complexity $\mathrm{Lempel}-\mathrm{Ziv}(S)$.

# ----
# ## Conclusion
# 
# - The Lempel-Ziv complexity is not too hard to implement, and it indeed represents a certain complexity of a binary sequence, capturing the regularity and reproducibility of the sequence.
# 
# - Using the [Cython](http://Cython.org/) was quite useful to have a $\simeq \times 100$ speed up on our manual naive implementation !
# 
# - The algorithm is not easy to analyze, we have a trivial $\mathcal{O}(n^2)$ bound but experiments showed it is more likely to be $\mathcal{O}(n \log n)$ in the worst case, and $\mathcal{O}(n)$ in practice for "not too complicated sequences" (or in average, for random sequences).

# ----
# ## (Experimental) [Julia](http://julialang.org) implementation
# 
# I want to (quickly) try to see if I can use [Julia](http://julialang.org) to write a faster version of this function.
# See [issue #1](https://github.com/Naereen/Lempel-Ziv_Complexity/issues/1).
# 
# **Disclaimer:** I am still learning Julia!

# In[16]:


get_ipython().run_cell_magic('time', '', '%%script julia\n\n"""Lempel-Ziv complexity for a binary sequence, in simple Julia code."""\nfunction lempel_ziv_complexity(binary_sequence)\n    u, v, w = 0, 1, 1\n    v_max = 1\n    size = length(binary_sequence)\n    complexity = 1\n    while true\n        if binary_sequence[u + v] == binary_sequence[w + v]\n            v += 1\n            if w + v >= size\n                complexity += 1\n                break\n            end\n        else\n            if v > v_max\n                v_max = v\n            end\n            u += 1\n            if u == w\n                complexity += 1\n                w += v_max\n                if w > size\n                    break\n                else\n                    u = 0\n                    v = 1\n                    v_max = 1\n                end\n            else\n                v = 1\n            end\n        end\n    end\n    return complexity\nend\n\ns = "1001111011000010"\nlempel_ziv_complexity(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010\n\nM = 100;\nN = 10000;\nfor _ in 1:M\n    s = join(rand(0:1, N));\n    lempel_ziv_complexity(s);\nend\nlempel_ziv_complexity(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010')


# And to compare it fairly, let us use [Pypy](http://pypy.org) for comparison.

# In[17]:


get_ipython().run_cell_magic('time', '', '%%pypy\n\ndef lempel_ziv_complexity(binary_sequence):\n    """Lempel-Ziv complexity for a binary sequence, in simple Python code."""\n    u, v, w = 0, 1, 1\n    v_max = 1\n    length = len(binary_sequence)\n    complexity = 1\n    while True:\n        if binary_sequence[u + v - 1] == binary_sequence[w + v - 1]:\n            v += 1\n            if w + v >= length:\n                complexity += 1\n                break\n        else:\n            if v > v_max:\n                v_max = v\n            u += 1\n            if u == w:\n                complexity += 1\n                w += v_max\n                if w > length:\n                    break\n                else:\n                    u = 0\n                    v = 1\n                    v_max = 1\n            else:\n                v = 1\n    return complexity\n\ns = "1001111011000010"\nlempel_ziv_complexity(s)  # 1 / 0 / 01 / 1110 / 1100 / 0010\n\nfrom random import random\n\nM = 100\nN = 10000\nfor _ in range(M):\n    s = \'\'.join(str(int(random() < 0.5)) for _ in range(N))\n    lempel_ziv_complexity(s)')


# So we can check that on these 100 random trials on strings of size 10000, the naive Julia version is about twice as fast as the naive Python version (executed by Pypy for speedup).
# 
# That's good, but it's not much...

# ----
# ## Ending notes
# > Thanks for reading!
# > My implementation is [now open-source and available on GitHub](https://github.com/Naereen/Lempel-Ziv_Complexity), on https://github.com/Naereen/Lempel-Ziv_Complexity.
# 
# > It will be available from PyPi very soon, see https://pypi.python.org/pypi/lempel_ziv_complexity.
# 
# > See [this repo on GitHub](https://github.com/Naereen/notebooks/) for more notebooks, or [on nbviewer.jupyter.org](https://nbviewer.jupyter.org/github/Naereen/notebooks/).
# 
# > That's it for this demo! See you, folks!
