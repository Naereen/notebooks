
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Python-Pi-Day-2017" data-toc-modified-id="Python-Pi-Day-2017-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Python Pi Day 2017</a></div><div class="lev1 toc-item"><a href="#Computing-a-lot-of-digits-of-$\pi$?" data-toc-modified-id="Computing-a-lot-of-digits-of-$\pi$?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Computing a lot of digits of <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-388-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C0;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2745" role="math" style="width: 0.702em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.554em; height: 0px; font-size: 125%;"><span style="position: absolute; clip: rect(1.941em, 1000.55em, 2.572em, -1000em); top: -2.462em; left: 0em;"><span class="mrow" id="MathJax-Span-2746"><span class="mi" id="MathJax-Span-2747" style="font-family: STIXMathJax_Main; font-style: italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.032em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.462em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.061em; border-left: 0px solid; width: 0px; height: 0.634em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi></math></span></span><script type="math/tex" id="MathJax-Element-388">\pi</script>?</a></div><div class="lev2 toc-item"><a href="#Two-simple-methods-for-finding-the-first-digits-of-$\pi$" data-toc-modified-id="Two-simple-methods-for-finding-the-first-digits-of-$\pi$-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Two simple methods for finding the first digits of <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-391-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C0;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2754" role="math" style="width: 0.693em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.541em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.953em, 1000.54em, 2.615em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-2755"><span class="mi" id="MathJax-Span-2756" style="font-family: STIXMathJax_Main; font-style: italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.032em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 0.653em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi></math></span></span><script type="math/tex" id="MathJax-Element-391">\pi</script></a></div><div class="lev3 toc-item"><a href="#Fraction-approximations,-and-$\pi$-imported-from-the-math-module" data-toc-modified-id="Fraction-approximations,-and-$\pi$-imported-from-the-math-module-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Fraction approximations, and <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-392-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C0;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2757" role="math" style="width: 0.736em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.56em; height: 0px; font-size: 129%;"><span style="position: absolute; clip: rect(1.898em, 1000.56em, 2.602em, -1000em); top: -2.455em; left: 0em;"><span class="mrow" id="MathJax-Span-2758"><span class="mi" id="MathJax-Span-2759" style="font-family: STIXMathJax_Main; font-style: italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.032em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.455em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.079em; border-left: 0px solid; width: 0px; height: 0.686em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi></math></span></span><script type="math/tex" id="MathJax-Element-392">\pi</script> imported from the <code>math</code> module</a></div><div class="lev3 toc-item"><a href="#A-simple-Monte-Carlo-method" data-toc-modified-id="A-simple-Monte-Carlo-method-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>A simple <a href="https://en.wikipedia.org/wiki/Pi#Monte_Carlo_methods" target="_blank">Monte-Carlo method</a></a></div><div class="lev2 toc-item"><a href="#$100$-first-digits-of-$\pi$" data-toc-modified-id="$100$-first-digits-of-$\pi$-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span><span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-397-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mn>100</mn></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2778" role="math" style="width: 1.92em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.515em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.885em, 1001.49em, 2.792em, -1000em); top: -2.67em; left: 0em;"><span class="mrow" id="MathJax-Span-2779"><span class="mn" id="MathJax-Span-2780" style="font-family: STIXMathJax_Main;">100</span></span><span style="display: inline-block; width: 0px; height: 2.67em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.063em; border-left: 0px solid; width: 0px; height: 0.96em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></span></span><script type="math/tex" id="MathJax-Element-397">100</script> first digits of <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-398-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C0;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2781" role="math" style="width: 0.693em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.541em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.953em, 1000.54em, 2.615em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-2782"><span class="mi" id="MathJax-Span-2783" style="font-family: STIXMathJax_Main; font-style: italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.032em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 0.653em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>π</mi></math></span></span><script type="math/tex" id="MathJax-Element-398">\pi</script></a></div><div class="lev2 toc-item"><a href="#Using-mpmath" data-toc-modified-id="Using-mpmath-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Using <a href="http://mpmath.org/" target="_blank"><code>mpmath</code></a></a></div><div class="lev2 toc-item"><a href="#The-Gauss–Legendre-iterative-algorithm" data-toc-modified-id="The-Gauss–Legendre-iterative-algorithm-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>The Gauss–Legendre iterative algorithm</a></div><div class="lev3 toc-item"><a href="#Using-float-numbers" data-toc-modified-id="Using-float-numbers-241"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Using float numbers</a></div><div class="lev3 toc-item"><a href="#Using-decimal.Decimal-to-improve-precision" data-toc-modified-id="Using-decimal.Decimal-to-improve-precision-242"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Using <code>decimal.Decimal</code> to improve precision</a></div><div class="lev2 toc-item"><a href="#Methods-based-on-a-convergent-series" data-toc-modified-id="Methods-based-on-a-convergent-series-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Methods based on a convergent series</a></div><div class="lev3 toc-item"><a href="#A-Leibniz-formula-(easy):" data-toc-modified-id="A-Leibniz-formula-(easy):-251"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span><a href="https://en.wikipedia.org/wiki/Leibniz_formula_for_pi" target="_blank">A Leibniz formula</a> (<em>easy</em>):</a></div><div class="lev3 toc-item"><a href="#Bailey-Borwein-Plouffe-series-(medium):" data-toc-modified-id="Bailey-Borwein-Plouffe-series-(medium):-252"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span><a href="https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula" target="_blank">Bailey-Borwein-Plouffe series</a> (<em>medium</em>):</a></div><div class="lev3 toc-item"><a href="#Bellard's-formula-(hard):" data-toc-modified-id="Bellard's-formula-(hard):-253"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span><a href="https://en.wikipedia.org/wiki/Bellard%27s_formula" target="_blank">Bellard's formula</a> (<em>hard</em>):</a></div><div class="lev3 toc-item"><a href="#One-Ramanujan's-formula-(hard):" data-toc-modified-id="One-Ramanujan's-formula-(hard):-254"><span class="toc-item-num">2.5.4&nbsp;&nbsp;</span>One <a href="https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Efficient_methods" target="_blank">Ramanujan's formula</a> (<em>hard</em>):</a></div><div class="lev3 toc-item"><a href="#Chudnovsky-brothers'-formula-(hard):" data-toc-modified-id="Chudnovsky-brothers'-formula-(hard):-255"><span class="toc-item-num">2.5.5&nbsp;&nbsp;</span><a href="https://en.wikipedia.org/wiki/Chudnovsky_algorithm" target="_blank">Chudnovsky brothers' formula</a> (<em>hard</em>):</a></div><div class="lev2 toc-item"><a href="#Other-methods" data-toc-modified-id="Other-methods-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Other methods</a></div><div class="lev3 toc-item"><a href="#Trigonometric-methods-(hard)" data-toc-modified-id="Trigonometric-methods-(hard)-261"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Trigonometric methods (<em>hard</em>)</a></div><div class="lev4 toc-item"><a href="#High-precision-arccot-computation" data-toc-modified-id="High-precision-arccot-computation-2611"><span class="toc-item-num">2.6.1.1&nbsp;&nbsp;</span><a href="http://en.literateprograms.org/Pi_with_Machin%27s_formula_%28Python%29#High-precision_arccot_computation" target="_blank">High-precision arccot computation</a></a></div><div class="lev4 toc-item"><a href="#Applying-Machin's-formula" data-toc-modified-id="Applying-Machin's-formula-2612"><span class="toc-item-num">2.6.1.2&nbsp;&nbsp;</span>Applying Machin's formula</a></div><div class="lev4 toc-item"><a href="#Trying-to-solve-my-question!" data-toc-modified-id="Trying-to-solve-my-question!-2613"><span class="toc-item-num">2.6.1.3&nbsp;&nbsp;</span>Trying to solve my question!</a></div><div class="lev4 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-2614"><span class="toc-item-num">2.6.1.4&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#(hard)-Unbounded-Spigot-Algorithm" data-toc-modified-id="(hard)-Unbounded-Spigot-Algorithm-262"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>(<em>hard</em>) <a href="http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf" target="_blank">Unbounded Spigot Algorithm</a></a></div><div class="lev3 toc-item"><a href="#(hard)-Borwein's-algorithm" data-toc-modified-id="(hard)-Borwein's-algorithm-263"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>(<em>hard</em>) <a href="https://en.wikipedia.org/wiki/Borwein%27s_algorithm#Nonic_convergence" target="_blank">Borwein's algorithm</a></a></div><div class="lev2 toc-item"><a href="#Examples-and-references" data-toc-modified-id="Examples-and-references-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Examples and references</a></div><div class="lev3 toc-item"><a href="#Links" data-toc-modified-id="Links-271"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Links</a></div><div class="lev3 toc-item"><a href="#Pie-!" data-toc-modified-id="Pie-!-272"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Pie !</a></div>

