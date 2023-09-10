# -*- coding: utf-8 -*-

import string
import random
import matplotlib.pyplot as plt
import numpy as np
import pylab


tour_counter = 0
rep = ""
z = int(input("Nombre d'itérations"))
lista = []
recu_match = []
fin = [2, 3, 4, 5, 6, 7]
g = 0
while tour_counter != z:
    al = random.randint(0,25)
    rep += list(string.ascii_lowercase)[al]
    tour_counter += 1


f = open("../liste_francais.txt", "r")
text = f.read()
text = text.lower()
for word in text.split():
    if word in rep:
        g += 1
        # print("Mot en cours :", word)
        lista.append(word)
        recu_match.append(len(word))

trie = sorted(recu_match)
trie_mot = sorted(lista)
print(rep)
print(lista)
print(trie)
print(trie_mot)
print(f"Liste fin : {fin}")


nombres = {
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5': 0,
    '6': 0,
    '7': 0,
}

for nb in trie:
    #print(str(nb))
    if str(nb) in nombres:
        nombres[str(nb)] += 1
    else:
        pass

print(type(trie[0]))
print(nombres)
plt.figure(figsize=(9, 3))
plt.bar(fin, nombres.values())
plt.ylabel('Nombres de mots',color='black', weight='bold', size=16)
plt.xlabel('Taille des mots',color='black', weight='bold', size=16)
plt.title(f"Nombre de mot trouvé : {g} sur {z} lettres")
plt.show()