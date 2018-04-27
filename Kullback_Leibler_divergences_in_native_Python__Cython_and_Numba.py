
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></div><div class="lev1 toc-item"><a href="#KL-divergences-and-KL-UCB-indexes,-in-naive-Python" data-toc-modified-id="KL-divergences-and-KL-UCB-indexes,-in-naive-Python-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>KL divergences and KL-UCB indexes, in naive Python</a></div><div class="lev2 toc-item"><a href="#KL-divergences" data-toc-modified-id="KL-divergences-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>KL divergences</a></div><div class="lev3 toc-item"><a href="#Bernoulli-distributions" data-toc-modified-id="Bernoulli-distributions-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Bernoulli distributions</a></div><div class="lev3 toc-item"><a href="#Binomial-distributions" data-toc-modified-id="Binomial-distributions-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Binomial distributions</a></div><div class="lev3 toc-item"><a href="#Poisson-distributions" data-toc-modified-id="Poisson-distributions-213"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Poisson distributions</a></div><div class="lev3 toc-item"><a href="#Exponential-distributions" data-toc-modified-id="Exponential-distributions-214"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Exponential distributions</a></div><div class="lev3 toc-item"><a href="#Gamma-distributions" data-toc-modified-id="Gamma-distributions-215"><span class="toc-item-num">2.1.5&nbsp;&nbsp;</span>Gamma distributions</a></div><div class="lev3 toc-item"><a href="#Negative-binomial-distributions" data-toc-modified-id="Negative-binomial-distributions-216"><span class="toc-item-num">2.1.6&nbsp;&nbsp;</span>Negative binomial distributions</a></div><div class="lev3 toc-item"><a href="#Gaussian-distributions" data-toc-modified-id="Gaussian-distributions-217"><span class="toc-item-num">2.1.7&nbsp;&nbsp;</span>Gaussian distributions</a></div><div class="lev2 toc-item"><a href="#Generic-KL-UCB-indexes,-with-a-bisection-search" data-toc-modified-id="Generic-KL-UCB-indexes,-with-a-bisection-search-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Generic KL-UCB indexes, with a bisection search</a></div><div class="lev2 toc-item"><a href="#Distribution-specific-KL-UCB-indexes" data-toc-modified-id="Distribution-specific-KL-UCB-indexes-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Distribution-specific KL-UCB indexes</a></div><div class="lev3 toc-item"><a href="#Gaussian" data-toc-modified-id="Gaussian-231"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Gaussian</a></div><div class="lev3 toc-item"><a href="#Bernoulli" data-toc-modified-id="Bernoulli-232"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Bernoulli</a></div><div class="lev3 toc-item"><a href="#Poisson" data-toc-modified-id="Poisson-233"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Poisson</a></div><div class="lev3 toc-item"><a href="#Exponential" data-toc-modified-id="Exponential-234"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>Exponential</a></div><div class="lev3 toc-item"><a href="#Others" data-toc-modified-id="Others-235"><span class="toc-item-num">2.3.5&nbsp;&nbsp;</span>Others</a></div><div class="lev1 toc-item"><a href="#With-Numba" data-toc-modified-id="With-Numba-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>With Numba</a></div><div class="lev2 toc-item"><a href="#KL-divergences" data-toc-modified-id="KL-divergences-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>KL divergences</a></div><div class="lev3 toc-item"><a href="#Bernoulli-distributions" data-toc-modified-id="Bernoulli-distributions-311"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Bernoulli distributions</a></div><div class="lev3 toc-item"><a href="#Binomial-distributions" data-toc-modified-id="Binomial-distributions-312"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Binomial distributions</a></div><div class="lev3 toc-item"><a href="#Poisson-distributions" data-toc-modified-id="Poisson-distributions-313"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Poisson distributions</a></div><div class="lev3 toc-item"><a href="#Exponential-distributions" data-toc-modified-id="Exponential-distributions-314"><span class="toc-item-num">3.1.4&nbsp;&nbsp;</span>Exponential distributions</a></div><div class="lev3 toc-item"><a href="#Gamma-distributions" data-toc-modified-id="Gamma-distributions-315"><span class="toc-item-num">3.1.5&nbsp;&nbsp;</span>Gamma distributions</a></div><div class="lev3 toc-item"><a href="#Negative-binomial-distributions" data-toc-modified-id="Negative-binomial-distributions-316"><span class="toc-item-num">3.1.6&nbsp;&nbsp;</span>Negative binomial distributions</a></div><div class="lev3 toc-item"><a href="#Gaussian-distributions" data-toc-modified-id="Gaussian-distributions-317"><span class="toc-item-num">3.1.7&nbsp;&nbsp;</span>Gaussian distributions</a></div><div class="lev2 toc-item"><a href="#Generic-KL-UCB-indexes,-with-a-bisection-search" data-toc-modified-id="Generic-KL-UCB-indexes,-with-a-bisection-search-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Generic KL-UCB indexes, with a bisection search</a></div><div class="lev2 toc-item"><a href="#Distribution-specific-KL-UCB-indexes" data-toc-modified-id="Distribution-specific-KL-UCB-indexes-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Distribution-specific KL-UCB indexes</a></div><div class="lev3 toc-item"><a href="#Gaussian" data-toc-modified-id="Gaussian-331"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>Gaussian</a></div><div class="lev3 toc-item"><a href="#Bernoulli" data-toc-modified-id="Bernoulli-332"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>Bernoulli</a></div><div class="lev3 toc-item"><a href="#Poisson" data-toc-modified-id="Poisson-333"><span class="toc-item-num">3.3.3&nbsp;&nbsp;</span>Poisson</a></div><div class="lev3 toc-item"><a href="#Exponential" data-toc-modified-id="Exponential-334"><span class="toc-item-num">3.3.4&nbsp;&nbsp;</span>Exponential</a></div><div class="lev1 toc-item"><a href="#With-Cython" data-toc-modified-id="With-Cython-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>With Cython</a></div><div class="lev2 toc-item"><a href="#KL-divergences" data-toc-modified-id="KL-divergences-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>KL divergences</a></div><div class="lev3 toc-item"><a href="#Bernoulli-distributions" data-toc-modified-id="Bernoulli-distributions-411"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Bernoulli distributions</a></div><div class="lev3 toc-item"><a href="#Binomial-distributions" data-toc-modified-id="Binomial-distributions-412"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Binomial distributions</a></div><div class="lev3 toc-item"><a href="#Poisson-distributions" data-toc-modified-id="Poisson-distributions-413"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>Poisson distributions</a></div><div class="lev3 toc-item"><a href="#Exponential-distributions" data-toc-modified-id="Exponential-distributions-414"><span class="toc-item-num">4.1.4&nbsp;&nbsp;</span>Exponential distributions</a></div><div class="lev3 toc-item"><a href="#Gamma-distributions" data-toc-modified-id="Gamma-distributions-415"><span class="toc-item-num">4.1.5&nbsp;&nbsp;</span>Gamma distributions</a></div><div class="lev3 toc-item"><a href="#Negative-binomial-distributions" data-toc-modified-id="Negative-binomial-distributions-416"><span class="toc-item-num">4.1.6&nbsp;&nbsp;</span>Negative binomial distributions</a></div><div class="lev3 toc-item"><a href="#Gaussian-distributions" data-toc-modified-id="Gaussian-distributions-417"><span class="toc-item-num">4.1.7&nbsp;&nbsp;</span>Gaussian distributions</a></div><div class="lev2 toc-item"><a href="#Generic-KL-UCB-indexes,-with-a-bisection-search" data-toc-modified-id="Generic-KL-UCB-indexes,-with-a-bisection-search-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Generic KL-UCB indexes, with a bisection search</a></div><div class="lev1 toc-item"><a href="#With-the-C-API-for-Python" data-toc-modified-id="With-the-C-API-for-Python-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>With the C API for Python</a></div><div class="lev1 toc-item"><a href="#Tests-and-benchmarks" data-toc-modified-id="Tests-and-benchmarks-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Tests and benchmarks</a></div><div class="lev2 toc-item"><a href="#KL-divergences" data-toc-modified-id="KL-divergences-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>KL divergences</a></div><div class="lev3 toc-item"><a href="#Bernoulli" data-toc-modified-id="Bernoulli-611"><span class="toc-item-num">6.1.1&nbsp;&nbsp;</span>Bernoulli</a></div><div class="lev3 toc-item"><a href="#Binomial" data-toc-modified-id="Binomial-612"><span class="toc-item-num">6.1.2&nbsp;&nbsp;</span>Binomial</a></div><div class="lev3 toc-item"><a href="#Poisson" data-toc-modified-id="Poisson-613"><span class="toc-item-num">6.1.3&nbsp;&nbsp;</span>Poisson</a></div><div class="lev3 toc-item"><a href="#Exponential" data-toc-modified-id="Exponential-614"><span class="toc-item-num">6.1.4&nbsp;&nbsp;</span>Exponential</a></div><div class="lev3 toc-item"><a href="#Gamma" data-toc-modified-id="Gamma-615"><span class="toc-item-num">6.1.5&nbsp;&nbsp;</span>Gamma</a></div><div class="lev3 toc-item"><a href="#Negative-binomial" data-toc-modified-id="Negative-binomial-616"><span class="toc-item-num">6.1.6&nbsp;&nbsp;</span>Negative binomial</a></div><div class="lev3 toc-item"><a href="#Gaussian" data-toc-modified-id="Gaussian-617"><span class="toc-item-num">6.1.7&nbsp;&nbsp;</span>Gaussian</a></div><div class="lev2 toc-item"><a href="#KL-UCB-indexes" data-toc-modified-id="KL-UCB-indexes-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>KL-UCB indexes</a></div><div class="lev3 toc-item"><a href="#Gaussian" data-toc-modified-id="Gaussian-621"><span class="toc-item-num">6.2.1&nbsp;&nbsp;</span>Gaussian</a></div><div class="lev3 toc-item"><a href="#Bernoulli" data-toc-modified-id="Bernoulli-622"><span class="toc-item-num">6.2.2&nbsp;&nbsp;</span>Bernoulli</a></div><div class="lev3 toc-item"><a href="#Poisson" data-toc-modified-id="Poisson-623"><span class="toc-item-num">6.2.3&nbsp;&nbsp;</span>Poisson</a></div><div class="lev3 toc-item"><a href="#Exponential" data-toc-modified-id="Exponential-624"><span class="toc-item-num">6.2.4&nbsp;&nbsp;</span>Exponential</a></div><div class="lev2 toc-item"><a href="#Clean-up" data-toc-modified-id="Clean-up-63"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Clean up</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev2 toc-item"><a href="#Take-away-messages" data-toc-modified-id="Take-away-messages-71"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Take away messages</a></div><div class="lev2 toc-item"><a href="#Using-Cython-for-real-?" data-toc-modified-id="Using-Cython-for-real-?-72"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Using Cython <em>for real</em> ?</a></div><div class="lev2 toc-item"><a href="#Using-C-for-real-?" data-toc-modified-id="Using-C-for-real-?-73"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Using C <em>for real</em> ?</a></div>

