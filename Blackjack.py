from Kort import *
from time import sleep

randomOrdning(Kort)
# print(randomOrdning(Kort))
# print(KollaMägnd(['H6','C5']))
# Kort.pop(0)
# print(Kort)
print('\n'*2)
spelarHand = []
dealerHand = []
spelIgång = 1
print('\n'*20)
dealerHand.append(Kort[0])
Kort.pop(0)   
print(stortKort(dealerHand,1,1))
print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
spelarHand.append(Kort[0])
Kort.pop(0)
print(stortKort(spelarHand,1,1))
print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')
# print(stortKort(dealerHand))


print('\n'*20)
print(stortKort(dealerHand,1,1))
print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
print('\n')
spelarHand.append(Kort[0])
Kort.pop(0)
print(stortKort(spelarHand,2,0))
print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')

while True:
	