
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Manual-implementation-of-some-hash-functions" data-toc-modified-id="Manual-implementation-of-some-hash-functions-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Manual implementation of some hash functions</a></div><div class="lev2 toc-item"><a href="#What-is-a-hash-function?" data-toc-modified-id="What-is-a-hash-function?-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What is a hash function?</a></div><div class="lev2 toc-item"><a href="#Common-API-for-the-different-classes" data-toc-modified-id="Common-API-for-the-different-classes-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Common API for the different classes</a></div><div class="lev2 toc-item"><a href="#Checking-the-the-hashlib-module-in-Python-standard-library" data-toc-modified-id="Checking-the-the-hashlib-module-in-Python-standard-library-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Checking the <a href="https://docs.python.org/3/library/hashlib.html" target="_blank">the <code>hashlib</code> module in Python standard library</a></a></div><div class="lev2 toc-item"><a href="#First-stupid-example:-a-stupid-hashing-function" data-toc-modified-id="First-stupid-example:-a-stupid-hashing-function-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>First stupid example: a stupid hashing function</a></div><div class="lev2 toc-item"><a href="#First-real-example:-the-MD5-hashing-function" data-toc-modified-id="First-real-example:-the-MD5-hashing-function-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>First real example: the MD5 hashing function</a></div><div class="lev3 toc-item"><a href="#Useful-functions-for-the-MD5-algorithm" data-toc-modified-id="Useful-functions-for-the-MD5-algorithm-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Useful functions for the MD5 algorithm</a></div><div class="lev3 toc-item"><a href="#The-MD5-class" data-toc-modified-id="The-MD5-class-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>The <code>MD5</code> class</a></div><div class="lev3 toc-item"><a href="#First-check-on-MD5" data-toc-modified-id="First-check-on-MD5-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>First check on MD5</a></div><div class="lev3 toc-item"><a href="#A-less-stupid-check-on-MD5" data-toc-modified-id="A-less-stupid-check-on-MD5-154"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>A less stupid check on MD5</a></div><div class="lev3 toc-item"><a href="#Trying-1000-random-examples" data-toc-modified-id="Trying-1000-random-examples-155"><span class="toc-item-num">1.5.5&nbsp;&nbsp;</span>Trying 1000 random examples</a></div><div class="lev2 toc-item"><a href="#Second-real-example:-the-SHA-1-hashing-function" data-toc-modified-id="Second-real-example:-the-SHA-1-hashing-function-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Second real example: the SHA-1 hashing function</a></div><div class="lev3 toc-item"><a href="#Useful-functions-the-SHA-1-algorithm" data-toc-modified-id="Useful-functions-the-SHA-1-algorithm-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Useful functions the SHA-1 algorithm</a></div><div class="lev3 toc-item"><a href="#The-SHA1-class" data-toc-modified-id="The-SHA1-class-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>The <code>SHA1</code> class</a></div><div class="lev3 toc-item"><a href="#First-check-on-SHA-1" data-toc-modified-id="First-check-on-SHA-1-163"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>First check on SHA-1</a></div><div class="lev3 toc-item"><a href="#A-less-stupid-check-on-SHA-1" data-toc-modified-id="A-less-stupid-check-on-SHA-1-164"><span class="toc-item-num">1.6.4&nbsp;&nbsp;</span>A less stupid check on SHA-1</a></div><div class="lev3 toc-item"><a href="#Trying-1000-random-examples" data-toc-modified-id="Trying-1000-random-examples-165"><span class="toc-item-num">1.6.5&nbsp;&nbsp;</span>Trying 1000 random examples</a></div><div class="lev2 toc-item"><a href="#Third-real-example:-the-SHA-2-hashing-function" data-toc-modified-id="Third-real-example:-the-SHA-2-hashing-function-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Third real example: the SHA-2 hashing function</a></div><div class="lev3 toc-item"><a href="#Useful-functions-the-SHA-2-algorithm" data-toc-modified-id="Useful-functions-the-SHA-2-algorithm-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Useful functions the SHA-2 algorithm</a></div><div class="lev3 toc-item"><a href="#The-SHA2-class" data-toc-modified-id="The-SHA2-class-172"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>The <code>SHA2</code> class</a></div><div class="lev3 toc-item"><a href="#First-check-on-SHA-2" data-toc-modified-id="First-check-on-SHA-2-173"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>First check on SHA-2</a></div><div class="lev3 toc-item"><a href="#Check-on-SHA-2" data-toc-modified-id="Check-on-SHA-2-174"><span class="toc-item-num">1.7.4&nbsp;&nbsp;</span>Check on SHA-2</a></div><div class="lev3 toc-item"><a href="#Trying-1000-random-examples" data-toc-modified-id="Trying-1000-random-examples-175"><span class="toc-item-num">1.7.5&nbsp;&nbsp;</span>Trying 1000 random examples</a></div><div class="lev2 toc-item"><a href="#Comparison-:-MD5-vs-SHA-1-vs-SHA-2" data-toc-modified-id="Comparison-:-MD5-vs-SHA-1-vs-SHA-2-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Comparison : MD5 vs SHA-1 vs SHA-2</a></div><div class="lev2 toc-item"><a href="#Bonus-:-SHA-2-variants" data-toc-modified-id="Bonus-:-SHA-2-variants-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Bonus : SHA-2 variants</a></div><div class="lev3 toc-item"><a href="#SHA-224" data-toc-modified-id="SHA-224-191"><span class="toc-item-num">1.9.1&nbsp;&nbsp;</span>SHA-224</a></div><div class="lev4 toc-item"><a href="#The-SHA224-class" data-toc-modified-id="The-SHA224-class-1911"><span class="toc-item-num">1.9.1.1&nbsp;&nbsp;</span>The <code>SHA224</code> class</a></div><div class="lev4 toc-item"><a href="#Checks-on-SHA-224" data-toc-modified-id="Checks-on-SHA-224-1912"><span class="toc-item-num">1.9.1.2&nbsp;&nbsp;</span>Checks on SHA-224</a></div><div class="lev3 toc-item"><a href="#SHA-512" data-toc-modified-id="SHA-512-192"><span class="toc-item-num">1.9.2&nbsp;&nbsp;</span>SHA-512</a></div><div class="lev4 toc-item"><a href="#Useful-functions-the-SHA-512-algorithm" data-toc-modified-id="Useful-functions-the-SHA-512-algorithm-1921"><span class="toc-item-num">1.9.2.1&nbsp;&nbsp;</span>Useful functions the SHA-512 algorithm</a></div><div class="lev4 toc-item"><a href="#The-SHA512-class" data-toc-modified-id="The-SHA512-class-1922"><span class="toc-item-num">1.9.2.2&nbsp;&nbsp;</span>The <code>SHA512</code> class</a></div><div class="lev4 toc-item"><a href="#Checks-on-SHA-512" data-toc-modified-id="Checks-on-SHA-512-1923"><span class="toc-item-num">1.9.2.3&nbsp;&nbsp;</span>Checks on SHA-512</a></div><div class="lev3 toc-item"><a href="#SHA-384" data-toc-modified-id="SHA-384-193"><span class="toc-item-num">1.9.3&nbsp;&nbsp;</span>SHA-384</a></div><div class="lev4 toc-item"><a href="#The-SHA384-class" data-toc-modified-id="The-SHA384-class-1931"><span class="toc-item-num">1.9.3.1&nbsp;&nbsp;</span>The <code>SHA384</code> class</a></div><div class="lev4 toc-item"><a href="#Checks-on-SHA-384" data-toc-modified-id="Checks-on-SHA-384-1932"><span class="toc-item-num">1.9.3.2&nbsp;&nbsp;</span>Checks on SHA-384</a></div><div class="lev3 toc-item"><a href="#More-comparison" data-toc-modified-id="More-comparison-194"><span class="toc-item-num">1.9.4&nbsp;&nbsp;</span>More comparison</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Bonus" data-toc-modified-id="Bonus-1101"><span class="toc-item-num">1.10.1&nbsp;&nbsp;</span>Bonus</a></div>

