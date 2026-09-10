from random import *
# TEST all variables to make sure of working correct # 
TEST = bool(0)
def randomOrdning(k=list()):
    '''Literally just a shuffle function. Why does this exist?'''
    shuffle(k)
    return k

def KollaMägnd(x=list):
    '''Makes a list with the values of all cards in the given list(hand)
    if sum of cards exceed a value of 21 and there is at least one ace on
    hand, then an ace will have its value changed from 11 to 1.'''
    summa = []
    for i in range(len(x)):
        # y = x[i][:-1]
        # print(y)
        try:
             match int(x[i][:-1]):
                  case int():
                       summa += [int(x[i][:-1])]
        except ValueError:
            match x[i][:-1]:

                case 'J'|'Q'|'K':
                        summa += [10]
                case 'A':
                        summa += [11]
                case _:
                        summa +=[0]
        # change ace from a value of 11 to 1 if needed
        if sum(summa) > 21:
            try:
                findAce = summa.index(11)
                summa[findAce] = 1
                # print(summa[findAce])
            except ValueError:
                 pass
    return summa

def stortKort(valuta=list(), nVisade=1, gomKort=1):
    '''Creates big cards for display by stitching together lists. input
    the list of cards to make big cards, the amount of showncards shown
    from left to right, and how many hidden cards should be shown'''
    stort = []
    storList = []
    storListRem = []
    storString = ''
    if nVisade != 0:
        for i in range(nVisade):
            # print(valuta)
            # match valuta[i][len(valuta[i])-1]:
            # print(valuta[i][-1])
            match valuta[i][-1]:
                case 'H':
                       Valör = '\U00002764'
                case 'S':
                       Valör = '\U00002664'
                case 'D':
                       Valör = '\U00002666'
                case 'C':
                       Valör = '\U00002667'
                case _:
                       Valör =valuta[i][len(valuta[i])-1]
            stort.append([f'┌───────────┐',
                          f'│{valuta[i]}'.ljust(12)+'│',
                          f'│           │',
                          f'│           │',
                          f'│           │',
                          f'│     {Valör}     │',
                          f'│           │',
                          f'│           │',
                          f'│           │',
                          f'│'+f'{valuta[i]}│'.rjust(12),
                          f'└───────────┘'])
            # print(f'Stort: {stort}')  
    # Design for the backside of the cards       
    kortBack = ['\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591', # '\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025CF\U000025D9\U000025CF',
                '\U00002591\U00002592\U00002591\U00002592\U00002591\U00002591\U00002593\U00002592\U00002591\U00002591\U00002591', # '\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF'+'\U0000256D\U0000256E\U000025CF',
                '\U00002592\U00002593\U00002593\U00002588\U00002592\U00002592\U00002591\U00002593\U00002592\U00002591\U00002593',# '\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9'+'\U0000256F\U00002570\U000025D9',
                '\U00002593\U00002593\U00002588\U00002593\U00002588\U00002593'+'\U0001FB60\U0001FB55'+'\U00002593\U00002593\U00002588', # \U000025BC
                '\U00002588\U00002588\U00002588'+'\U0001FB5D\U0001FB5A\U0001FB6D  \U0001FB65\U0001FB52'+'\U00002588',
                '\U00002588\U00002588'+'\U0001FB60\U0001FB57  \U00002572  \U0001FB62'+'\U0001FB55',
                '\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594',
                '\U00002594\U00002594\U00002594\U0001FBB2\U0001FBB3\U0001FBB2\U0001FBB3\U00002594\U00002594\U00002594\U00002594',
                '\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594']
    # creates hidden cards from the design above
    if gomKort != 0:
        for i in range(gomKort):
            stort.append([f'┌───────────┐',
                          f'│{kortBack[0]}│',
                          f'│{kortBack[1]}│',
                          f'│{kortBack[2]}│',
                          f'│{kortBack[3]}│',
                          f'│{kortBack[4]}│',
                          f'│{kortBack[5]}│',
                          f'│{kortBack[6]}│',
                          f'│{kortBack[7]}│',
                          f'│{kortBack[8]}│',
                          f'└───────────┘']) 
    # for i in range(len(stort)):
    for j in range(len(stort[0])):
        for k in range(len(stort)):
            storListRem.append(stort[k][j]) # Sätter ihopp varje rad (['│C7         │', '│D6         │', '│H5         │'])
            # print(f'storListRem{j}{storListRem}')
        # print("XXXXXXXXXXXXXXXXXXXXXXXX")   
        storList.append(storListRem) # Sätter ihopp alla kortremsor i samma lista
        if TEST:
             print(f"Variable storListRem: \n{storListRem}")
        storListRem = []
        # storList.append(stort[0][j] + stort[1][j])
    # print(f'Test storList\n{storList} och Len: {len(storList)}')
    for i in range(len(storList)):
        for j in range(len(storList[i])):
            storString += ''.join(storList[i][j])
        storString += '\n'
    if TEST:
        print(f"Variable stort: \n{stort}")
        print(f"Variable storList: \n{storList}")
        print(f"Variable kortBack: \n{kortBack}")
        print(f"Variable storList: \n{storList}")
        print(f"Variable storString: \n{storString}")
    return storString

