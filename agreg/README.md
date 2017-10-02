# :notebook: Notebooks pour l'agrégation :fr:

Ce dossier contient des [notebooks Jupyter](http://jupyter.org/), écrits en [Python (version 3)](https://docs.python.org/3/), pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France).

Ces documents sont les seules corrections de texte de modélisation d'option info pour l'agrég de maths que vous pourrez trouver en ligne ([j'ai cherché](https://www.google.fr/search?q=correction+texte+modélisation+agrégation+informatique+ocaml) [partout](https://duckduckgo.com/?q=correction+texte+mod%C3%A9lisation+agr%C3%A9gation+informatique+ocaml&t=canonical&ia=web)).
Profitez en bien !

[Liste des notebooks sur nbviewer.jupyter.org](https://nbviewer.jupyter.org/github/Naereen/notebooks/tree/master/agreg/)

----

> :warning: Si vous êtes en train de préparer l'agrégation, lire des corrections sans avoir travailler (très sérieusement) le texte ou le développement avant, **ça ne sert à rien** !!
> Si vous êtes parmi mes élèves, **n'utilisez pas ces ressources pour tricher pendant les oraux blancs** : ça ne sert à rien, je le verrai, et vous n'aurez rien appris (spoiler alert : le jour des oraux, on ne peut pas tricher...).


> Cela étant dit, si vous avez travaillé un texte, n'hésitez pas à jeter un oeil à la correction et à la travailler aussi.
> Vous faites les choses différemment, et souvent plus vite et mieux, donc si vous avez envie, [contactez moi](http://perso.crans.org/besson/contact/) pour me signaler n'importe quoi (un bug, une meilleure façon de faire, une question ou autre).

## :pencil: Implémentation pour des leçons ou des développements
- [Algorithme de Cocke-Kasami-Younger](https://fr.wikipedia.org/wiki/Algorithme_de_Cocke-Younger-Kasami), pour résoudre le problème du mot pour une grammaire sous forme normale de Chomsky (et la mise en forme normale de Chomsky depuis la forme normale, en bonus) : [Algorithme de Cocke-Kasami-Younger (python3).ipynb](https://nbviewer.jupyter.org/github/Naereen/notebooks/blob/master/agreg/Algorithme%20de%20Cocke-Kasami-Younger%20%28python3%29.ipynb) ([sur GitHub](Algorithme%20de%20Cocke-Kasami-Younger%20%28python3%29.ipynb)) -- Leçons 906, 907, 910, 923.
- [Calcul du plus long sous mot commun](https://fr.wikipedia.org/wiki/Plus_longue_sous-séquence_commune) : [Plus long sous mot commun (python3).ipynb](https://nbviewer.jupyter.org/github/Naereen/notebooks/blob/master/agreg/Plus%20long%20sous%20mot%20commun%20%28python3%29.ipynb) ([sur GitHub](Plus%20long%20sous%20mot%20commun%20%28python3%29.ipynb)) -- Leçons 906, 907.
- [Tris à bulles et cocktail](https://fr.wikipedia.org/wiki/Tri_cocktail) : [Tri_a_bulle_et_tri_cocktail.ipynb](https://nbviewer.jupyter.org/github/Naereen/notebooks/blob/master/agreg/Tri_a_bulle_et_tri_cocktail.ipynb) ([sur GitHub](Tri_a_bulle_et_tri_cocktail.ipynb)) -- 903, 926, 927.
- [Lambda-Calcul embarqué en OCaml](https://fr.wikipedia.org/wiki/Lambda-calcul) : [Lambda_Calcul_en_OCaml.ipynb](https://nbviewer.jupyter.org/github/Naereen/notebooks/blob/master/agreg/Lambda_Calcul_en_OCaml.ipynb) ([sur GitHub](Lambda_Calcul_en_OCaml.ipynb)) -- 929.

----

### :information_desk_person: Plus d'informations ?
> - Plus d'informations sur ce dépôt se trouvent [ici](..).
> - Plus d'informations sur [les notebooks (documentation de IPython)](https://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) ou [FAQ sur le site de Jupyter](https://nbviewer.jupyter.org/faq).

### [Utiliser OCaml avec Jupyter](https://github.com/akabe/ocaml-jupyter)
Les solutions présentes ici sont rédigés comme des [notebooks](https://jupyter.org/documentation.html) [Jupyter](https://jupyter.org/).
J'utilise un *kernel* spécifique pour coder en OCaml via Jupyter.

Il ne devrait pas être trop compliqué à installer, avec [opam](https://opam.ocaml.org/) :
```bash
opam install jupyter
```

Cela demande d'avoir [déjà installé Jupyter](https://jupyter.org/install.html).

### :scroll: Licence
Tout ces documents sont distribues publiquement sous les conditions de la [licence MIT](http://lbesson.mit-license.org/) (fichier [LICENSE.txt](LICENSE.txt), en anglais).
© [Lilian Besson](https://github.com/Naereen), 2016-17.

[![made-with-jupyter](https://img.shields.io/badge/Made%20with-Jupyter-1f425f.svg)](http://jupyter.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-ocaml](https://img.shields.io/badge/Made%20with-OCaml-1f425f.svg)](https://ocaml.org/)

[![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/notebooks/agreg/README.md?pixel)](https://github.com/Naereen/notebooks/)
