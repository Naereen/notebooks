#!/usr/bin/env bash

# 1. Si besoin, donne les droits createdb à son utilisateur
# sudo -u postgres psql postgres
# sudo -u $USER psql $USER

# 2. Ensuite on lance la commande pgloader
pgloader command