# # Manual implementation of some hash functions
# 
# This small [Jupyter notebook](https://www.Jupyter.org/) is a short experiment, to see if I can implement the some basic [Hashing functions](https://en.wikipedia.org/wiki/Hash_function), more specifically [cryptographic hashing functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function), like `MD5`, `SHA1`, `SHA256`, `SHA512` etc
# 
# And then I want compare my manual implementations with the functions implemented in [the `hashlib` module in Python standard library](https://docs.python.org/3/library/hashlib.html).
# Ideally, my implementation should work exactly like the reference one, only slower!
# 
# 
# - *Reference*: Wikipedia pages on [Hash functions](https://en.wikipedia.org/wiki/Hash_function), [MD5](https://en.wikipedia.org/wiki/MD5), [SHA-1](https://en.wikipedia.org/wiki/SHA1) and [SHA-2](https://en.wikipedia.org/wiki/SHA-2), as well as [the `hashlib` module in Python standard library](https://docs.python.org/3/library/hashlib.html).
# - *Date*: 13 May 2017 (first part about MD5), 19 June 2017 (second part about SHA-1), 19 June 2017 (last part about SHA-2).
# - *Author*: [Lilian Besson](https://GitHub.com/Naereen/notebooks).
# - *License*: [MIT Licensed](https://LBesson.MIT-License.org/).

# ----
# ## What is a hash function?
# > TL;DR : [Hash functions](https://en.wikipedia.org/wiki/Hash_function) and [cryptographic hashing functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function) on Wikipedia.

# ----
# ## Common API for the different classes
# 
# I will copy the API proposed by [the `hashlib` module in Python standard library](https://docs.python.org/3/library/hashlib.html), so it will be very easy to compare my implementations with the one provided with your default [Python](https://www.Python.org/) installation.

# In[1]:


class Hash(object):
    """ Common class for all hash methods.
    
    It copies the one of the hashlib module (https://docs.python.org/3.5/library/hashlib.html).
    """
    
    def __init__(self, *args, **kwargs):
        """ Create the Hash object."""
        self.name = self.__class__.__name__  # https://docs.python.org/3.5/library/hashlib.html#hashlib.hash.name
        self.byteorder   = 'little'
        self.digest_size = 0                # https://docs.python.org/3.5/library/hashlib.html#hashlib.hash.digest_size
        self.block_size  = 0                # https://docs.python.org/3.5/library/hashlib.html#hashlib.hash.block_size

    def __str__(self):
        return self.name
        
    def update(self, arg):
        """ Update the hash object with the object arg, which must be interpretable as a buffer of bytes."""
        pass

    def digest(self):
        """ Return the digest of the data passed to the update() method so far. This is a bytes object of size digest_size which may contain bytes in the whole range from 0 to 255."""
        return b""

    def hexdigest(self):
        """ Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments."""
        digest = self.digest()
        raw = digest.to_bytes(self.digest_size, byteorder=self.byteorder)
        format_str = '{:0' + str(2 * self.digest_size) + 'x}'
        return format_str.format(int.from_bytes(raw, byteorder='big'))


# ----
# ## Checking the [the `hashlib` module in Python standard library](https://docs.python.org/3/library/hashlib.html)

# In[2]:


import hashlib


# We can check [the available algorithms](https://docs.python.org/3.5/library/hashlib.html#hashlib.algorithms_available), some of them being [guaranteed to be on any platform](https://docs.python.org/3.5/library/hashlib.html#hashlib.algorithms_guaranteed), some are not.

# In[3]:


list(hashlib.algorithms_available)


# I will need at least these ones:

# In[4]:


assert 'MD5' in hashlib.algorithms_available
assert 'SHA1' in hashlib.algorithms_available
assert 'SHA256' in hashlib.algorithms_available
assert 'SHA224' in hashlib.algorithms_available
assert 'SHA512' in hashlib.algorithms_available
assert 'SHA384' in hashlib.algorithms_available


# Lets check that they have the block size and digest size announced:

# In[5]:


for name, s in zip(
        ('MD5', 'SHA1', 'SHA256', 'SHA224', 'SHA512', 'SHA384'),
        (hashlib.md5(), hashlib.sha1(), hashlib.sha256(), hashlib.sha224(), hashlib.sha512(), hashlib.sha384())
    ):
    print("For {:<8} : the block size is {:<3} and the digest size is {:<2}.".format(name, s.block_size, s.digest_size))


# ----
# ## First stupid example: a stupid hashing function
# 
# This "stupid" hashing function will use `digest_size` of 128 bytes (= 16 bits), and compute it by ... just looking at the first 128 bytes of the input data.
# 
# This is just to check the API and how to read from a bytes buffer.

# In[6]:


class HeaderHash(Hash):
    """ This "stupid" hashing function will use `digest_size` of 128 bytes, and compute it by ... just looking at the first 128 bytes of the input data.
    """
    
    def __init__(self):
        # Common part
        self.digest_size = 16
        self.block_size  = 16
        self.name = "Header"
        # Specific part
        self._data = b""

    def update(self, arg):
        """ Update the hash object with the object arg, which must be interpretable as a buffer of bytes."""
        if len(self._data) == 0:
            self._data = arg[:self.block_size]

    def digest(self):
        """ Return the digest of the data passed to the update() method so far. This is a bytes object of size digest_size which may contain bytes in the whole range from 0 to 255."""
        return self._data


# Let us try it:

# In[7]:


h1 = HeaderHash()


# In[8]:


h1
print(h1)


# Let us use some toy data, to test here and after.

# In[9]:


data = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 100


# In[10]:


h1.update(data)
h1.digest()


