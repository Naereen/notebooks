
# coding: utf-8

# # Generating permutations, several approaches with Python
# 
# This small notebook implements, in [Python 3](https://docs.python.org/3/), several algorithms aiming at a simple task:
# given a certain list, generate *all* the [permutations](https://en.wikipedia.org/wiki/Permutation) of the list.
# 
# For instance, for `[1, 2]`, it should give `[1, 2]` and `[2, 1]`.
# 
# ## References
# - [This blog post, doing a similar job but in OCaml](http://typeocaml.com/2015/05/05/permutation/),
# - [The documentation for itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations).
# 
# ## About
# - *Date:* 06/02/2017.
# - *Author:* [Lilian Besson](https://GitHub.com/Naereen), (C) 2017.
# - *Licence:* [MIT Licence](http://lbesson.mit-license.org).
# 
# ----

# > This notebook should be compatible with both Python versions, [2](https://docs.python.org/2/) and [3](https://docs.python.org/3/).

# In[2]:


from __future__ import print_function, division  # Python 2 compatibility if needed


# ----
# # 1. Reference implementation: from `itertools`
# 
# The [`itertools`](https://docs.python.org/3/library/itertools.html) module, from the Python standard library, contains a function [`itertools.permutation`](https://docs.python.org/3/library/itertools.html#itertools.permutations):

# In[3]:


# Builtin implementation, as a reference
from itertools import permutations as itertools_permutations


# This will obviously be the quickest implementation, and there is no hope of beating it with pure Python (in terms of computational speed), as it is written in C and not in Python.
# 
# Let's check that it works as wanted:

# In[4]:


itertools_permutations([1, 2])


# What's that weird result? In fact, `itertools.permutations()` does not return the *list* of all permutations, but rather an *iterator*.
# It can be looped on in a similar way, and can be converted to a list easily:

# In[5]:


for p in itertools_permutations([1, 2]):
    print(p)

list(itertools_permutations([1, 2, 3]))


# So, what's the advantage of returning an *iterator* and not a list of lists? **Memory and time efficiency** !
# 
# The $n!$ permutations (if the list is of size $n$) take both a lot of time to compute and a lot of memory to store, so it's very clever if we can generate one after another, on demand, instead of having to compute all of them and storing them.
# 
# The first two algorithms presented below are not iterators, but the last one will be.

# > Permutations of the list are given as tuples, but there is no difference.

# We can check how quick is this first function:

# In[13]:


get_ipython().run_line_magic('time', 'len(list(itertools_permutations(list(range(4)))))')
get_ipython().run_line_magic('time', 'len(list(itertools_permutations(list(range(8)))))')
get_ipython().run_line_magic('time', 'len(list(itertools_permutations(list(range(9)))))')


# In[15]:


get_ipython().run_line_magic('timeit', 'len(list(itertools_permutations(list(range(10)))))')


# There is $n!$ permutations to generate, so obviously any algorithm is running in $\Omega(n!)$ time to generate all of them, and that is approximately the behavior observed above.
# 
# > This claim should need better measurements to be really empirically supported!

# ----
# # 2. First algorithm : The insert-into-all-positions solution
# 
# The basic idea is to separate the first element $x$ of the list, and the rest $xs$.
# 
# - For instance, for $l = [1, 2, 3]$, $x = 1$ and $xs = [2, 3]$.
# - Then the permutations of $l$ are obtained by inserting $x$ in every possible positions of every permutations of $xs$.
# - Here, the permutations of $xs$ are $[2, 3]$ and $[3, 2]$. Inserting $x = 1$ in the first one give $[1, 2, 3]$ (first position), $[2, 1, 3]$ and $[2, 3, 1]$. Similarly, we obtain the last permutations: $[1, 3, 2]$, $[3, 1, 2]$ and $[3, 2, 1]$.
# 
# So we first need a function that insert an element $x$ in every possible index of a list $l$.

# In[16]:


def ins_all_positions(x, l):
    """Return a list of lists obtained from l by inserting x at every possible index."""
    res = []
    for i in range(0, len(l) + 1):
        res.append(l[:i] + [x] + l[i:])
    return res


