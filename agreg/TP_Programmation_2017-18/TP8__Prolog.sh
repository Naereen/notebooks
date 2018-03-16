
ls -larth prolog.zip
zipinfo prolog.zip

unzip prolog.zip

ls prolog/

cd prolog/

/usr/bin/make clean
/usr/bin/make
rm -f *.cm[iox] *.annot

cd ..
ls prolog/prolog
file prolog/prolog

ls -larth exemples.zip
zipinfo exemples.zip

unzip exemples.zip

ls -larth exemples/*.pl

cat exemples/lapin.pl

cd prolog

cat pair.pl

./prolog pair.pl "pair(o)."  # une théorie vide : c'est axiomatiquement vrai !

./prolog pair.pl "pair(s(o))."  # aucune théorie : c'est faux !

./prolog pair.pl "pair(s(s(o)))."  # une théorie vide : c'est vrai !

./prolog nat.pl "infEq(s(s(o)), s(s(s(o))))."  # 2 <= 3 ? oui

./prolog nat.pl "infEq(s(s(s(s(o)))), s(s(s(o))))."  # 4 <= 3 ? non

./prolog nat.pl "plus(o,s(o),s(o))."  # 0+1 = 1 ? Oui

./prolog nat.pl "plus(s(o),s(o),s(s(o)))."  # 1+1 = 2 ? Oui

./prolog nat.pl "plus(s(o),o,s(s(o)))."  # 1+1 = 1 ? Non

cat pair.pl

echo "impair(s(o))." > impair.pl
echo "impair(s(s(X))) <-- impair(X)." >> impair

./prolog impair.pl "impair(o)."  # faux
./prolog impair.pl "impair(s(o))."  # vrai
./prolog impair.pl "impair(s(s(o)))."  # faux

rm -vf famille.pl

echo "parent(cyrill, renaud)." >> famille.pl
echo "parent(cyrill, claire)." >> famille.pl
echo "parent(renaud, clovis)." >> famille.pl
echo "parent(valentin, olivier)." >> famille.pl
echo "parent(claire, olivier)." >> famille.pl
echo "parent(renaud, claudia)." >> famille.pl
echo "parent(claire, gaelle)." >> famille.pl

./prolog famille.pl "parent(cyrill, renaud)."  # vrai
./prolog famille.pl "parent(claire, renaud)."  # faux

./prolog famille.pl "parent(X, renaud)."  # cyrill
./prolog famille.pl "parent(X, gaelle)."  # claire
./prolog famille.pl "parent(X, olivier)."  # claire, valentin

./prolog famille.pl "parent(renaud, X)."  # clovis, claudia
./prolog famille.pl "parent(gaelle, X)."  # {}
./prolog famille.pl "parent(olivier, X)."  # {}

echo "freresoeur(X,Y) <-- parent(Z,X), parent(Z,Y)." >> famille.pl
echo "grandparent(X,Y) <-- parent(X,Z), parent(Z,Y)." >> famille.pl
echo "cousin(X,Y) <-- grandparent(Z,X), grandparent(Z,Y)." >> famille.pl

./prolog famille.pl "freresoeur(cyrill, claire)."  # faux
./prolog famille.pl "freresoeur(renaud, claire)."  # vrai
./prolog famille.pl "freresoeur(claire, claire)."  # vrai

./prolog famille.pl "grandparent(X,olivier)."  # cyrill
./prolog famille.pl "grandparent(X,gaelle)."  # cyrill

#echo "ancetre(X,Y) <-- ancetre(X,Z), grandparent(Z,Y)." >> famille.pl
echo "ancetre(X,Y) <-- parent(X,Y)." >> famille.pl
echo "ancetre(X,Y) <-- grandparent(X,Y)." >> famille.pl
#echo "ancetre(X,X)." >> famille.pl

cat famille.pl

./prolog famille.pl "parent(X,olivier)."
./prolog famille.pl "grandparent(X,olivier)."


./prolog famille.pl "ancetre(X,olivier)."

./prolog famille.pl "ancetre(olivier,X),ancetre(renaud,X)."

./prolog famille.pl "ancetre(X,olivier),ancetre(X,renaud)."

./prolog famille.pl "freresoeur(gaelle,claudia)."  # faux
./prolog famille.pl "cousin(gaelle,claudia)."  # vrai

./prolog famille.pl "freresoeur(X,clovis)."
./prolog famille.pl "cousin(X,clovis)."
