
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#&quot;Living-in-a-noisy-world...&quot;,-using-James-Powell's-(dutc)-rwatch-module" data-toc-modified-id="&quot;Living-in-a-noisy-world...&quot;,-using-James-Powell's-(dutc)-rwatch-module-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><em>"Living in a noisy world..."</em>, using James Powell's (<code>dutc</code>) <code>rwatch</code> module</a></div><div class="lev2 toc-item"><a href="#Requirements-and-links" data-toc-modified-id="Requirements-and-links-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Requirements and links</a></div><div class="lev2 toc-item"><a href="#Defining-a-debugging-context-manager,-just-to-try" data-toc-modified-id="Defining-a-debugging-context-manager,-just-to-try-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Defining a debugging context manager, just to try</a></div><div class="lev3 toc-item"><a href="#Watching-just-one-object" data-toc-modified-id="Watching-just-one-object-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Watching just one object</a></div><div class="lev3 toc-item"><a href="#Can-we-delete-the-rwatch-?" data-toc-modified-id="Can-we-delete-the-rwatch-?-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Can we delete the <code>rwatch</code> ?</a></div><div class="lev3 toc-item"><a href="#More-useful-debuggin-information" data-toc-modified-id="More-useful-debuggin-information-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>More useful debuggin information</a></div><div class="lev3 toc-item"><a href="#Watching-any-object" data-toc-modified-id="Watching-any-object-124"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Watching <em>any</em> object</a></div><div class="lev3 toc-item"><a href="#A-first-context-manager-to-have-debugging-for-one-object" data-toc-modified-id="A-first-context-manager-to-have-debugging-for-one-object-125"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>A first context manager to have debugging for <em>one</em> object</a></div><div class="lev3 toc-item"><a href="#A-second-context-manager-to-debug-any-object" data-toc-modified-id="A-second-context-manager-to-debug-any-object-126"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>A second context manager to debug <em>any</em> object</a></div><div class="lev2 toc-item"><a href="#Defining-a-context-manager-to-add-white-noise" data-toc-modified-id="Defining-a-context-manager-to-add-white-noise-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Defining a context manager to add white noise</a></div><div class="lev3 toc-item"><a href="#Capturing-any-numerical-value" data-toc-modified-id="Capturing-any-numerical-value-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Capturing any numerical value</a></div><div class="lev3 toc-item"><a href="#Adding-a-white-noise-for-numbers" data-toc-modified-id="Adding-a-white-noise-for-numbers-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Adding a white noise for numbers</a></div><div class="lev3 toc-item"><a href="#WhiteNoiseComplex-context-manager" data-toc-modified-id="WhiteNoiseComplex-context-manager-133"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span><code>WhiteNoiseComplex</code> context manager</a></div><div class="lev2 toc-item"><a href="#Defining-a-generic-noisy-context-manager" data-toc-modified-id="Defining-a-generic-noisy-context-manager-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Defining a generic <code>noisy</code> context manager</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></div>

# # *"Living in a noisy world..."*, using James Powell's (`dutc`) `rwatch` module
# 
# Goal : I want to write a [context manager](https://docs.python.org/3.5/library/stdtypes.html#typecontextmanager) for [Python 3.5+](https://www.Python.org/), so that inside the context manager, every number is seen noisy (with a white Gaussian noise, for instance).
# 
# > It will be like being drunk, except that your it will be my Python interpretor and not me !
# 
# For instance, I will like to have this feature:

# ```python
# >>> x = 120193
# >>> print(x)
# 120193
# >>> np.random.seed(1234)
# >>> with WhiteNoise():
# >>>    print(x)
# 120193.47143516373249306
# ```

# ----
# ## Requirements and links

# First, we will need [numpy](https://docs.scipy.org/doc/numpy/user/whatisnumpy.html) to have some random number generator, as `numpy.random.normal` to have some 1D Gaussian noise.

# In[1]:


import numpy as np


# In[2]:


np.random.seed(1234)
np.random.normal()


# Then, the core part will be to install and import [James Powell (`dutc`)](https://github.com/dutc/) [`rwatch`](https://github.com/dutc/rwatch) module.
# If you don't have it installed :
# 
# 1. Be sure to have CPython 3.5. `rwatch` patches the CPython eval loop, so it's fixed to specific versions of Python & the author lazy about keeping it updated.
# 2. Then `pip install dutc-rwatch`. It should work, but it fails for me.
# 3. (alternative) You can just `cd /tmp/ && git clone https://github.com/dutc/rwatch && cd rwatch/src/ && make` and copy the `rwatch.so` dynamic library wherever you need...

# In[5]:


get_ipython().run_cell_magic('bash', '', 'tmpdir=$(mktemp -d)\ncd $tmpdir\ngit clone https://github.com/dutc/rwatch\ncd rwatch/src/\nmake\nls -larth ./rwatch.so\nfile ./rwatch.so\n# cp ./rwatch.so /where/ver/you/need/  # ~/publis/notebook/ for me')


# Anyhow, if `rwatch` is installed, we can import it, and it enables two new functions in the `sys` module:

# In[6]:


import rwatch
from sys import setrwatch, getrwatch