# # Python Pi Day 2017
# > This is heavily inspired by what I did two years ago, see this page [cs101/hackhaton/14_03/2015](http://perso.crans.org/besson/cs101/hackathon/14_03_2015) on my website.
# 
# Today is [Pi Day 2017](http://www.piday.org/), the day celebrating the number $\pi$.
# For more details on this number, see [this Wikipedia page](https://en.wikipedia.org/wiki/Pi).
# 
# ----
# 
# Let us use this occasion to showcase a few different approaches to compute the digits of the number $\pi$.
# I will use the [Python](https://www.python.org/) programming language, and you are reading a [Jupyter notebook](https://www.jupyter.org/).
# 
# [![made-with-jupyter](https://img.shields.io/badge/Made%20with-Jupyter-1f425f.svg)](http://jupyter.org/)[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# # Computing a lot of digits of $\pi$?
# 
# - **What to do ?** I will present and implement some methods that can be used to compute the first digits of the irrational number $\pi$.
# - **How ?** One method is based on random numbers, but all the other are simple (or not so simple) iterative algorithm: the more steps you compute, the more digits you will have!
# - **How to compare / assess the result ?** It is simple: the more digits you got, the better. We will also test the different methods implemented, and for the most efficient, see how fast it is to go up-to $140000$ digits.
# 
# The simple goal is to write a *small* function that computes digits of pi, as fast as possible, and find the 10 digits from position 140317 to 140327!
# (that's the challenge I posted on Facebook)

