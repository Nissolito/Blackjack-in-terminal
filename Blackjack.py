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

sleep(1)

spelIgång += 1
print('\n'*20)
print(stortKort(dealerHand,1,1))
print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
print('\n')
spelarHand.append(Kort[0])
Kort.pop(0)
print(stortKort(spelarHand,2,0))
print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')


while True:
	hitStand = "1.Hit, 2.stand: "
	if sum(KollaMägnd(spelarHand)) <=21 and spelIgång<3:
		for i in range(3,6):
			spelIgång = i
			if input(hitStand) == "2":
				break
			print('\n'*20)
			spelarHand.append(Kort[0])
			Kort.pop(0)
			print(stortKort(dealerHand,1,1))
			print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
			print('\n')
			print(stortKort(spelarHand,i,0))
			print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')
	else:
		#while sum(KollaMägnd(dealerHand)) <= 17:
		for i in range(2,6):
			sleep(1)
			if sum(KollaMägnd(dealerHand)) >= 17:
				break
			print('\n'*20)
			dealerHand.append(Kort[0])
			Kort.pop(0)
			print(stortKort(dealerHand,i,0))
			print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
			print('\n')
			print(stortKort(spelarHand,spelIgång-1,0))
			print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')
		break
dealerValue = sum(KollaMägnd(dealerHand))
spelarValue = sum(KollaMägnd(spelarHand))
if dealerValue <= 21 and spelarValue > 21:
	print("Datorn vann!")
elif spelarValue <= 21 and dealerValue >21:
	print("Du vann!")
elif dealerValue >= spelarValue:
	print("Datorn vann!")
else:
	print("Du vann!")