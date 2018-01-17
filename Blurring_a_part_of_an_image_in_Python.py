
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Blurring-a-part-of-an-image-in-Python" data-toc-modified-id="Blurring-a-part-of-an-image-in-Python-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Blurring a part of an image in Python</a></div><div class="lev2 toc-item"><a href="#Blur-all-the-image" data-toc-modified-id="Blur-all-the-image-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Blur all the image</a></div><div class="lev2 toc-item"><a href="#Blur-only-an-area-of-the-image" data-toc-modified-id="Blur-only-an-area-of-the-image-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Blur only an area of the image</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Blurring a part of an image in Python
# 
# This very short notebook shows how to open an image (eg a PNG image), and nicely blur a part of it.

# In[1]:


import numpy as np
import skimage


# In[2]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -a "Lilian Besson (Naereen)" -p numpy,skimage -g')


# ## Blur all the image
# Let's import one of the example image, and blur all of it using [`skimage.filters.gaussian`](http://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.gaussian).

# In[9]:


from skimage import data, io, filters

image = data.astronaut()


# In[10]:


def imshow(image):
    io.imshow(image)
    io.show()


# In[11]:


imshow(image)


# In[5]:


from skimage.filters import gaussian


# In[12]:


filtered_img = gaussian(image, sigma=1, multichannel=True)
imshow(filtered_img)


# In[13]:


filtered_img = gaussian(image, sigma=2, multichannel=True)
imshow(filtered_img)


# ## Blur only an area of the image

# In[17]:


image.shape


# In[71]:


def blur(image, x0, x1, y0, y1, sigma=1, imshowall=False):
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    im = image.copy()
    sub_im = im[x0:x1,y0:y1].copy()
    if imshowall: imshow(sub_im)
    blur_sub_im = gaussian(sub_im, sigma=sigma)
    if imshowall: imshow(blur_sub_im)
    blur_sub_im = np.round(255 * blur_sub_im)
    im[x0:x1,y0:y1] = blur_sub_im
    return im


# In[72]:


filtered_img = blur(image, 80, 180, 170, 270, sigma=1)
imshow(filtered_img)


# In[76]:


filtered_img = blur(image, 80, 180, 170, 270, sigma=5)
imshow(filtered_img)


# In[73]:


filtered_img = blur(image, 80, 180, 170, 270, sigma=10)
imshow(filtered_img)


# In[74]:


filtered_img = blur(image, 80, 180, 170, 270, sigma=20)
imshow(filtered_img)


# ## Conclusion
# 
# That's it.