# ----
# ## Two simple methods for finding the first digits of $\pi$
# ### Fraction approximations, and $\pi$ imported from the `math` module

# Three approximations, using fractions, were known from a very long time (Aristote used $\frac{355}{113}$ !).
# The first three approximations of pi are:

# In[3]:


print(" pi ~= 3.14 (two first digits).")
print(" pi ~= 22/7 = {} (two first digits).".format(22.0 / 7.0))
print(" pi ~= 355/113 = {} (six first digits).".format(355.0 / 113.0))


# This method is extremely limited, and will not give you more than 13 correct digits, as `math.pi` is stored as a *float* number (limited precision).

# In[4]:


def mathpi():
    from math import pi
    return pi

print("First method: using math.pi gives pi ~= {:.17f} (17 digits are displayed here).".format(mathpi()))


# If we know the digits, we can directly print them:

# In[5]:


from decimal import Decimal
bigpi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
print("The first 100 digits of pi are {}.".format(bigpi))


# ### A simple [Monte-Carlo method](https://en.wikipedia.org/wiki/Pi#Monte_Carlo_methods)
# A simple Monte Carlo method for computing $\pi$ is to draw a circle inscribed in a square, and randomly place dots in the square.
# The ratio of dots inside the circle to the total number of dots will approximately equal $\pi / 4$, which is also the ratio of the area of the circle by the area of the square:
# 
# ![Example of a random simulation of this Monte-Carlo method](https://upload.wikimedia.org/wikipedia/commons/8/84/Pi_30K.gif "Example of a random simulation of this Monte-Carlo method")
# 
# In Python, such simulation can basically be implemented like this:

# In[6]:


from random import uniform

def montecarlo_pi(nbPoints=10000):
    """Returns a probabilist estimate of pi, as a float number."""
    nbInside = 0
    # we pick a certain number of points (nbPoints)
    for i in range(nbPoints):
        x = uniform(0, 1)
        y = uniform(0, 1)
        # (x, y) is now a random point in the square [0, 1] × [0, 1]
        if (x**2 + y**2) < 1:
            # This point (x, y) is inside the circle C(0, 1)
            nbInside += 1

    return 4 * float(nbInside) / floor(nbPoints)
 


# In[9]:


print("The simple Monte-Carlo method with {} random points gave pi = {}".format(10000, montecarlo_pi(10000)))


# It is an interesting method, but it is just too limited for approximating digits of $\pi$.
# 
# 
# The previous two methods are quite limited, and not efficient enough if you want more than 13 digits (resp. 4 digits for the Monte-Carlo method).

# ## $100$ first digits of $\pi$
# $\pi \simeq 3.1415926535 ~ 8979323846 ~ 2643383279 ~ 5028841971 \\\\ 6939937510 ~ 5820974944 ~ 5923078164 ~ 9862803482 ~ 53421170679$ when computed to the first $100$ digits.
# 
# Can you compute up to $1000$ digits? Up to $10000$ digits? Up to $100000$ digits? **Up to 1 million digits?**

# ## Using [`mpmath`](http://mpmath.org/)
# This is a simple and lazy method, using the [`mpmath`](http://mpmath.org/) module.
# MPmath is a Python library for arbitrary-precision floating-point arithmetic (Multi-Precision), and it has a builtin highly-optimized algorithm to compute digits of $\pi$.
# 
# It works really fine up-to 1000000 digits (56 ms), from 1 million digits to be printed, printing them starts to get too time consuming (the IDE or the system might freeze).

# In[10]:


import mpmath
# from sympy import mpmath  # on older sympy versions
mp = mpmath.mp


# We can [arbitrarily set the precision](http://docs.sympy.org/dev/modules/mpmath/basics.html#setting-the-precision), with the constant `mp.dps` (digit numbers).

# In[11]:


mp.dps = 1000  # number of digits
my_pi = mp.pi  # Gives pi to a thousand places
print("A lazy method using the mpmath module:\npi is approximatly {} (with {} digits).".format(my_pi, mp.dps))


# Let save it for further comparison of simpler methods.

# In[87]:


mp.dps = 100000  # number of digits
len(str(mp.pi))
mpmath_pi = Decimal(str(mp.pi))


# We can solve the initial challenge easily:

# In[86]:


mp.dps = 140330
print(str(mp.pi)[2:][140317:140317+10])


# And it will most probably be the quickest method presented here:

# In[14]:


get_ipython().run_line_magic('timeit', 'mp.dps=140330;print(str(mp.pi)[2:][140317:140317+10])')


# Asking for $10$ times more digits take about $100$ more of time (that's a bad news).

# In[43]:


get_ipython().run_line_magic('timeit', 'mp.dps=1403230;print(str(mp.pi)[2:][1403217:1403217+10])')


# ## The Gauss–Legendre iterative algorithm
# > More details can be found on [this page](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm).
# 
# The first method given here is explained in detail.
# This algorithm is called the [Gauss-Legendre method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm), and for example it was used to compute the first $206 158 430 000$ decimal digits of $\pi$ on September 18th to 20th, $1999$.
# 
# It is a very simply **iterative algorithm** (ie. step by step, you update the variables, as long as you want):
# 
# 1. First, start with 4 variables $a_0, b_0, t_0, p_0$, and their initial values are $a_0 = 1, b_0 = 1/\sqrt{2}, t_0 = 1/4, p_0 = 1$.
# 
# 2. Then, update the variables (or create 4 new ones $a_{n+1}, b_{n+1}, t_{n+1}, p_{n+1}$) by repeating the following instructions (in this order) until the difference of $a_{n}$ and  $b_{n}$, is within the desired accuracy:
#    - $a_{n+1} = \frac{a_n + b_n}{2}$,
#    - $b_{n+1} = \sqrt{a_n \times b_n}$,
#    - $t_{n+1} = t_n - p_n (a_n - a_{n+1})^2$,
#    - $p_{n+1} = 2 p_n$.
# 
# 3. Finally, the desired approximation of $\pi$ is: $$\pi \simeq \frac{(a_{n+1} + b_{n+1})^2}{4 t_{n+1}}.$$

# ### Using float numbers
# The first three iterations give (approximations given up to and including the first incorrect digit):
# 
#     3.140 …
#     3.14159264 …
#     3.1415926535897932382 …
# 
# The algorithm has **second-order convergent nature**, which essentially means that the number of correct digits doubles with each step of the algorithm.
# Try to see how far it can go in less than 120 seconds (print the approximation of $\pi$ after every step, and stop/kill the program after 2 minutes).
# 
# > This method is based on [computing the limits of the arithmetic–geometric mean](https://en.wikipedia.org/wiki/Arithmetic%E2%80%93geometric_mean) of some well-chosen number ([see on Wikipédia for more mathematical details](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm#Mathematical_background)).

# In[17]:


import math

def gauss_legendre_1(max_step):
    """Float number implementation of the Gauss-Legendre algorithm, for max_step steps."""
    a = 1.
    b = 1./math.sqrt(2)
    t = 1./4.0
    p = 1.
    for i in range(max_step):
        at = (a + b) / 2.0
        bt = math.sqrt(a*b)
        tt = t - p*(a-at)**2
        pt = 2.0 * p
        a, b, t, p = at, bt, tt, pt

    my_pi = ((a+b)**2)/(4.0*t)
    return my_pi


# In[89]:


my_pi = gauss_legendre_1(4)
my_pi
print("pi is approximately: {:.15f} (as a float number, precision is limited).".format(my_pi))
accuracy = 100*abs(math.pi - my_pi)/math.pi
print("Accuracy % with math.pi: {:.4g}".format(accuracy))
accuracy = 100*abs(float(mpmath_pi) - my_pi)/float(mpmath_pi)
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[90]:


my_pi = gauss_legendre_1(40)
my_pi
print("pi is approximately: {:.15f} (as a float number, precision is limited).".format(my_pi))
accuracy = 100*abs(math.pi - my_pi)/math.pi
print("Accuracy % with math.pi: {:.4g}".format(accuracy))
accuracy = 100*abs(float(mpmath_pi) - my_pi)/float(mpmath_pi)
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# This first implementation of the Gauss-Legendre algorithm is limited to a precision of 13 or 14 digits. But it converges quickly ! (4 steps here).

# ### Using `decimal.Decimal` to improve precision
# The limitation of this first algorithm came from using simple *float* numbers.
# Let us now use [`Decimal`](https://docs.python.org/3/library/decimal.html) numbers to keep as many digits after the decimal as we need.