# ----
# # Introduction
# 
# In this small notebook, I implement various [Kullback-Leibler divergence functions](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), in [Python](https://www.python.org/), using different approaches: naive Python, and using Numba and Cython.
# 
# I also implement KL-UCB indexes, in the three approaches, and finally I present some basic benchmarks to compare the time and memory efficiency of the different approaches, for each function.

# Requirements:

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -a "Lilian Besson (Naereen)" -p numpy,numba -g')


# In[2]:


import numpy as np


# ----
# # KL divergences and KL-UCB indexes, in naive Python
# 
# I will copy and paste parts of [this file](https://github.com/SMPyBandits/SMPyBandits/blob/master/SMPyBandits/Policies/kullback.py) from my [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits/) library.

# In[3]:


eps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]


# I will include docstrings and examples only for the naive implementation.

# ## KL divergences

# ### Bernoulli distributions

# In[4]:


def klBern(x, y):
    r""" Kullback-Leibler divergence for Bernoulli distributions. https://en.wikipedia.org/wiki/Bernoulli_distribution#Kullback.E2.80.93Leibler_divergence

    .. math:: \mathrm{KL}(\mathcal{B}(x), \mathcal{B}(y)) = x \log(\frac{x}{y}) + (1-x) \log(\frac{1-x}{1-y})."""
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y))


# In[5]:


klBern(0.5, 0.5)
klBern(0.1, 0.9)
klBern(0.9, 0.1)
klBern(0.4, 0.5)
klBern(0.01, 0.99)
klBern(0, 1)


# ### Binomial distributions

# In[6]:


def klBin(x, y, n):
    r""" Kullback-Leibler divergence for Binomial distributions. https://math.stackexchange.com/questions/320399/kullback-leibner-divergence-of-binomial-distributions

    - It is simply the n times :func:`klBern` on x and y.

    .. math:: \mathrm{KL}(\mathrm{Bin}(x, n), \mathrm{Bin}(y, n)) = n \times \left(x \log(\frac{x}{y}) + (1-x) \log(\frac{1-x}{1-y}) \right).

    .. warning:: The two distributions must have the same parameter n, and x, y are p, q in (0, 1).
    """
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return n * (x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y)))


# In[7]:


klBin(0.5, 0.5, 10)
klBin(0.1, 0.9, 10)
klBin(0.9, 0.1, 10)
klBin(0.4, 0.5, 10)
klBin(0.01, 0.99, 10)
klBin(0, 1, 10)


# ### Poisson distributions

# In[8]:


def klPoisson(x, y):
    r""" Kullback-Leibler divergence for Poison distributions. https://en.wikipedia.org/wiki/Poisson_distribution#Kullback.E2.80.93Leibler_divergence

    .. math:: \mathrm{KL}(\mathrm{Poisson}(x), \mathrm{Poisson}(y)) = y - x + x \times \log(\frac{x}{y}).
    """
    x = max(x, eps)
    y = max(y, eps)
    return y - x + x * np.log(x / y)