def Results(PlayerHand=list(),DealerHand = list):
    '''Compares two hands against eachother, meant to be with variables
    for the computers/dealers hand and then one of the players hands'''
    dealerValue = sum(KollaMägnd(DealerHand))
    spelarValue = sum(KollaMägnd(PlayerHand))
    if dealerValue == spelarValue:
        print("Oavgjort. Push")
    elif dealerValue <= 21 and spelarValue > 21:
        print("Datorn vann!")
    elif spelarValue <= 21 and dealerValue >21:
        print("Du vann!")
    elif dealerValue > spelarValue:
        print("Datorn vann!")
    else:
        print("Du vann!")

def playerHitorstand(playerCard = list,dealerCard = list,MainorSplit = bool, splitHand = list):
    '''Gives the player the choice to hit, stand, or if the hands two first cards of the same value, be able to split.'''
    MainorSplit = 1
    for i in range(1,5):
        h_s_s = "1.Hit, 2. Stand: "
        if sum(KollaMägnd(playerCard)) > 21:
            return
        if i == 1:
            playerCard.append(Kort[0])
            Kort.pop()
        else:
            while True:
                # print(playerCard[0] +playerCard[1])
                if len(playerCard)== 2 and playerCard[0][:-1] == playerCard[1][:-1]:
                     h_s_s = "1.Hit, 2. Stand, 3. Split: "
                answer = input(h_s_s)
                if answer == "1":
                    playerCard.append(Kort[0])
                    Kort.pop()
                    break
                elif answer == "2":
                    return
                elif answer == "3" and (len(playerCard)== 2 and playerCard[0][:-1] == playerCard[1][:-1]):
                    splitHand.append(playerCard[1])
                    playerCard.pop(1)
                    playerCard.append(Kort[0])
                    Kort.pop()
                    break
        print(stortKort(dealerCard,1,1))
        print(f'Dealer hand: {dealerCard}\n värde {KollaMägnd(dealerCard)}, summa: {sum(KollaMägnd(dealerCard))}')
        print(stortKort(playerCard,i+1,0))
        print(f'Spelar hand: {playerCard}\n värde {KollaMägnd(playerCard)}, summa: {sum(KollaMägnd(playerCard))}')

def deckMaker():
    '''Creates a deck out of four suits and 13 ranks.'''
    Kort = []
    # Suit = ['\U00002764','\U00002660','\U00002666','\U00002663']
    Suit = ['H','S','D','C']
    Rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for i in range(len(Suit)):
        for j in range(len(Rank)):
            Kort.append(Rank[j]+Suit[i])
    orderedKort = tuple(Kort)
    return Kort, orderedKort
Kort = deckMaker()[0]
ordereddeck = deckMaker()[1]

if __name__ == "__main__":
    TEST = bool(0)
    print(stortKort(ordereddeck,13,0))
    testKort = ['2H','10C','AD','AD','AS']
    print(f"stortKort ({testKort}): \n{stortKort(testKort,len(testKort))}")
    print(f"KollaMägnd ({testKort}): \n{KollaMägnd(testKort)}")