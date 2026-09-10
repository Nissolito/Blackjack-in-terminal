from Kort import *
from time import sleep
while True:
    randomOrdning(Kort)
    spelarHand = []
    dealerHand = []
    splitHand = []
    spelIgång = 1

    spelarHand.append(Kort[0])
    Kort.pop(0)
    dealerHand.append(Kort[0])
    Kort.pop(0)
    print(stortKort(dealerHand,1,1))
    print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
    print(stortKort(spelarHand,1,1))
    print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')

    playerHitorstand(spelarHand,dealerHand, 0,splitHand)
    Results(spelarHand,dealerHand)
    if input("Play again?(Y/n):") == "n":
        break
