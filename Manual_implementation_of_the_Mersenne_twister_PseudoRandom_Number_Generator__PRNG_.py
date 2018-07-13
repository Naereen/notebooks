
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Manual-implementation-of-the-Mersenne-twister-PseudoRandom-Number-Generator-(PRNG)" data-toc-modified-id="Manual-implementation-of-the-Mersenne-twister-PseudoRandom-Number-Generator-(PRNG)-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Manual implementation of the Mersenne twister PseudoRandom Number Generator (PRNG)</a></div><div class="lev2 toc-item"><a href="#Common-API-for-the-PRNG-defined-here" data-toc-modified-id="Common-API-for-the-PRNG-defined-here-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Common API for the PRNG defined here</a></div><div class="lev2 toc-item"><a href="#First-example:-a-simple-linear-congruential-generator" data-toc-modified-id="First-example:-a-simple-linear-congruential-generator-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>First example: a simple linear congruential generator</a></div><div class="lev2 toc-item"><a href="#Trying-to-write-a-cell-in-cython,-for-speeding-things-up" data-toc-modified-id="Trying-to-write-a-cell-in-cython,-for-speeding-things-up-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Trying to write a cell in <a href="http://cython.org/" target="_blank"><code>cython</code></a>, for speeding things up</a></div><div class="lev2 toc-item"><a href="#Checking-and-plotting-the-result?" data-toc-modified-id="Checking-and-plotting-the-result?-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Checking and plotting the result?</a></div><div class="lev2 toc-item"><a href="#A-second-example:-Multiple-Recursive-Generator" data-toc-modified-id="A-second-example:-Multiple-Recursive-Generator-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>A second example: Multiple-Recursive Generator</a></div><div class="lev2 toc-item"><a href="#A-third-example:-combined-Multiple-Recursive-Generator,-with-MRG32k3a" data-toc-modified-id="A-third-example:-combined-Multiple-Recursive-Generator,-with-MRG32k3a-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>A third example: combined Multiple-Recursive Generator, with <code>MRG32k3a</code></a></div><div class="lev2 toc-item"><a href="#Finally,-the-Mersenne-twister-PRNG" data-toc-modified-id="Finally,-the-Mersenne-twister-PRNG-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Finally, the Mersenne twister PRNG</a></div><div class="lev3 toc-item"><a href="#Period" data-toc-modified-id="Period-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Period</a></div><div class="lev3 toc-item"><a href="#Random-seeds" data-toc-modified-id="Random-seeds-172"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Random seeds</a></div><div class="lev3 toc-item"><a href="#Implementing-the-Mersenne-twister-algorithm" data-toc-modified-id="Implementing-the-Mersenne-twister-algorithm-173"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>Implementing the Mersenne twister algorithm</a></div><div class="lev3 toc-item"><a href="#Small-review-of-bitwise-operations" data-toc-modified-id="Small-review-of-bitwise-operations-174"><span class="toc-item-num">1.7.4&nbsp;&nbsp;</span>Small review of bitwise operations</a></div><div class="lev3 toc-item"><a href="#Mersenne-twister-algorithm-in-cython" data-toc-modified-id="Mersenne-twister-algorithm-in-cython-175"><span class="toc-item-num">1.7.5&nbsp;&nbsp;</span>Mersenne twister algorithm in <a href="http://www.cython.org/" target="_blank"><code>cython</code></a></a></div><div class="lev3 toc-item"><a href="#Testing-our-implementations" data-toc-modified-id="Testing-our-implementations-176"><span class="toc-item-num">1.7.6&nbsp;&nbsp;</span>Testing our implementations</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev1 toc-item"><a href="#Generating-samples-from-other-distributions" data-toc-modified-id="Generating-samples-from-other-distributions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Generating samples from other distributions</a></div><div class="lev2 toc-item"><a href="#Bernoulli-distribution" data-toc-modified-id="Bernoulli-distribution-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Bernoulli distribution</a></div><div class="lev2 toc-item"><a href="#Uniform-distribution-on-$[a,-b)$,-for-floats-and-integers" data-toc-modified-id="Uniform-distribution-on-$[a,-b)$,-for-floats-and-integers-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Uniform distribution on $[a, b)$, for floats and integers</a></div><div class="lev2 toc-item"><a href="#Exponential-distribution" data-toc-modified-id="Exponential-distribution-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exponential distribution</a></div><div class="lev2 toc-item"><a href="#Gaussian-distribution-(normal)" data-toc-modified-id="Gaussian-distribution-(normal)-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Gaussian distribution (normal)</a></div><div class="lev2 toc-item"><a href="#Erlang-distribution" data-toc-modified-id="Erlang-distribution-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Erlang distribution</a></div><div class="lev2 toc-item"><a href="#Gamma-distribution" data-toc-modified-id="Gamma-distribution-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Gamma distribution</a></div><div class="lev2 toc-item"><a href="#Beta-distribution" data-toc-modified-id="Beta-distribution-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Beta distribution</a></div><div class="lev2 toc-item"><a href="#Integer-Beta-distribution" data-toc-modified-id="Integer-Beta-distribution-28"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Integer Beta distribution</a></div><div class="lev2 toc-item"><a href="#Binomial-distribution" data-toc-modified-id="Binomial-distribution-29"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Binomial distribution</a></div><div class="lev2 toc-item"><a href="#Geometric-distribution" data-toc-modified-id="Geometric-distribution-210"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Geometric distribution</a></div><div class="lev2 toc-item"><a href="#Poisson-distribution" data-toc-modified-id="Poisson-distribution-211"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>Poisson distribution</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-212"><span class="toc-item-num">2.12&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev1 toc-item"><a href="#Generating-vectors" data-toc-modified-id="Generating-vectors-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Generating vectors</a></div><div class="lev2 toc-item"><a href="#Discrete-distribution" data-toc-modified-id="Discrete-distribution-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Discrete distribution</a></div><div class="lev2 toc-item"><a href="#Generating-a-random-vector-uniformly-on-a-n-dimensional-ball" data-toc-modified-id="Generating-a-random-vector-uniformly-on-a-n-dimensional-ball-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Generating a random vector uniformly on a n-dimensional ball</a></div><div class="lev2 toc-item"><a href="#Generating-a-random-permutation" data-toc-modified-id="Generating-a-random-permutation-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Generating a random permutation</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Conclusion</a></div>

# # Manual implementation of the Mersenne twister PseudoRandom Number Generator (PRNG)
# This small notebook is a short experiment, to see if I can implement the [Mersenne twister](https://en.wikipedia.org/wiki/Mersenne_twister) PseudoRandom Number Generator ([PRNG](https://en.wikipedia.org/wiki/Pseudo-random_number_generator)).
# 
# And then I want to use it to define a `rand()` function, and use it to samples from the most famous discrete and continuous probability distributions.
# Random permutations will also be studied.
# 
# - *Reference*: [Wikipedia](https://en.wikipedia.org/wiki/Mersenne_twister), and this book: ["Simulation and the Monte-Carlo method", by R.Y.Rubinstein & D.P.Kroese](http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118632168.html) ([Rubinstein & Kroese, 2017]), chapter 2 pages 52-53. If you are curious, [this webpage](https://realpython.com/python-random/) is a good explanation of the difference between PRNG, Cryptographically Secure PRNG (CSPRNG) and "True" NRG.
# - *Date*: 11 March 2017.
# - *Author*: [Lilian Besson](https://GitHub.com/Naereen/notebooks).
# - *License*: [MIT Licensed](https://lbesson.mit-license.org/).
# 
# ----

# ## Common API for the PRNG defined here
# First, I want to define a simple object-oriented API, in order to write all the examples of PNRG with the same interface.

# In[131]:


import numpy as np


# In[132]:


class PRNG(object):
    """Base class for any Pseudo-Random Number Generator."""
    def __init__(self, X0=0):
        """Create a new PRNG with seed X0."""
        self.X0 = X0
        self.X = X0
        self.t = 0
        self.max = 0
    
    def __iter__(self):
        """self is already an iterator!"""
        return self
    
    def seed(self, X0=None):
        """Reinitialize the current value with X0, or self.X0.
        
        - Tip: Manually set the seed if you need reproducibility in your results.
        """
        self.t = 0
        self.X = self.X0 if X0 is None else X0
    
    def __next__(self):
        """Produce a next value and return it."""
        # This default PRNG does not produce random numbers!
        self.t += 1
        return self.X
    
    def randint(self, *args, **kwargs):
        """Return an integer number in [| 0, self.max - 1 |] from the PRNG."""
        return self.__next__()

    def int_samples(self, shape=(1,)):
        """Get a numpy array, filled with integer samples from the PRNG, of shape = shape."""
        # return [ self.randint() for _ in range(size) ]
        return np.fromfunction(np.vectorize(self.randint), shape=shape, dtype=int)

    def rand(self, *args, **kwargs):
        """Return a float number in [0, 1) from the PRNG."""
        return self.randint() / float(1 + self.max)

    def float_samples(self, shape=(1,)):
        """Get a numpy array, filled with float samples from the PRNG, of shape = shape."""
        # return [ self.rand() for _ in range(size) ]
        return np.fromfunction(np.vectorize(self.rand), shape=shape, dtype=int)


# ----
# ## First example: a simple linear congruential generator
# Let me start by implementing a simple linear congruential generator, with three parameters $m$, $a$, $c$, defined like this :
# 
# - Start from $X_0$,
# - And then follow the recurrence equation: $$ X_{t+1} = (a X_t + c) \mod m. $$
# 
# This algorithm produces a sequence $(X_t)_{t\in\mathbb{N}} \in \mathbb{N}^{\mathbb{N}}$.

# In[133]:


class LinearCongruentialGenerator(PRNG):
    """A simple linear congruential Pseudo-Random Number Generator."""
    def __init__(self, m, a, c, X0=0):
        """Create a new PRNG with seed X0."""
        super(LinearCongruentialGenerator, self).__init__(X0=X0)
        self.m = self.max = m
        self.a = a
        self.c = c
    
    def __next__(self):
        """Produce a next value and return it, following the recurrence equation: X_{t+1} = (a X_t + c) mod m."""
        self.t += 1
        x = self.X
        self.X = (self.a * self.X + self.c) % self.m
        return x


# The values recommended by the authors, Lewis, Goodman and Miller, are the following:

# In[134]:


m = 1 << 31 - 1  # 1 << 31 = 2**31
a = 7 ** 4
c = 0


# The seed is important. If $X_0 = 0$, this first example PRNG will only produce $X_t = 0, \forall t$.

# In[135]:


FirstExample = LinearCongruentialGenerator(m=m, a=a, c=c)


# In[136]:


def test(example, nb=3):
    for t, x in enumerate(example):
        print("{:>3}th value for {.__class__.__name__} is X_t = {:>10}".format(t, example, x))
        if t >= nb - 1:
            break


# In[137]:


test(FirstExample)


# But with any positive seed, the sequence will appear random.

# In[138]:


SecondExample = LinearCongruentialGenerator(m=m, a=a, c=c, X0=12011993)


# In[139]:


test(SecondExample)


# The sequence is completely determined by the seed $X_0$:

# In[140]:


SecondExample.seed(12011993)
test(SecondExample)


# > Note: I prefer to use this custom class to define iterators, instead of a simple generator (with `yield` keyword) as I want them to have a `.seed(X0)` method.

# ## Trying to write a cell in [`cython`](http://cython.org/), for speeding things up
# > For more details, see [this blog post](https://acsgsoc15.wordpress.com/2015/04/07/using-cython-in-ipython/), and [this other one](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/#22-writing-functions-in-other-languages).

# In[141]:


# Thanks to https://nbviewer.jupyter.org/gist/minrk/7715212
from __future__ import print_function
from IPython.core import page
def myprint(s):
    try:
        print(s['text/plain'])
    except (KeyError, TypeError):
        print(s)
page.page = myprint


# In[142]:


get_ipython().run_line_magic('load_ext', 'cython')


# Then we define a function `LinearCongruentialGenerator_next`, in a Cython cell.

# In[143]:


get_ipython().run_cell_magic('cython', '', 'def nextLCG(int x, int a, int c, int m):\n    """Compute x, nextx = (a * x + c) % m, x in Cython."""\n    cdef int nextx = (a * x + c) % m\n    return (x, nextx)')


# In[144]:


from __main__ import nextLCG
nextLCG
get_ipython().run_line_magic('pinfo', 'nextLCG')


# Then it's easy to use it to define another Linear Congruential Generator.

# In[145]:


class CythonLinearCongruentialGenerator(LinearCongruentialGenerator):
    """A simple linear congruential Pseudo-Random Number Generator, with Cython accelerated function __next__."""
    
    def __next__(self):
        """Produce a next value and return it, following the recurrence equation: X_{t+1} = (a X_t + c) mod m."""
        self.t += 1
        x, self.X = nextLCG(self.X, self.a, self.c, self.m)
        return x


# Let compare it with the first implementation (using pure Python).

# In[146]:


NotCythonSecondExample = LinearCongruentialGenerator(m=m, a=a, c=c, X0=13032017)
CythonSecondExample = CythonLinearCongruentialGenerator(m=m, a=a, c=c, X0=13032017)


# They both give the same values, that's a relief.

# In[147]:


test(NotCythonSecondExample)
test(CythonSecondExample)


# The speedup is not great, but still visible.

# In[148]:


get_ipython().run_line_magic('timeit', '[ NotCythonSecondExample.randint() for _ in range(1000000) ]')
get_ipython().run_line_magic('timeit', '[ CythonSecondExample.randint() for _ in range(1000000) ]')


# In[149]:


get_ipython().run_line_magic('prun', 'min(CythonSecondExample.randint() for _ in range(1000000))')


# ----
# ## Checking and plotting the result?
# First, we can generate a matrix of samples, as random floats in $[0, 1)$, and check that the mean is about $1/2$:

# In[150]:


shape = (400, 400)
image = SecondExample.float_samples(shape)


# In[151]:


np.mean(image), np.var(image)


# What about the speed? Of course, a hand-written Python code will always be really slower than a C-extension code, and the PRNG from the modules `random` or `numpy.random` are written in C (or Cython), and so will always be faster.
# But how much faster?

# In[152]:


import random
import numpy.random

print(np.mean(SecondExample.float_samples(shape)))
print(np.mean([ [ random.random() for _ in range(shape[0]) ] for _ in range(shape[1]) ]))
print(np.mean(numpy.random.random(shape)))


# In[153]:


get_ipython().run_line_magic('timeit', 'SecondExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', '[ [ random.random() for _ in range(shape[0]) ] for _ in range(shape[1]) ]')
get_ipython().run_line_magic('timeit', 'numpy.random.random(shape)')


# This was expected: of course `numpy.random.` functions are written and optimized to generate thousands of samples quickly, and of course my hand-written Python implementation for `LinearCongruentialGenerator` is slower than the C-code generating the module `random`.

# ----
# We can also plot this image as a grayscaled image, in order to visualize this "randomness" we just created.

# In[268]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

def showimage(image):
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray', interpolation='none')
    plt.axis('off')
    plt.show()


# In[269]:


showimage(image)


# It looks good already! We can't see any recurrence, but we see a regularity, with small squares.
# 
# And it does not seem to depend too much on the seed:

# In[270]:


SecondExample.seed(11032017)
image = SecondExample.float_samples((10, 10))
showimage(image)


# In[271]:


SecondExample.seed(1103201799)
image = SecondExample.float_samples((10, 10))
showimage(image)


# We can also visualize the generated numbers with a histogram, to visually check that the random numbers in $[0, 1)$ are indeed "uniformly" located.

# In[272]:


def plotHistogram(example, nb=100000, bins=200):
    numbers = example.float_samples((nb,))
    plt.figure(figsize=(16, 5))
    plt.hist(numbers, bins=bins, normed=True, alpha=0.8)
    plt.xlabel("Random numbers in $[0, 1)$")
    plt.ylabel("Mass repartition")
    plt.title("Repartition of ${}$ random numbers in $[0, 1)$".format(nb))
    plt.show()


# In[273]:


plotHistogram(SecondExample, 1000000, 200)


# ----
# ## A second example: Multiple-Recursive Generator
# Let start by writing a generic Multiple Recursive Generator, which is defined by the following linear recurrence equation, of order $k \geq 1$:
# 
# - Start from $X_0$, with a false initial history of $(X_{-k+1}, X_{-k}, \dots, X_{-1})$,
# - And then follow the recurrence equation: $$ X_{t} = (a_1 X_{t-1} + \dots + a_k X_{t-k}) \mod m. $$
# 
# This algorithm produces a sequence $(X_t)_{t\in\mathbb{N}} \in \mathbb{N}^{\mathbb{N}}$.

# In[160]:


class MultipleRecursiveGenerator(PRNG):
    """A Multiple Recursive Pseudo-Random Number Generator (MRG), with one sequence (X_t)."""
    def __init__(self, m, a, X0):
        """Create a new PRNG with seed X0."""
        assert np.shape(a) == np.shape(X0), "Error: the weight vector a must have the same shape as X0."
        super(MultipleRecursiveGenerator, self).__init__(X0=X0)
        self.m = self.max = m
        self.a = a
    
    def __next__(self):
        """Produce a next value and return it, following the recurrence equation: X_t = (a_1 X_{t-1} + ... + a_k X_{t-k}) mod m."""
        self.t += 1
        x = self.X[0]
        nextx = (np.dot(self.a, self.X)) % self.m
        self.X[1:] = self.X[:-1]
        self.X[0] = nextx
        return x


# For example, with an arbitrary choice of $k = 3$, of weights $a = [10, 9, 8]$ and $X_0 = [10, 20, 30]$:

# In[161]:


m = (1 << 31) - 1
X0 = np.array([10, 20, 30])
a = np.array([10, 9, 8])

ThirdExample = MultipleRecursiveGenerator(m, a, X0)

test(ThirdExample)


# We can again check for the mean and the variance of the generated sequence:

# In[275]:


shape = (400, 400)
image = ThirdExample.float_samples(shape)
np.mean(image), np.var(image)


# This Multiple Recursive Generator is of course slower than the simple Linear Recurrent Generator:

# In[163]:


get_ipython().run_line_magic('timeit', 'SecondExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'ThirdExample.float_samples(shape)')


# And it seems to work fine as well:

# In[276]:


showimage(image)


# In[277]:


plotHistogram(ThirdExample, 1000000, 200)


# > It looks also good!

# ----
# ## A third example: combined Multiple-Recursive Generator, with `MRG32k3a`
# 
# Let start by writing a generic Multiple Recursive Generator, which is defined by the following coupled linear recurrence equation, of orders $k_1, k_2 \geq 1$:
# 
# - Start from $X_0$ and $Y_0$, with a false initial history of $(X_{-k_1 + 1}, X_{-k_1}, \dots, X_{-1})$ and $(Y_{-k_2 + 1}, Y_{-k_2}, \dots, Y_{-1})$,
# - And then follow the recurrence equation: $$ X_{t} = (a_1 X_{t-1} + \dots + a_{k_1} X_{t-k_1}) \mod m. $$ and $$ Y_{t} = (b_1 Y_{t-1} + \dots + b_{k_2} Y_{t-k_2}) \mod m. $$
# 
# This algorithm produces two sequences $(X_t)_{t\in\mathbb{N}} \in \mathbb{N}^{\mathbb{N}}$ and $(X_t)_{t\in\mathbb{N}} \in \mathbb{N}^{\mathbb{N}}$, and usually the sequence used for the output is $U_t = X_t - Y_t + \max(m_1, m_2)$.

# In[166]:


class CombinedMultipleRecursiveGenerator(PRNG):
    """A Multiple Recursive Pseudo-Random Number Generator (MRG), with two sequences (X_t, Y_t)."""
    def __init__(self, m1, a, X0, m2, b, Y0):
        """Create a new PRNG with seeds X0, Y0."""
        assert np.shape(a) == np.shape(X0), "Error: the weight vector a must have the same shape as X0."
        assert np.shape(b) == np.shape(Y0), "Error: the weight vector b must have the same shape as Y0."
        self.t = 0
        # For X
        self.m1 = m1
        self.a = a
        self.X0 = self.X = X0
        # For Y
        self.m2 = m2
        self.b = b
        self.Y0 = self.Y = Y0
        # Maximum integer number produced is max(m1, m2)
        self.m = self.max = max(m1, m2)
    
    def __next__(self):
        """Produce a next value and return it, following the recurrence equation: X_t = (a_1 X_{t-1} + ... + a_k X_{t-k}) mod m."""
        self.t += 1
        # For X
        x = self.X[0]
        nextx = (np.dot(self.a, self.X)) % self.m1
        self.X[1:] = self.X[:-1]
        self.X[0] = nextx
        # For Y
        y = self.Y[0]
        nexty = (np.dot(self.b, self.Y)) % self.m2
        self.Y[1:] = self.Y[:-1]
        self.Y[0] = nexty
        # Combine them
        u = x - y + (self.m1 if x <= y else 0)
        return u


# To obtain the well-known `MRG32k3a` generator, designed by L'Ecuyer in 1999, we choose these parameters:

# In[167]:


m1 = (1 << 32) - 209                  # important choice!
a = np.array([0, 1403580, -810728])   # important choice!
X0 = np.array([1000, 10000, 100000])  # arbitrary choice!

m2 = (1 << 32) - 22853                # important choice!
b = np.array([527612, 0, -1370589])   # important choice!
Y0 = np.array([5000, 50000, 500000])  # arbitrary choice!

MRG32k3a = CombinedMultipleRecursiveGenerator(m1, a, X0, m2, b, Y0)

test(MRG32k3a)


# We can again check for the mean and the variance of the generated sequence:

# In[278]:


shape = (400, 400)
image = MRG32k3a.float_samples(shape)
np.mean(image), np.var(image)


# This combined Multiple Recursive Generator is of course slower than the simple Multiple Recursive Generator and the simple Linear Recurrent Generator:

# In[169]:


get_ipython().run_line_magic('timeit', 'SecondExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'ThirdExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'MRG32k3a.float_samples(shape)')


# In[279]:


showimage(image)


# In[280]:


plotHistogram(MRG32k3a, 1000000, 200)


# > This one looks fine too!

# ----
# ## Finally, the Mersenne twister PRNG
# 
# I won't explain all the details, and will follow closely the notations from my reference book [Rubinstein & Kroese, 2017].
# It will be harder to implement!
# 
# First, let us compute the period of the PRNG we will implement, with the default values for the parameters $w = 32$ (word length) and $n = 624$ ("big" integer).

# ### Period

# In[172]:


w = 32
n = 624


# In[173]:


def MersenneTwisterPeriod(n, w):
    return (1 << (w * (n - 1) + 1)) - 1

MersenneTwisterPeriod(n, w) == (2 ** 19937) - 1


# ### Random seeds
# Then we need to use a previously defined PRNG to set the random seeds.
# 
# To try to have "really random" seeds, let me use that classical trick of using the system time as a source of initial randomness.
# 
# - Namely, I will use the number of microseconds in the current time stamp as the seed for a `LinearCongruentialGenerator`,
# - Then use it to generate the seeds for a `MRG32k3a` generator,
# - And finally use it to get the seed for the Mersenne twister.

# In[174]:


from datetime import datetime

def get_seconds():
    d = datetime.today().timestamp()
    s = 1e6 * (d - int(d))
    return int(s)


# In[175]:


get_seconds()  # Example


# In[176]:


def seed_rows(example, n, w):
    return example.int_samples((n,))

def random_Mersenne_seed(n, w):
    linear = LinearCongruentialGenerator(m=(1 << 31) - 1, a=7 ** 4, c=0, X0=get_seconds())
    assert w == 32, "Error: only w = 32 was implemented"
    m1 = (1 << 32) - 209                  # important choice!
    a = np.array([0, 1403580, -810728])   # important choice!
    X0 = np.array(linear.int_samples((3,)))  # random choice!
    m2 = (1 << 32) - 22853                # important choice!
    b = np.array([527612, 0, -1370589])   # important choice!
    Y0 = np.array(linear.int_samples((3,)))  # random choice!
    MRG32k3a = CombinedMultipleRecursiveGenerator(m1, a, X0, m2, b, Y0)
    seed = seed_rows(MRG32k3a, n, w)
    assert np.shape(seed) == (n,)
    return seed

example_seed = random_Mersenne_seed(n, w)
example_seed


# In[177]:


for xi in example_seed:
    print("Integer xi = {:>12} and in binary, bin(xi) = {:>34}".format(xi, bin(xi)))


# ### Implementing the Mersenne twister algorithm
# Finally, the Mersenne twister can be implemented like this:

# In[179]:


class MersenneTwister(PRNG):
    """The Mersenne twister Pseudo-Random Number Generator (MRG)."""
    def __init__(self, seed=None,
                 w=32, n=624, m=397, r=31,
                 a=0x9908B0DF, b=0x9D2C5680, c=0xEFC60000,
                 u=11, s=7, v=15, l=18):
        """Create a new Mersenne twister PRNG with this seed."""
        self.t = 0
        # Parameters
        self.w = w
        self.n = n
        self.m = m
        self.r = r
        self.a = a
        self.b = b
        self.c = c
        self.u = u
        self.s = s
        self.v = v
        self.l = l
        # For X
        if seed is None:
            seed = random_Mersenne_seed(n, w)
        self.X0 = seed
        self.X = np.copy(seed)
        # Maximum integer number produced is 2**w - 1
        self.max = (1 << w) - 1
        
    def __next__(self):
        """Produce a next value and return it, following the Mersenne twister algorithm."""
        self.t += 1
        # 1. --- Compute x_{t+n}
        # 1.1.a. First r bits of x_t : left = (x_t >> (w - r)) << (w - r)
        # 1.1.b. Last w - r bits of x_{t+1} : right = x & ((1 << (w - r)) - 1)
        # 1.1.c. Concatenate them together in a binary vector x : x = left + right
        left = self.X[0] >> (self.w - self.r)
        right = (self.X[1] & ((1 << (self.w - self.r)) - 1))
        x = (left << (self.w - self.r)) + right
        xw = x % 2             # 1.2. get xw
        if xw == 0:
            xtilde = (x >> 1)            # if xw = 0, xtilde = (x >> 1)
        else:
            xtilde = (x >> 1) ^ self.a   # if xw = 1, xtilde = (x >> 1) ⊕ a
        nextx = self.X[self.m] ^ xtilde  # 1.3. x_{t+n} = x_{t+m} ⊕ \tilde{x}
        # 2. --- Shift the content of the n rows
        oldx0 = self.X[0]          # 2.a. First, forget x0
        self.X[:-1] = self.X[1:]   # 2.b. shift one index on the left, x1..xn-1 to x0..xn-2
        self.X[-1]  = nextx        # 2.c. write new xn-1
        # 3. --- Then use it to compute the answer, y
        y = nextx                      # 3.a. y = x_{t+n}
        y ^= (y >> self.u)             # 3.b. y = y ⊕ (y >> u)
        y ^= ((y << self.s) & self.b)  # 3.c. y = y ⊕ ((y << s) & b)
        y ^= ((y << self.v) & self.c)  # 3.d. y = y ⊕ ((y << v) & c)
        y ^= (y >> self.l)             # 3.e. y = y ⊕ (y >> l)
        return y


# ### Small review of bitwise operations
# 
# The Python documentation explains how to [use bitwise operations easily](https://docs.python.org/3/library/stdtypes.html?highlight=bitwise#bitwise-operations-on-integer-types), and also [this page](https://wiki.python.org/moin/BitwiseOperators) and [this StackOverflow answer](http://stackoverflow.com/a/1746642/).
# 
# The only difficult part of the algorithm is the first step, when we need to take the first $r$ bits of $X_t =$ `X[0]`, and the last $w - r$ bits of $X_{t+1} =$ `X[1]`.
# On some small examples, let quickly check that I implemented this correctly:

# In[180]:


def testsplit(x, r=None, w=None):
    if w is None:
        w = x.bit_length()
    if r is None:
        r = w - 1
    assert x.bit_length() == w
    left = x >> (w - r)
    right = x % 2 if w == 1 else x & ((1 << (w-r) - 1))
    x2 = (left << (w - r)) + right
    assert x == x2
    print("x = {:10} -> left r={} = {:10} and right w-r={} = {:4} -> x2 = {:10}".format(bin(x), r, bin(left), w-r, bin(right), bin(x2)))

x = 0b10011010
testsplit(x)
x = 0b10010011
testsplit(x)
x = 0b10011111
testsplit(x)
x = 0b11110001
testsplit(x)
x = 0b00110001
testsplit(x)


# ### Mersenne twister algorithm in [`cython`](http://www.cython.org/)
# As for the first example, let us write a Cython function to (try to) compute the next numbers more easily.
# 
# My reference was [this page of the Cython documentation](http://docs.cython.org/en/latest/src/userguide/numpy_tutorial.html).

# In[262]:


get_ipython().run_cell_magic('cython', '', 'from __future__ import division\nimport cython\nimport numpy as np\n# "cimport" is used to import special compile-time information\n# about the numpy module (this is stored in a file numpy.pxd which is\n# currently part of the Cython distribution).\ncimport numpy as np\n\n# We now need to fix a datatype for our arrays. I\'ve used the variable\n# DTYPE for this, which is assigned to the usual NumPy runtime\n# type info object.\nDTYPE = np.int64\n# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For\n# every type in the numpy module there\'s a corresponding compile-time\n# type with a _t-suffix.\nctypedef np.int64_t DTYPE_t\n\n\n@cython.boundscheck(False) # turn off bounds-checking for entire function\ndef nextMersenneTwister(np.ndarray[DTYPE_t, ndim=1] X, unsigned long w, unsigned long m, unsigned long r, unsigned long a, unsigned long u, unsigned long s, unsigned long b, unsigned long v, unsigned long c, unsigned long l):\n    """Produce a next value and return it, following the Mersenne twister algorithm, implemented in Cython."""\n    assert X.dtype == DTYPE\n    # 1. --- Compute x_{t+n}\n    # 1.1.a. First r bits of x_t : left = (x_t >> (w - r)) << (w - r)\n    # 1.1.b. Last w - r bits of x_{t+1} : right = x & ((1 << (w - r)) - 1)\n    # 1.1.c. Concatenate them together in a binary vector x : x = left + right\n    cdef unsigned long x = ((X[0] >> (w - r)) << (w - r)) + (X[1] & ((1 << (w - r)) - 1))\n    cdef unsigned long xtilde = 0\n    if x % 2 == 0:  # 1.2. get xw\n        xtilde = (x >> 1)            # if xw = 0, xtilde = (x >> 1)\n    else:\n        xtilde = (x >> 1) ^ a   # if xw = 1, xtilde = (x >> 1) ⊕ a\n    cdef unsigned long nextx = X[m] ^ xtilde  # 1.3. x_{t+n} = x_{t+m} ⊕ \\tilde{x}\n    # 2. --- Shift the content of the n rows\n    # oldx0 = X[0]            # 2.a. First, forget x0\n    X[:-1] = X[1:]            # 2.b. shift one index on the left, x1..xn-1 to x0..xn-2\n    X[-1]  = nextx            # 2.c. write new xn-1\n    # 3. --- Then use it to compute the answer, y\n    cdef unsigned long y = nextx        # 3.a. y = x_{t+n}\n    y ^= (y >> u)             # 3.b. y = y ⊕ (y >> u)\n    y ^= ((y << s) & b)       # 3.c. y = y ⊕ ((y << s) & b)\n    y ^= ((y << v) & c)       # 3.d. y = y ⊕ ((y << v) & c)\n    y ^= (y >> l)             # 3.e. y = y ⊕ (y >> l)\n    return y')


# In[263]:


nextMersenneTwister
get_ipython().run_line_magic('pinfo', 'nextMersenneTwister')


# That should be enough to define a Cython version of our `MersenneTwister` class.

# In[264]:


class CythonMersenneTwister(MersenneTwister):
    """The Mersenne twister Pseudo-Random Number Generator (MRG), accelerated with Cython."""

    def __next__(self):
        """Produce a next value and return it, following the Mersenne twister algorithm."""
        self.t += 1
        return nextMersenneTwister(self.X, self.w, self.m, self.r, self.a, self.u, self.s, self.b, self.v, self.c, self.l)


# ### Testing our implementations

# In[265]:


ForthExample = MersenneTwister(seed=example_seed)
CythonForthExample = CythonMersenneTwister(seed=example_seed)


# In[266]:


ForthExample.int_samples((10,))
CythonForthExample.int_samples((10,))


# Which one is the quickest?

# In[267]:


get_ipython().run_line_magic('timeit', '[ ForthExample.randint() for _ in range(100000) ]')
get_ipython().run_line_magic('timeit', '[ CythonForthExample.randint() for _ in range(100000) ]')


# Using Cython gives only a speedup of $2 \times$, that's disappointing!

# In[187]:


get_ipython().run_line_magic('prun', '[ ForthExample.randint() for _ in range(1000000) ]')


# In[188]:


get_ipython().run_line_magic('prun', '[ CythonForthExample.randint() for _ in range(1000000) ]')


# $\implies$ the Cython version is twice as fast as the pure-Python version.
# We can still improve this, I am sure.
# 
# ----

# We can again check for the mean and the variance of the generated sequence.
# Mean should be $\frac12 = 0.5$ and variance should be $\frac{(b-a)^2}{12} = \frac{1}{12} = 0.08333\dots$:

# In[189]:


shape = (400, 400)
image = ForthExample.float_samples(shape)
np.mean(image), np.var(image)


# This Python hand-written Mersenne twister is of course slower than the previous PRNG defined above (combined Multiple Recursive Generator, simple Multiple Recursive Generator, and the simple Linear Recurrent Generator):

# In[190]:


get_ipython().run_line_magic('timeit', 'SecondExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'ThirdExample.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'MRG32k3a.float_samples(shape)')
get_ipython().run_line_magic('timeit', 'ForthExample.float_samples(shape)')


# That's not too bad, for $400 \times 400 = 160000$ samples, but obviously it is incredibly slower than the optimized PRNG found in the [`numpy.random`](https://docs.scipy.org/doc/numpy/reference/routines.random.html) package.

# In[191]:


get_ipython().run_line_magic('timeit', 'numpy.random.random_sample(shape)')


# A good surprise is that this implementation Mersenne appears faster than the combined MRG of order $k = 3$ (i.e., `MRG32k3a`).

# In[192]:


showimage(image)


# In[193]:


plotHistogram(ForthExample, 1000000, 200)


# ----
# ## Conclusion
# Well, that's it, I just wanted to implement a few Pseudo-Random Number Generators, and compare them.
# 
# I should finish the job:
# - implement a test for "randomness", and check the various PRNG I implemented against it,
# - use these various `rand()` functions (uniform in $[0,1)$) to generate other distributions.

# ----
# # Generating samples from other distributions
# So far, I implemented some PRNG, which essentially give a function `rand()` to produce float number uniformly sampled from $[0, 1)$.
# 
# Let use it to generate samples from other distributions.

# In[194]:


def newrand():
    """Create a new random function rand()."""
    mersenne = MersenneTwister()
    rand = mersenne.rand
    return rand

rand = newrand()


# We will need an easy way to visualize the repartition of samples for the distributions defined below.

# In[195]:


def plotHistogramOfDistribution(distr, nb=10000, bins=200):
    numbers = [ distr() for _ in range(nb) ]
    plt.figure(figsize=(14, 3))
    plt.hist(numbers, bins=bins, normed=True, alpha=0.8)
    plt.xlabel("Random numbers from function %s" % distr.__name__)
    plt.ylabel("Mass repartition")
    plt.title("Repartition of ${}$ random numbers".format(nb))
    plt.show()


# ----
# ## Bernoulli distribution
# It is the simplest example, $X \in \{0, 1\}$, $\mathbb{P}(X = 0) = p$ and $\mathbb{P}(X = 1) = 1 - p$ for some parameter $p \in [0,1]$.

# In[196]:


def bernoulli(p=0.5):
    """Get one random sample X ~ Bern(p)."""
    assert 0 <= p <= 1, "Error: the parameter p for a bernoulli distribution has to be in [0, 1]."
    return int(rand() < p)


# In[197]:


print([ bernoulli(0.5) for _ in range(20) ])
print([ bernoulli(0.1) for _ in range(20) ])  # lots of 0
print([ bernoulli(0.9) for _ in range(20) ])  # lots of 1


# We can quickly check that the frequency of $1$ in a large sample of size $n$ will converge to $p$ as $n \to +\infty$:

# In[198]:


def delta_p_phat_bernoulli(p, nb=100000):
    samples = [ bernoulli(p) for _ in range(nb) ]
    return np.abs(np.mean(samples) - p)


# In[199]:


print(delta_p_phat_bernoulli(0.5))
print(delta_p_phat_bernoulli(0.1))
print(delta_p_phat_bernoulli(0.9))


# That's less than $1\%$ of absolute error, alright.

# In[200]:


plotHistogramOfDistribution(bernoulli)


# ----
# ## Uniform distribution on $[a, b)$, for floats and integers
# This one is obvious too:

# In[201]:


def uniform(a, b):
    """Uniform float number in [a, b)."""
    assert a < b, "Error: for uniform(a, b), a must be < b."
    return a + (b - a) * rand()


# In[202]:


def uniform_3_5():
    return uniform(3, 5)

plotHistogramOfDistribution(uniform_3_5, 100000)


# For integers, it is extremely similar:

# In[203]:


def randint(a, b):
    """Uniform float number in [a, b)."""
    assert a < b, "Error: for randint(a, b), a must be < b."
    assert isinstance(a, int), "Error: for randint(a, b), a must be an integer."
    assert isinstance(b, int), "Error: for randint(a, b), a must be an integer."
    return int(a + (b - a) * rand())


# In[204]:


def uniform_int_18_42():
    return randint(18, 42)

plotHistogramOfDistribution(uniform_int_18_42, 100000)


# ----
# ## Exponential distribution
# If $X \sim \mathrm{Exp}(\lambda)$, $F(x) = 1 - \mathrm{e}^{- \lambda x}$, and so $F^{-1}(u) = -\frac1{\lambda} \ln(1 - u)$.
# The inversion method is easy to apply here:

# In[205]:


from math import log

def exponential(lmbda=1):
    """Get one random sample X ~ Exp(lmbda)."""
    assert lmbda > 0, "Error: the parameter lmbda for exponential(lmbda) must be > 0."
    u = rand()  # 1 - u ~ U([0, 1]), so u and 1 - u follow the same distribution
    return -(1.0 / lmbda) * log(u)


# The resulting histogram has the shape we know as "exponential":

# In[206]:


plotHistogramOfDistribution(exponential)


# We can compare its efficiency with [`numpy.random.exponential()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.exponential), and of course it is slower.

# In[207]:


get_ipython().run_line_magic('timeit', '[ exponential(1.) for _ in range(10000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.exponential(1.) for _ in range(10000) ]  # about 50 times slower, not too bad!')


# ----
# ## Gaussian distribution (normal)
# By using the Box-Muller approach, if $U_1, U_2 \sim U(0, 1)$ are independent, then setting $X = \sqrt{- 2 \ln U_1} \cos(2 \pi U_2)$ and $Y = \sqrt{- 2 \ln U_1} \sin(2 \pi U_2)$ leads to $X, Y \sim N(0, 1)$.
# 
# Then $Z = \mu + \sigma * X$ will be distributed according to the Gaussian distribution of *mean* $\mu$ and *variance* $\sigma > 0$: $Z \sim N(\mu, \sigma)$.

# In[208]:


from math import sqrt, cos, pi

def normal(mu=0, sigma=1):
    """Get one random sample X ~ N(mu, sigma)."""
    assert sigma > 0, "Error: the parameter sigma for normal(mu, sigma) must be > 0."
    u1, u2 = rand(), rand()
    x = sqrt(- 2 * log(u1)) * cos(2 * pi * u2)
    return mu + sigma * x


# In[209]:


plotHistogramOfDistribution(normal, 100000)


# We can compare its efficiency with [`numpy.random.normal()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.normal), and of course it is slower.

# In[210]:


get_ipython().run_line_magic('timeit', '[ normal(0, 1) for _ in range(10000) ]')
get_ipython().run_line_magic('timeit', 'np.random.normal(0, 1, 10000)  # 550 times quicker! oh boy!')


# ----
# ## Erlang distribution
# If $X \sim \mathrm{Erl}(m, \lambda)$, then it simply is the sum of $m \in \mathbb{N}^{*}$ *iid* exponential random variables $Y_i \sim \mathrm{Exp}(\lambda)$.

# In[211]:


def erlang(m=1., lmbda=1.):
    """Get one random sample X ~ Erl(m, lmbda)."""
    assert m > 0, "Error: the parameter m for erlang(m, lmbda) must be > 0."
    assert lmbda > 0, "Error: the parameter lmbda for erlang(m, lmbda) must be > 0."
    return - 1. / lmbda * sum(log(rand()) for _ in range(int(m)) )


# In[212]:


def erlang_20_10():
    return erlang(20, 10)

plotHistogramOfDistribution(erlang_20_10)


# ----
# ## Gamma distribution
# The algorithm is more complicated.
# The pdf of $X \sim \mathrm{Gamma}(\alpha, \lambda)$ is $f(x) = x^{\alpha - 1} \lambda^{\alpha} \mathrm{e}^{- \lambda x} / \Gamma(\alpha)$, for parameters $\alpha>0, \lambda>0$.

# In[213]:


def gamma(alpha=1., lmbda=1.):
    """Get one random sample X ~ Gamma(alpha, lmbda)."""
    assert alpha > 0, "Error: the parameter alpha for gamma(alpha, lmbda) must be > 0."
    assert lmbda > 0, "Error: the parameter lmbda for gamma(alpha, lmbda) must be > 0."
    if alpha <= 1:
        x = gamma(alpha + 1., lmbda)
        u = rand()
        return x * (u ** (1. / alpha))
    else:
        d = alpha - (1. / 3.)
        oneByC = sqrt(9. * d)
        c = 1. / oneByC
        while True:
            z = normal(0, 1)
            if z > - oneByC:
                v = (1. + c * z)**3
                u = rand()
                if log(u) < (.5 * (z**2)) + d*(v + log(v)):
                    break
        return d * v / lmbda


# In[214]:


def gamma_pi_5():
    return gamma(pi, 5)

plotHistogramOfDistribution(gamma_pi_5)


# We can compare its efficiency with [`numpy.random.gamma()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.gamma), and of course it is slower.

# In[215]:


get_ipython().run_line_magic('timeit', '[ gamma(pi, 5) for _ in range(10000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.gamma(pi, 5) for _ in range(10000) ]  # 500 times quicker! oh boy!')


# ----
# ## Beta distribution
# By definition, a Beta distribution is straightforward to obtain as soon as we have a Gamma distribution:
# if $Y_1 \sim \mathrm{Gamma}(\alpha, 1)$ and $Y_2 \sim \mathrm{Gamma}(\beta, 1)$, then $X = \frac{Y_1}{Y_1 + Y_2}$ follows $\mathrm{Beta}(\alpha, \beta)$.

# In[216]:


def beta(a=1., b=1.):
    """Get one random sample X ~ Beta(a, b)."""
    assert a > 0, "Error: the parameter a for beta(a, b) must be > 0."
    assert b > 0, "Error: the parameter b for beta(a, b) must be > 0."
    y1 = gamma(a, 1.)
    y2 = gamma(b, 1.)
    return y1 / float(y1 + y2)


# In[217]:


def beta_40_5():
    return beta(40, 5)

plotHistogramOfDistribution(beta_40_5)

def beta_3_55():
    return beta(3, 55)

plotHistogramOfDistribution(beta_3_55)


# We can compare its efficiency with [`numpy.random.beta()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.beta), and of course it is slower.

# In[218]:


get_ipython().run_line_magic('timeit', '[ beta(pi, 5*pi) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ beta(5*pi, pi) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.beta(pi, 5*pi) for _ in range(1000) ]  # 200 times quicker! oh boy!')
get_ipython().run_line_magic('timeit', '[ np.random.beta(5*pi, pi) for _ in range(1000) ]  # 200 times quicker! oh boy!')


# ----
# ## Integer Beta distribution
# If $\alpha = m, \beta = n$ are integer, it is much simpler:

# In[219]:


def int_beta(m=1, n=1):
    """Get one random sample X ~ Beta(m, n) with integer parameters m, n."""
    assert m > 0, "Error: the parameter m for int_beta(m, n) must be > 0."
    assert n > 0, "Error: the parameter n for int_beta(m, n) must be > 0."
    us = [rand() for _ in range(m + n - 1)]
    return sorted(us)[m]  # inefficient to sort, but quick to write!


# In[220]:


def int_beta_40_5():
    return int_beta(40, 5)

plotHistogramOfDistribution(int_beta_40_5)


# We can again compare its efficiency with [`numpy.random.beta()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.beta), and of course it is slower, but this integer-specific implementation `int_beta()` is quicker than the generic `beta()` implementation.

# In[221]:


get_ipython().run_line_magic('timeit', '[ int_beta(40, 5) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ int_beta(3, 55) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.beta(40, 5) for _ in range(1000) ]  # 1500 times quicker! oh boy!')
get_ipython().run_line_magic('timeit', '[ np.random.beta(3, 55) for _ in range(1000) ]  # 2000 times quicker! oh boy!')


# ----
# ## Binomial distribution
# Very easy to obtain, by definition, from the sum of $n$ Bernoulli distribution:
# if $Y_1,\dots,Y_n \sim \mathrm{Bern}(p)$, then $X = \sum_{i=1}^n Y_i \sim \mathrm{Bin}(n, p)$.

# In[222]:


def binomial(n=1, p=0.5):
    """Get one random sample X ~ Bin(n, p)."""
    assert 0 <= p <= 1, "Error: the parameter p for binomial(n, p) has to be in [0, 1]."
    assert n > 0, "Error: the parameter n for binomial(n, p)  has to be in [0, 1]."
    return sum(bernoulli(p) for _ in range(n))


# In[223]:


def bin_50_half():
    return binomial(50, 0.5)

plotHistogramOfDistribution(bin_50_half)


# > It is an integer distribution, meaning that $X \sim \mathrm{Bin}(n, p)$ always is $X \in \mathbb{N}$.

# We can compare its efficiency with [`numpy.random.binomial()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.binomial), and of course it is slower.

# In[224]:


get_ipython().run_line_magic('timeit', '[ binomial(10, 1. / pi) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.binomial(10, 1. / pi) for _ in range(1000) ]  # 100 times quicker! oh boy!')


# ----
# ## Geometric distribution
# Again, it is very easy from the definition of a Geometric random variable.

# In[225]:


def geometric(p=0.5):
    """Get one random sample X ~ Geom(p)."""
    assert 0 <= p <= 1, "Error: the parameter p for binomial(n, p) has to be in [0, 1]."
    y = exponential(- log(1. - p))
    return 1 + int(y)


# In[226]:


def geom_05():
    return geometric(0.5)

plotHistogramOfDistribution(geom_05)

def geom_01():
    return geometric(0.1)

plotHistogramOfDistribution(geom_01)

def geom_001():
    return geometric(0.01)

plotHistogramOfDistribution(geom_001)


# We can compare its efficiency with [`numpy.random.geometric()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.geometric), and of course it is slower.

# In[227]:


get_ipython().run_line_magic('timeit', '[ geometric(1. / pi) for _ in range(10000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.geometric(1. / pi) for _ in range(10000) ]  # 50 times quicker, not too bad!')


# ----
# ## Poisson distribution
# If $X \sim \mathrm{Pois}(\lambda)$, then its pdf is $f(n) = \frac{\mathrm{e}^{-\lambda} \lambda^n}{n!}$.
# With the rejection method, and the close relationship between the Exponential and the Poisson distributions, it is not too hard to generate samples from a Poisson distribution if we know how to generate samples from a Exponential distribution.

# In[228]:


def poisson(lmbda=1.):
    """Get one random sample X ~ Poisson(lmbda)."""
    assert lmbda > 0, "Error: the parameter lmbda for poisson(lmbda) has to be > 0."
    n = 0
    a = 1
    while a >= exp(-lmbda):
        u = rand()
        a *= u
        n += 1
    return n - 1


# In[229]:


def poisson_5():
    return poisson(5.)

plotHistogramOfDistribution(poisson_5)

def poisson_50():
    return poisson(50.)

plotHistogramOfDistribution(poisson_50)


# We can compare its efficiency with [`numpy.random.poisson()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.poisson), and of course it is slower.

# In[230]:


get_ipython().run_line_magic('timeit', '[ poisson(12 * pi) for _ in range(1000) ]')
get_ipython().run_line_magic('timeit', '[ np.random.poisson(12 * pi) for _ in range(1000) ]  # 1000 times quicker! oh boy!')


# ---
# ## Conclusion
# Except the Gamma distribution, the algorithms presented above are easy to understand and to implement, and it was quick to obtain a dozen of the most common distributions, both continous (Exponential, Gaussian, Gamma, Beta) and discrete (Bernoulli, Binomial, Geometric, Poisson).

# ----
# # Generating vectors
# 
# Now that we have a nice Pseudo-Random Number Generator, using Mersenne twister, and that we have demonstrated how to use its `rand()` function to produce samples from the most common distributions, we can continue and explain how to produce vectors of samples.
# 
# For instance, one would need a `choice()` function to get a random sample from a list of $n$ values, following any discrete distribution, or a `shuffle()` function to randomly shuffle a list.

# ----
# ## Discrete distribution
# Let $p = [p_1, \dots, p_n] \in \mathbb{R}^n$ be a discrete distribution, meaning that $p_i > 0$ and $\sum_{i=1}^n p_i = 1$, then we can use the inverse-transform method to get a sample $i \in \{1, \dots, n\}$ with probability $\mathbb{P}(i = j) = p_j$.

# In[231]:


def discrete(p):
    """Return a random index i in [0..n-1] from the discrete distribution p = [p0,..,pn-1]."""
    n = len(p)
    assert n > 0, "Error: the distribution p for discrete(p) must not be empty!"
    assert all(0 <= pi <= 1 for pi in p), "Error: all coordinates of the distribution p for discrete(p) must be 0 <= pi <= 1."
    assert abs(sum(p) - 1) < 1e-9, "Error: the distribution p for discrete(p) does not sum to 1."
    u = rand()
    i = 0
    s = p[0]
    while i < n-1 and u > s:
        i += 1
        s += p[i]
    return i


# Then it is easy to get *one* random sample from a list of values:

# In[232]:


def one_choice(values, p=None):
    """Get a random sample from the values, from the dsicrete distribution p = [p0,..,pn-1]."""
    if p is None:
        return values[randint(0, len(values))]
    else:
        return values[discrete(p)]


# In[233]:


def example_choice():
    return one_choice(range(10))

plotHistogramOfDistribution(example_choice)


# And it is also easy to generate many samples, with replacement.

# In[234]:


def choices_with_replacement(values, m=1, p=None):
    """Get m random sample from the values, with replacement, from the discrete distribution p = [p0,..,pn-1]."""
    if p is None:
        return [ values[randint(0, len(values))] for _ in range(m) ]
    else:
        return [ values[discrete(p)] for _ in range(m) ]


# It is harder to handle the case without replacements. My approach is simple but slow: once a value is drawn, remove it from the input list, and update the discrete distribution accordingly.
# To be sure of not modifying the input list, I use `copy.copy()` to copy them.

# In[235]:


from copy import copy

def choices_without_replacement(values, m=1, p=None):
    """Get m random sample from the values, without replacement, from the discrete distribution p = [p0,..,pn-1]."""
    values = copy(values)
    if p is None:
        samples = []
        for _ in range(m):
            i = randint(0, len(values))
            samples.append(values[i])
            del values[i]
    else:
        p = copy(p)
        samples = []
        for _ in range(m):
            i = discrete(p)
            samples.append(values[i])
            del values[i]
            del p[i]
            renormalize_cst = float(sum(p))
            p = [ pi / renormalize_cst for pi in p ]
    return samples


# In[236]:


values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [0.5, 0.1, 0.1, 0.1, 0.1, 0.02, 0.02, 0.02, 0.02, 0.02]


# We can check that the input lists are not modified:

# In[237]:


print(choices_without_replacement(values, 5))
print(choices_without_replacement(values, 5))
print(choices_without_replacement(values, 5))

print(choices_without_replacement(values, 5, p))
print(choices_without_replacement(values, 5, p))
print(choices_without_replacement(values, 5, p))


# With an histogram, we can check that as a large weight is put on $0 =$ `values[0]`, the *sum* of $m = 5$ samples will be smaller if replacements are allowed (more chance to get twice a $0$ value).

# In[238]:


def example_with_replacement():
    return np.sum(choices_with_replacement(values, 5, p))
plotHistogramOfDistribution(example_with_replacement)

def example2_with_replacement():
    return np.sum(choices_with_replacement(values, 5))
plotHistogramOfDistribution(example2_with_replacement)


# In[239]:


def example_without_replacement():
    # this sum is at least >= 10 = 0 + 1 + 2 + 3 + 4 (5 smallest values)
    return np.sum(choices_without_replacement(values, 5, p))
plotHistogramOfDistribution(example_without_replacement)

def example2_without_replacement():
    # this sum is at least >= 10 = 0 + 1 + 2 + 3 + 4 (5 smallest values)
    return np.sum(choices_without_replacement(values, 5))
plotHistogramOfDistribution(example2_without_replacement)


# ----
# ## Generating a random vector uniformly on a n-dimensional ball
# 
# The acceptance-rejection method is easy to apply in this case.
# We use `uniform(-1, 1)` $n$ times to get a random vector in $[0,1]^n$, and keep trying as long as it is not in the $n$-dim ball.

# In[240]:


def on_a_ball(n=1, R=1):
    """Generate a vector of dimension n, uniformly from the n-dim ball of radius R."""
    rsquare = float('inf')
    Rsquare = R**2
    while rsquare > Rsquare:
        values = [ uniform(-R, R) for _ in range(n) ]
        rsquare = sum(xi ** 2 for xi in values)
    return values


# In[241]:


print(on_a_ball(4, 1))


# The radius of such a vector can be plotted in a histogram.

# In[242]:


def random_radius_dim3():
    return sqrt(sum(xi**2 for xi in on_a_ball(3, 1)))

plotHistogramOfDistribution(random_radius_dim3, 100000)


# And similarly, if we normalize the values before returning them, to move them to the surface of the $n$-dimensional ball, then we get an easy way to sample a uniform *direction*:

# In[243]:


def on_a_sphere(n=1, R=1):
    """Generate a vector of dimension n, uniformly on the surface of the n-dim ball of radius R."""
    rsquare = float('inf')
    Rsquare = R**2
    while rsquare > Rsquare:
        values = [ uniform(-1, 1) for _ in range(n) ]
        rsquare = sum(xi ** 2 for xi in values)
    r = sqrt(rsquare)
    return [ xi / r for xi in values ]


# All such samples have the same radius, but it can be interesting the see the smallest gap between two coordinates.

# In[244]:


def random_delta_dim3():
    return np.min(np.diff(sorted(on_a_sphere(3, 1))))

plotHistogramOfDistribution(random_radius_dim3, 100000)


# ----
# ## Generating a random permutation
# 
# The first approach is simple to write and understand, and it uses `choices_without_replacement([0..n-1], n)` with a uniform distribution $p$.

# In[245]:


def random_permutation(n=1):
    """Random permutation of [0..n-1], with the function choices_without_replacement."""
    return choices_without_replacement(list(range(n)), n)


# In[246]:


for _ in range(10):
    print(random_permutation(10))


# It seems random enough!
# 
# To check this first implementation, we can implement the stupidest sorting algorithm, the "shuffle sort":
# shuffle the input list, as long as it is not correctly sorted.

# In[247]:


def is_sorted(values, debug=False):
    """Check if the values are sorted in increasing order, worst case is O(n)."""
    n = len(values)
    if n <= 1:
        return True
    xn, xnext = values[0], values[1]
    for i in range(1, n + 1):
        if xn > xnext:
            if debug:
                print("Values x[{}] = {} > x[{}+1] = {} are not in the good order!".format(xn, i, i, xnext))
            return False
        if i >= n:
            return True
        xn, xnext = xnext, values[i]
    return True

print(is_sorted([1, 2, 3, 4], debug=True))
print(is_sorted([1, 2, 3, 4, 0], debug=True))
print(is_sorted([1, 2, 5, 4], debug=True))
print(is_sorted([1, 6, 3, 4], debug=True))


# We can easily apply a permutation, and return a shuffled version of a list of values.

# In[248]:


def apply_perm(values, perm):
    """Apply the permutation perm to the values."""
    return [values[pi] for pi in perm]

def shuffled(values):
    """Return a random permutation of the values."""
    return apply_perm(values, random_permutation(len(values)))


# Similarly, it is easy to shuffle in place a list of values.

# In[249]:


def shuffle(values):
    """Apply in place a random permutation of the values."""
    perm = random_permutation(len(values))
    v = copy(values)
    for (i, pi) in enumerate(perm):
        values[i] = v[pi]


# In[250]:


def shuffle_sort(values):
    """Can you think of a more stupid sorting algorithm? or a shorter one?"""
    values = copy(values)
    while not is_sorted(values):
        print(values)
        shuffle(values)
    return values  # modified in place but also returned


# In[251]:


shuffle_sort([2, 1])


# It is a **very** inefficient algorithm, but the fact that it works on small lists is enough to confirm that our algorithm to generate random permutations works fine.

# In[252]:


print(shuffle_sort(shuffled(list(range(3)))))
print(shuffle_sort(shuffled(list(range(4)))))


# We can think of another algorithm to generate a random permutation:
# - take $n$ values $u_1,\dots,u_n \sim U(0, 1)$,
# - order them,
# - return the index of the sort.

# In[253]:


def random_permutation_2(n=1):
    """Random permutation of [0..n-1], by sorting n uniform values in [0,1]."""
    return list(np.argsort([rand() for _ in range(n)]))


# In[254]:


for _ in range(10):
    print(random_permutation_2(10))


# It seems random enough too!
# 
# Let compare which of the two algorithms is the fastest:

# In[255]:


get_ipython().run_line_magic('timeit', 'random_permutation(100)')
get_ipython().run_line_magic('timeit', 'random_permutation_2(100)')


# In[256]:


get_ipython().run_line_magic('timeit', 'random_permutation(10000)')
get_ipython().run_line_magic('timeit', 'random_permutation_2(10000)')


# It seems that the first algorithm is slower, but this comes from the naively-written `choice_without_replacement()`, in fact we can implement it more efficiently.

# In[257]:


def random_permutation_3(n=1):
    """Random permutation of [0..n-1], with a smart implementation of choices_without_replacement."""
    p = list(range(n))
    values = []
    for i in range(n):
        j = randint(0, n - i)
        values.append(p[j])
        p[i], p[j] = p[j], p[i]
    return values


# In[258]:


for _ in range(10):
    print(random_permutation_3(10))


# In[259]:


get_ipython().run_line_magic('timeit', 'random_permutation(1000)')
get_ipython().run_line_magic('timeit', 'random_permutation_2(1000)')
get_ipython().run_line_magic('timeit', 'random_permutation_3(1000)')
get_ipython().run_line_magic('timeit', 'numpy.random.permutation(1000)')

get_ipython().run_line_magic('timeit', 'random_permutation(10000)')
get_ipython().run_line_magic('timeit', 'random_permutation_2(10000)')
get_ipython().run_line_magic('timeit', 'random_permutation_3(10000)')
get_ipython().run_line_magic('timeit', 'numpy.random.permutation(10000)  # About 1000 times slower! Oh boy!!')


# Hoho, not so sure on small lists...
# But for larger values of $n$, the second implementation of the first algorithm wins:

# In[260]:


get_ipython().run_line_magic('timeit', 'random_permutation(100000)')
get_ipython().run_line_magic('timeit', 'random_permutation_2(100000)')
get_ipython().run_line_magic('timeit', 'random_permutation_3(100000)')
get_ipython().run_line_magic('timeit', 'numpy.random.permutation(100000)  # About 1000 times slower! Oh boy!!')


# And the second algorithm wins, as it uses the optimized `numpy.argsort()` function as its core operator.

# ----
# ## Conclusion
# This last part presented how to generate from any discrete distribution, and then two algorithms to generate a random permutation, uniformly sampled from $\Sigma_n$ (set of $n!$ permutations of $\{0,\dots,n-1\}$).
# We applied them to the (very stupid) "shuffle sort" algorithm, to check their correctness.
# 
# ----
# > *That's it for today, folks!*
