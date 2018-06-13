#!/usr/bin/env bash

# # 1. On récupère les données sous forme de liste HTML
# # Les résultats d'admissibilités et d'admissions
# [ ! -d donnees_html/ ] && mkdir donnees_html/
# cd donnees_html/
# wget http://agreg.org/ResultatsMerite20{13..18}.html
# wget http://agreg.org/ResultatsAdm20{13..18}.html
# wget http://agreg.org/ResultatsAlpha20{03..18}.html
# cd ..

# # 2. On convertit ces fichiers HTML en fichiers CSV
# [ ! -d donnees_csv/ ] && mkdir donnees_csv/

# for fichier_html in donnees_html/*.html; do
#     fichier_csv="${fichier_html%.html}.csv"
#     if [ ! -f "$fichier_csv" ]; then
#         grep '^<tr><td>.*</tr>' "$fichier_html" | sed s_'<td>'_','_g | sed s_'<\.\?/\?\(b\|tr\|td\)>'_''_g | sed s_'^,'_''_ > donnees_csv/"$fichier_csv"
#     fi
# done

# find donnees_csv -type f -print0 | xargs -0 perl -pi.backup -e 's/[ \t]+$//'
# mv -vf donnees_csv/*.backup /tmp/

# 3. On créée une base de données et on insert les données des fichiers CSV
rm -vf resultats_agreg.sqlite
./csv2sqlite3.py

# 4. On vérifie qu'elle est bien crée
./csv2sqlite3.py --lire