# In[9]:


klPoisson(3, 3)
klPoisson(2, 1)
klPoisson(1, 2)
klPoisson(3, 6)
klPoisson(6, 8)
klPoisson(1, 0)
klPoisson(0, 0)


# ### Exponential distributions

# In[10]:


def klExp(x, y):
    r""" Kullback-Leibler divergence for exponential distributions. https://en.wikipedia.org/wiki/Exponential_distribution#Kullback.E2.80.93Leibler_divergence

    .. math::

        \mathrm{KL}(\mathrm{Exp}(x), \mathrm{Exp}(y)) = \begin{cases}
        \frac{x}{y} - 1 - \log(\frac{x}{y}) & \text{if} x > 0, y > 0\\
        +\infty & \text{otherwise}
        \end{cases}
    """
    if x <= 0 or y <= 0:
        return float('+inf')
    else:
        x = max(x, eps)
        y = max(y, eps)
        return x / y - 1 - np.log(x / y)


# In[11]:


klExp(3, 3)
klExp(3, 6)
klExp(1, 2)
klExp(2, 1)
klExp(4, 2)
klExp(6, 8)
klExp(-3, 2)
klExp(3, -2)
klExp(-3, -2)


# ### Gamma distributions

# In[12]:


def klGamma(x, y, a=1):
    r""" Kullback-Leibler divergence for gamma distributions. https://en.wikipedia.org/wiki/Gamma_distribution#Kullback.E2.80.93Leibler_divergence

    - It is simply the a times :func:`klExp` on x and y.

    .. math::

        \mathrm{KL}(\Gamma(x, a), \Gamma(y, a)) = \begin{cases}
        a \times \left( \frac{x}{y} - 1 - \log(\frac{x}{y}) \right) & \text{if} x > 0, y > 0\\
        +\infty & \text{otherwise}
        \end{cases}

    .. warning:: The two distributions must have the same parameter a.
    """
    if x <= 0 or y <= 0:
        return float('+inf')
    else:
        x = max(x, eps)
        y = max(y, eps)
        return a * (x / y - 1 - np.log(x / y))


# In[13]:


klGamma(3, 3)
klGamma(3, 6)
klGamma(1, 2)
klGamma(2, 1)
klGamma(4, 2)
klGamma(6, 8)
klGamma(-3, 2)
klGamma(3, -2)
klGamma(-3, -2)


# ### Negative binomial distributions

# In[14]:


def klNegBin(x, y, r=1):
    r""" Kullback-Leibler divergence for negative binomial distributions. https://en.wikipedia.org/wiki/Negative_binomial_distribution

    .. math:: \mathrm{KL}(\mathrm{NegBin}(x, r), \mathrm{NegBin}(y, r)) = r \times \log((r + x) / (r + y)) - x \times \log(y \times (r + x) / (x \times (r + y))).

    .. warning:: The two distributions must have the same parameter r.
    """
    x = max(x, eps)
    y = max(y, eps)
    return r * np.log((r + x) / (r + y)) - x * np.log(y * (r + x) / (x * (r + y)))


# In[15]:


klNegBin(0.5, 0.5)
klNegBin(0.1, 0.9)
klNegBin(0.9, 0.1)
klNegBin(0.4, 0.5)
klNegBin(0.01, 0.99)
klBern(0, 1)
klNegBin(0.5, 0.5, r=2)
klNegBin(0.1, 0.9, r=2)
klNegBin(0.1, 0.9, r=4)
klNegBin(0.9, 0.1, r=2)
klNegBin(0.4, 0.5, r=2)
klNegBin(0.01, 0.99, r=2)


# ### Gaussian distributions

# In[16]:


def klGauss(x, y, sig2x=0.25, sig2y=None):
    r""" Kullback-Leibler divergence for Gaussian distributions of means ``x`` and ``y`` and variances ``sig2x`` and ``sig2y``, :math:`\nu_1 = \mathcal{N}(x, \sigma_x^2)` and :math:`\nu_2 = \mathcal{N}(y, \sigma_x^2)`:

    .. math:: \mathrm{KL}(\nu_1, \nu_2) = \frac{(x - y)^2}{2 \sigma_y^2} + \frac{1}{2}\left( \frac{\sigma_x^2}{\sigma_y^2} - 1 \log\left(\frac{\sigma_x^2}{\sigma_y^2}\right) \right).

    See https://en.wikipedia.org/wiki/Normal_distribution#Other_properties

    - By default, sig2y is assumed to be sig2x (same variance).
    """
    if sig2y is None or - eps < (sig2y - sig2x) < eps:
        return (x - y) ** 2 / (2. * sig2x)
    else:
        return (x - y) ** 2 / (2. * sig2y) + 0.5 * ((sig2x/sig2y)**2 - 1 - np.log(sig2x/sig2y))


# In[17]:


klGauss(3, 3)
klGauss(3, 6)
klGauss(1, 2)
klGauss(2, 1)
klGauss(4, 2)
klGauss(6, 8)
klGauss(-3, 2)
klGauss(3, -2)
klGauss(-3, -2)
klGauss(3, 2)
klGauss(3, 3, sig2x=10)
klGauss(3, 6, sig2x=10)
klGauss(1, 2, sig2x=10)
klGauss(2, 1, sig2x=10)
klGauss(4, 2, sig2x=10)
klGauss(6, 8, sig2x=10)
klGauss(0, 0, sig2x=0.25, sig2y=0.5)
klGauss(0, 0, sig2x=0.25, sig2y=1.0)
klGauss(0, 0, sig2x=0.5, sig2y=0.25)
klGauss(0, 1, sig2x=0.25, sig2y=0.5)
klGauss(0, 1, sig2x=0.25, sig2y=1.0)
klGauss(0, 1, sig2x=0.5, sig2y=0.25)
klGauss(1, 0, sig2x=0.25, sig2y=0.5)
klGauss(1, 0, sig2x=0.25, sig2y=1.0)
klGauss(1, 0, sig2x=0.5, sig2y=0.25)


# ## Generic KL-UCB indexes, with a bisection search

# In[18]:


def klucb(x, d, kl, upperbound, lowerbound=float('-inf'), precision=1e-6, max_iterations=50):
    """ The generic KL-UCB index computation.

    - x: value of the cum reward,
    - d: upper bound on the divergence,
    - kl: the KL divergence to be used (:func:`klBern`, :func:`klGauss`, etc),
    - upperbound, lowerbound=float('-inf'): the known bound of the values x,
    - precision=1e-6: the threshold from where to stop the research,
    - max_iterations: max number of iterations of the loop (safer to bound it to reduce time complexity).

    .. note:: It uses a **bisection search**, and one call to ``kl`` for each step of the bisection search.
    """
    value = max(x, lowerbound)
    u = upperbound
    _count_iteration = 0
    while _count_iteration < max_iterations and u - value > precision:
        _count_iteration += 1
        m = (value + u) / 2.
        if kl(x, m) > d:
            u = m
        else:
            value = m
    return (value + u) / 2.