# Then we write a recursive function, following the description of the algorithm:

# In[21]:


from functools import reduce
# reduce(lambda acc, p: acc + f(p), l, []) is the same as the concatenation of list f(p) for p in l


# In[22]:


# Now the main permutations generator.
def first_permutations(iterable):
    """Second algorithm, insert-into-all-positions solution."""
    if len(iterable) == 0:
        return []
    # we must specify this edge case
    elif len(iterable) == 1:
        return [[iterable[0]]]
    else:
        x, xs = iterable[0], iterable[1:]
        # reduce is needed instead of a simple sum(...) as sum() only works for numerical values
        return reduce(lambda acc, p: acc + ins_all_positions(x, p), first_permutations(xs), [])


# We can try it out, but only on small list as it is *not efficient*.

# In[23]:


first_permutations([1, 2, 3])


# And let's measure its efficiency on small lists of size $4,5,6,7,8$:

# In[35]:


get_ipython().run_line_magic('time', 'len(list(first_permutations(list(range(4)))))')
get_ipython().run_line_magic('time', 'len(list(first_permutations(list(range(5)))))')
get_ipython().run_line_magic('time', 'len(list(first_permutations(list(range(6)))))')
get_ipython().run_line_magic('time', 'len(list(first_permutations(list(range(7)))))')
get_ipython().run_line_magic('time', 'len(list(first_permutations(list(range(8)))))')


# $\implies$ This implementation take about $8 s$ for a list with $n = 8$ elements: **it's crazily slow!**

# ----
# # 3. Second algorithm : The fixed-head solution
# 
# The second algorithm will not be more efficient, but it is different in his design.
# 
# Instead of inserting an element at every possible index, this second algorithm rather generate the permutations by considering that every element of the list will be the head of some of the permutation.
# 
# With a fixed head, ie an element $x$, removed from the list $xs = l \setminus x$, permutations of $l$ are obtained by simply adding $x$ as the head of every permutation of $xs$.
# 
# As for the first algorithm, this one is also recursive.
# 
# One limitation of its simple implementation below is that it requires all elements in the list to be different, as it will compute the list $xs = l \setminus x$ with this very simple function `rm(x, l)` :

# In[30]:


def rm(x, l):
    """List l without element x."""
    return [y for y in l if x != y]


# > Note that with comparisons on indexes instead of comparisons on values, we could treat the general case not much harder.
# 
# Then, we need, as before, a function to add $x$ as the head of all lists $p$ in a certain list of lists $l$.

# In[31]:


def head_of_all(x, l):
    """List of lists from l where x is the head of all the lists."""
    return [[x] + p for p in l]


# And finally, the fixed-head algorithm is easy to implement, as a recursive function.
# - The case of en empty list or a list with only one element are easy,
# - The recursion case uses, again, a call to `reduce(fun acc, x: acc + f(x), list, [])` to permforms the concatenation of all lists `f(x)` for `x` in `l`.

# In[32]:


def second_permutations(iterable):
    """Second algorithm, fixed-head solution."""
    if len(iterable) == 0:
        return []
    # we must specify this edge case
    elif len(iterable) == 1:
        return [[iterable[0]]]
    else:
        return reduce(lambda acc, x: acc + head_of_all(x, second_permutations(rm(x, iterable))), iterable, [])


# Let's try it out:

# In[36]:


second_permutations([1, 2, 3])


# And let's measure its efficiency on small lists of size $4,5,6,7,8$:

# In[38]:


get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(4)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(5)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(6)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(7)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(8)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(9)))))')


# $\implies$ this second algorithm is more efficient, as it requires only $0.6 s$ to generate the $8! = 40320$ different permutations of the list $[0, 1, 2, 3, 4, 5, 6, 7]$.

# In[40]:


from math import factorial
factorial(8)


