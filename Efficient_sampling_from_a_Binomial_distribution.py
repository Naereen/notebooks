
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Bernoulli-and-binomial-distribution" data-toc-modified-id="Bernoulli-and-binomial-distribution-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Bernoulli and binomial distribution</a></div><div class="lev2 toc-item"><a href="#Requirements" data-toc-modified-id="Requirements-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Requirements</a></div><div class="lev2 toc-item"><a href="#A-naive-generator" data-toc-modified-id="A-naive-generator-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>A naive generator</a></div><div class="lev2 toc-item"><a href="#The-generator-included-in-numpy.random" data-toc-modified-id="The-generator-included-in-numpy.random-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>The generator included in <code>numpy.random</code></a></div><div class="lev2 toc-item"><a href="#An-efficient-generator-using-the-inverse-transform-method" data-toc-modified-id="An-efficient-generator-using-the-inverse-transform-method-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>An efficient generator using the inverse transform method</a></div><div class="lev3 toc-item"><a href="#Explicit-computation-of-the-probabilities" data-toc-modified-id="Explicit-computation-of-the-probabilities-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Explicit computation of the probabilities</a></div><div class="lev3 toc-item"><a href="#First-function-using-the-inversion-method" data-toc-modified-id="First-function-using-the-inversion-method-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>First function using the inversion method</a></div><div class="lev3 toc-item"><a href="#Simplified-code-of-the-inversion-method" data-toc-modified-id="Simplified-code-of-the-inversion-method-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Simplified code of the inversion method</a></div><div class="lev3 toc-item"><a href="#In-Cython" data-toc-modified-id="In-Cython-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>In Cython</a></div><div class="lev2 toc-item"><a href="#Numerical-experiments-to-check-time-cost-of-the-different-versions" data-toc-modified-id="Numerical-experiments-to-check-time-cost-of-the-different-versions-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Numerical experiments to check time cost of the different versions</a></div><div class="lev2 toc-item"><a href="#Checking-that-sampling-from-$Bin(n,p)$-requires-a-time-$\Omega(n)$." data-toc-modified-id="Checking-that-sampling-from-$Bin(n,p)$-requires-a-time-$\Omega(n)$.-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Checking that sampling from <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-461-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>B</mi><mi>i</mi><mi>n</mi><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo>,</mo><mi>p</mi><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3306" style="width: 3.761em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.586em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.794em, 1003.54em, 2.887em, -999.998em); top: -2.576em; left: 0em;"><span class="mrow" id="MathJax-Span-3307"><span class="mi" id="MathJax-Span-3308" style="font-family: STIXMathJax_Normal-italic;">𝐵</span><span class="mi" id="MathJax-Span-3309" style="font-family: STIXMathJax_Normal-italic;">𝑖</span><span class="mi" id="MathJax-Span-3310" style="font-family: STIXMathJax_Normal-italic;">𝑛</span><span class="mo" id="MathJax-Span-3311" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-3312" style="font-family: STIXMathJax_Normal-italic;">𝑛</span><span class="mo" id="MathJax-Span-3313" style="font-family: STIXMathJax_Main;">,</span><span class="mi" id="MathJax-Span-3314" style="font-family: STIXMathJax_Normal-italic; padding-left: 0.177em;">𝑝</span><span class="mo" id="MathJax-Span-3315" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.581em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.225em; border-left: 0px solid; width: 0px; height: 1.002em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>i</mi><mi>n</mi><mo stretchy="false">(</mo><mi>n</mi><mo>,</mo><mi>p</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-461">Bin(n,p)</script> requires a time <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-462-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi mathvariant=&quot;normal&quot;>&amp;#x03A9;</mi><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3316" style="width: 1.969em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.882em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.794em, 1001.84em, 2.887em, -999.998em); top: -2.576em; left: 0em;"><span class="mrow" id="MathJax-Span-3317"><span class="mi" id="MathJax-Span-3318" style="font-family: STIXMathJax_Main;">Ω</span><span class="mo" id="MathJax-Span-3319" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-3320" style="font-family: STIXMathJax_Normal-italic;">𝑛</span><span class="mo" id="MathJax-Span-3321" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.581em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.225em; border-left: 0px solid; width: 0px; height: 1.002em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Ω</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-462">\Omega(n)</script>.</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></div>