# In[24]:


from decimal import Decimal, getcontext


# In[25]:


def gauss_legendre_2(max_step):
    """Decimal number implementation of the Gauss-Legendre algorithm, for max_step steps."""
    # trick to improve precision
    getcontext().prec = 3 + 2**(max_step + 2)

    cst_2 = Decimal(2.0)
    cst_4 = Decimal(4.0)
    a = Decimal(1.0)
    b = Decimal(0.5).sqrt()
    t = Decimal(0.25)
    p = Decimal(1.0)

    for i in range(max_step):
        new_a = (a+b)/cst_2
        new_b = (a*b).sqrt()
        new_t = Decimal(t - p*(a - new_a)**2)
        new_p = cst_2*p

        a, b, t, p = new_a, new_b, new_t, new_p

    my_pi = Decimal(((a+b)**2)/(cst_4*t))
    return my_pi


# In[91]:


my_pi = gauss_legendre_2(5)
print("pi is approximately: {}.".format(my_pi.to_eng_string()[:2**(5+1)]))

accuracy = 100*abs(Decimal(math.pi) - my_pi)/Decimal(math.pi)
print("Accuracy % with math.pi: {:.4g}".format(accuracy))
accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# The second implementation of the Gauss-Legendre algorithm is now working better (when we adapt the precision). And it converges quickly ! (8 steps give a precision upto the 697th digits).
# 
# How much did we lost in term of performance by using decimal numbers? About a factor $1000$, but that's normal as the second solution stores a lot of digits. They don't even compute the same response.

# In[92]:


get_ipython().run_line_magic('timeit', 'gauss_legendre_1(8)')
get_ipython().run_line_magic('timeit', 'gauss_legendre_2(8)')


# ## Methods based on a convergent series
# For the following formulae, you can try to write a program that computes the partial sum of the series, up to a certain number of term ($N \geq 1$).
# Basically, the bigger the $N$, the more digits you get (but the longer the program will run).
# 
# Some methods might be really efficient, only needing a few number of steps (a small $N$) for computing many digits.
# Try to implement and compare at least two of these methods.
# You can use the function `sum` (or `math.fsum`) to compute the sum, or a simple `while`/`for` loop.
# 
# All these partial sums are written up to an integer $N \geq 1$.

# ### [A Leibniz formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_pi) (*easy*):
# It has a number of digits sub-linear in the number $N$ of terms in the sum: we need $10$ times more terms to win just one digit.
# $$\pi \simeq 4\sum_{n=0}^{N} \cfrac {(-1)^n}{2n+1}. $$

# In[30]:


def leibniz(max_step):
    """ Computing an approximation of pi with Leibniz series."""
    my_pi = Decimal(0)
    for k in range(max_step):
        my_pi += Decimal((-1)**k) / Decimal(2*k+1)
    return Decimal(4) * my_pi


# In[98]:


getcontext().prec = 20  # trick to improve precision
my_pi = leibniz(1000)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[99]:


getcontext().prec = 20  # trick to improve precision
my_pi = leibniz(10000)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# This first formula is very inefficient!

# ### [Bailey-Borwein-Plouffe series](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula) (*medium*):
# It also has a number of digits linear in the number $N$ of terms in the sum.
# $$\pi \simeq \sum_{n = 1}^{N} \left( \frac{1}{16^{n}} \left( \frac{4}{8n+1} - \frac{2}{8n+4} - \frac{1}{8n+5} - \frac{1}{8n+6} \right) \right). $$

# In[100]:


def bbp(max_step):
    """ Computing an approximation of pi with Bailey-Borwein-Plouffe series."""
    my_pi = Decimal(0)
    for k in range(max_step):
        my_pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
    return my_pi


# In[101]:


getcontext().prec = 20  # trick to improve precision
my_pi = bbp(10)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# That's pretty impressive, in only $10$ steps!
# But that algorithm is highly dependent on the precision we ask, and on the number of terms in the sum.

# In[102]:


getcontext().prec = 200  # trick to improve precision
my_pi = bbp(200)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[103]:


getcontext().prec = 500  # trick to improve precision
my_pi = bbp(500)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# It is, of course, slower than the optimized algorithm from `mpmath`.
# And it does not scale well with the precision:

# In[104]:


getcontext().prec = 10 + 1000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'bbp(1000)')

getcontext().prec = 10 + 2000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'bbp(2000)')


# ### [Bellard's formula](https://en.wikipedia.org/wiki/Bellard%27s_formula) (*hard*):
# It is a more efficient formula.
# $$\pi \simeq \frac1{2^6} \sum_{n=0}^N \frac{(-1)^n}{2^{10n}} \, \left(-\frac{2^5}{4n+1} - \frac1{4n+3} + \frac{2^8}{10n+1} - \frac{2^6}{10n+3} - \frac{2^2}{10n+5} - \frac{2^2}{10n+7} + \frac1{10n+9} \right). $$