# For example, for `klucbBern`, the two steps are to first compute an upperbound (as precise as possible) and the compute the kl-UCB index:

# In[19]:


x, d = 0.9, 0.2
upperbound = 1
klucb(x, d, klBern, upperbound, lowerbound=0, precision=1e-3, max_iterations=10)
klucb(x, d, klBern, upperbound, lowerbound=0, precision=1e-6, max_iterations=10)
klucb(x, d, klBern, upperbound, lowerbound=0, precision=1e-3, max_iterations=50)
klucb(x, d, klBern, upperbound, lowerbound=0, precision=1e-6, max_iterations=100)


# ## Distribution-specific KL-UCB indexes

# ### Gaussian

# In[20]:


def klucbGauss(x, d, sig2x=0.25, precision=0.):
    """ KL-UCB index computation for Gaussian distributions.

    - Note that it does not require any search.

    .. warning:: it works only if the good variance constant is given.
    """
    return x + np.sqrt(2 * sig2x * d)


# In[21]:


klucbGauss(0.1, 0.2)
klucbGauss(0.5, 0.2)
klucbGauss(0.9, 0.2)
klucbGauss(0.1, 0.4)
klucbGauss(0.1, 0.9)
klucbGauss(0.5, 0.4)
klucbGauss(0.5, 0.9)
klucbGauss(0.9, 0.4)
klucbGauss(0.9, 0.9)


# ### Bernoulli

# In[22]:


def klucbBern(x, d, precision=1e-6):
    """ KL-UCB index computation for Bernoulli distributions, using :func:`klucb`."""
    upperbound = min(1., klucbGauss(x, d, sig2x=0.25))  # variance 1/4 for [0,1] bounded distributions
    # upperbound = min(1., klucbPoisson(x, d))  # also safe, and better ?
    return klucb(x, d, klBern, upperbound, precision)


# In[23]:


klucbBern(0.1, 0.2)
klucbBern(0.5, 0.2)
klucbBern(0.9, 0.2)
klucbBern(0.1, 0.4)
klucbBern(0.1, 0.9)
klucbBern(0.5, 0.4)
klucbBern(0.5, 0.9)
klucbBern(0.9, 0.4)
klucbBern(0.9, 0.9)


# ### Poisson

# In[24]:


def klucbPoisson(x, d, precision=1e-6):
    """ KL-UCB index computation for Poisson distributions, using :func:`klucb`."""
    upperbound = x + d + np.sqrt(d * d + 2 * x * d)  # looks safe, to check: left (Gaussian) tail of Poisson dev
    return klucb(x, d, klPoisson, upperbound, precision)


# In[25]:


klucbPoisson(0.1, 0.2)
klucbPoisson(0.5, 0.2)
klucbPoisson(0.9, 0.2)
klucbPoisson(0.1, 0.4)
klucbPoisson(0.1, 0.9)
klucbPoisson(0.5, 0.4)
klucbPoisson(0.5, 0.9)
klucbPoisson(0.9, 0.4)
klucbPoisson(0.9, 0.9)


# ### Exponential

# In[26]:


def klucbExp(x, d, precision=1e-6):
    """ KL-UCB index computation for exponential distributions, using :func:`klucb`."""
    if d < 0.77:  # XXX where does this value come from?
        upperbound = x / (1 + 2. / 3 * d - np.sqrt(4. / 9 * d * d + 2 * d))
        # safe, klexp(x,y) >= e^2/(2*(1-2e/3)) if x=y(1-e)
    else:
        upperbound = x * np.exp(d + 1)
    if d > 1.61:  # XXX where does this value come from?
        lowerbound = x * np.exp(d)
    else:
        lowerbound = x / (1 + d - np.sqrt(d * d + 2 * d))
    return klucb(x, d, klGamma, upperbound, lowerbound, precision)


# In[27]:


klucbExp(0.1, 0.2)
klucbExp(0.5, 0.2)
klucbExp(0.9, 0.2)
klucbExp(0.1, 0.4)
klucbExp(0.1, 0.9)
klucbExp(0.5, 0.4)
klucbExp(0.5, 0.9)
klucbExp(0.9, 0.4)
klucbExp(0.9, 0.9)


# ### Others
# We could do the same for more distributions, but that's enough.

# ----
# # With Numba
# 
# It will be *exactly* the same code as above, except that the [`numba.jit`](http://numba.pydata.org/numba-doc/latest/user/jit.html) decorator will be used for each functions, to let [numba](http://numba.pydata.org/) *try* to speed up the code!

# In[28]:


from numba import jit


# As much as possible, one should call `@jit(nopython=True)` to be sure that numba does not fall back silently to naive Python code. With `nopython=True`, any call to the generated function will fail if the compilation could not succeed.

# ## KL divergences

# ### Bernoulli distributions

# In[29]:


@jit(nopython=True)
def klBern_numba(x, y):
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y))


# ### Binomial distributions

# In[30]:


@jit(nopython=True)
def klBin_numba(x, y, n):
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return n * (x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y)))


# ### Poisson distributions

# In[31]:


@jit(nopython=True)
def klPoisson_numba(x, y):
    x = max(x, eps)
    y = max(y, eps)
    return y - x + x * np.log(x / y)


# ### Exponential distributions

# In[32]:


@jit(nopython=True)
def klExp_numba(x, y):
    if x <= 0 or y <= 0:
        return inf
    else:
        x = max(x, eps)
        y = max(y, eps)
        return x / y - 1 - np.log(x / y)


# ### Gamma distributions

# In[33]:


@jit(nopython=True)
def klGamma_numba(x, y, a=1):
    if x <= 0 or y <= 0:
        return inf
    else:
        x = max(x, eps)
        y = max(y, eps)
        return a * (x / y - 1 - np.log(x / y))


# ### Negative binomial distributions

# In[34]:


@jit(nopython=True)
def klNegBin_numba(x, y, r=1):
    x = max(x, eps)
    y = max(y, eps)
    return r * np.log((r + x) / (r + y)) - x * np.log(y * (r + x) / (x * (r + y)))


# ### Gaussian distributions

# In[35]:


@jit(nopython=True)
def klGauss_numba(x, y, sig2x=0.25, sig2y=0.25):
    if - eps < (sig2y - sig2x) and (sig2y - sig2x) < eps:
        return (x - y) ** 2 / (2. * sig2x)
    else:
        return (x - y) ** 2 / (2. * sig2y) + 0.5 * ((sig2x/sig2y)**2 - 1 - np.log(sig2x/sig2y))


# ## Generic KL-UCB indexes, with a bisection search

# In[36]:


@jit
def klucb_numba(x, d, kl, upperbound,
                lowerbound=float('-inf'), precision=1e-6, max_iterations=50):
    value = max(x, lowerbound)
    u = upperbound
    _count_iteration = 0
    while _count_iteration < max_iterations and u - value > precision:
        _count_iteration += 1
        m = (value + u) / 2.
        if kl(x, m) > d:
            u = m
        else:
            value = m
    return (value + u) / 2.


# For example, for `klucbBern`, the two steps are to first compute an upperbound (as precise as possible) and the compute the kl-UCB index:

# In[37]:


x, d = 0.9, 0.2
upperbound = 1
klucb_numba(x, d, klBern_numba, upperbound, lowerbound=0, precision=1e-3, max_iterations=10)
klucb_numba(x, d, klBern_numba, upperbound, lowerbound=0, precision=1e-6, max_iterations=10)
klucb_numba(x, d, klBern_numba, upperbound, lowerbound=0, precision=1e-3, max_iterations=50)
klucb_numba(x, d, klBern_numba, upperbound, lowerbound=0, precision=1e-6, max_iterations=100)


# ## Distribution-specific KL-UCB indexes

# ### Gaussian

# In[38]:


@jit(nopython=True)
def klucbGauss_numba(x, d, sig2x=0.25, precision=0.):
    return x + np.sqrt(2 * sig2x * d)


# ### Bernoulli
# 
# Here, the `nopython=True` fails as numba has a hard time typing linked function calls.

# In[39]:


@jit
def klucbBern_numba(x, d, precision=1e-6):
    upperbound = min(1., klucbGauss_numba(x, d, sig2x=0.25))  # variance 1/4 for [0,1] bounded distributions
    # upperbound = min(1., klucbPoisson(x, d))  # also safe, and better ?
    return klucb_numba(x, d, klBern_numba, upperbound, precision)


# ### Poisson

# In[40]:


@jit
def klucbPoisson_numba(x, d, precision=1e-6):
    upperbound = x + d + np.sqrt(d * d + 2 * x * d)  # looks safe, to check: left (Gaussian) tail of Poisson dev
    return klucb_numba(x, d, klPoisson_numba, upperbound, precision)


# ### Exponential

# In[41]:


@jit
def klucbExp_numba(x, d, precision=1e-6):
    if d < 0.77:  # XXX where does this value come from?
        upperbound = x / (1 + 2. / 3 * d - np.sqrt(4. / 9 * d * d + 2 * d))
        # safe, klexp(x,y) >= e^2/(2*(1-2e/3)) if x=y(1-e)
    else:
        upperbound = x * np.exp(d + 1)
    if d > 1.61:  # XXX where does this value come from?
        lowerbound = x * np.exp(d)
    else:
        lowerbound = x / (1 + d - np.sqrt(d * d + 2 * d))
    return klucb_numba(x, d, klGamma_numba, upperbound, lowerbound, precision)


# ----
# # With Cython
# 
# It will be *almost* exactly the same code, by using the [`cython`]() magic to have cells written in [Cython](http://cython.org/).

# In[42]:


get_ipython().run_line_magic('load_ext', 'cython')


# A cell can now be written in Cython.
# For instance, we can define a simple example function in Python, and then write a Cython version, simply by declaring variables and tagging their types, like this:

# In[43]:


def some_loop(n: int) -> int:
    s = 0
    for i in range(0, n, 2):
        s += i
    return s


# In[44]:


get_ipython().run_cell_magic('cython', '', 'def some_loop_cython(int n) -> int:\n    cdef int s = 0\n    cdef int i = 0\n    for i in range(0, n, 2):\n        s += i\n    return s')


# In[45]:


get_ipython().run_line_magic('timeit', 'np.random.randint(1000)')
get_ipython().run_line_magic('timeit', 'some_loop(np.random.randint(1000))')
get_ipython().run_line_magic('timeit', 'some_loop_cython(np.random.randint(1000))')


# Here we observe a large speed-up. But how large? $6$ times or $50$ times?
# 
# It's really important to include the time taken by the Pseudo-Random Number Generator:
# 
# - Wrong computation of the speed-up gives about $6$ times faster:

# In[46]:


14.6 / 2.21


# - But if we remove the time taken by the PRNG (which takes the same time for both the naive Python and the Cython function), we get a larger speed-up, closer to reality, about $50$ times and not just $6$ times faster!

# In[47]:


(14.6 - 1.95) / (2.21 - 1.95)


# ## KL divergences

# ### Bernoulli distributions

# In[48]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klBern_cython(float x, float y) -> float:\n    x = min(max(x, eps), 1 - eps)\n    y = min(max(y, eps), 1 - eps)\n    return x * log(x / y) + (1 - x) * log((1 - x) / (1 - y))')


# ### Binomial distributions

# In[49]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klBin_cython(float x, float y, int n) -> float:\n    x = min(max(x, eps), 1 - eps)\n    y = min(max(y, eps), 1 - eps)\n    return n * (x * log(x / y) + (1 - x) * log((1 - x) / (1 - y)))')


# ### Poisson distributions

# In[50]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klPoisson_cython(float x, float y) -> float:\n    x = max(x, eps)\n    y = max(y, eps)\n    return y - x + x * log(x / y)')


# ### Exponential distributions

# In[51]:


get_ipython().run_cell_magic('cython', '', "from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klExp_cython(float x, float y) -> float:\n    if x <= 0 or y <= 0:\n        return float('+inf')\n    else:\n        x = max(x, eps)\n        y = max(y, eps)\n        return x / y - 1 - log(x / y)")


# ### Gamma distributions

# In[52]:


get_ipython().run_cell_magic('cython', '', "from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klGamma_cython(float x, float y, float a=1) -> float:\n    if x <= 0 or y <= 0:\n        return float('+inf')\n    else:\n        x = max(x, eps)\n        y = max(y, eps)\n        return a * (x / y - 1 - log(x / y))")


# ### Negative binomial distributions

# In[53]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klNegBin_cython(float x, float y, float r=1) -> float:\n    x = max(x, eps)\n    y = max(y, eps)\n    return r * log((r + x) / (r + y)) - x * log(y * (r + x) / (x * (r + y)))')


# ### Gaussian distributions

# In[54]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klGauss_cython(float x, float y, float sig2x=0.25, float sig2y=0.25) -> float:\n    if - eps < (sig2y - sig2x) < eps:\n        return (x - y) ** 2 / (2. * sig2x)\n    else:\n        return (x - y) ** 2 / (2. * sig2y) + 0.5 * ((sig2x/sig2y)**2 - 1 - log(sig2x/sig2y))')


# ## Generic KL-UCB indexes, with a bisection search

# For these, they need previously defined functions, which have to be rewritten from inside the `cython` cell to be accessible from Cython.
# To minimize repetitions, I use only one cell to define all functions.

# In[55]:


get_ipython().run_cell_magic('cython', '', "from libc.math cimport sqrt, log, exp\neps = 1e-15  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\n\ndef klucbGauss_cython(float x, float d, float sig2x=0.25, float precision=0.) -> float:\n    return x + sqrt(2 * sig2x * d)\n\ncdef float klucbGauss_cython_x(float x, float d, float sig2x=0.25, float precision=0.):\n    return x + sqrt(2 * sig2x * d)\n\n\ndef klucb_cython(float x, float d, kl, float upperbound,\n                 float lowerbound=float('-inf'),\n                 float precision=1e-6, int max_iterations=50) -> float:\n    cdef float value = max(x, lowerbound)\n    cdef float u = upperbound\n    cdef int _count_iteration = 0\n    cdef float m = 0\n    while _count_iteration < max_iterations and u - value > precision:\n        _count_iteration += 1\n        m = (value + u) / 2.\n        if kl(x, m) > d:\n            u = m\n        else:\n            value = m\n    return (value + u) / 2.\n\n\ncdef float klBern_cython_x(float x, float y):\n    x = min(max(x, eps), 1 - eps)\n    y = min(max(y, eps), 1 - eps)\n    return x * log(x / y) + (1 - x) * log((1 - x) / (1 - y))\n\ndef klucbBern_cython(float x, float d, float precision=1e-6) -> float:\n    cdef float upperbound = min(1., klucbGauss_cython_x(x, d, sig2x=0.25))  # variance 1/4 for [0,1] bounded distributions\n    # upperbound = min(1., klucbPoisson(x, d))  # also safe, and better ?\n    return klucb_cython(x, d, klBern_cython_x, upperbound, precision)\n\n\ncdef float klPoisson_cython_x(float x, float y):\n    x = max(x, eps)\n    y = max(y, eps)\n    return y - x + x * log(x / y)\n\ndef klucbPoisson_cython(float x, float d, float precision=1e-6) -> float:\n    cdef float upperbound = x + d + sqrt(d * d + 2 * x * d)  # looks safe, to check: left (Gaussian) tail of Poisson dev\n    return klucb_cython(x, d, klPoisson_cython_x, upperbound, precision)\n\n\ncdef float klGamma_cython_x(float x, float y):\n    if x <= 0 or y <= 0:\n        return float('+inf')\n    else:\n        x = max(x, eps)\n        y = max(y, eps)\n        return x / y - 1 - log(x / y)\n\ndef klucbExp_cython(float x, float d, float precision=1e-6) -> float:\n    cdef float upperbound = 1\n    cdef float lowerbound = 0\n    if d < 0.77:  # XXX where does this value come from?\n        upperbound = x / (1 + 2. / 3 * d - sqrt(4. / 9 * d * d + 2 * d))\n        # safe, klexp(x,y) >= e^2/(2*(1-2e/3)) if x=y(1-e)\n    else:\n        upperbound = x * exp(d + 1)\n    if d > 1.61:  # XXX where does this value come from?\n        lowerbound = x * exp(d)\n    else:\n        lowerbound = x / (1 + d - sqrt(d * d + 2 * d))\n    return klucb_cython(x, d, klGamma_cython_x, upperbound, lowerbound, precision)")


# For example, for `klucbBern_cython`, the two steps are to first compute an upperbound (as precise as possible) and the compute the kl-UCB index:

# In[56]:


x, d = 0.9, 0.2
upperbound = 1
klucb_cython(x, d, klBern_cython, upperbound, lowerbound=0, precision=1e-3, max_iterations=10)
klucb_cython(x, d, klBern_cython, upperbound, lowerbound=0, precision=1e-6, max_iterations=10)
klucb_cython(x, d, klBern_cython, upperbound, lowerbound=0, precision=1e-3, max_iterations=50)
klucb_cython(x, d, klBern_cython, upperbound, lowerbound=0, precision=1e-6, max_iterations=100)


# ----
# # With the C API for Python
# 
# It is more tedious, and won't be included here, but Python can easily [be extended](https://docs.python.org/3/c-api/) using C.
# It is the best way to obtain close-to-optimal performance for some parts of your code, and I will let you read [the introduction to the official documentation](https://docs.python.org/3/c-api/intro.html) if you are curious.
# 
# For my [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits/), I reused [some code from the py/maBandits](http://mloss.org/software/view/415/) project, and the authors implemented some of the previously defined KL-divergences and KL-UCB indexes in [pure Python](https://github.com/SMPyBandits/SMPyBandits/tree/master/SMPyBandits/Policies/kullback.py) as well as in [C optimized](https://github.com/SMPyBandits/SMPyBandits/tree/master/SMPyBandits/Policies/C/).
# I copied the compiled library in the current directory, and it can be imported:

# In[57]:


get_ipython().run_cell_magic('bash', '', 'ls -larth *kullback*\n[ -f kullback.py ] && mv -vf kullback.py kullback.py.old')


# In[58]:


get_ipython().system('ls -larth kullback*.so')


# In[59]:


import kullback


# In[60]:


help(kullback.klBern)


# In[72]:


[ s for s in dir(kullback) if not s.startswith('_') ]


# In[73]:


klBern_c = kullback.klBern
klBin_c = kullback.klBin
klExp_c = kullback.klExp
klGamma_c = kullback.klGamma
klGauss_c = kullback.klGauss
klPoisson_c = kullback.klPoisson
klucbBern_c = kullback.klucbBern
klucbExp_c = kullback.klucbExp
klucbGamma_c = kullback.klucbGamma
klucbGauss_c = kullback.klucbGauss
klucbPoisson_c = kullback.klucbPoisson


# If you want to reproduce this notebook, download the [`kullback_py3.c`](https://github.com/SMPyBandits/SMPyBandits/blob/master/SMPyBandits/Policies/C/kullback_py3.c) and follow the [build instructions](https://github.com/SMPyBandits/SMPyBandits/blob/master/SMPyBandits/Policies/C/).

# ----
# # Tests and benchmarks
# 
# For each of the functions defined in three approaches above, I will do some numerical tests to compare their speed − and memory −  efficiency. Simple.
# 
# The benchmark will be to test the computation time on random entries.
# It includes a constant time: creating random values! So I also compare the time to simply generate the values.

# In[61]:


r = np.random.random
rn = lambda: np.random.randint(1000)


# In[85]:


get_ipython().run_line_magic('timeit', '(r(), r())')
get_ipython().run_line_magic('timeit', '(r(), r(), rn())')


# - The time to generate random numbers like this is small, but not zero!
# - Generating a uniform integer, in particular, takes some time (more than 1 µs is not something that can be ignored!).
# 
# $\implies$ we will remove this $700$ ns or $2.5$ µs overhead when computing speed-up ratio between naive Python and numb or Cython versions.

# But we also need to test that the three versions of each function gives the same results (up-to approximation errors less than 
# $10^{-6}$ (at least)).

# In[63]:


def test_fs(fs, inputs, tolerance=1e-5, nb_tests=100):
    for _ in range(nb_tests):
        args = inputs()
        ref_f = fs[0]  # Python version
        output = ref_f(*args)
        for other_f in fs[1:]:
            other_output = other_f(*args)
            if abs(output) > 1:
                rel_diff = (output - other_output) / output
            else:
                rel_diff = (output - other_output)
            assert abs(rel_diff) <= tolerance, "Error: function {} gave {} and function {} gave {} on inputs {}, and the two outputs are too different.".format(ref_f, output, other_f, other_output, args)


