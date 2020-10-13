#!/usr/bin/env python
# coding: utf-8

# # A tiny regex challenge solved without another regex
# 
# This notebook presents a small challenge a friend of mine asked me (in Python).
# I'll write Python code valid for versions $\geq$ 3.6, and to show of I use the [`typing`](https://docs.python.org/3/library/typing.html) module to have type hints.

# In[4]:


import sys
print(sys.version)


# In[5]:


from typing import List, Tuple

Position = int
Interval = Tuple[Position, Position]


# ## Introduction: the problem a friend of mine asked me

# In[2]:


import re


# In[6]:


def bad_events(pattern: str, string: str) -> List[Interval]:
    # m.span(1) = (m.start(1), m.end(1))
    return [m.span(1) for m in re.finditer(f"(?=({pattern}))", string)]

pat = "aca"
strng = "acacavcacabacacbbacacazdbacaca"

# Do you know if there is a regex trick to obtain
# [(0, 5), (7, 10), (11, 14), (17, 22), (25, 30)]
# instead of
bad_events(pat, strng)
# [(0, 3), (2, 5), (7, 10), (11, 14), (17, 20), (19, 22), (25, 28), (27, 30)]
# ?


# ## The solution I came up with
# 
# Let's write a simple function that will read this list of intervals, and compress the ones that are not disjoint.
# 
# For instance, when reading `[(0, 3), (2, 5)]`, the second interval is not disjoint from the first one, so both can be compressed to `(0, 5)`, which is disjoint from the next one `(7, 10)`.

# - Let's test (in constant time wrt $n$ number of intervals) if two consecutive intervals are disjoint or not:

# In[11]:


def are_not_disjoint(interval1: Interval, interval2: Interval) -> bool:
    x1, y1 = interval1
    assert x1 <= y1, f"Error: interval = {intervals1} is not a valid interval."
    x2, y2 = interval2
    assert x2 <= y2, f"Error: interval = {intervals2} is not a valid interval."
    if x1 <= x2 <= y1 <= y2:   # interval1 finishes in interval2
        return True
    elif x2 <= x1 <= y2 <= y1: # interval2 finishes in interval1
        return True
    elif x1 <= x2 <= y2 <= y1: # interval2 is included in interval1
        return True
    elif x2 <= x1 <= y1 <= y2: # interval1 is included in interval2
        return True
    return False


# In[14]:


assert are_not_disjoint((0, 3), (2, 5))  # True
assert not are_not_disjoint((0, 5), (7, 10))  # False


# - Let's compute the union of two consecutive intervals, if they are not disjoint: (again in constant time)

# In[7]:


def union_intervals(interval1: Interval, interval2: Interval) -> bool:
    x1, y1 = interval1
    assert x1 <= y1, f"Error: interval = {intervals1} is not a valid interval."
    x2, y2 = interval2
    assert x2 <= y2, f"Error: interval = {intervals2} is not a valid interval."
    return (min(x1, x2), max(y1, y2))


# In[8]:


union_intervals((0, 3), (2, 5))


# - And now we are reading to compress the list of intervals (in linear time):

# In[28]:


def compress_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals_after_compression: List[Interval] = []
    n = len(intervals)
    assert n > 0
    current_interval = intervals[0]   # eg (0, 3)
    i = 1
    # as long as we can read another interval in the list
    while i < n:  # ==> O(n) as the inside of the loop is O(1)
        next_interval = intervals[i]  # eg (2, 5)
        if are_not_disjoint(current_interval, next_interval):
            # eg (0, 3) and (2, 5) -> (0, 5)
            current_interval = union_intervals(current_interval, next_interval)
        else:
            # eg (0, 5) and (7, 10) -> (0, 5) is added,
            intervals_after_compression.append(current_interval)
            # and current_interval = next_interval = (7, 10)
            current_interval = next_interval
        i += 1
    # we add the last current interval if it was not yet added
    if current_interval not in intervals_after_compression:
        intervals_after_compression.append(current_interval)
    return intervals_after_compression


# - Example:

# In[29]:


# Do you know if there is a regex trick to obtain
# [(0, 5), (7, 10), (11, 14), (17, 22), (25, 30)]
# instead of
intervals = bad_events(pat, strng)
print(intervals)
# [(0, 3), (2, 5), (7, 10), (11, 14), (17, 20), (19, 22), (25, 28), (27, 30)]
# ?


# In[26]:


compress_intervals(intervals)


# - So now we can write the requested function:

# In[30]:


def bad_events_compressed(pat: str, strng: str) -> List[Interval]:
    intervals1 = bad_events(pat, strng)
    intervals2 = compress_intervals(intervals1)
    return intervals2


# In[32]:


def test(pat: str, strng: str) -> None:
    print(f"For pattern {pat} and string {strng}, the bad events uncompressed are:\n{bad_events(pat, strng)}\nand the bad events compressed are:\n{bad_events_compressed(pat, strng)}")


# In[33]:


test(pat, strng)


# ## Other examples

# In[34]:


test("acab", "acabacabacabacacavcacabacacbbacacazdbacacaacacavcacabacacbbacacazdbacacaacabacab")


# In[35]:


test("merci", "mercimerciderienmercimerki")


# ## Conclusion
# It was fun!
# 
# > See [GitHub.com/Naereen/notebooks](https://github.com/Naereen/notebooks/) for other notebooks!
# > This one and all the others I wrote are open-source [under the MIT License](https://lbesson.mit-license.org/).
