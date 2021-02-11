from random import *

rightprice = randint(1, 1000)


prix = int(input("Veuillez saisir le prix en 1 et 1000"))
while prix > 1000:
    continue
while prix != rightprice:
    if prix > rightprice:
        print("Le juste prix est inférieur")
        prix = int(input("Veuillez saisir le prix en 0 et 1000"))
    else:
        print("Le juste prix est supérieur")
        prix = int(input("Veuillez saisir le prix en 0 et 1000"))


print("Vous avez trouvé le juste prix qui est de {}".format(rightprice))