# <span style="color:red;">WARNING</span> in the following, I use a very manual approach: I copied the time of each '%timeit' example, to compare speed-up ratios.
# So when I rerun the cells, the times might vary (a little bit), and I cannot keep an up-to-date versions of the computations of each ratio, so bear with me the (tiny) incoherences.

# ## KL divergences

# ### Bernoulli

# In[75]:


test_fs([klBern, klBern_numba, klBern_cython, klBern_c], lambda: (r(), r()))


# In[65]:


get_ipython().run_line_magic('timeit', 'klBern(r(), r())')


# In[66]:


get_ipython().run_line_magic('timeit', 'klBern_numba(r(), r())')


# In[67]:


get_ipython().run_line_magic('timeit', 'klBern_cython(r(), r())')


# In[74]:


get_ipython().run_line_magic('timeit', 'klBern_c(r(), r())')


# This is a speed-up ratio of about $12$ times faster for Numba and Cython, and $25$ times faster for the C version.

# In[87]:


(6280 - 576) / (1000 - 576)  # for Python vs numba
(6280 - 576) / (882 - 576)   # for Python vs Cython
(6280 - 576) / (811 - 576)   # for Python vs C


# ### Binomial

# In[76]:


test_fs([klBin, klBin_numba, klBin_cython, klBin_c], lambda: (r(), r(), rn()))


# Too much numerical difference? Let's try again with a larger tolerance:

# In[77]:


test_fs([klBin, klBin_numba, klBin_cython, klBin_c], lambda: (r(), r(), rn()), tolerance=1e-3)


# In[78]:


get_ipython().run_line_magic('timeit', 'klBin(r(), r(), rn())')


# In[79]:


get_ipython().run_line_magic('timeit', 'klBin_numba(r(), r(), rn())')


# In[80]:


get_ipython().run_line_magic('timeit', 'klBin_cython(r(), r(), rn())')


# In[81]:


get_ipython().run_line_magic('timeit', 'klBin_c(r(), r(), rn())')


# This is a speed-up ratio of about $5$ times faster for both Numba and Cython. Not so great, but still something!

# In[89]:


(7005 - 2350) / (3070 - 2350)  # for Python vs numba
(7005 - 2350) / (3331 - 2350)  # for Python vs Cython
(7005 - 2350) / (2980 - 2350)  # for Python vs C


# ### Poisson

# In[90]:


test_fs([klPoisson, klPoisson_numba, klPoisson_cython, klPoisson_c], lambda: (r(), r()))


# In[91]:


get_ipython().run_line_magic('timeit', 'klPoisson(r(), r())')


# In[92]:


get_ipython().run_line_magic('timeit', 'klPoisson_numba(r(), r())')


# In[93]:


get_ipython().run_line_magic('timeit', 'klPoisson_cython(r(), r())')


# In[94]:


get_ipython().run_line_magic('timeit', 'klPoisson_c(r(), r())')


# This is a speed-up ratio of about $7.5$ times faster for Numba, and about $7$ times for Cython and C.

# In[95]:


(2350 - 576) / (935 - 576)  # for Python vs numba
(2350 - 576) / (859 - 576)  # for Python vs Cython
(2350 - 576) / (811 - 576)  # for Python vs C


# ### Exponential

# In[96]:


test_fs([klExp, klExp_numba, klExp_cython, klExp_c], lambda: (r(), r()))


# In[97]:


get_ipython().run_line_magic('timeit', 'klExp(r(), r())')


# In[98]:


get_ipython().run_line_magic('timeit', 'klExp_numba(r(), r())')


# In[99]:


get_ipython().run_line_magic('timeit', 'klExp_cython(r(), r())')


# In[100]:


get_ipython().run_line_magic('timeit', 'klExp_c(r(), r())')


# This is a speed-up ratio of about $3$ times faster for Numba and $6$ times faster for Cython.
# Cython starts to win the race!

# In[101]:


(2210 - 576) / (1070 - 576)  # for Python vs numba
(2210 - 576) / (842 - 576)   # for Python vs Cython
(2210 - 576) / (869 - 576)   # for Python vs C


# ### Gamma

# In[105]:


klGamma_c = lambda x, y: kullback.klGamma(x, y, 1)


# In[106]:


test_fs([klGamma, klGamma_numba, klGamma_cython, klGamma_c], lambda: (r(), r()))


# In[107]:


get_ipython().run_line_magic('timeit', 'klGamma(r(), r())')


# In[108]:


get_ipython().run_line_magic('timeit', 'klGamma_numba(r(), r())')


# In[109]:


get_ipython().run_line_magic('timeit', 'klGamma_cython(r(), r())')


# In[110]:


get_ipython().run_line_magic('timeit', 'klGamma_c(r(), r())')


# This is a speed-up ratio of about $6$ times faster for Numba, and $6$ or $5$ times faster for Cython and C.
# Note that the C version probably looses a little bit due to this `lambda , y: ...` trick.

# In[111]:


(2700 - 576) / (1070 - 576)  # for Python vs numba
(2700 - 576) / (889 - 576)   # for Python vs Cython
(2700 - 576) / (997 - 576)   # for Python vs C


# ### Negative binomial

# In[112]:


test_fs([klNegBin, klNegBin_numba, klNegBin_cython], lambda: (r(), r()))


# In[113]:


get_ipython().run_line_magic('timeit', 'klNegBin(r(), r())')


# In[114]:


get_ipython().run_line_magic('timeit', 'klNegBin_numba(r(), r())')


# In[115]:


get_ipython().run_line_magic('timeit', 'klNegBin_cython(r(), r())')


# This is a speed-up ratio of about $5$ times faster for Numba and $10$ times faster for Cython.

# In[116]:


(3890 - 576) / (1160 - 576)  # for Python vs numba
(3890 - 576) / (901 - 576)   # for Python vs Cython


# ### Gaussian

# In[120]:


klGauss_c = lambda x, y: kullback.klGauss(x, y, 0.25)


# In[121]:


test_fs([klGauss, klGauss_numba, klGauss_cython, klGauss_c], lambda: (r(), r()))


# In[122]:


get_ipython().run_line_magic('timeit', 'klGauss(r(), r())')


# In[123]:


get_ipython().run_line_magic('timeit', 'klGauss_numba(r(), r())')


# In[124]:


get_ipython().run_line_magic('timeit', 'klGauss_cython(r(), r())')


# In[125]:


get_ipython().run_line_magic('timeit', 'klGauss_c(r(), r())')


# This is a speed-up ratio of about $45$ times faster for Cython, but Numba completely here!
# Why? No idea!
# C is also slower than the Python version here, due to this `lambda x,y: ...` trick.

# In[126]:


(852 - 576) / (1070 - 576)  # for Python vs numba
(852 - 576) / (745 - 576)   # for Python vs Cython
(852 - 576) / (911 - 576)   # for Python vs C


# ## KL-UCB indexes

# ### Gaussian

# In[128]:


klucbGauss_c = lambda x, y: kullback.klucbGauss(x, y, 0.25)


# In[129]:


test_fs([klucbGauss, klucbGauss_numba, klucbGauss_cython, klucbGauss_c], lambda: (r(), r()))


# In[130]:


get_ipython().run_line_magic('timeit', 'klucbGauss(r(), r())')


# In[131]:


get_ipython().run_line_magic('timeit', 'klucbGauss_numba(r(), r())')


# In[132]:


get_ipython().run_line_magic('timeit', 'klucbGauss_cython(r(), r())')


# In[133]:


get_ipython().run_line_magic('timeit', 'klucbGauss_c(r(), r())')


# This is a speed-up ratio of about $14$ times faster for Cython and $4$ times for C, and one more failure case for Numba.
# The C version looses again due to the `lambda x,y` trick.

# In[135]:


(1960 - 576) / (31300 - 576)  # for Python vs numba
(1960 - 576) / (676 - 576)    # for Python vs Cython
(1960 - 576) / (939 - 576)    # for Python vs C


# ### Bernoulli

# In[139]:


klucbBern_c = lambda x, y: kullback.klucbBern(x, y, 1e-6)


# In[140]:


test_fs([klucbBern, klucbBern_numba, klucbBern_cython, klucbBern_c], lambda: (r(), r()))


# In[141]:


get_ipython().run_line_magic('timeit', 'klucbBern(r(), r())')


# In[142]:


get_ipython().run_line_magic('timeit', 'klucbBern_numba(r(), r())')


# In[143]:


get_ipython().run_line_magic('timeit', 'klucbBern_cython(r(), r())')


# In[144]:


get_ipython().run_line_magic('timeit', 'klucbBern_c(r(), r())')


# This is a speed-up ratio of about $15$ times faster for Cython, and one more failure case for Numba.
# The speed-up for the C version is CRAZY here, and it shows that optimizing loops is the most important!

# In[146]:


(91900 - 576) / (170000 - 576)  # for Python vs numba
(91900 - 576) / (6930 - 576)    # for Python vs Cython
(91900 - 576) / abs(314 - 576)  # for Python vs C


# ### Poisson

# In[148]:


klucbPoisson_c = lambda x, y: kullback.klucbPoisson(x, y, 1e-6)


# In[149]:


test_fs([klucbPoisson, klucbPoisson_numba, klucbPoisson_cython, klucbPoisson_c], lambda: (r(), r()))


# In[150]:


get_ipython().run_line_magic('timeit', 'klucbPoisson(r(), r())')


# In[151]:


get_ipython().run_line_magic('timeit', 'klucbPoisson_numba(r(), r())')


# In[152]:


get_ipython().run_line_magic('timeit', 'klucbPoisson_cython(r(), r())')


# In[153]:


get_ipython().run_line_magic('timeit', 'klucbPoisson_c(r(), r())')


# This is a speed-up ratio of about $15$ times faster for Cython, and one more failure case for Numba.
# It's again a strong victory for the C version, with a speed up of about $45$ !

# In[154]:


(72600 - 576) / (167000 - 576)  # for Python vs numba
(72600 - 576) / (5330 - 576)    # for Python vs Cython
(72600 - 576) / (2180 - 576)    # for Python vs Cython


# ### Exponential

# In[155]:


klucbExp_c = lambda x, y: kullback.klucbExp(x, y, 1e-6)


# In[156]:


test_fs([klucbExp, klucbExp_numba, klucbExp_cython, klucbExp_c], lambda: (r(), r()))


# In[157]:


get_ipython().run_line_magic('timeit', 'klucbExp(r(), r())')


# In[158]:


get_ipython().run_line_magic('timeit', 'klucbExp_numba(r(), r())')


# In[159]:


get_ipython().run_line_magic('timeit', 'klucbExp_cython(r(), r())')


# In[160]:


get_ipython().run_line_magic('timeit', 'klucbExp_c(r(), r())')


# This is a speed-up ratio of about $17$ times faster for Cython, and one more failure case for Numba.
# Strong victory for the C version, a speed-up of $50$ is impressive!

# In[161]:


(78700 - 576) / (156000 - 576)  # for Python vs numba
(78700 - 576) / (4410 - 576)    # for Python vs Cython
(78700 - 576) / (2040 - 576)    # for Python vs Cython


# ## Clean up

# In[162]:


get_ipython().run_cell_magic('bash', '', '[ -f kullback.py.old ] && mv -vf kullback.py.old kullback.py')


# ----
# # Conclusion
# 
# - As expected, the Numba, Cython and C versions are *way* faster than the naive Python versions, on very simple functions,
# - The simpler the function, the closer the speed-up is between Numba and Cython or C,
# - Cython and C always give the best improvement,
# - On less simple functions, Numba can fail to produce `nopython` code, and on some examples the `nopython` code can be *slower* than naive Python (like, crazily slower). No idea why, and the point was precisely not to try too much optimizing this use of Numba.
# - Cython gives speed-up factors typically between $100$ and $12$ times faster than naive Python.
# - C alsways gives the best speed-up, with a speed-up between $150$ and $50$ times faster than naive Python, and usually $10$ times faster than Cython!
# 
# ## Take away messages
# The take away messages are the following:
# 
# 1. if your code makes a heavy use of a few small and not-too-complicated functions, it is probably worth using `numba.jit` to speed them up,
# 2. but be careful, and do some basic benchmark on each "possibly optimized" function, to check that using Numba actually speeds it up instead of slowing it down!
# 3. if Numba is not enough to speed up your code, try to write a Cython version of the bottleneck functions.
# 4. if your bottleneck is *still* too slow, try to write a C extension, but it requires a good knowledge of both the internals of the C language, as well as a (basic) knowledge of the [C-API of CPython](https://docs.python.org/3/c-api/).
# 
# ## Using Cython *for real* ?
# My advice for using Cython are the following:
# 
# 1. First try in a notebook, using this [`%%cython` magic is very easy!](https://cython.readthedocs.io/en/latest/src/quickstart/build.html#using-the-jupyter-notebook)
# 2. Then if you are happy about your implementation, save it to a `.pyx` file, and use [`pyximport`](https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#pyximport) from your Python code to automatically compile and import it. It works perfectly fine, believe me!
# 
# ## Using C *for real* ?
# It's not too hard, but it's certainly not as easy as Cython.
# My approach from now will to not even consider writing C code, as Cython offers a very good speedup when carefully used. And it's much easier to just write `import pyximport` before importing your Cython-accelerated module, in comparison to writing a `setupy.py` and requiring a compilation step for a C-optimized module!
# 
# > That's it for today, folks! See [this page](https://github.com/Naereen/notebooks) for other notebooks I wrote recently.
