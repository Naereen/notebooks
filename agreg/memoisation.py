#!/usr/bin/env python
# -*- coding: utf8 -*-

from time import sleep


def f1(n):
    sleep(3)
    return n + 3

print("3 secondes...")
print(f1(10))  # 13, 3 secondes après

def f2(n):
    sleep(4)
    return n * n

print("4 secondes...")
print(f2(10))  # 100, 4 secondes après


# Mémoïsation générique, non typée

def memo(f):
    memoire = {}  # dictionnaire vide, {} ou dict()
    def memo_f(n):
        if n not in memoire:
             memoire[n] = f(n)
        return memoire[n]
    return memo_f


memo_f1 = memo(f1)

print("3 secondes...")
print(memo_f1(10))  # 13, 3 secondes après
print("0 secondes !")
print(memo_f1(10))  # instanné !

# différent de ces deux lignes !

print("3 secondes...")
print(memo(f1)(10))
print("3 secondes...")
print(memo(f1)(10))  # 3 secondes aussi !


memo_f2 = memo(f2)

print("4 secondes...")
print(memo_f2(10))  # 100, 4 secondes après
print("0 secondes !")
print(memo_f2(10))  # instanné !



# bonus : on peut utiliser la syntaxe d'un décorateur en Python :

def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() non mémoisée :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


# version plus rapide !
@memo
def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() mémoisée (plus rapide) :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


@memo
def factorielle(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return n * factorielle(n-1)

print("Test de factorielle() mémoisée :")
for n in range(10):
    print("{}! = {}".format(n, factorielle(n)))


