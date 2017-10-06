
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Benchmark-between-Python-and-Julia" data-toc-modified-id="Benchmark-between-Python-and-Julia-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Benchmark between Python and Julia</a></div><div class="lev2 toc-item"><a href="#The-Romberg-method" data-toc-modified-id="The-Romberg-method-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>The Romberg method</a></div><div class="lev2 toc-item"><a href="#The-Romberg-method,-naive-recursive-version-in-Python" data-toc-modified-id="The-Romberg-method,-naive-recursive-version-in-Python-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>The Romberg method, naive recursive version in Python</a></div><div class="lev2 toc-item"><a href="#The-Romberg-method,-dynamic-programming-version-in-Python" data-toc-modified-id="The-Romberg-method,-dynamic-programming-version-in-Python-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>The Romberg method, dynamic programming version in Python</a></div><div class="lev2 toc-item"><a href="#The-Romberg-method,-better-dynamic-programming-version-in-Python" data-toc-modified-id="The-Romberg-method,-better-dynamic-programming-version-in-Python-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>The Romberg method, better dynamic programming version in Python</a></div><div class="lev2 toc-item"><a href="#First-benchmark" data-toc-modified-id="First-benchmark-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>First benchmark</a></div><div class="lev2 toc-item"><a href="#Using-Pypy-for-speedup" data-toc-modified-id="Using-Pypy-for-speedup-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Using Pypy for speedup</a></div><div class="lev2 toc-item"><a href="#Numba-version-for-Python" data-toc-modified-id="Numba-version-for-Python-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Numba version for Python</a></div><div class="lev2 toc-item"><a href="#Naive-Julia-version" data-toc-modified-id="Naive-Julia-version-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Naive Julia version</a></div><div class="lev2 toc-item"><a href="#Benchmark-between-Python,-Pypy-and-Julia" data-toc-modified-id="Benchmark-between-Python,-Pypy-and-Julia-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Benchmark between Python, Pypy and Julia</a></div><div class="lev2 toc-item"><a href="#Second-benchmark" data-toc-modified-id="Second-benchmark-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Second benchmark</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-111"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Remark" data-toc-modified-id="Remark-1111"><span class="toc-item-num">1.11.1&nbsp;&nbsp;</span>Remark</a></div>

# # Benchmark between Python and Julia
# 
# This small [Jupyter notebook](http://jupyter.org/) shows a simple benchmark comparing various implementations in Python and one in Julia of a specific numerical algorithm, the [Romberg integration method](https://en.wikipedia.org/wiki/Romberg%27s_method).
# 
# For Python:
# 
# - a recursive implementation,
# - a dynamic programming implementation,
# - also using Pypy instead,
# - (maybe a Numba version of the dynamic programming version)
#   + (maybe a Cython version too)
# 
# For Julia:
# 
# - a dynamic programming implementation will be enough.

# ----
# ## The Romberg method
# 
# > For mathematical explanations, see [the Wikipedia page](https://en.wikipedia.org/wiki/Romberg%27s_method)

# We will use [`scipy.integrate.quad`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html) function to compare the result of our manual implementations.

# In[1]:


from scipy.integrate import quad


# Let try it with this function $f(x)$ on $[a,b]=[1993,2015]$:
# 
# $$ f(x) := \frac{12x+1}{1+\cos(x)^2} $$

# In[2]:


import math

f = lambda x: (12*x+1)/(1+math.cos(x)**2)
a, b = 1993, 2017


# In[3]:


quad(f, a, b)


# The first value is the numerical value of the integral $\int_{a}^{b} f(x) \mathrm{d}x$ and the second value is an estimate of the numerical error.
# 
# $0.4\%$ is not much, alright.

# ----
# ## The Romberg method, naive recursive version in Python
# 
# See https://mec-cs101-integrals.readthedocs.io/en/latest/_modules/integrals.html#romberg_rec for the code and https://mec-cs101-integrals.readthedocs.io/en/latest/integrals.html#integrals.romberg_rec for the doc

# In[4]:


def romberg_rec(f, xmin, xmax, n=8, m=None):
    if m is None:  # not m was considering 0 as None
        m = n
    assert n >= m
    if n == 0 and m == 0:
        return ((xmax - xmin) / 2.0) * (f(xmin) + f(xmax))
    elif m == 0:
        h = (xmax - xmin) / float(2**n)
        N = (2**(n - 1)) + 1
        term = math.fsum(f(xmin + ((2 * k) - 1) * h) for k in range(1, N))
        return (term * h) + (0.5) * romberg_rec(f, xmin, xmax, n - 1, 0)
    else:
        return (1.0 / ((4**m) - 1)) * ((4**m) * romberg_rec(f, xmin, xmax, n, m - 1) - romberg_rec(f, xmin, xmax, n - 1, m - 1))


# In[5]:


romberg_rec(f, a, b, n=0)  # really not accurate!
romberg_rec(f, a, b, n=1)  # alreay pretty good!
romberg_rec(f, a, b, n=2)
romberg_rec(f, a, b, n=3)
romberg_rec(f, a, b, n=8)  # Almost the exact value.
romberg_rec(f, a, b, n=10)  # Almost the exact value.
romberg_rec(f, a, b, n=12)  # Almost the exact value.


# It converges quite quickly to the "true" value as given by `scipy.integrate.quad`.

# ----
# ## The Romberg method, dynamic programming version in Python
# 
# See https://mec-cs101-integrals.readthedocs.io/en/latest/_modules/integrals.html#romberg for the code and https://mec-cs101-integrals.readthedocs.io/en/latest/integrals.html#integrals.romberg for the doc.

# It is not hard to make this function non-recursive, by storing the intermediate results.

# In[6]:


def romberg(f, xmin, xmax, n=8, m=None):
    assert xmin <= xmax
    if m is None:
        m = n
    assert n >= m >= 0
    # First value:
    r = {(0, 0): 0.5 * (xmax - xmin) * (f(xmax) + f(xmin))}

    # One side of the triangle:
    for i in range(1, n + 1):
        h_i = (xmax - xmin) / float(2**i)
        xsamples = [xmin + ((2 * k - 1) * h_i) for k in range(1, 1 + 2**(i - 1))]
        r[(i, 0)] = (0.5 * r[(i - 1, 0)]) + h_i * math.fsum(f(x) for x in xsamples)

    # All the other values:
    for j in range(1, m + 1):
        for i in range(j, n + 1):
            try:
                r[(i, j)] = (((4**j) * r[(i, j - 1)]) - r[(i - 1, j - 1)]) / float((4**j) - 1)
            except:
                raise ValueError("romberg() with n = {}, m = {} and i = {}, j = {} was an error.".format(n, m, i, j))

    return r[(n, m)]


# In[7]:


romberg(f, a, b, n=0)  # really not accurate!
romberg(f, a, b, n=1)  # alreay pretty good!
romberg(f, a, b, n=2)
romberg(f, a, b, n=3)
romberg(f, a, b, n=8)  # Almost the exact value.
romberg(f, a, b, n=10)  # Almost the exact value.
romberg(f, a, b, n=12)  # Almost the exact value.


# It converges quite quickly to the "true" value as given by `scipy.integrate.quad`.

# ----
# ## The Romberg method, better dynamic programming version in Python
# 
# Instead of using a dictionary, which gets filled up dynamically (and so, slowly), let us use a numpy arrays, as we already know the size of the array we need ($n+1 \times m+1$).
# 
# Note that only half of the array is used, so we could try to use [sparse matrices](https://docs.scipy.org/doc/scipy/reference/sparse.html) maybe, for triangular matrices? From what I know, it is not worth it, both in term of memory information (if the sparsity measure is $\simeq 1/2$, you don't win anything from [LIL](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.lil_matrix.html#scipy.sparse.lil_matrix) or other sparse matrices representation...
# We could use [`numpy.tri`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tri.html) but this uses a dense array so nope.

# In[8]:


import numpy as np

