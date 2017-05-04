# [Jupyter Notebooks](http://mybinder.org/repo/Naereen/notebooks) :notebook: by [Naereen @ GitHub](https://naereen.github.io/)

This repository hosts some [Jupyter Notebooks](http://jupyter.org/), covering various subjects.

- At the beginning, this repository was only here to host some small experiments, for me to learn how to use [the wonderful Jupyter tools](http://jupyter.org/) correctly (baby notebooks :baby_bottle:);
- Some notebooks are small tutorials, on :shell: ``bash`` commands (or some of my [command-line my scripts](https://bitbucket.org/lbesson/bin/src/master/)) (as [example #1](https://github.com/Naereen/notebooks/blob/master/Tutorial%20on%20head%20and%20tail%20%28bash%29.ipynb)), or on :snake: Python (as [example #2](https://github.com/Naereen/notebooks/blob/master/Demonstration%20of%20numpy.polynomial.Polynomial%20and%20nice%20display%20with%20LaTeX%20and%20MathJax%20%28python3%29.ipynb));
- Some notebooks are written in French :fr:, mainly [documents written for the preparation](agreg/) to the highly competitive French national exam to become a professor (aka the ["agrégation"](http://agreg.org/)), as in 2016-17 I am [a teaching assistant](https://www.irisa.fr/fr/emplois/enseignants/missions-denseignement-au-departement-informatique-lens-rennes) at [ENS de Rennes](http://www.ens-rennes.fr/) in the [Computer Science department](http://www.dit.ens-rennes.fr/), for the ["Fundamental Computer Science" minor option (D) for the agrégation exam](http://www.dit.ens-rennes.fr/agregation-option-d/). (:fr: Voir [ce sous-dossier](agreg/) | :gb: See [this sub-folder](agreg/) ).
- I also wrote some notebooks on numerical simulations of dice games (:fr: Voir [ce sous-dossier](simus/) | :gb: See [this sub-folder](simus)).
- [This notebook](Manual_implementation_of_the_Mersenne_twister_PseudoRandom_Number_Generator__PRNG_.ipynb) shows a hand-written and clear implementation of several Pseudo-Random Number Generators, including the famous Mersenne twister algorithm, and then uses it to samples from the most famous discrete and continuous distributions, showcasing use of the Inverse-Transform method and Acceptance-Rejection method (cf. Markov Chain Monte-Carlo methods).
- [This notebook written for the Pi Day 2017](Py_Pi_Day_2017.ipynb) demonstrates a dozen of algorithms to compute digits of the number pi.
- [This other notebook](Obfuscated_code_or_piece_of_art.ipynb) shows some "obfuscated" code, producing :sparkles: [nice figures](art/)... Or maybe they are pieces of code art :art: ?
- I will try to write more *artistic* notebooks, showcasing nice pieces of *code* :art:!
- :fr: [Ce notebook en français](Introduction_aux_algorithmes_de_bandit__comme_UCB1_et_Thompson_Sampling.ipynb) présente les problèmes de bandits multi-bras stochastiques (multi-armed bandit, MAB), et les algorithmes dits "de bandits" pour les résoudre (UCB "Upper Confidence Bounds", Thompson Sampling, Approximated Finite-Horizon Gittins index etc).
- And more will come... soon!

[![made-with-jupyter](https://img.shields.io/badge/Made%20with-Jupyter-1f425f.svg)](http://jupyter.org/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

----

## 1. *How to read these documents*?

### 1.a. View the notebooks statically :memo:
- Either directly in GitHub: [see the list of notebooks](https://github.com/Naereen/notebooks/search?l=jupyter-notebook);
- Or on [nbviewer.jupiter.org](http://nbviewer.jupiter.org/): [list of notebooks](http://nbviewer.jupyter.org/github/Naereen/notebooks/).

### 1.b. Play with the notebooks dynamically :boom:
[![MyBinder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/Naereen/notebooks)

Anyone can use the [mybinder.org](http://mybinder.org/) website (by [clicking](http://mybinder.org/repo/Naereen/notebooks) on the icon above) to run the notebook in her/his web-browser.
You can then play with it as long as you like, for instance by modifying the values or experimenting with the code.

----

## 2. *Requirements to run the notebooks locally*?
All [the requirements](requirements.txt) can be installed with [``pip``](https://pip.readthedocs.io/) and by running a few ``python -m ...`` commands.

> Note: if you use [Python 3](https://docs.python.org/3/) instead of [Python 2](https://docs.python.org/2/), you *might* have to *replace* ``pip`` and ``python`` by ``pip3`` and ``python3`` in the next commands (if both pip and pip3 are installed).

### 2.a. [Jupyter Notebook](http://jupyter.readthedocs.org/en/latest/install.html) and [IPython](http://ipython.org/)

```bash
sudo pip install jupyter ipython
```

It will also install all the dependencies, afterward you should have a ``jupyter-notebook`` command (or a ``jupyter`` command, to be ran as ``jupyter notebook``) available in your ``PATH``:

```bash
$ whereis jupyter-notebook
jupyter-notebook: /usr/local/bin/jupyter-notebook
$ jupyter-notebook --version  # version >= 4 is recommended
4.2.1
```

### 2.b. Other kernels (*optional*):
> They are only needed to run the notebooks written for Bash or Octave (or OCaml):

#### 2.b.1. [GNU Bash kernel](https://github.com/takluyver/bash_kernel)
- You have to have [``bash``](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) installed ([already there](https://tiswww.case.edu/php/chet/bash/bashtop.html) on all Linux distribution, installable with [``brew``](http://brew.sh/) or [``macports``](https://www.macports.org/) on Mac OS, available on Windows through [``cygwin``](http://cygwin.org/)):

```bash
$ bash --version | head -n1
GNU bash, version 4.3.42(1)-release (x86_64-pc-linux-gnu)
```

- And then install the kernel ``bash_kernel`` with these *two* commands:

```bash
sudo pip install bash_kernel
python -m bash_kernel.install
```

#### 2.b.2. [GNU Octave kernel](https://github.com/calysto/octave_kernel)
- You have to have [``octave``](https://www.gnu.org/software/octave/) installed (installable with the package manager on major Linux distributions (``apt-get``, ``pacman``, ``yum`` etc), installable with [``brew``](http://brew.sh/) or [``macports``](https://www.macports.org/) on Mac OS, available on Windows through [``cygwin``](http://cygwin.org/) or [natively](https://ftp.gnu.org/gnu/octave/windows/)):

```bash
$ octave --version | head -n1
GNU Octave, version 4.0.0
```

- Your version of Octave should be installed with [gnuplot]() support (it is usually the case):

```bash
$ gnuplot --version | head -n1
gnuplot 5.0 patchlevel 1
```

- And then install the kernel ``bash_kernel`` with these *two* commands:

```bash
sudo pip install octave_kernel
python -m octave_kernel.install
```

#### 2.b.3. [OCaml kernel](https://github.com/andrewray/iocaml/wiki/jupyter)
> The instructions are not so simple, cf. the tutorial by @andrewray on [iocaml's wiki](https://github.com/andrewray/iocaml/wiki/).

----

### :information_desk_person: More information?
> - More information about [notebooks (on the documentation of IPython)](http://nbviewer.jupiter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) or [on the FAQ on Jupyter's website](http://nbviewer.jupyter.org/faq).
> - More information about [mybinder.org](http://mybinder.org/): on [this example repository](https://github.com/binder-project/example-requirements).


## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/notebooks.svg)](https://github.com/Naereen/notebooks/blob/master/LICENSE)
All the notebooks in this repository are published under the terms of the [MIT License](https://lbesson.mit-license.org/) (file [LICENSE.txt](LICENSE.txt)).
© [Lilian Besson](https://GitHub.com/Naereen), 2016-17.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/notebooks/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/notebooks/README.md?pixel)](https://GitHub.com/Naereen/notebooks/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