# In[105]:


def bellard(max_step):
    """ Computing an approximation of pi with Bellard series."""
    my_pi = Decimal(0)
    for k in range(max_step):
        my_pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
    return my_pi * Decimal(1.0/(2**6))


# In[106]:


getcontext().prec = 40  # trick to improve precision
my_pi = bellard(10)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# That's pretty impressive, in only $10$ steps!
# But that algorithm is again highly dependent on the precision we ask, and on the number of terms in the sum.

# In[107]:


getcontext().prec = 800  # trick to improve precision
my_pi = bellard(200)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# It is, of course, slower than the optimized algorithm from `mpmath`.
# And it does not scale well with the precision:

# In[73]:


getcontext().prec = 10 + 1000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'bellard(1000)')

getcontext().prec = 10 + 2000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'bellard(2000)')


# It is also slower than BBP formula.

# ### One [Ramanujan's formula](https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Efficient_methods) (*hard*):
# It is efficient but harder to compute easily with high precision, due to the factorial.
# But hopefully, the function `math.factorial` works with Python *integers*, of arbitrary size, so this won't be an issue.
# 
# $$\frac{1}{\pi} \simeq \frac{2\sqrt{2}}{9801} \sum_{n=0}^N \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}. $$
# 
# *Remark:* This method and the next one compute approximation of $\frac{1}{\pi}$, not $\pi$.
# 
# This method has a quadratic precision (the number of correct digits is of the order $\mathcal{O}(N^2)$.

# In[123]:


from math import factorial

def ramanujan(max_step):
    """ Computing an approximation of pi with a Ramanujan's formula."""
    my_pi = Decimal(0)
    d_1103 = Decimal(1103)
    d_26390 = Decimal(26390)
    d_396 = Decimal(396)
    for k in range(max_step):
        my_pi += ((Decimal(factorial(4 * k))) * (d_1103 + d_26390 * Decimal(k))) / ( (Decimal(factorial(k)))**4 * (d_396**(4*k)))
    my_pi = my_pi * 2 * Decimal(2).sqrt() / Decimal(9801)
    my_pi = my_pi**(-1)
    return my_pi


# In[124]:


getcontext().prec = 40  # trick to improve precision
my_pi = ramanujan(4)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[125]:


getcontext().prec = 400  # trick to improve precision
my_pi = ramanujan(40)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[126]:


getcontext().prec = 2000  # trick to improve precision
my_pi = ramanujan(200)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# $1595$ correct digits with $200$ terms, that's quite good!!

# In[127]:


getcontext().prec = 10 + 2000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'ramanujan(200)')

getcontext().prec = 10 + 5000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'ramanujan(400)')


# Let's try to answer my initial question, using this naive implementation.

# In[128]:


get_ipython().run_cell_magic('time', '', 'getcontext().prec = 140350  # trick to improve precision\ni = 140317\nmy_pi = ramanujan(10000)\nprint(str(my_pi)[2:][i:i+10])\n\nmp.dps=140330\nprint(str(mp.pi)[2:][i:i+10])')


# ... It was too slow!

# ### [Chudnovsky brothers' formula](https://en.wikipedia.org/wiki/Chudnovsky_algorithm) (*hard*):
# $$\frac{1}{\pi} \simeq 12 \sum_{n=0}^N \frac {(-1)^{n}(6n)!(545140134n+13591409)}{(3n)!(n!)^{3}640320^{{3n+3/2}}}. $$
# In 2015, the best method is still the Chudnovsky brothers's formula.
# 
# > Be careful when you use these formulae, *check carefully* the constants you wrote (545140134 will work well, 545140135 might not work as well!).
# 
# > This formula is used as the logo of the [French agrégation of Mathematics](https://en.wikipedia.org/wiki/Agr%C3%A9gation) [website `agreg.org`](http://agreg.org/) :
# > ![http://agreg.org/LogoAgreg.gif](http://agreg.org/LogoAgreg.gif)

# In[129]:


from math import factorial

def chudnovsky(max_step):
    """ Computing an approximation of pi with Bellard series."""
    my_pi = Decimal(0)
    for k in range(max_step):
        my_pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
    my_pi = my_pi * Decimal(10005).sqrt()/4270934400
    my_pi = my_pi**(-1)
    return my_pi


# It is very efficient, as Ramanujan's formula.

# In[131]:


getcontext().prec = 3000  # trick to improve precision
my_pi = chudnovsky(200)
my_pi

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# It gets $2834$ correct numbers in $200$ steps!
# It is more efficient that Ramanujan's formula, but slower to compute.

