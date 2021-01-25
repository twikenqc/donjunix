
import itertools, random

deck=list(itertools.product(["detruire-monstre","stocker-objet","deposer-objet","recule-d'une-case","retour-au-depart"]))
          
random.shuffle(deck)
          
print("vous avez obtenu:")
for i in range(1):
    print(deck[i][0])

pile=[]
pile.append(deck[i][0])

print(pile)

