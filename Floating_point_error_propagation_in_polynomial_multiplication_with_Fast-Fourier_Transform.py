
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Floating-point-error-propagation-in-polynomial-multiplication-with-Fast-Fourier-Transform" data-toc-modified-id="Floating-point-error-propagation-in-polynomial-multiplication-with-Fast-Fourier-Transform-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Floating point error propagation in polynomial multiplication with Fast-Fourier Transform</a></div><div class="lev2 toc-item"><a href="#Requirements" data-toc-modified-id="Requirements-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Requirements</a></div><div class="lev2 toc-item"><a href="#Examples" data-toc-modified-id="Examples-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Examples</a></div><div class="lev3 toc-item"><a href="#Naive-interpolation-values" data-toc-modified-id="Naive-interpolation-values-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Naive interpolation values</a></div><div class="lev3 toc-item"><a href="#Chebyshev-nodes-as-interpolation-values" data-toc-modified-id="Chebyshev-nodes-as-interpolation-values-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Chebyshev nodes as interpolation values</a></div><div class="lev3 toc-item"><a href="#Benchmark" data-toc-modified-id="Benchmark-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Benchmark</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Floating point error propagation in polynomial multiplication with Fast-Fourier Transform
# 
# - *Simple question*: when using the [FFT](https://en.wikipedia.org/wiki/Multiplication_algorithm#Fourier_transform_methods) (or any Fourier transform methods) for multiplying two polynomials, how to deal with floating point error propagation?
# 
# In this [Jupyter notebook](https://www.jupyter.org/), [I](http://perso.crans.org/besson/) will try to understand this phenomena.

# ----
# ## Requirements
# - The [`numpy.polymul`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polymul.html#numpy.polymul) and [`numpy.polyfit`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html#numpy.polyfit) functions.

# In[96]:


import numpy as np
np.version.full_version


# ----
# ## Examples
# 
# Let consider the polynomials $P(X) = 1 + X + X^3$ and $Q(X) = X^2 + X^5$, of degrees $n=3$ and $m=5$:

# In[116]:


P = [      1, 0, 1, 1]
n = len(P) - 1
P, n


# In[117]:


Q = [1, 0, 0, 1, 0, 0]
m = len(Q) - 1
Q, m


# Their product is $(PQ)(X)$, of degree $n+m=8$:
# $$ \begin{align*}(PQ)(X) &= (1 + X + X^3) (X^2 + X^5) \\
# &= X^2 + X^5 + X^3 + X^7 + X^5 + X^8 \\
# &= X^2 + X^3 + 2 X^5 + X^7 + X^8
# \end{align*} $$

# In[36]:


PQ = polymul(P, Q)
d = len(PQ) - 1
PQ, d


# If we evaluate both $P(X)$ and $Q(X)$, on $n+m$ different points, $\lambda_i \in \mathbb{R}$ or $\in\mathbb{N}$, then we can *fit* a polynomial of degree $n+m = \delta(PQ)$ on these sampling points, and by uniqueness (thanks to [the Fundamental Theorem of Algebra](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra#Corollaries)), it will be equal to $(PQ)(X)$.
# 
# The fit can be obtained, for instance, by Lagrange interpolation, which is not so efficient but easy to implement.
# Here, I will simply use the [`numpy.polyfit`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html#numpy.polyfit) function.

# In[39]:


assert d == n + m


# ### Naive interpolation values
# 
# Let us consider the points $\lambda_i = i$, $i=0,\dots,n+m$.

# In[67]:


lambdas = np.arange(0, d + 1)
lambdas


# In[68]:


values_P = np.polyval(P, lambdas)
values_P


# In[69]:


values_Q = np.polyval(Q, lambdas)
values_Q


# In[70]:


values_PQ = values_P * values_Q
values_PQ


# In[71]:


PQ_sampled = np.polyfit(lambdas, values_PQ, d)
PQ_sampled


# In[72]:


PQ


# In[74]:


np.asarray(np.round(PQ_sampled), dtype=int)


# Ok, at least it seems to work!
# 
# But we saw that even with very small degrees ($n=3, m=5$), floating point errors were not so small on these wrongly chosen points $\lambda_i = i$, $i=0,\dots,n+m$.
# The largest "should be 0" value (i.e., $\simeq 0$) value was:

# In[80]:


np.max(np.abs(PQ_sampled)[np.abs(PQ_sampled) < 0.9])


