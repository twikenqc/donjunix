import itertools, random
deck=list(itertools.product(["detruire-monstre","stocker-objet","deposer-objet","recule-d'une-case","retour-au-depart"]))
a=[]
z=0
for i in range (1):
    random.shuffle(deck)
    if z< 21:
            print("vous avez obtenu:",deck[i][0])
            a.append(deck[i][0])
            z=z+1
            print(z)
    else:
            print('fin')

