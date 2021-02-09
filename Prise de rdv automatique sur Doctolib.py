#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Prise-de-rendez-vous-automatique-sur-Doctolib---COVID-19" data-toc-modified-id="Prise-de-rendez-vous-automatique-sur-Doctolib---COVID-19-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Prise de rendez-vous automatique sur Doctolib - COVID 19</a></span><ul class="toc-item"><li><span><a href="#But-initial" data-toc-modified-id="But-initial-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>But initial</a></span></li><li><span><a href="#Premier-tutoriel-pour-prendre-en-main-selenium" data-toc-modified-id="Premier-tutoriel-pour-prendre-en-main-selenium-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Premier tutoriel pour prendre en main selenium</a></span></li><li><span><a href="#Solution" data-toc-modified-id="Solution-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Solution</a></span></li><li><span><a href="#Automatisation-toutes-les-55-minutes" data-toc-modified-id="Automatisation-toutes-les-55-minutes-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Automatisation toutes les 55 minutes</a></span></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></li></ul></div>

# # Prise de rendez-vous automatique sur Doctolib - COVID 19
# *Ceci est une expérimentation, et n'est pas encore terminé*
# 
# ## But initial
# 
# 1. utiliser [Selenium](https://www.selenium.dev/) et [selenium Python](https://selenium-python.readthedocs.io/installation.html) pour automatiser l'utilisation du site <https://partners.doctolib.fr/hopital-public/perigueux/vaccination-covid?speciality_id=5494&enable_cookies_consent=1>,                                     
# 
# 2. vérifier si le site a changé, et m'envoyer un SMS si oui.
# 
# - Auteur : [Lilian Besson](https://perso.crans.org/besson/) ([@Naereen](https://GitHub.com/Naereen) sur GitHub)
# - Licence : [MIT Licensed](https://lbesson.mit-license.org/)
# - Date : Mardi 09 février 2021

# ---
# ## Premier tutoriel pour prendre en main selenium

# Note : je n'avais jamais utilisé selenium ou ce genre de module pour contrôler un navigateur en mode "headless".
# Ce n'est pas très compliqué, et j'ai trouvé que ce petit tutoriel est bien fait : https://pythonbasics.org/selenium-firefox-headless/
# [Cette documentation est bien complète, pour le module Python de selenium](https://selenium-python.readthedocs.io/).

# In[1]:


URL = "https://partners.doctolib.fr/hopital-public/perigueux/vaccination-covid?speciality_id=5494&enable_cookies_consent=1"


# In[2]:


from selenium import webdriver

try:
    print(f"Downloading '{URL}'...")
    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.headless = True
    browser = webdriver.Firefox(options=firefoxOptions)

    browser.get(URL)
    print(browser.page_source[:500])
finally:
    try:
        browser.close()
    except:
        pass


# J'ai bien réussi à installer et utiliser Selenium. Ca marche bien !

# ## Solution

# J'aurai besoin de ces modules là :

# In[3]:


import time
from datetime import datetime
import urllib.request
import subprocess
from selenium import webdriver


# Vérifions le contenu de la page, et voir si elle affiche ce message suivant :
# 
# > En raison d'une forte demande, ce centre n'a plus de disponibilités : 3362 vaccinations vont avoir lieu dans les 28 prochains jours. Réessayez prochainement ou cherchez un autre centre.

# In[7]:


print(f"Downloading '{URL}'...")
firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.headless = True
browser = webdriver.Firefox(options=firefoxOptions)

browser.get(URL)


# In[11]:


message = "ce centre n'a plus de disponibilités"

if message in browser.page_source:
    print(f"{URL} indique :\n{message}")
else:
    print(f"{URL} n'indique pas :\n{message}\nPeut être qu'il y a des disponibilités désormais !")
    get_ipython().system('FreeSMS.py f"{URL} semble indiquer qu\'il y a des disponibilités désormais."')


# Quand on a fini, on ferme le navigateur :

# In[ ]:


browser.close()


# ## Automatisation toutes les 55 minutes
# 
# Je ne ferai pas ça dans Python mais avec un simple script bash et un `watch`

# In[71]:


get_ipython().system('watch -help')


# ## Conclusion
# 
# C'était drôle. C'était une expérimentation. Mais ne vous servez pas de ça !
