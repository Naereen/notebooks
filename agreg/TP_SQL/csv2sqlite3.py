#!/usr/bin/env python3
#-*- coding: utf8 -*-
""" Créer ou afficher une base SQLite qui rassemble les résultats d'admissibilité et d'admission à l'agrégation de mathématiques (2013-2018).
"""

import sys
import os
import glob
import csv
import sqlite3
import re


nom_sqlite = "resultats_agreg.sqlite"


def ecrire_donnees():
    # on récupère les CSV
    liste_fichiers_csv = glob.glob('./donnees_csv/*.csv')
    # on créé ou on se connecte à la base SQLite
    connection = sqlite3.connect(nom_sqlite)
    con = connection.cursor()
    # On crée une table, une seule fois
    con.execute("""
        CREATE TABLE resultats
        (annee INTEGER, admissibilite INTEGER, genre TEXT, nom TEXT, prenoms TEXT, academie TEXT, rang INTEGER)
    """)
    # on va lire chaque CSV, y insérer les données
    for fichier_csv in liste_fichiers_csv:
        if "Alpha" in fichier_csv and fichier_csv.replace("Alpha", "Merite") in liste_fichiers_csv:
            continue
        print(f"fichier_csv = {fichier_csv}")
        nom_html = os.path.basename(fichier_csv).replace('.csv', '')
        annee = re.search('[0-9]+', nom_html)[0]
        #
        est_merite = "Merite" in nom_html
        est_admissibilite = "Adm" in nom_html
        est_alpha = "Alpha" in nom_html
        # on lit le fichier
        with open(fichier_csv, 'r') as f_csv:
            for row in f_csv:
                print("\nrow =", row[:-1])
                tuple_row = (annee, est_admissibilite, ) + tuple(row[:-1].split(','))
                if est_admissibilite or len(tuple_row) == 6:
                    # rang = -1
                    tuple_row += (-1,)
                elif est_alpha or len(tuple_row) == 5:
                    # académie ?, rang = -1
                    tuple_row += ("?", -1,)
                print("tuple_row =", tuple_row)
                con.execute("""
                    INSERT INTO resultats
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, tuple_row)
        connection.commit()  # not needed
    con.close()


def lire_donnees():
    # on se connecte à la base SQLite
    connection = sqlite3.connect(nom_sqlite)
    con = connection.cursor()
    # Récupère liste d'années
    res_requetes = list(con.execute("""
        SELECT annee from resultats
    """))
    annees = sorted(list(set(res[0] for res in res_requetes)))
    print(f"Années : {annees}")
    # Affiche le contenu de la table, pour chaque année
    for annee in annees:
        res_requetes = list(con.execute("""
            SELECT rang, prenoms, nom from resultats
            WHERE annee = ?
                AND rang <= 25
                AND rang > 0
            ORDER BY rang
        """, (annee,)))
        for nom_prenoms in res_requetes:
            print(f"25 premiers de l'année {annee} : {nom_prenoms}")
    # Affiche le nombre d'admissibles et d'admis, par année
    for annee in annees:
        nombre_admissibles = list(con.execute("""
            SELECT COUNT(*) from resultats
            WHERE annee = ?
                AND admissibilite = 1
        """, (annee,)))[0][0]
        nombre_admis = list(con.execute("""
            SELECT COUNT(*) from resultats
            WHERE annee = ?
                AND admissibilite = 0
        """, (annee,)))[0][0]
        print(f"Pour l'année {annee}, il y avait {nombre_admissibles} admissibles à {nombre_admis} admis.")

    con.close()


def main(lire=False):
    if lire:
        return lire_donnees()
    else:
        return ecrire_donnees()


if __name__ == '__main__':
    from sys import argv
    lire = '--lire' in argv
    main(lire)
