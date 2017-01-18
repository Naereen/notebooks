# Using bash and not sh, cf. http://stackoverflow.com/a/589300/
SHELL := /bin/bash -o pipefail

run:
	# time runipy -o Calcul_d_une_paire_de_des_un_peu_particuliers.ipynb 2>&1 | tee Calcul_d_une_paire_de_des_un_peu_particuliers.log
	time ~/runipy/runipy.bin --logback -o Calcul_d_une_paire_de_des_un_peu_particuliers.ipynb 2>&1 | tee Calcul_d_une_paire_de_des_un_peu_particuliers.log

fail:
	time false | tee /tmp/t.log
