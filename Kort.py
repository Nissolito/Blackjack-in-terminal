from random import *
# TEST all variables to make sure of working correct # 
TEST = 0
def randomOrdning(k=list()):
    shuffle(k)
    return k

def KollaMägnd(x=list):
    summa = []
    '''for i in range(len(x)):
        match x[i]:
            case '2H'|'2S'|'2D'|'2C':
                    summa += [2]
            case '3H'|'3S'|'3D'|'3C':
                    summa += [3]
            case '4H'|'4S'|'4D'|'4C':
                    summa += [4]
            case '5H'|'5S'|'5D'|'5C':
                    summa += [5]
            case '6H'|'6S'|'6D'|'6C':
                    summa += [6]
            case '7H'|'7S'|'7D'|'7C':
                    summa += [7]
            case '8H'|'8S'|'8D'|'8C':
                    summa += [8]
            case '9H'|'9S'|'9D'|'9C':
                    summa += [9]
            case '10H'|'10S'|'10D'|'10C'|'JH'|'JS'|'JD'|'JC'|'QH'|'QS'|'QD'|'QC'|'KH'|'KS'|'KD'|'KC':
                    summa += [10]
            case 'AH'|'AS'|'AD'|'AC':
                    summa += [11]
            case _:
                    summa +=[0]
    return summa'''

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
    return summa

def stortKort(valuta=list(), nVisade=1, gomKort=1):
    stort = []
    storList = []
    storListRem = []
    storString = ''
    if nVisade ==0:
        return 0
    for i in range(nVisade):
        # print(valuta)
        match valuta[i][len(valuta[i])-1]:
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
    kortBack = ['\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591\U00002591', # '\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025CF\U000025D9\U000025CF',
                '\U00002591\U00002592\U00002591\U00002592\U00002591\U00002591\U00002593\U00002592\U00002591\U00002591\U00002591', # '\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF'+'\U0000256D\U0000256E\U000025CF',
                '\U00002592\U00002593\U00002593\U00002588\U00002592\U00002592\U00002591\U00002593\U00002592\U00002591\U00002593',# '\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9\U000025CF\U000025D9'+'\U0000256F\U00002570\U000025D9',
                '\U00002593\U00002593\U00002588\U00002593\U00002588\U00002593'+'\U0001FB60\U0001FB55'+'\U00002593\U00002593\U00002588', # \U000025BC
                '\U00002588\U00002588\U00002588'+'\U0001FB5D\U0001FB5A\U0001FB6D  \U0001FB65\U0001FB52'+'\U00002588',
                '\U00002588\U00002588'+'\U0001FB60\U0001FB57  \U00002572  \U0001FB62'+'\U0001FB55',
                '\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594',
                '\U00002594\U00002594\U00002594\U0001FBB2\U0001FBB3\U0001FBB2\U0001FBB3\U00002594\U00002594\U00002594\U00002594',
                '\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594\U00002594']
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
        print(f"Variable storListRem: \n{storListRem}")
        print(f"Variable storList: \n{storList}")
        print(f"Variable storString: \n{storString}")
    return storString

Kort = []
# Suit = ['\U00002764','\U00002660','\U00002666','\U00002663']
Suit = ['H','S','D','C']
Rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
for i in range(len(Suit)):
    for j in range(len(Rank)):
        Kort.append(Rank[j]+Suit[i])
orderdKort = tuple(Kort)
# print(stortKort(['2H']))

print(KollaMägnd(['2H','KC','10D']))