# > Well... It seems to work, even if this first example is stupid.

# ----
# ## First real example: the MD5 hashing function
# Let start with a simple one: [the MD5 hashing function](https://en.wikipedia.org/wiki/MD5), from Rivest in 1992.
# 
# <center><span style="font-size: large; color: red;"><b>Warning</b>: it is considered broken since at least 2012, never use it for security purposes.</span></center>

# ### Useful functions for the MD5 algorithm
# Instead of writing the complete MD5 algorithm in the class below, I preferred to define here some useful functions, using [Bitwise operators](https://wiki.python.org/moin/BitwiseOperators).

# In[11]:


def MD5_f1(b, c, d):
    """ First ternary bitwise operation."""
    return ((b & c) | ((~b) & d)) & 0xFFFFFFFF

def MD5_f2(b, c, d):
    """ Second ternary bitwise operation."""
    return ((b & d) | (c & (~d))) & 0xFFFFFFFF

def MD5_f3(b, c, d):
    """ Third ternary bitwise operation."""
    return (b ^ c ^ d) & 0xFFFFFFFF

def MD5_f4(b, c, d):
    """ Forth ternary bitwise operation."""
    return (c ^ (b | (~d))) & 0xFFFFFFFF


# In[12]:


def leftrotate(x, c):
    """ Left rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF


# In[13]:


def leftshift(x, c):
    """ Left shift the number x by c bytes."""
    return x << c


# In[14]:


from math import floor, sin


# ### The `MD5` class

# It is a direct implementation of the pseudo-code, as given for instance on the Wikipedia page, or the original research article by Rivest.

# In[15]:


class MD5(Hash):
    """MD5 hashing, see https://en.wikipedia.org/wiki/MD5#Algorithm."""
    
    def __init__(self):
        self.name        = "MD5"
        self.byteorder   = 'little'
        self.block_size  = 64
        self.digest_size = 16
        # Internal data
        s = [0] * 64
        K = [0] * 64
        # Initialize s, s specifies the per-round shift amounts
        s[ 0:16] = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
        s[16:32] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
        s[32:48] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
        s[48:64] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
        # Store it
        self._s = s
        # Use binary integer part of the sines of integers (Radians) as constants:
        for i in range(64):
            K[i] = floor(2**32 * abs(sin(i + 1))) & 0xFFFFFFFF
        # Store it
        self._K = K
        # Initialize variables:
        a0 = 0x67452301   # A
        b0 = 0xefcdab89   # B
        c0 = 0x98badcfe   # C
        d0 = 0x10325476   # D
        self.hash_pieces = [a0, b0, c0, d0]
    
    def update(self, arg):
        s, K = self._s, self._K
        a0, b0, c0, d0 = self.hash_pieces
        # 1. Pre-processing
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 448 (mod 512)
        while len(data) % 64 != 56:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 64) to message
        data += orig_len_in_bits.to_bytes(8, byteorder='little')
        assert len(data) % 64 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 512-bit = 64-bytes chunks:
        for offset in range(0, len(data), 64):
            # 2.a. 512-bits = 64-bytes chunks
            chunks = data[offset : offset + 64]
            # 2.b. Break chunk into sixteen 32-bit = 4-bytes words M[j], 0 ≤ j ≤ 15
            A, B, C, D = a0, b0, c0, d0
            # 2.c. Main loop
            for i in range(64):
                if 0 <= i <= 15:
                    F = MD5_f1(B, C, D)
                    g = i
                elif 16 <= i <= 31:
                    F = MD5_f2(B, C, D)
                    g = (5 * i + 1) % 16
                elif 32 <= i <= 47:
                    F = MD5_f3(B, C, D)
                    g = (3 * i + 5) % 16
                elif 48 <= i <= 63:
                    F = MD5_f4(B, C, D)
                    g = (7 * i) % 16
                # Be wary of the below definitions of A, B, C, D
                to_rotate = (A + F + K[i] + int.from_bytes(chunks[4*g : 4*g+4], byteorder='little')) & 0xFFFFFFFF
                new_B = (B + leftrotate(to_rotate, s[i])) & 0xFFFFFFFF
                A, B, C, D = D, new_B, B, C
            # Add this chunk's hash to result so far:
            a0 = (a0 + A) & 0xFFFFFFFF
            b0 = (b0 + B) & 0xFFFFFFFF
            c0 = (c0 + C) & 0xFFFFFFFF
            d0 = (d0 + D) & 0xFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [a0, b0, c0, d0]

    def digest(self):
        return sum(leftshift(x, (32 * i)) for i, x in enumerate(self.hash_pieces))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[16]:


def hash_MD5(data):
    """ Shortcut function to directly receive the hex digest from MD5(data)."""
    h = MD5()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# <div style="text-align:right;"><blockquote> *Note:* [This page helped for debugging](https://rosettacode.org/wiki/MD5/Implementation#Python).</blockquote></div>

# ### First check on MD5
# 
# Let us try it:

# In[17]:


h2 = MD5()
h2
print(h2)


# In[18]:


h2.update(data)
h2.digest()


# In[19]:


h2.hexdigest()


# ### A less stupid check on MD5
# 
# Let try the example from [MD5 Wikipedia page](https://en.wikipedia.org/wiki/MD5#MD5_hashes) :

# In[20]:


hash_MD5("The quick brown fox jumps over the lazy dog")
assert hash_MD5("The quick brown fox jumps over the lazy dog") == '9e107d9d372bb6826bd81d3542a419d6'


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period to the end of the sentence:

# In[21]:


hash_MD5("The quick brown fox jumps over the lazy dog.")
assert hash_MD5("The quick brown fox jumps over the lazy dog.") == 'e4d909c290d0fb1ca068ffaddf22cbd0'


# The hash of the zero-length string is:

# In[22]:


hash_MD5("")
assert hash_MD5("") == 'd41d8cd98f00b204e9800998ecf8427e'


# $\implies$ We obtained the same result, OK our function works!

# ### Trying 1000 random examples
# On a small sentence:

# In[23]:


hash_MD5("My name is Zorro !")


# In[24]:


h = hashlib.md5()
h.update(b"My name is Zorro !")
h.hexdigest()


# It starts to look good.

# In[25]:


def true_hash_MD5(data):
    h = hashlib.md5()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# On some random data:

# In[26]:


import numpy.random as nr
alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_string(size=10000):
    return ''.join(alphabets[nr.randint(len(alphabets))] for _ in range(size))


# In[27]:


random_string(10)


# In[28]:


from tqdm import tqdm_notebook as tqdm


# In[29]:


get_ipython().run_cell_magic('time', '', 'for _ in tqdm(range(1000)):\n    x = random_string()\n    assert hash_MD5(x) == true_hash_MD5(x), "Error: x = {} gave two different MD5 hashes: my implementation = {} != hashlib implementation = {}...".format(x, hash_MD5(x), true_hash_MD5(x))')