# In[134]:


getcontext().prec = 6000  # trick to improve precision
my_pi = chudnovsky(400)

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# In[135]:


getcontext().prec = 3000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'chudnovsky(200)')

getcontext().prec = 6000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'chudnovsky(400)')


# About $2$ seconds to find correctly the first $5671$ digits? That's slow! But hey, it's Python (dynamic typing etc).

# ----
# ## Other methods

# ### Trigonometric methods (*hard*)
# Some methods are based on the $\mathrm{arccot}$ or $\arctan$ functions, and use the appropriate Taylor series to approximate these functions.
# The best example is [Machin's formula](http://en.literateprograms.org/Pi_with_Machin%27s_formula_%28Python%29):
# $$\pi = 16 \;\mathrm{arccot}(5) - 4 \;\mathrm{arccot}(239).$$
# 
# And we use the Taylor series to approximate $\mathrm{arccot}(x)$:
# $$\mathrm{arccot}(x) = \frac{1}{x} - \frac{1}{3x^3} + \frac{1}{5x^5} - \frac{1}{7x^7} + \dots = \sum_{n=0}^{+\infty} \frac{(-1)^n}{(2n+1) x^{2n+1}} .$$
# 
# This method is also explained here with some details.
# In order to obtain $n$ digits, we will use *fixed-point* arithmetic to compute $\pi \times 10^n$ as a Python `long` integer.

# #### [High-precision arccot computation](http://en.literateprograms.org/Pi_with_Machin%27s_formula_%28Python%29#High-precision_arccot_computation)
# To calculate $\mathrm{arccot}$ of an argument $x$, we start by dividing the number $1$ (represented by $10^n$, which we provide as the argument `unity`) by $x$ to obtain the first term.
# 
# We then repeatedly divide by $x^2$ and a counter value that runs over $3$, $5$, $7$ etc, to obtain each next term.
# The summation is stopped at the first zero `term`, which in this *fixed-point* representation corresponds to a real value less than $10^{-n}$:
# 
# ```python
# def arccot(x, unity):
#     xpower = unity / x
#     sum = xpower
#     n = 3
#     sign = -1
#     while True:
#         xpower = xpower / (x*x)
#         term = xpower / n
#         if term == 0:
#             break  # we are done
#         sum += sign * term
#         sign = -sign
#         n += 2
#     return sum
# ```

# Adapting it to use Decimal numbers is easy:

# In[171]:


def arccot(x, unity):
    """Compute arccot(x) with a certain level of precision."""
    x = Decimal(x)
    unity = Decimal(unity)
    mysum = xpower = unity / x
    n = 3
    sign = -1
    while True:
        xpower = xpower / (x*x)
        term = xpower / n
        if not term:
            break
        mysum += sign * term
        sign = -sign  # we alternate the sign
        n += 2
    return mysum


# #### Applying Machin's formula
# Finally, the main function uses Machin's formula to compute $\pi$ using the necessary level of precision, by using this high precision $\mathrm{arccot}$ function:
# $$\pi = 16 \;\mathrm{arccot}(5) - 4 \;\mathrm{arccot}(239).$$
# 
# ```python
# def machin(digits):
#     unity = 10**(digits + 10)
#     pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
#     return pi / unity
# ```
# 
# To avoid rounding errors in the result, we use 10 guard digits internally during the calculation.
# We may now reproduce the historical result obtained by [Machin in 1706](https://en.wikipedia.org/wiki/John_Machin).

# In[172]:


def machin(digits):
    """Compute pi with Machin's formula, with precision at least digits."""
    unity = 10**(digits + 10)
    my_pi = Decimal(4) * (Decimal(4)*arccot(5, unity) - arccot(239, unity))
    return my_pi / Decimal(unity)


# In[173]:


getcontext().prec = 10000  # trick to improve precision
my_pi = machin(100)

accuracy = 100*abs(mpmath_pi - my_pi)/mpmath_pi
print("Accuracy % with mpmath_pi: {:.4g}".format(accuracy))


# So we got the first $9995$ digits correctly... in $45$ seconds.
# That will still be too slow to have the digits at position $130317$.

# In[174]:


getcontext().prec = 5000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'machin(50)')

getcontext().prec = 10000  # trick to improve precision
get_ipython().run_line_magic('timeit', 'machin(100)')


# The program can be used to compute tens of thousands of digits in just a few seconds on a modern computer.
# Typical implementation will be in highly efficient compiled language; like C or maybe Julia.
# 
# Many [Machin-like formulas](https://en.wikipedia.org/wiki/Machin-like_formula) also exist, like:
# $$\pi = 4\arctan\left(\frac{1}{2}\right) + 4 \arctan\left(\frac{1}{3}\right).$$