# ### Chebyshev nodes as interpolation values
# 
# Let us consider the points $\lambda_k = \cos\left(\frac{2k-1}{2d} \pi\right)$, $k=1,\dots,1+d=n+m+1$.
# These are called the [Chebyshev nodes](https://en.wikipedia.org/wiki/Chebyshev_nodes).

# In[85]:


lambdas = np.cos(np.pi * (2 * np.arange(1, 2 + d) - 1) / (2 * d))
lambdas


# In[86]:


values_P = np.polyval(P, lambdas)
values_P


# In[87]:


values_Q = np.polyval(Q, lambdas)
values_Q


# In[88]:


values_PQ = values_P * values_Q
values_PQ


# In[91]:


PQ_sampled2 = np.polyfit(lambdas, values_PQ, d)
PQ_sampled2


# In[92]:


PQ


# In[93]:


np.asarray(np.round(PQ_sampled2), dtype=int)


# Ok, at least it seems to work!
# 
# But we saw that even with very small degrees ($n=3, m=5$), floating point errors were not so small on these points: the largest "should be 0" value (i.e., $\simeq 0$) value was:

# In[94]:


np.max(np.abs(PQ_sampled2)[np.abs(PQ_sampled2) < 0.9])


# ### Benchmark
# 
# Stupidly, let us check if our naive implementation of $(P, Q) \mapsto PQ$ by evaluation-and-interpolation is more or less efficient than `numpy.polyfit`:

# In[123]:


def mypolymul(P, Q):
    n = len(P) - 1
    m = len(Q) - 1
    d = n + m
    lambdas = np.cos(np.pi * (2 * np.arange(1, 2 + d) - 1) / (2 * d))
    values_P = np.polyval(P, lambdas)
    values_Q = np.polyval(Q, lambdas)
    values_PQ = values_P * values_Q
    PQ_sampled = np.polyfit(lambdas, values_PQ, d)
    # return PQ_sampled
    return np.asarray(np.round(PQ_sampled), dtype=int)


# In[124]:


np.polymul(P, Q)


# In[125]:


mypolymul(P, Q)


# In[121]:


import warnings
warnings.simplefilter('ignore', np.RankWarning)

get_ipython().run_line_magic('timeit', 'np.polymul(P, Q)')
get_ipython().run_line_magic('timeit', 'mypolymul(P, Q)')


# Of course, our implementation is slower.
# But on small polynomials, not so slower.
# 
# What about larger polynomials?

# In[126]:


def random_polynomial(d=10, maxcoef=1):
    return np.random.randint(low=-maxcoef, high=maxcoef+1, size=d+1)


# In[134]:


P = random_polynomial()
Q = random_polynomial()
P, Q
get_ipython().run_line_magic('timeit', 'np.polymul(P, Q)')
np.polymul(P, Q)
get_ipython().run_line_magic('timeit', 'mypolymul(P, Q)')
mypolymul(P, Q)
assert np.all(np.polymul(P, Q) == mypolymul(P, Q))


# On a larger example:

# In[138]:


d = 100
maxcoef = 1
get_ipython().run_line_magic('timeit', 'np.polymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')
get_ipython().run_line_magic('timeit', 'mypolymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')

P, Q = random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef)
assert np.all(np.polymul(P, Q) == mypolymul(P, Q))


# In[139]:


d = 10
maxcoef = 3
get_ipython().run_line_magic('timeit', 'np.polymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')
get_ipython().run_line_magic('timeit', 'mypolymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')

P, Q = random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef)
assert np.all(np.polymul(P, Q) == mypolymul(P, Q))


# In[140]:


d = 10
maxcoef = 50
get_ipython().run_line_magic('timeit', 'np.polymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')
get_ipython().run_line_magic('timeit', 'mypolymul(random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef))')

P, Q = random_polynomial(d=d, maxcoef=maxcoef), random_polynomial(d=d, maxcoef=maxcoef)
assert np.all(np.polymul(P, Q) == mypolymul(P, Q))


# Our method is slower.
# And wrong.
# 
# That's sad.

# ----
# ## Conclusion
# 
# Implementing naively the multiplication of 1D polynomials with evaluation-and-interpolation does not work.
# 
# - It is slower that the FFT based method (available in any numerical computation environment), e.g., `numpy.polymul` in Python with NumPy.
# - And it does not work. Booum!

# ----
# > Thanks for reading!
# 
# > See [this repo on GitHub](https://github.com/Naereen/notebooks/) for more notebooks, or [on nbviewer.jupyter.org](https://nbviewer.jupyter.org/github/Naereen/notebooks/).
# 
# > That's it for this demo! See you, folks!
