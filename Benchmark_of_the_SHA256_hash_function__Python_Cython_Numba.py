
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Benchmark-of-the-SHA256-hash-function,-with-Python,-Cython-and-Numba" data-toc-modified-id="Benchmark-of-the-SHA256-hash-function,-with-Python,-Cython-and-Numba-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Benchmark of the SHA256 hash function, with Python, Cython and Numba</a></div><div class="lev2 toc-item"><a href="#What-is-a-hash-function?" data-toc-modified-id="What-is-a-hash-function?-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What is a hash function?</a></div><div class="lev2 toc-item"><a href="#Common-API-for-the-different-classes" data-toc-modified-id="Common-API-for-the-different-classes-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Common API for the different classes</a></div><div class="lev2 toc-item"><a href="#Checking-the-the-hashlib-module-in-Python-standard-library" data-toc-modified-id="Checking-the-the-hashlib-module-in-Python-standard-library-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Checking the <a href="https://docs.python.org/3/library/hashlib.html" target="_blank">the <code>hashlib</code> module in Python standard library</a></a></div><div class="lev2 toc-item"><a href="#Pure-Python-code-for-the-SHA-2-hashing-function" data-toc-modified-id="Pure-Python-code-for-the-SHA-2-hashing-function-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Pure Python code for the SHA-2 hashing function</a></div><div class="lev3 toc-item"><a href="#Useful-functions-the-SHA-2-algorithm" data-toc-modified-id="Useful-functions-the-SHA-2-algorithm-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Useful functions the SHA-2 algorithm</a></div><div class="lev3 toc-item"><a href="#The-SHA2-class" data-toc-modified-id="The-SHA2-class-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>The <code>SHA2</code> class</a></div><div class="lev3 toc-item"><a href="#Check-on-SHA-2" data-toc-modified-id="Check-on-SHA-2-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Check on SHA-2</a></div><div class="lev3 toc-item"><a href="#Trying-1000-random-examples" data-toc-modified-id="Trying-1000-random-examples-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>Trying 1000 random examples</a></div><div class="lev2 toc-item"><a href="#Numba-powered-code-for-the-SHA-2-hashing-function" data-toc-modified-id="Numba-powered-code-for-the-SHA-2-hashing-function-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Numba-powered code for the SHA-2 hashing function</a></div><div class="lev3 toc-item"><a href="#Requirements" data-toc-modified-id="Requirements-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Requirements</a></div><div class="lev3 toc-item"><a href="#Useful-functions-the-SHA-2-algorithm" data-toc-modified-id="Useful-functions-the-SHA-2-algorithm-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Useful functions the SHA-2 algorithm</a></div><div class="lev3 toc-item"><a href="#The-SHA2_Numba-class" data-toc-modified-id="The-SHA2_Numba-class-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>The <code>SHA2_Numba</code> class</a></div><div class="lev3 toc-item"><a href="#Check-on-SHA-2" data-toc-modified-id="Check-on-SHA-2-154"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>Check on SHA-2</a></div><div class="lev2 toc-item"><a href="#Cython-power-code-for-the-SHA-2-hashing-function" data-toc-modified-id="Cython-power-code-for-the-SHA-2-hashing-function-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Cython-power code for the <code>SHA-2</code> hashing function</a></div><div class="lev3 toc-item"><a href="#Requirements" data-toc-modified-id="Requirements-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Requirements</a></div><div class="lev3 toc-item"><a href="#Useful-functions-the-SHA-2-algorithm" data-toc-modified-id="Useful-functions-the-SHA-2-algorithm-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Useful functions the SHA-2 algorithm</a></div><div class="lev3 toc-item"><a href="#The-SHA2_Cython-class" data-toc-modified-id="The-SHA2_Cython-class-163"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>The <code>SHA2_Cython</code> class</a></div><div class="lev3 toc-item"><a href="#Check-on-SHA-2" data-toc-modified-id="Check-on-SHA-2-164"><span class="toc-item-num">1.6.4&nbsp;&nbsp;</span>Check on SHA-2</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Bonus" data-toc-modified-id="Bonus-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Bonus</a></div>

# # Benchmark of the SHA256 hash function, with Python, Cython and Numba
# 
# This small [Jupyter notebook](https://www.Jupyter.org/) is a short experiment, to compare the time complexity of three different implementations of the [SHA-256 hash function](https://en.wikipedia.org/wiki/SHA-2), in pure [Python](https://www.Python.org/), with [Cython](http://Cython.org/), and with [Numba](http://Numba.PyData.org/).
# 
# - *Reference*: Wikipedia pages on [Hash functions](https://en.wikipedia.org/wiki/Hash_function) and [SHA-2](https://en.wikipedia.org/wiki/SHA-2).
# - *Date*: 21 June 2017.
# - *Author*: [Lilian Besson](https://GitHub.com/Naereen/notebooks).
# - *License*: [MIT Licensed](https://LBesson.MIT-License.org/).