def romberg_better(f, xmin, xmax, n=8, m=None):
    assert xmin <= xmax
    if m is None:
        m = n
    assert n >= m >= 0
    # First value:
    r = np.zeros((n+1, m+1))
    r[0, 0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.

    # One side of the triangle:
    for i in range(1, n + 1):
        h_i = (xmax - xmin) / 2.**i
        r[i, 0] = (0.5 * r[i - 1, 0]) + h_i * math.fsum(
            f(xmin + ((2 * k - 1) * h_i))
            for k in range(1, 1 + 2**(i - 1))
        )

    # All the other values:
    for j in range(1, m + 1):
        for i in range(j, n + 1):
            r[i, j] = (((4.**j) * r[i, j - 1]) - r[i - 1, j - 1]) / ((4.**j) - 1.)

    return r[n, m]


# In[9]:


romberg_better(f, a, b, n=0)  # really not accurate!
romberg_better(f, a, b, n=1)  # alreay pretty good!
romberg_better(f, a, b, n=2)
romberg_better(f, a, b, n=3)
romberg_better(f, a, b, n=8)  # Almost the exact value.
romberg_better(f, a, b, n=10)  # Almost the exact value.
romberg_better(f, a, b, n=12)  # Almost the exact value.


# It converges quite quickly to the "true" value as given by `scipy.integrate.quad`.

# ----
# ## First benchmark

# In[10]:


get_ipython().run_line_magic('timeit', 'quad(f, a, b)')


# In[11]:


get_ipython().run_line_magic('timeit', 'romberg_rec(f, a, b, n=10)')


# In[12]:


get_ipython().run_line_magic('timeit', 'romberg(f, a, b, n=10)')


# In[13]:


get_ipython().run_line_magic('timeit', 'romberg_better(f, a, b, n=10)')


# We already see that the recursive version is *much* slower than the dynamic programming one!
# 
# But there is not much difference between the one using dictionary (`romberg()`) and the one using a numpy array of a known size (`romberg_better()`).

# ----
# ## Using Pypy for speedup

# In[14]:


get_ipython().run_cell_magic('time', '', '\nimport numpy as np\nimport math\nimport random\n\nf = lambda x: (12*x+1)/(1+math.cos(x)**2)\n\n# Same code\ndef romberg(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = np.zeros((n+1, m+1))\n    r[0, 0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i, 0] = (0.5 * r[i - 1, 0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i, j] = (((4.**j) * r[i, j - 1]) - r[i - 1, j - 1]) / ((4.**j) - 1.)\n\n    return r[n, m]\n\nfor _ in range(100000):\n    a = random.randint(-2000, 2000)\n    b = a + random.randint(0, 100)\n    romberg(f, a, b)')


# And now the same code executed by an external [Pypy](http://pypy.org) interpreter (Python 2.7.13 and PyPy 5.8.0 with GCC 5.4.0)

# In[15]:


get_ipython().run_cell_magic('time', '', '%%pypy\n\nimport math\nimport random\n\nf = lambda x: (12*x+1)/(1+math.cos(x)**2)\n\n# Same code\ndef romberg_pypy(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = [[0 for _ in range(n+1)] for _ in range(m+1)]\n    r[0][0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i][0] = (0.5 * r[i - 1][0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i][j] = (((4.**j) * r[i][j - 1]) - r[i - 1][j - 1]) / ((4.**j) - 1.)\n\n    return r[n][m]\n\nfor _ in range(100000):\n    a = random.randint(-2000, 2000)\n    b = a + random.randint(0, 100)\n    romberg_pypy(f, a, b)')


# > This version uses the improved memoization trick (no dictionary), but uses nested lists and not numpy arrays, I didn't bother to install numpy on my Pypy installation (even thought [it should be possible](https://bitbucket.org/pypy/numpy.git)).

# ----
# ## Numba version for Python

# In[16]:


from numba import jit


# In[17]:


@jit
def romberg_numba(f, xmin, xmax, n=8):
    assert xmin <= xmax
    m = n
    # First value:
    r = {(0, 0): 0.5 * (xmax - xmin) * (f(xmax) + f(xmin))}

    # One side of the triangle:
    for i in range(1, n + 1):
        h_i = (xmax - xmin) / float(2**i)
        xsamples = [xmin + ((2 * k - 1) * h_i) for k in range(1, 1 + 2**(i - 1))]
        r[(i, 0)] = (0.5 * r[(i - 1, 0)]) + h_i * math.fsum(f(x) for x in xsamples)

    # All the other values:
    for j in range(1, m + 1):
        for i in range(j, n + 1):
            try:
                r[(i, j)] = (((4**j) * r[(i, j - 1)]) - r[(i - 1, j - 1)]) / float((4**j) - 1)
            except:
                raise ValueError("romberg() with n = {}, m = {} and i = {}, j = {} was an error.".format(n, m, i, j))

    return r[(n, m)]


# In[18]:


romberg_numba(f, a, b, n=8)  # Almost the exact value.


# > It fails! Almost as always when trying Numba, it fails cryptically, too bad. I don't want to spend time debugging this.

# ----
# ## Naive Julia version

# > Thanks to [this page](https://learnxinyminutes.com/docs/julia/) for a nice and short introduction to Julia.

# In[19]:


get_ipython().run_cell_magic('script', 'julia', '\nfunction f(x)\n    (12*x + 1) / (1 + cos(x)^2)\nend\n\na = 1993\nb = 2017\n\nfunction romberg_julia(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = Dict()\n    r[(0, 0)] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[(i, 0)] = (r[(i - 1, 0)] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[(i, j)] = (((4^j) * r[(i, j - 1)]) - r[(i - 1, j - 1)]) / (4^j - 1.)\n        end\n    end\n\n    r[(n, m)]\nend\n\n\nprintln(romberg_julia(f, a, b, n=0))  # really not accurate!\nprintln(romberg_julia(f, a, b, n=1))  # alreay pretty good!\nprintln(romberg_julia(f, a, b, n=2))\nprintln(romberg_julia(f, a, b, n=3))\nprintln(romberg_julia(f, a, b, n=8))  # Almost the exact value.\nprintln(romberg_julia(f, a, b, n=10))  # Almost the exact value.\nprintln(romberg_julia(f, a, b, n=12))  # Almost the exact value.')


# It seems to work well, like the Python implementation. We get the same numerical result:

# In[20]:


f = lambda x: (12*x+1)/(1+math.cos(x)**2)
a, b = 1993, 2017

quad(f, a, b)
romberg(f, a, b, n=12)


# Let try a less naive version using a fixed-size array instead of a dictionary. (as we did before for the Python version)

# In[21]:


get_ipython().run_cell_magic('script', 'julia', '\nfunction f(x)\n    (12*x + 1) / (1 + cos(x)^2)\nend\n\na = 1993\nb = 2017\n\nfunction romberg_julia_better(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = zeros((n+1, m+1))  # https://docs.julialang.org/en/latest/stdlib/arrays/#Base.zeros\n    r[1, 1] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[i + 1, 1] = (r[i, 1] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[i + 1, j + 1] = (((4.^j) * r[i + 1, j]) - r[i, j]) / (4.^j - 1.)\n        end\n    end\n\n    r[n + 1, m + 1]\nend\n\n\nprintln(romberg_julia_better(f, a, b, n=0))  # really not accurate!\nprintln(romberg_julia_better(f, a, b, n=1))  # alreay pretty good!\nprintln(romberg_julia_better(f, a, b, n=2))\nprintln(romberg_julia_better(f, a, b, n=3))\nprintln(romberg_julia_better(f, a, b, n=8))  # Almost the exact value.\nprintln(romberg_julia_better(f, a, b, n=10))  # Almost the exact value.\nprintln(romberg_julia_better(f, a, b, n=12))  # Almost the exact value.')


# ----
# ## Benchmark between Python, Pypy and Julia

# First with Python:

# In[22]:


get_ipython().run_cell_magic('time', '', '\nimport numpy as np\nimport math\nimport random\n\nf = lambda x: (12*x+1)/(1+math.cos(x)**2)\n\n# Same code\ndef romberg(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = np.zeros((n+1, m+1))\n    r[0, 0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i, 0] = (0.5 * r[i - 1, 0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i, j] = (((4.**j) * r[i, j - 1]) - r[i - 1, j - 1]) / ((4.**j) - 1.)\n\n    return r[n, m]\n\nfor _ in range(100000):\n    a = random.randint(-2000, 2000)\n    b = a + random.randint(0, 100)\n    romberg(f, a, b)')


# And now the same code executed by an external [Pypy](http://pypy.org) interpreter (Python 2.7.13 and PyPy 5.8.0 with GCC 5.4.0)

# In[23]:


get_ipython().run_cell_magic('time', '', '%%pypy\n\nimport math\nimport random\n\nf = lambda x: (12*x+1)/(1+math.cos(x)**2)\n\n# Same code\ndef romberg_pypy(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = [[0 for _ in range(n+1)] for _ in range(m+1)]\n    r[0][0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i][0] = (0.5 * r[i - 1][0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i][j] = (((4.**j) * r[i][j - 1]) - r[i - 1][j - 1]) / ((4.**j) - 1.)\n\n    return r[n][m]\n\nfor _ in range(100000):\n    a = random.randint(-2000, 2000)\n    b = a + random.randint(0, 100)\n    romberg_pypy(f, a, b)')


# And finally with Julia:

# In[24]:


get_ipython().run_cell_magic('time', '', '%%script julia\n\nfunction f(x)\n    (12*x + 1) / (1 + cos(x)^2)\nend\n\nfunction romberg_julia(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = Dict()\n    r[(0, 0)] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[(i, 0)] = (r[(i - 1, 0)] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[(i, j)] = (((4^j) * r[(i, j - 1)]) - r[(i - 1, j - 1)]) / (4^j - 1.)\n        end\n    end\n\n    r[(n, m)]\nend\n\nfor _ in 1:100000\n    a = rand(-2000:2000)\n    b = a + rand(0:100)\n    romberg_julia(f, a, b)\nend')


# On this first test, it doesn't look faster than Pypy...
# But what if we use the improved version, with an array instead of dictionary?

# In[25]:


get_ipython().run_cell_magic('time', '', '%%script julia\n\nfunction f(x)\n    (12*x + 1) / (1 + cos(x)^2)\nend\n\nfunction romberg_julia_better(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = zeros((n+1, m+1))  # https://docs.julialang.org/en/latest/stdlib/arrays/#Base.zeros\n    r[1, 1] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[i + 1, 1] = (r[i, 1] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[i + 1, j + 1] = (((4.^j) * r[i + 1, j]) - r[i, j]) / (4.^j - 1.)\n        end\n    end\n\n    r[n + 1, m + 1]\nend\n\nfor _ in 1:100000\n    a = rand(-2000:2000)\n    b = a + rand(0:100)\n    romberg_julia_better(f, a, b)\nend')


# Oh, this time it finally seems faster. Really faster? Yes, about 3 to 4 time faster than Pypy.
# 
# Remark also that this last cells compared by using the magic `%%pypy` and `%%script julia`, so they both need a warm-up time (opening the pipe, the sub-process, initializing the JIT compiler etc).
# But it is fair to compare Pypy to Julia this way.

# ----
# ## Second benchmark

# Let try the same numerical algorithm but with a different integrand function.
# 
# $$\int_{0}^{1} \exp(-x^2) \mathrm{d}x \approx 0.842700792949715$$

# First with Python:

# In[26]:


get_ipython().run_cell_magic('time', '', '\nimport numpy as np\nimport math\nimport random\n\nf = lambda x: (2.0 / math.sqrt(math.pi)) * math.exp(-x**2)\n\n# Same code\ndef romberg(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = np.zeros((n+1, m+1))\n    r[0, 0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i, 0] = (0.5 * r[i - 1, 0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i, j] = (((4.**j) * r[i, j - 1]) - r[i - 1, j - 1]) / ((4.**j) - 1.)\n\n    return r[n, m]\n\nfor _ in range(100000):\n    a = 0\n    b = 1\n    romberg(f, a, b)\nprint(romberg(f, a, b))')


# And now the same code executed by an external [Pypy](http://pypy.org) interpreter (Python 2.7.13 and PyPy 5.8.0 with GCC 5.4.0)

# In[27]:


get_ipython().run_cell_magic('time', '', '%%pypy\n\nimport math\nimport random\n\nf = lambda x: (2.0 / math.sqrt(math.pi)) * math.exp(-x**2)\n\n# Same code\ndef romberg_pypy(f, xmin, xmax, n=8, m=None):\n    assert xmin <= xmax\n    if m is None:\n        m = n\n    assert n >= m >= 0\n    # First value:\n    r = [[0 for _ in range(n+1)] for _ in range(m+1)]\n    r[0][0] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in range(1, n + 1):\n        h_i = (xmax - xmin) / 2.**i\n        r[i][0] = (0.5 * r[i - 1][0]) + h_i * math.fsum(\n            f(xmin + ((2 * k - 1) * h_i))\n            for k in range(1, 1 + 2**(i - 1))\n        )\n\n    # All the other values:\n    for j in range(1, m + 1):\n        for i in range(j, n + 1):\n            r[i][j] = (((4.**j) * r[i][j - 1]) - r[i - 1][j - 1]) / ((4.**j) - 1.)\n\n    return r[n][m]\n\nfor _ in range(100000):\n    a = 0\n    b = 1\n    romberg_pypy(f, a, b)\nprint(romberg_pypy(f, a, b))')


# And finally with Julia:

# In[28]:


get_ipython().run_cell_magic('time', '', '%%script julia\n\nfunction f(x)\n    (2.0 / sqrt(pi)) * exp(-x^2)\nend\n\nfunction romberg_julia(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = Dict()\n    r[(0, 0)] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[(i, 0)] = (r[(i - 1, 0)] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[(i, j)] = (((4^j) * r[(i, j - 1)]) - r[(i - 1, j - 1)]) / (4^j - 1.)\n        end\n    end\n\n    r[(n, m)]\nend\n\nfor _ in 1:100000\n    a = 0\n    b = 1\n    romberg_julia(f, a, b)\nend\nprintln(romberg_julia(f, 0, 1))')


# Still not faster than Pypy... So what is the goal of Julia?

# In[29]:


get_ipython().run_cell_magic('time', '', '%%script julia\n\nfunction f(x)\n    (2.0 / sqrt(pi)) * exp(-x^2)\nend\n\n\nfunction romberg_julia_better(f, xmin, xmax; n=8)\n    m = n\n    # First value:\n    r = zeros((n+1, m+1))  # https://docs.julialang.org/en/latest/stdlib/arrays/#Base.zeros\n    r[1, 1] = (xmax - xmin) * (f(xmax) + f(xmin)) / 2.\n\n    # One side of the triangle:\n    for i in 1 : n\n        h_i = (xmax - xmin) / (2^i)\n        sum_f_x = 0\n        for k in 1 : 2^(i - 1)\n            sum_f_x += f(xmin + ((2 * k - 1) * h_i))\n        end\n        r[i + 1, 1] = (r[i, 1] / 2.) + (h_i * sum_f_x)\n    end\n\n    # All the other values:\n    for j in 1 : m\n        for i in j : n\n            r[i + 1, j + 1] = (((4.^j) * r[i + 1, j]) - r[i, j]) / (4.^j - 1.)\n        end\n    end\n\n    r[n + 1, m + 1]\nend\n\nfor _ in 1:100000\n    a = 0\n    b = 1\n    romberg_julia_better(f, a, b)\nend\nprintln(romberg_julia_better(f, 0, 1))')


# This is also faster than Pypy, but not that much...

# ----
# ## Conclusion
# 
# $\implies$
# On this (baby) example of a real world numerical algorithms, tested on thousands of random inputs or on thousands time the same input, the speed-up is in favor of Julia, but it doesn't seem impressive enough to make me want to use it (at least for now).
# 
# If I have to use 1-based indexing and a slightly different language, just to maybe gain a speed-up of 2 to 3 (compared to Pypy) or even a 10x speed-up compare to naive Python, why bother?
# 
# ### Remark
# Of course, this was a *baby* benchmark, on a small algorithm, and probably wrongly implemented in both Python and Julia.
# 
# But still, I am surprised to see that the naive Julia version was *slower* than the naive Python version executed with Pypy...
# For the less naive version (without dictionary), the Julia version was about *2 to 3* times faster than the Python version with Pypy.
