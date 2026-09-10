from Kort import *
from time import sleep
while True:
	randomOrdning(Kort)
	# print(randomOrdning(Kort))
	# print(KollaMägnd(['H6','C5']))
	# Kort.pop(0)
	# print(Kort)
	print('\n'*2)
	spelarHand = []
	dealerHand = []
	splitHand = []
	spelIgång = 1
	print('\n'*20)
	spelarHand.append(Kort[0])
	Kort.pop(0)
	dealerHand.append(Kort[0])
	Kort.pop(0)
	print(stortKort(dealerHand,1,1))
	print(f'Dealer hand: {dealerHand}\n värde {KollaMägnd(dealerHand)}, summa: {sum(KollaMägnd(dealerHand))}')
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
			for i in range(spelIgång+1,6):
				spelIgång = i
				a = input(hitStand)
				if a != "1" or sum(KollaMägnd(spelarHand)) > 21:
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
				print(stortKort(spelarHand,spelIgång,0))
				print(f'Spelar hand: {spelarHand}\n värde {KollaMägnd(spelarHand)}, summa: {sum(KollaMägnd(spelarHand))}')
			break
	Results(dealerHand,spelarHand)
	if input("Play again?(Y/n)?: ").capitalize() == "N":
		break
