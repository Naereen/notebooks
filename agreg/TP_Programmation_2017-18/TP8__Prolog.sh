
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

./prolog pair.pl "pair(o)."  # une valuation vide : c'est axiomatiquement vrai !

./prolog pair.pl "pair(s(o))."  # aucune valuation : c'est faux !

./prolog pair.pl "pair(s(s(o)))."  # une valuation vide : c'est vrai !

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

cd exemples

cat listes.pl

../prolog/prolog listes.pl "liste(nil)."  # vrai
../prolog/prolog listes.pl "liste(cons(toto, nil))."  # vrai
../prolog/prolog listes.pl "liste(pasliste)."  # faux
../prolog/prolog listes.pl "liste(cons(zorro, pasliste))."  # faux

../prolog/prolog listes.pl "dernier(X, nil)."  # {} aucune solution !
../prolog/prolog listes.pl "dernier(X, cons(toto, nil))."  # X = toto
../prolog/prolog listes.pl "avant_dernier(X, cons(zorro, cons(toto, nil)))."  # X = toto
../prolog/prolog listes.pl "avant_dernier(X, cons(titeuf, cons(zorro, cons(toto, nil))))."  # X = zorro

../prolog/prolog listes.pl "taille(K, nil)."  # K = o
../prolog/prolog listes.pl "taille(K, cons(toto, nil))."  # K = s(o)
../prolog/prolog listes.pl "taille(K, cons(zorro, cons(toto, nil)))."  # K = s(s(o))
../prolog/prolog listes.pl "taille(K, cons(titeuf, cons(zorro, cons(toto, nil))))."  # K = s(s(s(o)))

../prolog/prolog listes.pl "element_numero(X, o, nil)."  # {} erreur
../prolog/prolog listes.pl "element_numero(X, o, cons(toto, nil))."  # X = toto
../prolog/prolog listes.pl "element_numero(X, s(o), cons(zorro, cons(toto, nil)))."  # X = toto
../prolog/prolog listes.pl "element_numero(X, o, cons(titeuf, cons(zorro, cons(toto, nil))))."  # X = titeuf

../prolog/prolog listes.pl "element_numero(X, s(s(o)), cons(un, cons(deux, cons(trois, cons(quatre, nil)))))."  # X = titeuf

../prolog/prolog listes.pl "dupliquer(X, cons(a, cons(b, cons(c, nil))))."  # X = [a, a, b, b, c, c]

cd exemples

[ -f dominos.pl ] && rm -vf dominos.pl

echo "est_liste(nil)." >> dominos.pl
echo "est_liste(c(X, L)) <-- est_liste(L)." >> dominos.pl

echo "est_paire(p(A, B))." >> dominos.pl

echo "enchainement(nil)." >> dominos.pl
echo "enchainement(c(p(A, B), nil))." >> dominos.pl
echo "enchainement(c(p(Z, X), c(p(X, Y), Q))) <-- enchainement(c(p(X, Y), Q))." >> dominos.pl

../prolog/prolog dominos.pl "enchainement(nil)."  # vrai
../prolog/prolog dominos.pl "enchainement(c(p(a, b), nil))."  # vrai
../prolog/prolog dominos.pl "enchainement(c(p(a, b), c(p(a, b), nil)))."  # faux
../prolog/prolog dominos.pl "enchainement(c(p(b, a), c(p(a, b), nil)))."  # vrai : b-a a-b s'enchaine bien

echo "insere(X, L, c(X, L))." >> dominos.pl
echo "insere(X, c(T, Q1), c(T, Q2)) <-- insere(X, Q1, Q2)." >> dominos.pl

../prolog/prolog dominos.pl "insere(a, c(b, c(d, nil)), L2)."  # 2+1 possibilités

echo "perm(nil, nil)." >> dominos.pl
echo "perm(L, c(T, Q)) <-- insere(T, L2, L), perm(L2, Q)." >> dominos.pl

../prolog/prolog dominos.pl "perm(c(a,c(b,nil)), X)."  # [a;b] et [b;a]

../prolog/prolog dominos.pl "perm(c(a,c(b,c(d,nil))), X)."  # 6 = 3! possibilités, toutes montrées

../prolog/prolog dominos.pl "perm(c(u,c(v,c(w,c(x,nil)))), X)."  # 24 = 4! possibilités, pas toutes montrées ?!

echo "miroir(p(A, B), p(B, A))." >> dominos.pl

../prolog/prolog dominos.pl "miroir(p(u,v), X)."  # X = p(v,u)

echo "arrangement(nil, nil)." >> dominos.pl
echo "arrangement(L, c(T,Q)) <-- insere(T, L2, L), arrangement(L2, Q)." >> dominos.pl
echo "arrangement(L, c(T,Q)) <-- miroir(T2, T), insere(T2, L2, L), arrangement(L2, Q)." >> dominos.pl

../prolog/prolog dominos.pl "arrangement(nil, L)."  # L = nil
../prolog/prolog dominos.pl "arrangement(c(a,nil)), L)."  # rien

../prolog/prolog dominos.pl "arrangement(c(a,c(b,nil)), X)."  # X = [a;b] ou [b;a]

../prolog/prolog dominos.pl "arrangement(c(a,c(b,c(d,nil))), X)."  # 6 réponses

# X = [(u,v);(w,u)] ou [(w,u);(u,v)] avec 0 miroir
# ou X = [(v,u);(w,u)] ou [(w,u);(v,u)] avec 1 miroir sur (u,v)
# ou X = [(u,v);(u,w)] ou [(u,w);(u,v)] avec 1 miroir sur (w,u)
# ou X = [(v,u);(u,w)] ou [(u,w);(v,u)] avec 2 miroirs
../prolog/prolog dominos.pl "arrangement(c(p(u,v),c(p(w,u),nil)), X)."

echo "quasisolution(L1, L2) <-- perm(L1, L2), enchainement(L2)." >> dominos.pl
echo "solution(L1, L2) <-- arrangement(L1, L2), enchainement(L2)." >> dominos.pl

../prolog/prolog dominos.pl "quasisolution(c(p(un,deux),c(p(trois,un),c(p(deux,quatre),nil))), L)."

../prolog/prolog dominos.pl "solution(c(p(un,deux),c(p(trois,un),c(p(deux,quatre),nil))), L)."

cat domino.pl

cat dominos.pl