# # Bernoulli and binomial distribution
# - References: [Bernoulli distribution on Wikipedia](https://en.wikipedia.org/wiki/Bernoulli_distribution) and [Binomial distribution on Wikipedia](https://en.wikipedia.org/wiki/Binomial_distribution#Generating_binomial_random_variates).
# 
# The Bernoulli distribution of mean $p\in[0,1]$ is defined as the distribution on $\{0,1\}$ such that $\mathbb{P}(X=1) = p$ and $\mathbb{P}(X=0) = 1-p$.
# 
# If $X$ follows a Binomial distribution of mean $p\in[0,1]$ and $n$ samples, $X$ is defined as the sum of $n$ independent and identically distributed (iid) samples from a Bernoulli distribution of mean $p$, that is $X\in\{0,\dots,n\}$ ($X\in\mathbb{N}$) and $\forall k\in\{0,\dots,n\}, \mathbb{P}(X=k) = {n \choose k} p^k (1-p)^{n-k}$.

# ## Requirements
# Let's import the modules required for this notebook.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[3]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-a "Lilian Besson (Naereen)" -i -v -p numpy,matplotlib,cython')


# ## A naive generator
# Using the pseudo-random generator of (`float`) random numbers in $[0,1]$ from the `random` or `numpy.random` module, we can easily generate a sample from a Bernoulli distribution.

# In[5]:


import random

def uniform_01() -> float:
    return random.random()


# In[7]:


[ uniform_01() for _ in range(5) ]


# It's very quick now:

# In[12]:


def bernoulli(p: float) -> int:
    return 1 if uniform_01() <= p else 0


# In[13]:


[ bernoulli(0) for _ in range(5) ]


# In[14]:


[ bernoulli(0.12345) for _ in range(5) ]


# In[15]:


[ bernoulli(1) for _ in range(5) ]


# So we can naively generate samples from a Binomial distribution by summing iid samples generated using this `bernoulli` function.

# In[16]:


def naive_binomial(n: int, p: float) -> int:
    result = 0
    for k in range(n):  # sum of n iid samples from Bernoulli(p)
        result += bernoulli(p)
    return result


# For example :

# In[17]:


[ naive_binomial(10, 0.1) for _ in range(5) ]


# In[18]:


[ naive_binomial(10, 0.5) for _ in range(5) ]


# In[19]:


[ naive_binomial(10, 0.9) for _ in range(5) ]


# We can quickly illustrate the generated distribution, to check it has the correct "shape":

# In[21]:


m = 1000
n = 10
p = 0.12345
X = [ naive_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[22]:


m = 1000
n = 10
p = 0.5
X = [ naive_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[23]:


m = 1000
n = 10
p = 0.98765
X = [ naive_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# ## The generator included in `numpy.random`

# In[28]:


def numpy_binomial(n: int, p: float) -> int:
    return np.random.binomial(n, p)


# Let's try this out:

# In[29]:


[ numpy_binomial(10, 0.1) for _ in range(5) ]


# In[30]:


[ numpy_binomial(10, 0.5) for _ in range(5) ]


# In[31]:


[ numpy_binomial(10, 0.9) for _ in range(5) ]


# Let's plot this out also.

# In[32]:


m = 1000
n = 10
p = 0.12345
X = [ numpy_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[33]:


m = 1000
n = 10
p = 0.5
X = [ naive_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[34]:


m = 1000
n = 10
p = 0.98765
X = [ naive_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# ## An efficient generator using the inverse transform method
# 
# 1. We start by computing the binomial coefficients and then the probability $\mathbb{P}(X=k)$ for $k\in\{0,\dots,n\}$, if $X\sim Bin(n, p)$, and,
# 2. Then use this to write a generator of Binomial-distributed random values.
# 3. This function is then simplified to inline all computations.
# 4. We propose a fast and simple Cython implementation, to be as efficient as possible, and hopefully comparably efficient when compared against the implementation in Numpy.

# ### Explicit computation of the probabilities

# In[36]:


def binomial_coefficient(n: int, k: int) -> int:
    """From https://en.wikipedia.org/wiki/Binomial_coefficient#Binomial_coefficient_in_programming_languages"""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k) # take advantage of symmetry
    c = 1
    for i in range(k):
        c = (c * (n - i)) / (i + 1)
    return c


# In[37]:


def proba_binomial(n: int, p: float, k: int) -> float:
    """Compute {n \choose k} p^k (1-p)^(n-k)"""
    q = 1.0 - p
    return binomial_coefficient(n, k) * p**k * q**(n-k)


# ### First function using the inversion method

# This first function is a generic implementation of the discrete inverse transform method.
# For more details, see [the Wikipedia page](https://en.wikipedia.org/wiki/Inverse_transform_sampling).
# 
# > Inverse transformation sampling takes uniform samples of a number $u$ between $0$ and $1$, interpreted as a probability, and then returns the largest number $x$ from the domain of the distribution $\mathbb{P}(X)$ such that $\mathbb{P}(-\infty <X<x)\leq u$.

# In[47]:


# a generic function
from typing import Callable

def inversion_method(compute_proba: Callable[[int], int], xmax: int, xmin: int =0) -> int:
    probas = [ compute_proba(x) for x in range(xmin, xmax + 1) ]
    result = xmin
    current_proba = 0
    one_uniform_sample = uniform_01()
    while current_proba <= one_uniform_sample:
        current_proba += probas[result]
        result += 1
    return result - 1


# In[48]:


def first_inversion_binomial(n: int, p: float) -> int:
    def compute_proba(x):
        return proba_binomial(n, p, x)
    xmax = n
    xmin = 0
    return inversion_method(compute_proba, xmax, xmin=xmin)


# Let's try out.

# In[51]:


[ first_inversion_binomial(10, 0.1) for _ in range(5) ]


# In[52]:


[ first_inversion_binomial(10, 0.5) for _ in range(5) ]


# In[53]:


[ first_inversion_binomial(10, 0.9) for _ in range(5) ]


# It seems to work as wanted!

# ### Simplified code of the inversion method
# 
# The previous function as a few weaknesses: it stores the $n+1$ values of $\mathbb{P}(X=k)$ before hand, it computes all of them even if the `for` loop of the inversion method stops in average before the end (in average, it takes $np$ steps, which can be much smaller than $n$ for small $p$).
# Furthermore, the computations of both the binomial coefficients and the values $p^k (1-p)^{n-k}$ is using powers and not iterative multiplications, leading to more rounding errors.
# 
# We can solve all these issues by inlining all the computations.

# In[104]:


def inversion_binomial(n: int, p: float) -> int:
    if p <= 1e-10:
        return 0
    if p >= 1 - 1e-10:
        return n
    if p > 0.5:  # speed up by computing for q and then substracting
        return n - inversion_binomial(n, 1.0 - p)
    result = 0
    q = 1.0 - p
    current_proba = q**n
    cum_proba = current_proba
    one_uniform_sample = uniform_01()
    while cum_proba <= one_uniform_sample:
        current_proba *= (p * (n - result)) / (q * (result + 1))
        cum_proba += current_proba
        result += 1
    return result


# Let's try out.

# In[64]:


[ inversion_binomial(10, 0.1) for _ in range(5) ]


# In[82]:


[ inversion_binomial(10, 0.5) for _ in range(5) ]


# In[67]:


[ inversion_binomial(10, 0.9) for _ in range(5) ]


# It seems to work as wanted!
# 
# And now the storage is indeed $O(1)$, and the computation time is $O(x)$ if the return value is $x$, so the mean computation time is $O(np)$.
# 
# Note that if $p=1/2$, then $O(np) = O(n/2) = O(n)$, and thus this improved method using the inversion method is (asymptotically) as costly as the naive method (the first method which consists of summing $n$ iid samples from a Bernoulli of mean $p$).

# Let's plot this out also.

# In[68]:


m = 1000
n = 10
p = 0.12345
X = [ inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[87]:


m = 1000
n = 10
p = 0.5
X = [ inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[88]:


m = 1000
n = 10
p = 0.98765
X = [ inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# ### In Cython

# In[89]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[112]:


get_ipython().run_cell_magic('cython', '--annotate', '\nimport random\n\ndef cython_inversion_binomial(int n, double p) -> int:\n    if p <= 1e-9:\n        return 0\n    if p >= 1 - 1e-9:\n        return n\n    if p > 0.5:  # speed up by computing for q and then substracting\n        return n - cython_inversion_binomial(n, 1.0 - p)\n    cdef int result = 0\n    cdef double q = 1.0 - p\n    cdef double current_proba = q**n\n    cdef double cum_proba = current_proba\n    cdef double one_uniform_sample = random.random()\n    while cum_proba < one_uniform_sample:\n        current_proba *= (p * (n - result)) / (q * (result + 1))\n        cum_proba += current_proba\n        result += 1\n    return result')


# Let's try out.

# In[113]:


[ cython_inversion_binomial(10, 0.1) for _ in range(5) ]


# In[114]:


[ cython_inversion_binomial(10, 0.5) for _ in range(5) ]


# In[115]:


[ cython_inversion_binomial(10, 0.9) for _ in range(5) ]


# It seems to work as wanted!

# Let's plot this out also.

# In[116]:


m = 1000
n = 10
p = 0.12345
X = [ cython_inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[117]:


m = 1000
n = 10
p = 0.5
X = [ cython_inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# In[118]:


inversion_binomialm = 1000
n = 10
p = 0.98765
X = [ cython_inversion_binomial(n, p) for _ in range(m) ]
plt.figure()
plt.hist(X)
plt.title(f"{m} samples from a Binomial distribution with n = {n} and p = {p}.")
plt.show()


# ## Numerical experiments to check time cost of the different versions

# In[119]:


n = 100


# In[120]:


naive_binomial
first_inversion_binomial
inversion_binomial
cython_inversion_binomial
numpy_binomial


# We can use the `%timeit` magic to check the (mean) computation time of all the previously mentioned functions:

# In[106]:


get_ipython().run_line_magic('timeit', 'naive_binomial(n, 0.123456)')
get_ipython().run_line_magic('timeit', 'first_inversion_binomial(n, 0.123456)')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, 0.123456)')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, 0.123456)')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, 0.123456)')


# Apparently, our `cython` method is faster than the function from `numpy`!
# 
# We also check that our first naive implementation of the inversion method was suboptimal, as announced, because of its pre computation of all the values of $\mathbb{P}(X=k)$.
# However, we check that the naive method, using the sum of $n$ binomial samples, is as comparably efficient to the pure-Python inversion-based method (for this small $n=100$).

# In[121]:


get_ipython().run_line_magic('timeit', 'naive_binomial(n, 0.5)')
get_ipython().run_line_magic('timeit', 'first_inversion_binomial(n, 0.5)')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, 0.5)')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, 0.5)')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, 0.5)')


# In[108]:


get_ipython().run_line_magic('timeit', 'naive_binomial(n, 0.987654)')
get_ipython().run_line_magic('timeit', 'first_inversion_binomial(n, 0.987654)')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, 0.987654)')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, 0.987654)')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, 0.987654)')


# It's quite awesome to see that our inversion-based method is more efficient that the numpy function, both in the pure-Python and the Cython versions!
# But it's weird, as the numpy function is... based on the inversion method, and itself written in C!
# 
# > See the source code, [numpy/distributions.c line 426](https://github.com/numpy/numpy/blob/7c41164f5340dc998ea1c04d2061f7d246894955/numpy/random/mtrand/distributions.c#L426) (on the 28th February 2019, commit 7c41164).
# 
# But the trick is that the implementation in numpy uses the inversion method (running in $\Omega(np)$) if $pn < 30$, and a method denoted "BTPE" otherwise.
# I need to work on this method! The BTPE algorithm is much more complicated, and it is described in the following paper:
# 
# > Kachitvichyanukul, V.; Schmeiser, B. W. (1988). "Binomial random variate generation". Communications of the ACM. 31 (2): 216–222. [doi:10.1145/42372.42381](https://doi.org/10.1145%2F42372.42381).
# 
# > See the source code, [numpy/distributions.c line 263](https://github.com/numpy/numpy/blob/7c41164f5340dc998ea1c04d2061f7d246894955/numpy/random/mtrand/distributions.c#L263) (on the 28th February 2019, commit 7c41164).

# ## Checking that sampling from $Bin(n,p)$ requires a time $\Omega(n)$.

# In[123]:


n = 100
get_ipython().run_line_magic('timeit', 'naive_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, random.random())')


# In[124]:


n = 1000
get_ipython().run_line_magic('timeit', 'naive_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, random.random())')


# In[ ]:


n = 10000
get_ipython().run_line_magic('timeit', 'naive_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'cython_inversion_binomial(n, random.random())')
get_ipython().run_line_magic('timeit', 'numpy_binomial(n, random.random())')


# As we can see, our inversion method (no matter the implementation) runs in $O(n)$ (for $p$ in average $1/2$ in the trials above).
# But numpy's implementation is using the BTPE method, which runs in $O(1)$.

# ## Conclusion
# 
# - So I was write, for the inversion method the computation time is in average $O(np)$ so it is $\Omega(n)$ and cannot be $O(1)$.
# - But there has been many algorithms proposed in the literature which achieves a $O(1)$ running time, and the state-of-the-art algorithm is the BTPE method by V. Kachitvichyanukul & B. W. Schmeiser (from 1988). It is implemented in numpy, for the cases when $np > 30$ (that is, as soon as $n>60$ for $p=1/2$).
# - So the authors of [[Perturbed-History Exploration in Stochastic Multi-Armed Bandits, by Branislav Kveton, Csaba Szepesvari, Mohammad Ghavamzadeh, Craig Boutilier, 26 Feb 2019, arXiv:1902.10089]](https://arxiv.org/abs/1902.10089) were correct, it can indeed cost $O(1)$ time to generate the sum of $t$ samples from $Bern(1/2)$ (that is, a sample from $Bin(t, 1/2)$).