# ----
# ## Second real example: the SHA-1 hashing function

# Let now study and implement another hashing function, slightly harder to write but more secure: SHA1, "Secure Hash Algorithm, version 1".
# See [the SHA1 hashing function](https://en.wikipedia.org/wiki/SHA-1) on Wikipedia, if needed.
# 
# <center><span style="font-size: large; color: red;"><b>Warning</b>: it is considered broken since at least 2011, it is not advised to use it for real security purposes. SHA-2 or SHA-3 is better advised.</span></center>
# 
# For instance, see [this nice blog post](https://konklone.com/post/why-google-is-hurrying-the-web-to-kill-sha-1).

# ### Useful functions the SHA-1 algorithm

# Pretty similar to the ones used for the MD5 algorithm.

# In[30]:


def SHA1_f1(b, c, d):
    """ First ternary bitwise operation."""
    return ((b & c) | ((~b) & d)) & 0xFFFFFFFF

def SHA1_f2(b, c, d):
    """ Second ternary bitwise operation."""
    return (b ^ c ^ d) & 0xFFFFFFFF

def SHA1_f3(b, c, d):
    """ Third ternary bitwise operation."""
    return ((b & c) | (b & d) | (c & d) ) & 0xFFFFFFFF

def SHA1_f4(b, c, d):
    """ Forth ternary bitwise operation, = SHA1_f1."""
    return (b ^ c ^ d) & 0xFFFFFFFF


# This is exactly like for MD5.

# In[31]:


def leftrotate(x, c):
    """ Left rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF


# As SHA-1 plays with big-endian and little-endian integers, and at the end it requires a leftshift to combine the 5 hash pieces into one.

# In[32]:


def leftshift(x, c):
    """ Left shift the number x by c bytes."""
    return x << c


# ### The `SHA1` class
# 
# I will use a simple class, very similar to the class used for the MD5 algorithm (see above).
# It is a direct implementation of the pseudo-code, as given for instance on the Wikipedia page.

# In[33]:


class SHA1(Hash):
    """SHA1 hashing, see https://en.wikipedia.org/wiki/SHA-1#Algorithm."""
    
    def __init__(self):
        self.name        = "SHA1"
        self.byteorder   = 'big'
        self.block_size  = 64
        self.digest_size = 20
        # Initialize variables
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0
        # Store them
        self.hash_pieces = [h0, h1, h2, h3, h4]
    
    def update(self, arg):
        h0, h1, h2, h3, h4 = self.hash_pieces
        # 1. Pre-processing, exactly like MD5
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 448 (mod 512)
        while len(data) % 64 != 56:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 64) to message
        data += orig_len_in_bits.to_bytes(8, byteorder='big')
        assert len(data) % 64 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 512-bit = 64-bytes chunks:
        for offset in range(0, len(data), 64):
            # 2.a. 512-bits = 64-bytes chunks
            chunks = data[offset : offset + 64]
            w = [0 for i in range(80)]
            # 2.b. Break chunk into sixteen 32-bit = 4-bytes words w[i], 0 ≤ i ≤ 15
            for i in range(16):
                w[i] = int.from_bytes(chunks[4*i : 4*i + 4], byteorder='big')
            # 2.c. Extend the sixteen 32-bit words into eighty 32-bit words
            for i in range(16, 80):
                w[i] = leftrotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)
            # 2.d. Initialize hash value for this chunk
            a, b, c, d, e = h0, h1, h2, h3, h4
            # 2.e. Main loop, cf. http://www.faqs.org/rfcs/rfc3174.html
            for i in range(80):
                if 0 <= i <= 19 :
                    f = SHA1_f1(b, c, d)
                    k = 0x5A827999
                elif 20 <= i <= 39 :
                    f = SHA1_f2(b, c, d)
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59 :
                    f = SHA1_f3(b, c, d)
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79 :
                    f = SHA1_f4(b, c, d)
                    k = 0xCA62C1D6

                new_a = leftrotate(a, 5) + f + e + k + w[i] & 0xFFFFFFFF
                new_c = leftrotate(b, 30)
                # Rotate the 5 variables
                a, b, c, d, e = new_a, a, new_c, c, d

            # Add this chunk's hash to result so far:
            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [h0, h1, h2, h3, h4]

    def digest(self):
        return sum(leftshift(x, 32 * i) for i, x in enumerate(self.hash_pieces[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[34]:


def hash_SHA1(data):
    """ Shortcut function to directly receive the hex digest from SHA1(data)."""
    h = SHA1()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# ### First check on SHA-1
# 
# Let us try it:

# In[35]:


h3 = SHA1()
h3
print(h3)


# In[36]:


h3.update(data)
h3.digest()


# In[37]:


digest = h3.digest()
bin(digest)
len(bin(digest))


# In[38]:


h3.hexdigest()


# ### A less stupid check on SHA-1
# 
# Let try the example from [SHA-1 Wikipedia page](https://en.wikipedia.org/wiki/SHA-1#SHA-1_hashes) :

# In[39]:


hash_SHA1("The quick brown fox jumps over the lazy dog")
assert hash_SHA1("The quick brown fox jumps over the lazy dog") == '2fd4e1c67a2d28fced849ee1bb76e7391b93eb12'


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, changing one letter in the sentence:

# In[40]:


hash_SHA1("The quick brown fox jumps over the lazy cog")
assert hash_SHA1("The quick brown fox jumps over the lazy cog") == 'de9f2c7fd25e1b3afad3e85a0bd17d9b100db4b3'


# The hash of the zero-length string is:

# In[41]:


hash_SHA1("")
assert hash_SHA1("") == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'


# $\implies$ We obtained the same result, OK our function works!

# ### Trying 1000 random examples
# On a small sentence:

# In[42]:


hash_SHA1("My name is Zorro !")


# In[43]:


h = hashlib.sha1()
h.update(b"My name is Zorro !")
h.hexdigest()


# It starts to look good.

# In[44]:


def true_hash_SHA1(data):
    h = hashlib.sha1()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# On some random data:

# In[45]:


random_string(10)


# In[46]:


from tqdm import tqdm_notebook as tqdm


# In[47]:


get_ipython().run_cell_magic('time', '', 'for _ in tqdm(range(1000)):\n    x = random_string()\n    assert hash_SHA1(x) == true_hash_SHA1(x), "Error: x = {} gave two different SHA1 hashes: my implementation = {} != hashlib implementation = {}...".format(x, hash_SHA1(x), true_hash_SHA1(x))')


# ----
# ## Third real example: the SHA-2 hashing function

# Let now study and implement a last hashing function, again slightly harder to write but more secure: SHA-2, "Secure Hash Algorithm, version 2".
# See [the SHA-2 hashing function](https://en.wikipedia.org/wiki/SHA-2) on Wikipedia, if needed.
# 
# <center><span style="font-size: large; color: green;"><i>Remark</i>: it is not (yet) considered broken, and it is the military standard for security and cryptographic hashing. SHA-3 is preferred for security purposes.</span></center>

# ### Useful functions the SHA-2 algorithm

# This is exactly like for MD5. But SHA-2 requires right-rotate as well.

# In[48]:


def leftrotate(x, c):
    """ Left rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def rightrotate(x, c):
    """ Right rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x >> c) | (x << (32 - c))) & 0xFFFFFFFF


# As SHA-2 plays with big-endian and little-endian integers, and at the end it requires a leftshift to combine the 5 hash pieces into one.

# In[49]:


def leftshift(x, c):
    """ Left shift the number x by c bytes."""
    return x << c

def rightshift(x, c):
    """ Right shift the number x by c bytes."""
    return x >> c


# ### The `SHA2` class
# 
# I will use a simple class, very similar to the class used for the SHA-1 algorithm (see above).
# It is a direct implementation of the pseudo-code, as given for instance on the Wikipedia page.
# 
# I will only implement the simpler one, SHA-256, of digest size of 256 bits. Other variants are SHA-224, SHA-384, SHA-512 (and others include SHA-512/224, SHA-512/256).

# In[50]:


class SHA2(Hash):
    """SHA256 hashing, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
    def __init__(self):
        self.name        = "SHA256"
        self.byteorder   = 'big'
        self.block_size  = 64
        self.digest_size = 32
        # Note 2: For each round, there is one round constant k[i] and one entry in the message schedule array w[i], 0 ≤ i ≤ 63
        # Note 3: The compression function uses 8 working variables, a through h
        # Note 4: Big-endian convention is used when expressing the constants in this pseudocode,
        #         and when parsing message block data from bytes to words, for example,
        #         the first word of the input message "abc" after padding is 0x61626380

        # Initialize hash values:
        # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
        h0 = 0x6a09e667
        h1 = 0xbb67ae85
        h2 = 0x3c6ef372
        h3 = 0xa54ff53a
        h4 = 0x510e527f
        h5 = 0x9b05688c
        h6 = 0x1f83d9ab
        h7 = 0x5be0cd19
        
        # Initialize array of round constants:
        # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
        self.k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        # Store them
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]
    
    def update(self, arg):
        h0, h1, h2, h3, h4, h5, h6, h7 = self.hash_pieces
        # 1. Pre-processing, exactly like MD5
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 448 (mod 512)
        while len(data) % 64 != 56:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 64) to message
        data += orig_len_in_bits.to_bytes(8, byteorder='big')
        assert len(data) % 64 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 512-bit = 64-bytes chunks:
        for offset in range(0, len(data), 64):
            # 2.a. 512-bits = 64-bytes chunks
            chunks = data[offset : offset + 64]
            w = [0 for i in range(64)]
            # 2.b. Break chunk into sixteen 32-bit = 4-bytes words w[i], 0 ≤ i ≤ 15
            for i in range(16):
                w[i] = int.from_bytes(chunks[4*i : 4*i + 4], byteorder='big')
            # 2.c.  Extend the first 16 words into the remaining 48
            #       words w[16..63] of the message schedule array:
            for i in range(16, 64):
                s0 = (rightrotate(w[i-15], 7) ^ rightrotate(w[i-15], 18) ^ rightshift(w[i-15], 3)) & 0xFFFFFFFF
                s1 = (rightrotate(w[i-2], 17) ^ rightrotate(w[i-2], 19) ^ rightshift(w[i-2], 10)) & 0xFFFFFFFF
                w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF
            # 2.d. Initialize hash value for this chunk
            a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
            # 2.e. Main loop, cf. https://tools.ietf.org/html/rfc6234
            for i in range(64):
                S1 = (rightrotate(e, 6) ^ rightrotate(e, 11) ^ rightrotate(e, 25)) & 0xFFFFFFFF
                ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFF
                temp1 = (h + S1 + ch + self.k[i] + w[i]) & 0xFFFFFFFF
                S0 = (rightrotate(a, 2) ^ rightrotate(a, 13) ^ rightrotate(a, 22)) & 0xFFFFFFFF
                maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFF
                temp2 = (S0 + maj) & 0xFFFFFFFF

                new_a = (temp1 + temp2) & 0xFFFFFFFF
                new_e = (d + temp1) & 0xFFFFFFFF
                # Rotate the 8 variables
                a, b, c, d, e, f, g, h = new_a, a, b, c, new_e, e, f, g

            # Add this chunk's hash to result so far:
            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]

    def digest(self):
        # h0 append h1 append h2 append h3 append h4 append h5 append h6 append h7
        return sum(leftshift(x, 32 * i) for i, x in enumerate(self.hash_pieces[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[51]:


def hash_SHA2(data):
    """ Shortcut function to directly receive the hex digest from SHA2(data)."""
    h = SHA2()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# ### First check on SHA-2
# 
# Let us try it:

# In[52]:


h4 = SHA2()
h4
print(h4)


# In[53]:


h4.update(data)
h4.digest()


# In[54]:


digest = h4.digest()
bin(digest)
len(bin(digest))


# In[55]:


h4.hexdigest()


# ### Check on SHA-2
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[56]:


hash_SHA2("The quick brown fox jumps over the lazy dog")
assert hash_SHA2("The quick brown fox jumps over the lazy dog") == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period at the end of the sentence:

# In[57]:


hash_SHA2("The quick brown fox jumps over the lazy dog.")
assert hash_SHA2("The quick brown fox jumps over the lazy dog.") == 'ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c'


# The hash of the zero-length string is:

# In[58]:


hash_SHA2("")
assert hash_SHA2("") == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


# $\implies$ We obtained the same result, OK our function works!

# ### Trying 1000 random examples
# On a small sentence:

# In[59]:


hash_SHA2("My name is Zorro !")


# In[60]:


h = hashlib.sha256()
h.update(b"My name is Zorro !")
h.hexdigest()


# It starts to look good.

# In[61]:


def true_hash_SHA2(data):
    h = hashlib.sha256()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# On some random data:

# In[62]:


random_string(10)


# In[63]:


from tqdm import tqdm_notebook as tqdm


# In[64]:


get_ipython().run_cell_magic('time', '', 'for _ in tqdm(range(1000)):\n    x = random_string()\n    assert hash_SHA2(x) == true_hash_SHA2(x), "Error: x = {} gave two different SHA2 hashes: my implementation = {} != hashlib implementation = {}...".format(x, hash_SHA2(x), true_hash_SHA2(x))')


# ----
# ## Comparison : MD5 vs SHA-1 vs SHA-2
# 
# It can be interesting to compare each hash functions, with respect to its time complexity.

# In[65]:


def test_MD5():
    x = random_string()
    return hash_MD5(x) == true_hash_MD5(x)

get_ipython().run_line_magic('timeit', 'test_MD5()')


# In[66]:


def test_SHA1():
    x = random_string()
    return hash_SHA1(x) == true_hash_SHA1(x)

get_ipython().run_line_magic('timeit', 'test_SHA1()')


# In[67]:


def test_SHA2():
    x = random_string()
    return hash_SHA2(x) == true_hash_SHA2(x)

get_ipython().run_line_magic('timeit', 'test_SHA2()')


# As expected, the MD5 hash is the fastest, and SHA-2 is slower than SHA-1.
# 
# $\implies$ The more secure, the slowest. Of course.

# ----
# ## Bonus : SHA-2 variants
# 
# Now that we have implemented SHA-256, it should be quick to add the SHA-224 variant, which is simply the SHA-256 with different initial values and a shorter digest.
# 
# The SHA-512 variant is working with 64-bits words and 1024-bits chunks, instead of 32-bits words and 512-bits chunks, and the SHA-384 is very similar to SHA-512 with different initial values and a shorter digest.
# 
# > Sorry about the length of this part, I know all these variants are very similar, but I wanted to write them all.

# ### SHA-224
# 
# As said on the Wikipedia page:
# > SHA-224 is identical to SHA-256, except that:
# > - the initial hash values `h0` through `h7` are different, and
# > - the output is constructed by omitting `h7`.

# #### The `SHA224` class

# In[68]:


class SHA224(Hash):
    """SHA224 hashing, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
    def __init__(self):
        self.name        = "SHA224"
        self.byteorder   = 'big'
        self.block_size  = 64
        self.digest_size = 28
        # Note 2: For each round, there is one round constant k[i] and one entry in the message schedule array w[i], 0 ≤ i ≤ 63
        # Note 3: The compression function uses 8 working variables, a through h
        # Note 4: Big-endian convention is used when expressing the constants in this pseudocode,
        #         and when parsing message block data from bytes to words, for example,
        #         the first word of the input message "abc" after padding is 0x61626380

        # Initialize hash values:
        # (The second 32 bits of the fractional parts of the square roots of the 9th through 16th primes 23..53)
        h0 = 0xc1059ed8
        h1 = 0x367cd507
        h2 = 0x3070dd17
        h3 = 0xf70e5939
        h4 = 0xffc00b31
        h5 = 0x68581511
        h6 = 0x64f98fa7
        h7 = 0xbefa4fa4
        
        # Initialize array of round constants:
        # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
        self.k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        # Store them
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]
    
    def update(self, arg):
        h0, h1, h2, h3, h4, h5, h6, h7 = self.hash_pieces
        # 1. Pre-processing, exactly like MD5
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 448 (mod 512)
        while len(data) % 64 != 56:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 64) to message
        data += orig_len_in_bits.to_bytes(8, byteorder='big')
        assert len(data) % 64 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 512-bit = 64-bytes chunks:
        for offset in range(0, len(data), 64):
            # 2.a. 512-bits = 64-bytes chunks
            chunks = data[offset : offset + 64]
            w = [0 for i in range(64)]
            # 2.b. Break chunk into sixteen 32-bit = 4-bytes words w[i], 0 ≤ i ≤ 15
            for i in range(16):
                w[i] = int.from_bytes(chunks[4*i : 4*i + 4], byteorder='big')
            # 2.c.  Extend the first 16 words into the remaining 48
            #       words w[16..63] of the message schedule array:
            for i in range(16, 64):
                s0 = (rightrotate(w[i-15], 7) ^ rightrotate(w[i-15], 18) ^ rightshift(w[i-15], 3)) & 0xFFFFFFFF
                s1 = (rightrotate(w[i-2], 17) ^ rightrotate(w[i-2], 19) ^ rightshift(w[i-2], 10)) & 0xFFFFFFFF
                w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF
            # 2.d. Initialize hash value for this chunk
            a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
            # 2.e. Main loop, cf. https://tools.ietf.org/html/rfc6234
            for i in range(64):
                S1 = (rightrotate(e, 6) ^ rightrotate(e, 11) ^ rightrotate(e, 25)) & 0xFFFFFFFF
                ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFF
                temp1 = (h + S1 + ch + self.k[i] + w[i]) & 0xFFFFFFFF
                S0 = (rightrotate(a, 2) ^ rightrotate(a, 13) ^ rightrotate(a, 22)) & 0xFFFFFFFF
                maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFF
                temp2 = (S0 + maj) & 0xFFFFFFFF

                new_a = (temp1 + temp2) & 0xFFFFFFFF
                new_e = (d + temp1) & 0xFFFFFFFF
                # Rotate the 8 variables
                a, b, c, d, e, f, g, h = new_a, a, b, c, new_e, e, f, g

            # Add this chunk's hash to result so far:
            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]

    def digest(self):
        # h0 append h1 append h2 append h3 append h4 append h5 append h6
        pieces_without_h7 = self.hash_pieces[:-1]
        return sum(leftshift(x, 32 * i) for i, x in enumerate(pieces_without_h7[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[69]:


def hash_SHA224(data):
    """ Shortcut function to directly receive the hex digest from SHA224(data)."""
    h = SHA224()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# #### Checks on SHA-224
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[70]:


def true_hash_SHA224(data):
    h = hashlib.sha224()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# In[71]:


hash_SHA224("The quick brown fox jumps over the lazy dog")
assert hash_SHA224("The quick brown fox jumps over the lazy dog") == '730e109bd7a8a32b1cb9d9a09aa2325d2430587ddbc0c38bad911525'
assert hash_SHA224("The quick brown fox jumps over the lazy dog") == true_hash_SHA224("The quick brown fox jumps over the lazy dog")


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period at the end of the sentence:

# In[72]:


hash_SHA224("The quick brown fox jumps over the lazy dog.")
assert hash_SHA224("The quick brown fox jumps over the lazy dog.") == '619cba8e8e05826e9b8c519c0a5c68f4fb653e8a3d8aa04bb2c8cd4c'
assert hash_SHA224("The quick brown fox jumps over the lazy dog.") == true_hash_SHA224("The quick brown fox jumps over the lazy dog.")


# The hash of the zero-length string is:

# In[73]:


hash_SHA224("")
assert hash_SHA224("") == 'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f'
assert hash_SHA224("") == true_hash_SHA224("")


# $\implies$ We obtained the same result, OK our function works!

# ### SHA-512
# 
# As said on the Wikipedia page:
# 
# > SHA-512 is identical in structure to SHA-256, but:
# > 
# > - the message is broken into 1024-bit chunks,
# > - the initial hash values and round constants are extended to 64 bits,
# > - there are 80 rounds instead of 64,
# > - the message schedule array w has 80 64-bit words instead of 64 32-bit words,
# > - to extend the message schedule array w, the loop is from 16 to 79 instead of from 16 to 63,
# > - the round constants are based on the first 80 primes 2..409,
# > - the word size used for calculations is 64 bits long,
# > - the appended length of the message (before pre-processing), in bits, is a 128-bit big-endian integer, and
# > - the shift and rotate amounts used are different.
# 

# #### Useful functions the SHA-512 algorithm

# This is exactly like for SHA-256, except we work with 64-bits words instead of 32-bits.

# In[74]:


def leftrotate_64(x, c):
    """ Left rotate the number x by c bytes, for 64-bits numbers."""
    x &= 0xFFFFFFFFFFFFFFFF
    return ((x << c) | (x >> (64 - c))) & 0xFFFFFFFFFFFFFFFF

def rightrotate_64(x, c):
    """ Right rotate the number x by c bytes, for 64-bits numbers."""
    x &= 0xFFFFFFFFFFFFFFFF
    return ((x >> c) | (x << (64 - c))) & 0xFFFFFFFFFFFFFFFF


# #### The `SHA512` class

# In[75]:


class SHA512(Hash):
    """SHA384 hashing, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
    def __init__(self):
        self.name        = "SHA512"
        self.byteorder   = 'big'
        self.block_size  = 128
        self.digest_size = 64
        # Note 2: For each round, there is one round constant k[i] and one entry in the message schedule array w[i], 0 ≤ i ≤ 79
        # Note 3: The compression function uses 8 working variables, a through h
        # Note 4: Big-endian convention is used when expressing the constants in this pseudocode

        # Initialize hash values:
        # (The second 64 bits of the fractional parts of the square roots of the first 8 primes 2..19)
        h0 = 0x6a09e667f3bcc908
        h1 = 0xbb67ae8584caa73b
        h2 = 0x3c6ef372fe94f82b
        h3 = 0xa54ff53a5f1d36f1
        h4 = 0x510e527fade682d1
        h5 = 0x9b05688c2b3e6c1f
        h6 = 0x1f83d9abfb41bd6b
        h7 = 0x5be0cd19137e2179

        # Initialize array of round constants:
        # (first 64 bits of the fractional parts of the cube roots of the first 80 primes 2..409):
        self.k = [
            0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538, 
            0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe, 
            0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 
            0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65, 
            0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab, 
            0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725, 
            0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 
            0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b, 
            0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218, 
            0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 
            0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 
            0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec, 
            0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c, 
            0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6, 
            0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 
            0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
        ]

        # Store them
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]
    
    def update(self, arg):
        h0, h1, h2, h3, h4, h5, h6, h7 = self.hash_pieces
        # 1. Pre-processing, exactly like MD5
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 896 (mod 1024)
        while len(data) % 128 != 112:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 128) to message
        data += orig_len_in_bits.to_bytes(16, byteorder='big')
        assert len(data) % 128 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 1024-bit = 128-bytes chunks:
        for offset in range(0, len(data), 128):
            # 2.a. 1024-bits = 128-bytes chunks
            chunks = data[offset : offset + 128]
            w = [0 for i in range(80)]
            # 2.b. Break chunk into sixteen 128-bit = 8-bytes words w[i], 0 ≤ i ≤ 15
            for i in range(16):
                w[i] = int.from_bytes(chunks[8*i : 8*i + 8], byteorder='big')
            # 2.c.  Extend the first 16 words into the remaining 64
            #       words w[16..79] of the message schedule array:
            for i in range(16, 80):
                s0 = (rightrotate_64(w[i-15], 1) ^ rightrotate_64(w[i-15], 8) ^ rightshift(w[i-15], 7)) & 0xFFFFFFFFFFFFFFFF
                s1 = (rightrotate_64(w[i-2], 19) ^ rightrotate_64(w[i-2], 61) ^ rightshift(w[i-2], 6)) & 0xFFFFFFFFFFFFFFFF
                w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFFFFFFFFFF
            # 2.d. Initialize hash value for this chunk
            a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
            # 2.e. Main loop, cf. https://tools.ietf.org/html/rfc6234
            for i in range(80):
                S1 = (rightrotate_64(e, 14) ^ rightrotate_64(e, 18) ^ rightrotate_64(e, 41)) & 0xFFFFFFFFFFFFFFFF
                ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFFFFFFFFFF
                temp1 = (h + S1 + ch + self.k[i] + w[i]) & 0xFFFFFFFFFFFFFFFF
                S0 = (rightrotate_64(a, 28) ^ rightrotate_64(a, 34) ^ rightrotate_64(a, 39)) & 0xFFFFFFFFFFFFFFFF
                maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFFFFFFFFFF
                temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

                new_a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF
                new_e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
                # Rotate the 8 variables
                a, b, c, d, e, f, g, h = new_a, a, b, c, new_e, e, f, g

            # Add this chunk's hash to result so far:
            h0 = (h0 + a) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFFFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFFFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFFFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFFFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFFFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFFFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]

    def digest(self):
        # h0 append h1 append h2 append h3 append h4 append h5 append h6 append h7
        return sum(leftshift(x, 64 * i) for i, x in enumerate(self.hash_pieces[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[76]:


def hash_SHA512(data):
    """ Shortcut function to directly receive the hex digest from SHA512(data)."""
    h = SHA512()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# #### Checks on SHA-512
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[77]:


def true_hash_SHA512(data):
    h = hashlib.sha512()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# In[78]:


hash_SHA512("The quick brown fox jumps over the lazy dog")
assert hash_SHA512("The quick brown fox jumps over the lazy dog") == true_hash_SHA512("The quick brown fox jumps over the lazy dog")


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period at the end of the sentence:

# In[79]:


hash_SHA512("The quick brown fox jumps over the lazy dog.")
assert hash_SHA512("The quick brown fox jumps over the lazy dog.") == true_hash_SHA512("The quick brown fox jumps over the lazy dog.")


# The hash of the zero-length string is:

# In[80]:


hash_SHA512("")
assert hash_SHA512("") == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
assert hash_SHA512("") == true_hash_SHA512("")


# $\implies$ We obtained the same result, OK our function works!

# ### SHA-384
# 
# As said on the Wikipedia page:
# 
# > SHA-384 is identical to SHA-512, except that:
# > - the initial hash values h0 through h7 are different (taken from the 9th through 16th primes), and
# > - the output is constructed by omitting h6 and h7.

# #### The `SHA384` class

# In[81]:


class SHA384(Hash):
    """SHA384 hashing, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
    def __init__(self):
        self.name        = "SHA384"
        self.byteorder   = 'big'
        self.block_size  = 96
        self.digest_size = 48
        # Note 2: For each round, there is one round constant k[i] and one entry in the message schedule array w[i], 0 ≤ i ≤ 79
        # Note 3: The compression function uses 8 working variables, a through h
        # Note 4: Big-endian convention is used when expressing the constants in this pseudocode

        # Initialize hash values:
        # (The second 64 bits of the fractional parts of the square roots of the first 9th through 16th primes 23..53)
        h0 = 0xcbbb9d5dc1059ed8
        h1 = 0x629a292a367cd507
        h2 = 0x9159015a3070dd17
        h3 = 0x152fecd8f70e5939
        h4 = 0x67332667ffc00b31
        h5 = 0x8eb44a8768581511
        h6 = 0xdb0c2e0d64f98fa7
        h7 = 0x47b5481dbefa4fa4
 

        # Initialize array of round constants:
        # (first 64 bits of the fractional parts of the cube roots of the first 80 primes 2..409):
        self.k = [
            0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538, 
            0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe, 
            0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 
            0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65, 
            0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab, 
            0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725, 
            0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 
            0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b, 
            0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218, 
            0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 
            0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 
            0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec, 
            0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c, 
            0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6, 
            0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 
            0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
        ]

        # Store them
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]
    
    def update(self, arg):
        h0, h1, h2, h3, h4, h5, h6, h7 = self.hash_pieces
        # 1. Pre-processing, exactly like MD5
        data = bytearray(arg)
        orig_len_in_bits = (8 * len(data)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        # 1.a. Add a single '1' bit at the end of the input bits
        data.append(0x80)
        # 1.b. Padding with zeros as long as the input bits length ≡ 896 (mod 1024)
        while len(data) % 128 != 112:
            data.append(0)
        # 1.c. append original length in bits mod (2 pow 128) to message
        data += orig_len_in_bits.to_bytes(16, byteorder='big')
        assert len(data) % 128 == 0, "Error in padding"
        # 2. Computations
        # Process the message in successive 1024-bit = 128-bytes chunks:
        for offset in range(0, len(data), 128):
            # 2.a. 1024-bits = 128-bytes chunks
            chunks = data[offset : offset + 128]
            w = [0 for i in range(80)]
            # 2.b. Break chunk into sixteen 128-bit = 8-bytes words w[i], 0 ≤ i ≤ 15
            for i in range(16):
                w[i] = int.from_bytes(chunks[8*i : 8*i + 8], byteorder='big')
            # 2.c.  Extend the first 16 words into the remaining 64
            #       words w[16..79] of the message schedule array:
            for i in range(16, 80):
                s0 = (rightrotate_64(w[i-15], 1) ^ rightrotate_64(w[i-15], 8) ^ rightshift(w[i-15], 7)) & 0xFFFFFFFFFFFFFFFF
                s1 = (rightrotate_64(w[i-2], 19) ^ rightrotate_64(w[i-2], 61) ^ rightshift(w[i-2], 6)) & 0xFFFFFFFFFFFFFFFF
                w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFFFFFFFFFF
            # 2.d. Initialize hash value for this chunk
            a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
            # 2.e. Main loop, cf. https://tools.ietf.org/html/rfc6234
            for i in range(80):
                S1 = (rightrotate_64(e, 14) ^ rightrotate_64(e, 18) ^ rightrotate_64(e, 41)) & 0xFFFFFFFFFFFFFFFF
                ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFFFFFFFFFF
                temp1 = (h + S1 + ch + self.k[i] + w[i]) & 0xFFFFFFFFFFFFFFFF
                S0 = (rightrotate_64(a, 28) ^ rightrotate_64(a, 34) ^ rightrotate_64(a, 39)) & 0xFFFFFFFFFFFFFFFF
                maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFFFFFFFFFF
                temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

                new_a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF
                new_e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
                # Rotate the 8 variables
                a, b, c, d, e, f, g, h = new_a, a, b, c, new_e, e, f, g

            # Add this chunk's hash to result so far:
            h0 = (h0 + a) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFFFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFFFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFFFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFFFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFFFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFFFFFFFFFF
        # 3. Conclusion
        self.hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]

    def digest(self):
        # h0 append h1 append h2 append h3 append h4 append h5
        hash_pieces_without_67 = self.hash_pieces[:-2]
        return sum(leftshift(x, 64 * i) for i, x in enumerate(hash_pieces_without_67[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[82]:


def hash_SHA384(data):
    """ Shortcut function to directly receive the hex digest from SHA384(data)."""
    h = SHA384()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# #### Checks on SHA-384
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[83]:


def true_hash_SHA384(data):
    h = hashlib.sha384()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# In[84]:


hash_SHA384("The quick brown fox jumps over the lazy dog")
assert hash_SHA384("The quick brown fox jumps over the lazy dog") == true_hash_SHA384("The quick brown fox jumps over the lazy dog")


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period at the end of the sentence:

# In[85]:


hash_SHA384("The quick brown fox jumps over the lazy dog.")
assert hash_SHA384("The quick brown fox jumps over the lazy dog.") == true_hash_SHA384("The quick brown fox jumps over the lazy dog.")


# The hash of the zero-length string is:

# In[86]:


hash_SHA384("")
assert hash_SHA384("") == '38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b'
assert hash_SHA384("") == true_hash_SHA384("")


# $\implies$ We obtained the same result, OK our function works!

# ### More comparison

# In[87]:


def test_SHA224():
    x = random_string()
    return hash_SHA224(x) == true_hash_SHA224(x)

get_ipython().run_line_magic('timeit', 'test_SHA224()')


# In[88]:


def test_SHA512():
    x = random_string()
    return hash_SHA512(x) == true_hash_SHA512(x)

get_ipython().run_line_magic('timeit', 'test_SHA512()')


# In[89]:


def test_SHA384():
    x = random_string()
    return hash_SHA384(x) == true_hash_SHA384(x)

get_ipython().run_line_magic('timeit', 'test_SHA384()')


# `SHA512` and `SHA384` are slower than `SHA256` obviously, but it's weird that `SHA224` is slower than the 64-bits versions...

# ----
# ## Conclusion

# Well, it was fun and interesting to implement these hashing functions, manually.
# Using [Python](https://www.Python.org) made it easy!
# 
# > Note that a Python 2 library implementing manually all these hashing functions already exist: [`pysha2`](https://github.com/thomdixon/pysha2), by [@thomdixon](https://github.com/thomdixon).
# > (I discovered it *after* writing this notebook!)
# 
# [![made-with-jupyter](https://img.shields.io/badge/Made%20for-Jupyter%20notebook-1f425f.svg)](https://www.jupyter.org/)
# [![GitHub license](https://img.shields.io/github/license/Naereen/notebooks.svg)](https://github.com/Naereen/notebooks/blob/master/LICENSE.txt)
# [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 
# [![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
# [![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)

# ### Bonus
# "SHA" is pronouced like the French word "chat", which means *cat*.
# 
# ![a cat playing on a computer](https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)

# > See [my GitHub `notebooks` project](https://GitHub.com/Naereen/notebooks/) for others notebooks.
