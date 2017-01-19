# Using bash and not sh, cf. http://stackoverflow.com/a/589300/
SHELL := /bin/bash -o pipefail

runipy:
	# nice -n 19 time runipy -o Calcul_d_une_paire_de_des_un_peu_particuliers.ipynb 2>&1 | tee Calcul_d_une_paire_de_des_un_peu_particuliers.log
	# Using my fork, see https://github.com/paulgb/runipy/pull/134
	nice -n 19 time ~/runipy/runipy.bin --logback -o Calcul_d_une_paire_de_des_un_peu_particuliers.ipynb 2>&1 | tee Calcul_d_une_paire_de_des_un_peu_particuliers.log

ipython3:
	jupyter-nbconvert --to python Calcul_d_une_paire_de_des_un_peu_particuliers.ipynb
	nice -n 19 time ipython3 Calcul_d_une_paire_de_des_un_peu_particuliers.py 2>&1 | tee Calcul_d_une_paire_de_des_un_peu_particuliers.log
