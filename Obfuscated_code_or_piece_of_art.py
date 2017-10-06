
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Obfuscated-code-or-piece-of-art?" data-toc-modified-id="Obfuscated-code-or-piece-of-art?-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Obfuscated code or piece of art?</a></div><div class="lev2 toc-item"><a href="#Mandelbrot-set" data-toc-modified-id="Mandelbrot-set-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Mandelbrot set</a></div><div class="lev2 toc-item"><a href="#Penrose-patterns" data-toc-modified-id="Penrose-patterns-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Penrose patterns</a></div><div class="lev2 toc-item"><a href="#Bitcoin-address-&amp;-private-key-generator" data-toc-modified-id="Bitcoin-address-&amp;-private-key-generator-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Bitcoin address &amp; private key generator</a></div>

# # Obfuscated code or piece of art?
# 
# This short notebooks shows a few examples of Python code, designed to draw something, and shaped as what they will draw...

# ## Mandelbrot set
# 
# This nice little code will write a visualization of the [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set), on the domain $[-3, 3] \times [-3i, 3i]$, for $1500 \times 1500$ points, as a Bitmap (written manually in binary).

# In[2]:


get_ipython().run_cell_magic('time', '', "b_                                      =   (\n                                        255,\n                                      lambda\n                               V       ,B,c\n                             :c   and Y(V*V+B,B,  c\n                               -1)if(abs(V)<6)else\n               (              2+c-4*abs(V)**-0.4)/i\n                 )  ;v,      x=1500,1000;C=range(v*x\n                  );import  struct;P=struct.pack;M,\\\n            j  ='<QIIHHHH',open('art/M.bmp','wb').write\nfor X in j('BM'+P(M,v*x*3+26,26,12,v,x,1,24))or C:\n            i  ,Y=_;j(P('BBB',*(lambda T:(T*80+T**9\n                  *i-950*T  **99,T*70-880*T**18+701*\n                 T  **9     ,T*i**(1-T**45*2)))(sum(\n               [              Y(0,(A%3/3.+X%v+(X/v+\n                               A/3/3.-x/2)/1j)*2.5\n                             /x   -2.7,i)**2 for  \\\n                               A       in C\n                                      [:9]])\n                                        /9)\n                                       )   )")


# ![](art/M.bmp)

# ----
# 
# ## Penrose patterns
# 
# This second nice little code will write a visualization of a [Penrose tiling (infinite pattern)](https://en.wikipedia.org/wiki/Penrose_tiling) to a PNG image, of resolution $2000 \times 2000$.

# In[3]:


get_ipython().run_cell_magic('time', '', '_                                 =\\\n                                """if!\n                              1:"e,V=200\n                            0,(0j-1)**-.2;\n                           v,S=.5/  V.real,\n                         [(0,0,4      *e,4*e*\n                       V)];w=1          -v"def!\n                      E(T,A,              B,C):P\n                  ,Q,R=B*w+                A*v,B*w+C\n            *v,A*w+B*v;retur              n[(1,Q,C,A),(1,P\n     ,Q,B),(0,Q,P,A)]*T+[(0,C            ,R,B),(1,R,C,A)]*(1-T)"f\nor!i!in!_[:11]:S       =sum([E          (*x)for       !x!in!S],[])"imp\n  ort!cair               o!as!O;      s=O.Ima               geSurfac\n   e(1,e,e)               ;c=O.Con  text(s);               M,L,G=c.\n     move_to                ,c.line_to,c.s                et_sour\n       ce_rgb                a"def!z(f,a)                :f(-a.\n        imag,a.       real-e-e)"for!T,A,B,C!in[i       !for!i!\n          in!S!if!i[""";exec(reduce(lambda x,i:x.replace(chr\n           (i),"\\n "[34-i:]),   range(   35),_+"""0]]:z(M,A\n             );z(L,B);z         (L,C);         c.close_pa\n             th()"G             (.4,.3             ,1);c.\n             paint(             );G(.7             ,.7,1)\n             ;c.fil             l()"fo             r!i!in\n             !range             (9):"!             g=1-i/\n             8;d=i/          4*g;G(d,d,d,          1-g*.8\n             )"!def     !y(f,a):z(f,a+(1+2j)*(     1j**(i\n             /2.))*g)"!for!T,A,B,C!in!S:y(M,C);y(L,A);y(M\n             ,A);y(L,B)"!c.st            roke()"s.write_t\n             o_png(\'art/                    penrose.png\')\n             """                                       ))')


# ![](art/penrose.png)

# ----
# 
# ## Bitcoin address & private key generator
# 
# This is the most concise (and the most sexy!) implementation of the Bitcoin protocol to generate a new address and private key!

# In[26]:


get_ipython().run_cell_magic('time', '', '_                   =r"""A(W/2,*M(3*G\n               *G*V(2*J%P),G,J,G)+((M((J-T\n            )*V((G-S)%P),S,T,G)if(S@(G,J))if(\n         W%2@(S,T)))if(W@(S,T);H=2**256;import&h\n       ashlib&as&h,os,re,bi    nascii&as&k;J$:int(\n     k.b2a_hex(W),16);C$:C    (W/    58)+[W%58]if(W@\n    [];X=h.new("rip           em    d160");Y$:h.sha25\n   6(W).digest();I$                 d=32:I(W/256,d-1)+\n  chr(W%256)if(d>0@"";                  U$:J(k.a2b_base\n 64(W));f=J(os.urando       m(64))        %(H-U("AUVRIxl\nQt1/EQC2hcy/JvsA="))+      1;M$Q,R,G       :((W*W-Q-G)%P,\n(W*(G+2*Q-W*W)-R)%P)       ;P=H-2**       32-977;V$Q=P,L=\n1,O=0:V(Q%W,W,O-Q/W*                      L,L)if(W@O%P;S,\nT=A(f,U("eb5mfvncu6                    xVoGKVzocLBwKb/Nst\nzijZWfKBWxb4F5g="),      U("SDra         dyajxGVdpPv8DhEI\nqP0XtEimhVQZnEfQj/       sQ1Lg="),        0,0);F$:"1"+F(W\n [1:])if(W[:1           ]=="\\0"@""        .join(map(B,C(\n  J(W))));K$:               F(W          +Y(Y(W))[:4]);\n   X.update(Y("\\4"+                     I(S)+I(T)));B$\n    :re.sub("[0OIl    _]|            [^\\\\w]","","".jo\n     in(map(chr,ra    nge    (123))))[W];print"Addre\n       ss:",K("\\0"+X.dig    est())+"\\nPrivkey:",K(\n         "\\x80"+I(f))""";exec(reduce(lambda W,X:\n            W.replace(*X),zip(" \\n&$@",["","",\n               " ","=lambda W,",")else "])\n                    ,"A$G,J,S,T:"+_))')


# ----
# 
# Disclaimer: I am *not* the author of these small examples!
# 
# > That's it for today!