# #### Trying to solve my question!
# The important parameter to tune is not the precision given to `machin()` but the `Decimal.prec` precision.

# In[179]:


get_ipython().run_cell_magic('time', '', 'i = 14031\ngetcontext().prec = i + 20  # trick to improve precision\nmp.dps = i + 20\nprint(str(mp.pi)[2:][i:i+10])\n\nmy_pi = machin(11)\nprint(str(my_pi)[2:][i:i+10])')


# In[180]:


get_ipython().run_cell_magic('time', '', 'i = 140317\ngetcontext().prec = i + 20  # trick to improve precision\nmp.dps = i + 20\nprint(str(mp.pi)[2:][i:i+10])\n\nmy_pi = machin(50)\nprint(str(my_pi)[2:][i:i+10])')


# It was too slow too! But at least it worked!
# 
# My manual implementation of Machin's formula took about $10$ minutes, on an old laptop with $1$ core running Python 3.5, to find the $10$ digits of $\pi$ at index $140317$.
# 
# #### Conclusion
# $\implies$ To the question "What are the $10$ digits of $\pi$ at index $140317..140326$", the answer is $9341076406$.

# For more, see http://fredrikj.net/blog/2011/03/100-mpmath-one-liners-for-pi/.

# ### (*hard*) [Unbounded Spigot Algorithm](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf)
# This algorithm is quite efficient, but not easy to explain. Go check on-line if you want.
# 
# See this page (http://codepad.org/3yDnw0n9) for a 1-line C program that uses a simpler Spigot algorithm for computing the first 15000 digits
# 
# A nice method, with a generator yielding the next digit each time, comes from http://stackoverflow.com/a/9005163.
# It uses only integer, so no need to do any `Decimal` trick here.

# In[149]:


def next_pi_digit(max_step):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(max_step):
        if 4 * q + r - t < m * t:
            yield m
            # More details on Python generators can be found here http://stackoverflow.com/a/231855
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


# In[161]:


def generator_pi(max_step):
    big_str = ''.join(str(d) for d in next_pi_digit(max_step))
    return Decimal(big_str[0] + '.' + big_str[1:])


# It does not use `Decimal` numbers.

# In[164]:


getcontext().prec = 50  # trick to improve precision
generator_pi(1000)


# In[165]:


getcontext().prec = 5000  # trick to improve precision
generator_pi(1000)


# ### (*hard*) [Borwein's algorithm](https://en.wikipedia.org/wiki/Borwein%27s_algorithm#Nonic_convergence)
# It has several versions, one with a cubic convergence (each new step multiplies by $3$ the number of digits), one with a nonic convergence (of order $9$) etc.
# They are not so easy to explain either.
# Please check on-line, here [en.WikiPedia.org/wiki/Borwein's_algorithm](https://en.wikipedia.org/wiki/Borwein%27s_algorithm).
# 
# The cubic method is similar to the Gauss-Legendre algorithm:
# 
# 1. Start with $a_0 = 1/3$, and $s_0 = \frac{\sqrt{3}-1}{2}$,
# 2. And then iterate, as much as you want, by defining $r_{k+1} = \frac{3}{1+2(1-s_k^3)^{1/3}}$, and updating $s_{k+1} = \frac{r_{k+1}-1}{2}$ and $a_{k+1} = r_{k+1}^2 a_k - 3^k (r_{k+1}^2 - 1)$.
# 
# Then the numbers $a_k$ will converge to $\frac{1}{\pi}$.

# ----
# ## Examples and references
# ### Links
# - [en.WikiPedia.org/wiki/Pi#Modern_quest_for_more_digits](https://en.wikipedia.org/wiki/Pi#Modern_quest_for_more_digits),
# - [www.JoyOfPi.com/pi.html](http://www.joyofpi.com/pi.html) and [www.JoyOfPi.com/pilinks.html](http://www.joyofpi.com/pilinks.html),
# - [www.EveAndersson.com/pi/digits/](http://www.eveandersson.com/pi/digits/) has great interactive tools,
# - more crazy stuff [MathWorld.Wolfram.com/PiDigits.html](http://mathworld.wolfram.com/PiDigits.html), or [MathWorld.Wolfram.com/Pi.html](http://mathworld.wolfram.com/Pi.html),
# - [one idea with Fibonacci numbers](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibpi.html#section2),
# - [and this incredibly long list of digits](http://piworld.calico.jp/estart.html) at [PiWorld.calico.jp/estart.html](http://piworld.calico.jp/estart.html).
# - http://bellard.org/pi/ by Francois Bellard (and http://bellard.org/pi/pi_n2/pi_n2.html)

# > That's it for today! Happy Pi Day!

# ----
# ### Pie !
# ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Apple_pie.jpg/600px-Apple_pie.jpg)
# 
# ----