# ----
# ## What is a hash function?
# > TL;DR : [Hash functions](https://en.wikipedia.org/wiki/Hash_function) and [cryptographic hashing functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function) on Wikipedia.

# ----
# ## Common API for the different classes
# 
# I will copy the API proposed by [the `hashlib` module in Python standard library](https://docs.python.org/3/library/hashlib.html), so it will be very easy to compare my implementations with the one provided with your default [Python](https://www.Python.org/) installation.

# In[2]:


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

# In[3]:


import hashlib


# We can check [the available algorithms](https://docs.python.org/3.5/library/hashlib.html#hashlib.algorithms_available), some of them being [guaranteed to be on any platform](https://docs.python.org/3.5/library/hashlib.html#hashlib.algorithms_guaranteed), some are not.

# In[4]:


list(hashlib.algorithms_available)


# I will need at least this one:

# In[5]:


assert 'SHA256' in hashlib.algorithms_available


# Lets check that they have the block size and digest size announced:

# In[6]:


name = 'SHA256'
s = hashlib.sha256()
print("For {:<8} : the block size is {:<3} and the digest size is {:<2}.".format(name, s.block_size, s.digest_size))


# ----
# ## Pure Python code for the SHA-2 hashing function

# Let now study and implement a last hashing function, again slightly harder to write but more secure: SHA-2, "Secure Hash Algorithm, version 2".
# See [the SHA-2 hashing function](https://en.wikipedia.org/wiki/SHA-2) on Wikipedia, if needed.
# 
# <center><span style="font-size: large; color: green;"><i>Remark</i>: it is not (yet) considered broken, and it is the military standard for security and cryptographic hashing. SHA-3 is preferred for security purposes.</span></center>

# ### Useful functions the SHA-2 algorithm

# This is exactly like for MD5. But SHA-2 requires right-rotate as well.

# In[19]:


def leftrotate(x, c):
    """ Left rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def rightrotate(x, c):
    """ Right rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x >> c) | (x << (32 - c))) & 0xFFFFFFFF


# As SHA-2 plays with big-endian and little-endian integers, and at the end it requires a leftshift to combine the 5 hash pieces into one.

# In[20]:


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

# In[21]:


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

# In[22]:


def hash_SHA2(data):
    """ Shortcut function to directly receive the hex digest from SHA2(data)."""
    h = SHA2()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# ### Check on SHA-2
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[25]:


hash_SHA2("The quick brown fox jumps over the lazy dog")
assert hash_SHA2("The quick brown fox jumps over the lazy dog") == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'


# Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the [**avalanche effect**](https://en.wikipedia.org/wiki/Avalanche_effect). For example, adding a period at the end of the sentence:

# In[26]:


hash_SHA2("The quick brown fox jumps over the lazy dog.")
assert hash_SHA2("The quick brown fox jumps over the lazy dog.") == 'ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c'


# The hash of the zero-length string is:

# In[27]:


hash_SHA2("")
assert hash_SHA2("") == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


# $\implies$ We obtained the same result, OK our function works!

# ### Trying 1000 random examples
# On a small sentence:

# In[28]:


hash_SHA2("My name is Zorro !")


# In[29]:


h = hashlib.sha256()
h.update(b"My name is Zorro !")
h.hexdigest()


# It starts to look good.

# In[30]:


def true_hash_SHA2(data):
    h = hashlib.sha256()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# On some random data:

# In[32]:


import numpy.random as nr
alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_string(size=10000):
    return ''.join(alphabets[nr.randint(len(alphabets))] for _ in range(size))


# In[33]:


random_string(10)


# In[34]:


from tqdm import tqdm_notebook as tqdm


# In[35]:


get_ipython().run_cell_magic('time', '', 'for _ in tqdm(range(1000)):\n    x = random_string()\n    assert hash_SHA2(x) == true_hash_SHA2(x), "Error: x = {} gave two different SHA2 hashes: my implementation = {} != hashlib implementation = {}...".format(x, hash_SHA2(x), true_hash_SHA2(x))')


# ----
# ## Numba-powered code for the SHA-2 hashing function

# ### Requirements
# You need [numba](http://numba.pydata.org/) to be installed.

# In[16]:


from numba import jit, jitclass


# ### Useful functions the SHA-2 algorithm
# 
# Let just add the [`numba.jit`](http://numba.pydata.org/numba-doc/latest/user/jit.html) decorator to every function we defined before:

# In[14]:


@jit
def leftrotate_numba(x, c):
    """ Left rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

@jit
def rightrotate_numba(x, c):
    """ Right rotate the number x by c bytes."""
    x &= 0xFFFFFFFF
    return ((x >> c) | (x << (32 - c))) & 0xFFFFFFFF


# In[15]:


@jit
def leftshift_numba(x, c):
    """ Left shift the number x by c bytes."""
    return x << c

@jit
def rightshift_numba(x, c):
    """ Right shift the number x by c bytes."""
    return x >> c


# ### The `SHA2_Numba` class
# 
# And similarly for the `SHA2` class, with the [`numba.jit`](http://numba.pydata.org/numba-doc/latest/user/jit.html) decorator to the `update` function.

# In[42]:


class SHA2_Numba(Hash):
    """SHA256 hashing, speed-up with Numba.jit, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
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
    
    @jit
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

# In[43]:


def hash_SHA2_Numba(data):
    """ Shortcut function to directly receive the hex digest from SHA2_Numba(data)."""
    h = SHA2_Numba()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    h.update(data)
    return h.hexdigest()


# ### Check on SHA-2
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[44]:


hash_SHA2_Numba("The quick brown fox jumps over the lazy dog")
assert hash_SHA2_Numba("The quick brown fox jumps over the lazy dog") == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'


# I failed to make `numba.jit` work on that function :-(

# ----
# ## Cython-power code for the `SHA-2` hashing function

# ### Requirements
# You need [cython](http://cython.org/) and the cython Jupyter extension to be installed.

# In[45]:


get_ipython().run_line_magic('load_ext', 'cython')


# ### Useful functions the SHA-2 algorithm
# 
# For the functions defined before, we rewrite them with type annotations in `%%cython` cells.
# All variables are `int`, i.e., 32-bits integer (64-bits are `long`).

# In[59]:


get_ipython().run_cell_magic('cython', '', '\ncpdef int leftrotate_cython(int x, int c):\n    """ Left rotate the number x by c bytes."""\n    return (x << c) | (x >> (32 - c))\n\ncpdef int rightrotate_cython(int x, int c):\n    """ Right rotate the number x by c bytes."""\n    return (x >> c) | (x << (32 - c))')


# In[60]:


get_ipython().run_line_magic('pinfo', 'leftrotate_cython')
get_ipython().run_line_magic('pinfo', 'rightrotate_cython')


# On basic functions like this, of course we don't get any speedup with Cython:

# In[63]:


from numpy.random import randint

get_ipython().run_line_magic('timeit', 'leftrotate(randint(0, 100000), 5)')
get_ipython().run_line_magic('timeit', 'leftrotate_cython(randint(0, 100000), 5)')

get_ipython().run_line_magic('timeit', 'rightrotate(randint(0, 100000), 5)')
get_ipython().run_line_magic('timeit', 'rightrotate_cython(randint(0, 100000), 5)')


# In[52]:


get_ipython().run_cell_magic('cython', '', '\ncpdef int leftshift_cython(int x, int c):\n    """ Left shift the number x by c bytes."""\n    return x << c\n\ncpdef int rightshift_cython(int x, int c):\n    """ Right shift the number x by c bytes."""\n    return x >> c')


# In[53]:


get_ipython().run_line_magic('pinfo', 'leftshift_cython')
get_ipython().run_line_magic('pinfo', 'rightshift_cython')


# On basic functions like this, of course we don't get any speedup with Cython:

# In[64]:


get_ipython().run_line_magic('timeit', 'leftshift(randint(0, 100000), 5)')
get_ipython().run_line_magic('timeit', 'leftshift_cython(randint(0, 100000), 5)')

get_ipython().run_line_magic('timeit', 'rightshift(randint(0, 100000), 5)')
get_ipython().run_line_magic('timeit', 'rightshift_cython(randint(0, 100000), 5)')


# ### The `SHA2_Cython` class
# 
# And similarly for the `SHA2` class, we write it in a `%%cython` cell, and we type everything.

# In[182]:


get_ipython().run_cell_magic('cython', '', '# cython: c_string_type=unicode, c_string_encoding=utf8\n\ncdef int rightrotate_cython(int x, int c):\n    """ Right rotate the number x by c bytes."""\n    return (x >> c) | (x << (32 - c))\n\ncdef int rightshift_cython(int x, int c):\n    """ Right shift the number x by c bytes."""\n    return x >> c\n\n# See http://cython.readthedocs.io/en/latest/src/tutorial/array.html\nfrom cpython cimport array\nimport array\n\ncdef array.array empty_64 = array.array(\'i\', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])\ncdef int[:] view_empty_64 = empty_64\n\n\ncpdef void update_cython(int[:] hash_pieces, int[:] k, bytearray arg):\n    """ One pass of the SHA-256 algorithm, update hash_pieces on place. """\n    # Extract the 8 variables\n    cdef int h0 = hash_pieces[0], h1 = hash_pieces[1], h2 = hash_pieces[2], h3 = hash_pieces[3], h4 = hash_pieces[4], h5 = hash_pieces[5], h6 = hash_pieces[6], h7 = hash_pieces[7]\n    # 1. Pre-processing, exactly like MD5\n    cdef bytearray data = arg\n    cdef long orig_len_in_bits = 8 * len(data)\n    # 1.a. Add a single \'1\' bit at the end of the input bits\n    data.append(0x80)\n    # 1.b. Padding with zeros as long as the input bits length ≡ 448 (mod 512)\n    while len(data) % 64 != 56:\n        data.append(0x0)\n    # 1.c. append original length in bits mod (2 pow 64) to message\n    data += orig_len_in_bits.to_bytes(8, byteorder=\'big\')\n    assert len(data) % 64 == 0, "Error in padding"\n\n    # Declare loop indexes and variables\n    cdef int offset, i\n    cdef int a, b, c, d, e, f, g, h\n    cdef int temp1, temp2\n\n    # 2. Computations\n    # Process the message in successive 512-bit = 64-bytes chunks:\n    cdef int[:] w = view_empty_64\n\n    for offset in range(0, len(data), 64):\n        # 2.a. 512-bits = 64-bytes chunks\n        # 2.b. Break chunk into sixteen 32-bit = 4-bytes words w[i], 0 ≤ i ≤ 15\n        for i in range(16):\n            w[i] = int.from_bytes(data[offset : offset + 64][4*i : 4*i + 4], byteorder=\'big\')\n        # 2.c.  Extend the first 16 words into the remaining 48\n        #       words w[16..63] of the message schedule array:\n        for i in range(16, 64):\n            w[i] = w[i-16] + (rightrotate_cython(w[i-15], 7) ^ rightrotate_cython(w[i-15], 18) ^ rightshift_cython(w[i-15], 3)) + w[i-7] + (rightrotate_cython(w[i-2], 17) ^ rightrotate_cython(w[i-2], 19) ^ rightshift_cython(w[i-2], 10))\n        # 2.d. Initialize hash value for this chunk\n        a = h0\n        b = h1\n        c = h2\n        d = h3\n        e = h4\n        f = h5\n        g = h6\n        h = h7\n        # 2.e. Main loop, cf. https://tools.ietf.org/html/rfc6234\n        for i in range(64):\n            temp1 = h + (rightrotate_cython(e, 6) ^ rightrotate_cython(e, 11) ^ rightrotate_cython(e, 25)) + ((e & f) ^ ((~e) & g)) + k[i] + w[i]\n            temp2 = (rightrotate_cython(a, 2) ^ rightrotate_cython(a, 13) ^ rightrotate_cython(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))\n\n            # Rotate the 8 variables\n            a, b, c, d, e, f, g, h = temp1 + temp2, a, b, c, d + temp1, e, f, g\n\n        # Add this chunk\'s hash to result so far:\n        h0 += a\n        h1 += b\n        h2 += c\n        h3 += d\n        h4 += e\n        h5 += f\n        h6 += g\n        h7 += h\n    # 3. Conclusion\n    hash_pieces[0] = h0\n    hash_pieces[1] = h1\n    hash_pieces[2] = h2\n    hash_pieces[3] = h3\n    hash_pieces[4] = h4\n    hash_pieces[5] = h5\n    hash_pieces[6] = h6\n    hash_pieces[7] = h7')


# In[183]:


class SHA2_Cython(Hash):
    """SHA256 hashing, speed-up with Numba.jit, see https://en.wikipedia.org/wiki/SHA-2#Pseudocode."""
    
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
    
    def update(self, data):
        update_cython(self.hash_pieces, self.k, data)

    def digest(self):
        # h0 append h1 append h2 append h3 append h4 append h5 append h6 append h7
        return sum(leftshift(x, 32 * i) for i, x in enumerate(self.hash_pieces[::-1]))


# We can also write a function to directly compute the hex digest from some bytes data.

# In[184]:


def hash_SHA2_Cython(data):
    """ Shortcut function to directly receive the hex digest from SHA2_Cython(data)."""
    h = SHA2_Cython()
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    print("type(data) =", type(data))
    h.update(data)
    return h.hexdigest()


# In[185]:


data = bytes("", encoding='utf8')
h = SHA2_Cython()

h.hash_pieces[:1]
type(h.hash_pieces)
h.k[:1]
type(h.k)
data
type(data)

update_cython(h.hash_pieces, h.k, bytearray(data))


# ### Check on SHA-2
# 
# Let try the example from [SHA-2 Wikipedia page](https://en.wikipedia.org/wiki/SHA-2#Test_vectors) :

# In[90]:


hash_SHA2_Cython("The quick brown fox jumps over the lazy dog")
assert hash_SHA2_Cython("The quick brown fox jumps over the lazy dog") == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'


# ----
# ## Conclusion

# I still have to work on that.
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