# ----
# # 3. Third algorithm : the Johnson-Trotter algorithm
# 
# This algorithm is more complicated to explain, I will let you refer to [its Wikipedia page](https://en.wikipedia.org/wiki/Johnson-Trotter), or for more details, [this blog post](http://typeocaml.com/2015/05/05/permutation/).
# 
# We use simple values to denote directions, `left` or `right`:

# In[41]:


left = False
right = True


# We will need a first function to attach a direction to every element of an array `t`, and then to remove them.

# In[51]:


def attach_direction(t, d=left):
    """Attach the direction d to all elements of array t."""
    return [(x, d) for x in t]


# In[43]:


def remove_direction(t):
    """Remove the attached direction d to all elements of array t."""
    return [y for y, _ in t]


# This classical function `swap(t, i, j)` exchange the position of the elements `t[i]` and `t[j]`:

# In[44]:


def swap(t, i, j):
    """Swap t[i] and t[j] in array t."""
    t[i], t[j] = t[j], t[i]


# We first need to know if the element `a[i]` can be moved, according to its attached direction, to the left or right.
# The rule is that an element can only be swapped to a **small** element.

# In[45]:


def is_movable(a, i):
    """Can a[i] be moved?"""
    x, d = a[i]
    if d == left:
        return i > 0 and x > a[i - 1][0]
    elif d == right:
        return i < len(a) - 1 and x > a[i + 1][0]
    else:
        raise ValueError("unknown direction d = {}".format(d))


# Then the function `move(a, i)` simply swaps `a[i]` to the left or right, if it is possible.
# 
# It raises a `ValueError` exception if it cannot swap, to be general, but of course the algorithm will never be in such a undesirable state.

# In[46]:


def move(a, i):
    """Move it if possible."""
    x, d = a[i]
    if is_movable(a, i):
        if d == left:
            swap(a, i, i - 1)
        elif d == right:
            swap(a, i, i + 1)
        else:
            raise ValueError("unknown direction d = {}".format(d))
    else:
        raise ValueError("not movable")


# Then we need a function to scan the array `a`, from its beginning, to find the largest movable element.
# This can cost upto a time of $O(n)$ (if $n = \#a$), but it could hardly be improved.

# In[47]:


def scan_largest_movable(a):
    """Find the largest movable element."""
    def aux(acc, i):
        if i >= len(a):
            return acc
        else:
            if not is_movable(a, i):
                return aux(acc, i + 1)
            else:
                x, _ = a[i]
                if acc is None:
                    return aux(i, i + 1)
                else:
                    j = acc if x < a[acc][0] else i
                    return aux(j, i + 1)
    return aux(None, 0)


# Directions will be flipped, alternating `left` and `right`, with `flip(d)`:

# In[52]:


def flip(d):
    """Flip direction d : left -> right, right -> left"""
    return not d


# Then the list will need to be scanned, and flip the directions of all elements larger than some `x`:

# In[49]:


def scan_flip_larger(x, a):
    """Scan to flip larger."""
    for i, (y, d) in enumerate(a):
        if y > x:
            a[i] = y, flip(d)


# We finally have all the pieces needed to implement the Johnson-Trotter algorithm:

# In[50]:


def third_permutations(iterable):
    """Third algorithm, Johnson-Trotter algorithm."""
    i = sorted(list(iterable))  # Required by the algorithm
    # We attach directions, and we will only use the array a
    a = attach_direction(i)
    # First permutation
    r = list(iterable)[:]
    while True:
        yield r[:]  # A copy of the current permutation is yielded
        i = scan_largest_movable(a)
        if i is None:  # No more permutation!
            raise StopIteration
        else:
            x, _ = a[i]
            move(a, i)
            scan_flip_larger(x, a)
            # The next permutation should not have direction information attached to it
            r = remove_direction(a)


# Yeay, we finally have an **iterator** on permutations of a list, instead of generating all of them.
# 
# Let's try it out:

# In[53]:


third_permutations([1, 2, 3])


# In[54]:


list(third_permutations([1, 2, 3]))


# And let's measure its efficiency on small lists of size $4,5,6,7,8$:

# In[55]:


get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(4)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(5)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(6)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(7)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(8)))))')
get_ipython().run_line_magic('time', 'len(list(second_permutations(list(range(9)))))')


# $\implies$ the Johnson-Trotter algorithm is, as expected, quicker than the previous naive implementations, but it's still pretty slow compared to the reference implementation [`itertools.permutation`](https://docs.python.org/3/library/itertools.html#itertools.permutations).

# ----
# # 4. Comparing our Johnson-Trotter implementation and `itertools.permutation`
# 
# To compare them fairly, we need to run them several times:

# In[63]:


get_ipython().run_line_magic('timeit', 'len(list(itertools_permutations([1, 2, 3])))')
get_ipython().run_line_magic('timeit', 'len(list(third_permutations([1, 2, 3])))')


# In[64]:


get_ipython().run_line_magic('timeit', 'len(list(itertools_permutations([1, 2, 3, 4, 5])))')
get_ipython().run_line_magic('timeit', 'len(list(third_permutations([1, 2, 3, 4, 5])))')


# However, [IPython](http://ipython.org/)'s `%timeit` function warns us that `itertools.permutation` *could* use caching, and that could bias the result.
# 
# One easy way to remove any caching is to test on different input lists, and that can be done, for instance, with random lists.

# In[61]:


from numpy.random import choice

def random_list_of_size_n(n=5, N=1000):
    return list(choice(list(range(1, N + 1)), size=n, replace=False))

random_list_of_size_n(5)


# In[65]:


get_ipython().run_line_magic('timeit', 'len(list(itertools_permutations(random_list_of_size_n(5))))')
get_ipython().run_line_magic('timeit', 'len(list(third_permutations(random_list_of_size_n(5))))')


# In[66]:


get_ipython().run_line_magic('timeit', 'len(list(itertools_permutations(random_list_of_size_n(6))))')
get_ipython().run_line_magic('timeit', 'len(list(third_permutations(random_list_of_size_n(6))))')


# ----
# # 5. Testing our $3$ implementations
# 
# Additionnally to comparing the speed efficiency, we would also like to simply check that all the functions we wrote are working as expected!

# In[72]:


def test(list_of_f, iterable):
    """ Test that all functions in list_of_f give the same list of permutation on this iterable."""
    print("Testing for the list of functions {} ...".format([f.__name__ for f in list_of_f]))  # DEBUG
    result = True
    print("Testing for the iterable {} ...".format(iterable))  # DEBUG
    i = iterable
    allperms = []
    for f in list_of_f:
        allperms.append(sorted([list(p) for p in f(iterable)]))
    for i, pi in enumerate(allperms):
        for j in range(i + 1, len(allperms)):
            pj = allperms[j]
            if pi != pj:
                print(" - Function #{} ({.__name__}) gave a different list of permutations as function #{} ({.__name__}) ...".format(i, list_of_f[i], j, list_of_f[j]))  # DEBUG
                result = False
            else:
                print(" - Function #{} ({.__name__}) gave the same list of permutations as function #{} ({.__name__}) ...".format(i, list_of_f[i], j, list_of_f[j]))  # DEBUG
    return result


# We will test and compare the reference implementation, `itertools.permutation`, with the three other implementations given above.

# In[73]:


list_of_f = [itertools_permutations, first_permutations, second_permutations, third_permutations]


# In[74]:


iterable = [1, 2, 3]
test(list_of_f, iterable)


# In[75]:


iterable = [1, 2, 3, 4, 5]
test(list_of_f, iterable)


# In[76]:


iterable = [1, 2, 3, 4, 5, 6]
test(list_of_f, iterable)


# ----
# > That's it for today, folks!
# 
# - If you want to read more about permutations and algorithms *to generate them all*, [this page is very helpful](https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations),
# - But if you want to find *one ring to rule them all*, [Bilbo is the guy to ask to](http://www.lmgtfy.com/?q=one%20ring%20to%20rule%20them%20all).
# 
# More notebooks can be found on [my GitHub page](https://GitHub.com/Naereen/notebooks).