setrwatch({})  # clean any previously installed rwatch
getrwatch()


# Finally, we need the [`collections`](https://docs.python.org/3/library/collections.html) module and its [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) magical datastructure.

# In[7]:


from collections import defaultdict


# ----
# ## Defining a debugging context manager, just to try
# 
# This is the first example given in [James presentation]() at PyCon Canada 2016.
# 
# We will first define and add a `rwatch` for just one object, let say a variable `x`, and then for any object using `defaultdict`.
# From there, writing a context manager that enables this feature only locally is easy.

# ### Watching just one object
# 1. Write the function, that needs two argument `frame, obj`, and should return `obj`,
# 2. Install it...
# 3. Check it!

# In[15]:


def basic_view(frame, obj):
    print("Python saw the object {} from frame {}".format(obj, frame))
    return obj


# In[16]:


x = "I am alive!"


# In[17]:


setrwatch({
    id(x): basic_view
})


# In[18]:


print(x)


# That's awesome, it works!

# ### Can we delete the `rwatch` ?
# Sure!

# In[19]:


def delrwatch(idobj):
    getrwatch().pop(idobj, None)


# In[20]:


print(x)
delrwatch(id(x))
print(x)  # no more rwatch on this!
print(x)  # no more rwatch on this!


# We can also delete rwatches that are not defined, without a failure:

# In[21]:


y = "I am Zorro !"
print(y)
delrwatch(y)  # No issue!
print(y)


# ### More useful debuggin information
# What is this `frame` thing?
# It is described in the documentation of the [`inspect`](https://docs.python.org/3/library/inspect.html) module.
# 
# We can actually use it to display some useful information about the object and where was it called etc.

# In[22]:


from inspect import getframeinfo

def debug_view(frame, obj):
    info = getframeinfo(frame)
    msg = '- Access to {!r} (@{}) at {}:{}:{}'
    print(msg.format(obj, hex(id(obj)), info.filename, info.lineno, info.function))
    return obj


# In[23]:


setrwatch({})
setrwatch({
    id(x): debug_view
})
getrwatch()


# In[24]:


print(x)


# That can be quite useful!

# ### Watching *any* object
# We can actually pass a `defaultdict` to the `setrwatch` function, so that *any* object will have a rwatch!
# 
# > **Warning**: obviously, this will crazily slowdown your interpreter!
# 
# So let be cautious, and only deal with strings here.
# 
# But I want to be safe, so it will only works if the frame indicate that the variable does not come from a file.

# In[25]:


setrwatch({})


# In[26]:


def debug_view_for_str(frame, obj):
    if isinstance(obj, str):
        info = getframeinfo(frame)
        if '<stdin>' in info.filename or '<ipython-' in info.filename:
            msg = '- Access to {!r} (@{}) at {}:{}:{}'
            print(msg.format(obj, hex(id(obj)), info.filename, info.lineno, info.function))
    return obj


# In[27]:


setrwatch(defaultdict(lambda: debug_view_for_str))


# In[28]:


print(x)


# Clearly, there is a lot of strings involved, mainly because this is a notebook and not the simple Python interpreter, so filtering on the `info.filename` as I did was smart.

# In[29]:


setrwatch({})


# But obviously, having this for all objects is incredibly verbose!

# In[30]:


def debug_view_for_any_object(frame, obj):
    info = getframeinfo(frame)
    if '<stdin>' in info.filename or '<ipython-' in info.filename:
        msg = '- Access to {!r} (@{}) at {}:{}:{}'
        print(msg.format(obj, hex(id(obj)), info.filename, info.lineno, info.function))
    return obj


# Let check that one, on a very simple example (which runs in less than `20` micro seconds):

# In[52]:


print(x)
get_ipython().run_line_magic('time', '123 + 134')


# In[53]:


setrwatch({})
setrwatch(defaultdict(lambda: debug_view_for_any_object))
print(x)
get_ipython().run_line_magic('time', '123 + 134')
setrwatch({})


# It seems to work very well!
# 
# But it slows down everything, obviously the filtering takes time (for *every* object!)
# Computing `123 + 134 = 257` took about `10` miliseconds! That's just CRAZY!

# ### A first context manager to have debugging for *one* object
# 
# It would be nice to be able to turn on and off this debugging tool whenever you want.
# 
# Well, it turns out that [context managers](https://docs.python.org/3.5/library/stdtypes.html#typecontextmanager) are exactly meant for that!
# They are simple classes with just a `__enter__()` and `__exit__()` special methods.
# 
# First, let us write a context manager to debug ONE object.

# In[54]:


class InspectThisObject(object):
    def __init__(self, obj):
        self.idobj = id(obj)
    
    def __enter__(self):
        getrwatch()[self.idobj] = debug_view

    def __exit__(self, exc_type, exc_val, exc_tb):
        delrwatch(self.idobj)


# We can check it:

# In[55]:


z = "I am Batman!"
print(z)

with InspectThisObject(z):
    print(z)

print(z)


# The first debug information shows line 5, which is the line where `print(z)` is.

# ### A second context manager to debug *any* object
# Easy:

# In[56]:


class InspectAllObjects(object):
    def __init__(self):
        pass

    def __enter__(self):
        setrwatch(defaultdict(lambda: debug_view_for_any_object))

    def __exit__(self, exc_type, exc_val, exc_tb):
        setrwatch({})


# It will probably break everything in the notebook, but works in a basic Python interpreter.

# In[57]:


with InspectAllObjects():
    print(0)


# The 5th debug information printed is `Access to 0 (@0xXXX) at <ipython-input-41-XXX>:2:<module>`, showing the access in line `#2` of the constant `0`.

# In[58]:


with InspectAllObjects():
    print("Darth Vader -- No Luke, I am your Father!")
    print("Luke -- I have a father? Yay! Let's eat cookies together!")


# We also see here the `None` and `{}` objects being given to the context manager (see the `__enter__` method at first, and `__exit__` at the end).

# ----
# ## Defining a context manager to add white noise
# 
# Basically, we will do as above, but instead of debug information, a white noise sampled from a Normal distribution (i.e., $\sim \mathcal{N}(0, 1)$) will be *added* to any number.

# ### Capturing any numerical value
# To capture both integers and float numbers, the [`numbers.Number`](https://docs.python.org/2/library/numbers.html#numbers.Number) abstract class is useful.

# In[59]:


from numbers import Number


# ### Adding a white noise for numbers
# This is very simple.
# 
# But I want to be safe, so it will only works if the frame indicate that the number does not come from a file, as previously.

# In[60]:


def add_white_noise_to_numbers(frame, obj):
    if isinstance(obj, Number):
        info = getframeinfo(frame)
        if '<stdin>' in info.filename or '<ipython-' in info.filename:
            return obj + np.random.normal()
    return obj


# Let us try it out!

# In[63]:


np.random.seed(1234)
setrwatch({})
x = 1234
print(x)
getrwatch()[id(x)] = add_white_noise_to_numbers
print(x)  # huhoww, that's noisy!
print(10 * x + x + x**2)  # and noise propagate!
setrwatch({})
print(x)
print(10 * x + x + x**2)


# It seems to work!
# Let's do it for any number then...
# 
# ... Sadly, it's actually breaking the interpreter, which obviously has to have access to non-noisy constants and numbers to work !
# 
# We can lower the risk by only adding noise to *complex* numbers.
# I guess the interpreter doesn't need complex numbers, write?

# In[64]:


def add_white_noise_to_complex(frame, obj):
    if isinstance(obj, complex):
        info = getframeinfo(frame)
        if '<stdin>' in info.filename or '<ipython-' in info.filename:
            return obj + np.random.normal() + np.random.normal() * 1j
    return obj


# In[65]:


np.random.seed(1234)
setrwatch({})
y = 1234j
print(y)
setrwatch(defaultdict(lambda: add_white_noise_to_complex))
print(y)  # huhoww, that's noisy!
setrwatch({})
print(y)


# Awesome!
# 
# > « Now, the real world is non noisy, but the complex one is! »
# 
# That's one sentence I thought I would never say!

# ### `WhiteNoiseComplex` context manager
# 
# To stay cautious, I only add noise to complex numbers.

# In[67]:


class WhiteNoiseComplex(object):
    def __init__(self):
        pass

    def __enter__(self):
        setrwatch(defaultdict(lambda: add_white_noise_to_complex))

    def __exit__(self, exc_type, exc_val, exc_tb):
        setrwatch({})


# And it works as expected:

# In[69]:


np.random.seed(120193)
print(120193, 120193j)
with WhiteNoiseComplex():
    print(120193, 120193j)  # Huhoo, noisy!
print(120193, 120193j)

print(0*1j)
with WhiteNoiseComplex():
    print(0*1j)  # Huhoo, noisy!
print(0*1j)


# ----
# ## Defining a generic `noisy` context manager
# 
# This will be a very simple change from the previous one, by letting the `Noisy` class accept *any* noisy function, which takes `obj` and return a noisy version of `obj`, only for complex-valued objects.

# In[71]:


class Noisy(object):
    def __init__(self, noise):
        def add_white_noise_to_complex(frame, obj):
            if isinstance(obj, complex):
                info = getframeinfo(frame)
                if '<stdin>' in info.filename or '<ipython-' in info.filename:
                    return noise(obj)
            return obj

        self.rwatch = add_white_noise_to_complex

    def __enter__(self):
        setrwatch(defaultdict(lambda: self.rwatch))

    def __exit__(self, exc_type, exc_val, exc_tb):
        setrwatch({})


# In[73]:


print(1j)
with Noisy(lambda obj: obj + np.random.normal()):
    print(1j)
print(1j)


# In[74]:


print(1j)
with Noisy(lambda obj: obj * np.random.normal()):
    print(1j)
print(1j)


# In[75]:


print(1j)
with Noisy(lambda obj: obj + np.random.normal(10, 0.1) + np.random.normal(10, 0.1) * 1j):
    print(1j)
print(1j)


# ----
# ## Conclusion
# Clearly, that was a BAD idea, and not so useful.
# 
# But it was interesting!
# 
# I don't have any idea of a context where this could be useful, but still!
