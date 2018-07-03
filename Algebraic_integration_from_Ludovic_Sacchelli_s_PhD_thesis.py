
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Presentation" data-toc-modified-id="Presentation-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Presentation</a></div><div class="lev1 toc-item"><a href="#Computations" data-toc-modified-id="Computations-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Computations</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Conclusion</a></div>

# # Presentation
# 
# I want to reproduce the symbolic (algebraic) computations done in §5.A of [L.S.'s PhD thesis](http://www.cmap.polytechnique.fr/~sacchelli/).

# I want to only use a free and open-source software, so I'm using [Python 3](https://docs.python.org/3) with the [Sympy](https://sympy.org) module.

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -p sympy -g')


# In[2]:


from sympy import *


# In[3]:


init_printing(use_latex='mathjax')


# Just a small introduction to SymPy: it works by using Python expressions on formal variables.
# First, we define variables, and then we can solve linear equations for example:

# In[4]:


var("x y z")


# In[5]:


solve(x + 2 + 19)


# In[6]:


solve(x + 2*y + 19)


# # Computations

# We start by defining $b_1 > 0$ and the other variables.

# In[7]:


b1 = symbols("b1", positive=True)


# We need a lot of variables.

# In[8]:


var("h1 h2 h3 h4 k131 k132 k141 k142 k231 k232 k241 k242 rest1 rest2 t s a b");


# Then we can start to follow Ludovic's notebook and define the first expressions.

# In[13]:


J = Matrix([[0, -b1], [b1, 0]])
J


# In[14]:


h0 = Matrix([h1, h2])
h0


# $\hat{h}$ is defined as $t \mapsto \exp(t J) . h_0$ and $\hat{x}$ as $t \mapsto \int_{s=0}^{s=t} \hat{h}(s) \mathrm{d}s$.

# In[15]:


hhat = Lambda(t, (t * J).exp() * h0)
hhat


# In[16]:


xhat = Lambda(t, integrate(hhat(s), (s, 0, t)))
xhat


# $\hat{z}$ is slightly more complex:

# In[20]:


integrand = simplify(b1 * (hhat(s)[0] * xhat(s)[1] - hhat(s)[1] * xhat(s)[0] )/2)
integrand


# In[21]:


zhat = Lambda(t, integrate(integrand, (s, 0, t)))
zhat


# As we asked $b_1 > 0$, this won't get too complicated:

# In[22]:


factor(zhat(t))


# Two more expressions:

# In[23]:


exp21 = (3 * a * h1**2 + a * h2**2 + 2 * b * h1 * h2 + k131 * h1 * h3 + k141 * h1 * h4
         + k231 * h2 * h3 + k241 * h2 * h4 + rest1(h3, h4))


# In[24]:


exp22 = (b * h1**2 + 3 * b * h2**2 + 2 * a * h1 * h2 + k132 * h1 * h3 + k142 * h1 * h4
         + k232 * h2 * h3 + k242 * h2 * h4 + rest2(h3, h4))


# Both terms `rest1` and `rest2` are not important, they only depend on $h_3$ and $h_4$ and will vanish as soon as we only differentiate with respect to $h_1$ and $h_2$.

# So far so good. Next cell:

# In[27]:


C10 = 2 * (pi / b1) * Matrix([h1, h2])
C10


# In[29]:


A0 = simplify(Matrix([
    [diff(exp21, h1), diff(exp21, h2)],
    [diff(exp22, h1), diff(exp22, h2)],
]))
A0


# `rest1` and `rest2` already vanished.

# In[32]:


jacobian = simplify(Matrix([
    [diff(exp21, h1), diff(exp21, h2), C10[0]],
    [diff(exp22, h1), diff(exp22, h2), C10[1]],
    [diff(zhat(2 * pi / b1), h1), diff(zhat(2 * pi / b1), h2), 0],
]))
jacobian


# We need one more variable to solve an equation.

# In[33]:


var('dt')


# In[34]:


tc = factor(solve(Equality((jacobian + Matrix([[dt,0,0], [0,dt,0], [0,0,0]])).det(), 0), dt)[0])


# In[35]:


tc


# I can compare by copying the result from the document:

# In[36]:


tc2 = (-1 / (h1**2 + h2**2)) * (
      2 * a * h1**3
    + 6 * a * h1**2 * h2
    - 4 * b * h1**2 * h2
    + 2 * a * h1 * h2**2
    + 2 * b * h2**3
    + h2**2 * h3 * k131
    - h1 * h2 * h3 * k132
    + h2**2 * h4 * k141
    - h1 * h2 * h4 * k142
    - h1 * h2 * h3 * k231
    + h1**2 * h3 * k232
    - h1 * h2 * h4 * k241
    + h1**2 * h4 * k242 )


# Drat, they are not equal! We might have a mistake somewhere, even though I just CAN'T find it!

# In[37]:


simplify(tc - tc2)


# Let's use the one from Ludovic's notebook.

# In[38]:


tc = tc2


# Next cell.

# In[39]:


A12 = simplify(A0 + Matrix([[tc, 0], [0, tc]]))


# In[40]:


var("u1 u2 u5")


# In[41]:


Psi = Lambda((u1, u2, u5), simplify(
    u5 * Matrix(A12.dot(Matrix([h1, h2]))).dot(Matrix([h2, -h1])) + 2 * pi / b1 * ( h1**2 + h2**2) * (h1 * u2 - h2 * u1)
))


# In[43]:


my_psi = factor(simplify(Psi(u1, u2, u5)))
my_psi


# Let's compare with the value from Ludovic's notebook:

# In[44]:


his_psi = (1 / b1) * (
    2 * h1**3 * (pi * u2 - b * b1 * u5 ) -
    h1**2 * (2 * h2 * pi * u1 - 2 * a * b1 * h2 * u5 + b1 * h3 * k132 * u5 +
             b1 * h4 * k142 * u5 ) +
    h2**2 * ( -2 * h2 * pi * u1 + 2 * a * b1 * h2 * u5 + b1 * h3 * k231 * u5 +
            b1 * h4 * k241 * u5 ) +
    h1 * h2 * (b1 * (h3 * k131 + h4 * k141 - h3 * k232 - h4 * k242) * u5 +
    2 * h2 * (pi * u2 - b * b1 * u5))
)


# In[45]:


simplify(my_psi - his_psi)


# Ok, we have the same result so far! Great!

# Next cell.

# In[46]:


var("nu0")


# Here again, Sympy fails to solve the equation. It can solve on both lines separately, but cannot find a solution that satisfies both lines.

# In[47]:


s1 = solve(Eq((Matrix(A12.dot(Matrix([-h2, h1]))) + nu0 * C10)[0]), nu0)[0]


# In[48]:


s2 = solve(Eq((Matrix(A12.dot(Matrix([-h2, h1]))) + nu0 * C10)[1]), nu0)[0]


# In[49]:


solve(Eq(s1, s2))


# It is not possible to impose these constraints. And Sympy fails to solve both equation simultaneously:

# In[50]:


solve(Eq(Matrix(A12.dot(Matrix([-h2, h1]))) + nu0 * C10, Matrix([0,0])), nu0)


# In[51]:


nu = simplify(solve(Eq(Matrix(A12.dot(Matrix([-h2, h1]))) + nu0 * C10, Matrix([0,0])), nu0))
if nu == []:
    nu = var("nu")


# We can continue by using a formal variable for $\nu$ (`nu`).

# In[52]:


v = Matrix([nu, -h2, h1])


# In[53]:


v


# Let's finish.

# In[54]:


var("eta f F");


# In[55]:


d = [
    lambda F: -eta**2 * diff(F, eta) + eta * t * diff(F, t),
    lambda F: diff(F, h1),
    lambda F: diff(F, h2)
]


# In[56]:


d


# Next cell.

# In[57]:


var("i1 i2 g1 g2 dt1 dt2");


# In[59]:


g = eta * g1(t + eta * dt1, h1, h2) + eta**2 * g2(t, h1, h2)
g


# We have a sum to compute:

# In[60]:


res = 0
for i1 in range(0, 3):
    for i2 in range(0, 3):
        res += v[i1] * v[i2] * d[i1](d[i2](g))


# In[61]:


simplify(res)


# Then a double derivative

# In[62]:


d2f = simplify((diff(res, eta, eta) / 2).subs(eta, 0))


# Now, we should replace $g_1$ and $g_2$ with the following expression:

# In[63]:


g1 = Lambda((t, h1, h2), simplify(Matrix(list(xhat(t)) + [0])))


# In[64]:


g1(t, h1, h2)


# In[65]:


g2 = Lambda((t, h1, h2), simplify(Matrix([exp21, exp22] + [zhat(t)])))


# In[66]:


g2(t, h1, h2)


# Let's see if the replacement is possible:

# In[67]:


simplify(d2f)


# In[68]:


simplify(d2f.subs({
    g1: Lambda((t, h1, h2), simplify(Matrix(list(xhat(t)) + [0]))),
    g2: Lambda((t, h1, h2), simplify(Matrix([exp21, exp22] +[zhat(t)]))),
}))


# OK. This failed. But we can copy and paste this and the replacement of $g_1$ and $g_2$ will be effective:

# In[69]:


d2f = (
    h1**2*(dt1*diff(g1(t, h1, h2), t, h2, h2)
         + diff(g2(t, h1, h2), h2, h2))
    - 2*h1*h2*(dt1*diff(g1(t, h1, h2), t, h1, h2)
               + diff(g2(t, h1, h2), h1, h2))
    + 2*h1*nu*(t*diff(g1(t, h1, h2), t, h2)
               - diff(g1(t, h1, h2), h2))
    + h2**2*(dt1*diff(g1(t, h1, h2), t, h1, h1)
             + diff(g2(t, h1, h2), h1, h1))
    - 2*h2*nu*(t*diff(g1(t, h1, h2), t, h1)
               - diff(g1(t, h1, h2), h1))
)


# And the same for $t$.

# In[70]:


t = 2 * pi / b1


# In[71]:


d2f


# The replacement does not work apparently, so let's do it manually:

# In[72]:


d2f = Matrix([
[ 2*a*h1**2 + 6*a*h2**2 - 4*b*h1*h2 + 2*h1*nu*(I*t*(-(exp(2*I*b1*t) - 2*exp(I*b1*t) + 1)*exp(-I*b1*t)/2 + exp(I*b1*t) - 1) - (exp(2*I*b1*t) - 2*exp(I*b1*t) + 1)*exp(-I*b1*t)/(2*b1)) - 2*h2*nu*(t*(-(exp(2*I*b1*t) - 1)*exp(-I*b1*t)/2 + exp(I*b1*t)) - (-I*exp(2*I*b1*t) + I)*exp(-I*b1*t)/(2*b1))],
[-4*a*h1*h2 + 6*b*h1**2 + 2*b*h2**2 + 2*h1*nu*(t*(-(exp(2*I*b1*t) - 1)*exp(-I*b1*t)/2 + exp(I*b1*t)) - (-I*exp(2*I*b1*t) + I)*exp(-I*b1*t)/(2*b1)) - 2*h2*nu*(I*t*((exp(2*I*b1*t) - 2*exp(I*b1*t) + 1)*exp(-I*b1*t)/2 - exp(I*b1*t) + 1) - (-exp(2*I*b1*t) + 2*exp(I*b1*t) - 1)*exp(-I*b1*t)/(2*b1))],
[                                                                                                                                                       -h1**2*(2*b1*t*exp(I*b1*t) + I*exp(2*I*b1*t) - I)*exp(-I*b1*t)/(2*b1) - h2**2*(2*b1*t*exp(I*b1*t) + I*exp(2*I*b1*t) - I)*exp(-I*b1*t)/(2*b1)]])


# In[73]:


d2Exp = simplify(d2f)


# It still works well. And we removed the complex exponential, this result is purely real now!

# In[74]:


d2Exp


# In[75]:


Psi


# So now we can call $\Psi$ on the three components of this `d2Exp` :

# In[76]:


Psi(d2Exp[0], d2Exp[1], d2Exp[2])


# In[77]:


simplify(expand(Psi(d2Exp[0], d2Exp[1], d2Exp[2]) / (1 / (1/b1 * 2 * (h1**2 + h2**2) * pi))))


# We don't have the value for `nu` !

# ## Conclusion

# We do NOT obtain the same result as the document. Everything failed at the end.
# 
# Too bad, but still, it was interesting. I guess?

# > See [here](https://github.com/Naereen/notebooks) for other notebooks I wrote.
