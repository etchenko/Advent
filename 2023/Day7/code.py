import functools

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def winnings(data, Joker):
    hands = {}
    sortedHands = []
    sum = 0
    for line in data:
        hand = line.split(' ')[0]
        bet = line[:-1].split(' ')[1]
        hands[hand] = bet
    sortedHands = sorted(list(hands.keys()), key=(functools.cmp_to_key(compareJoker) if Joker else functools.cmp_to_key(compareNormal)))
    for i, hand in enumerate(sortedHands):
        sum += int(hands[hand])*(i + 1)
    return sum

def compareJoker(x,y):
    return compare(x,y,True)

def compareNormal(x,y):
    return compare(x,y,False)


def compare(x,y, Joker = False):
    xTier = getTier(x, Joker)
    yTier = getTier(y, Joker)
    if xTier > yTier:
        return 1
    if xTier < yTier:
        return -1
    cardPower = '23456789TJQKA' if not Joker else 'J23456789TQKA'
    for i,card in enumerate(x):
        if cardPower.find(card) > cardPower.find(y[i]):
            return 1
        elif cardPower.find(card) < cardPower.find(y[i]):
            return -1
    return 0
        

def getTier(cards, Joker):
    unique = ''.join(set(cards))
    jokers = cards.count('J')
    if Joker and ('J' in cards):
        cards = cards.replace('J','')
    if len(unique) == 1:
        return 7
    if jokers > 0 and len(unique) == 2 and jokers + max([cards.count(i) for i in unique]) == 5:
        return 7
    if len(unique) == 2 or (jokers > 0 and len(unique) == 3 and jokers + max([cards.count(i) for i in unique]) >= 3):
        if 4 in [cards.count(i) for i in unique] or (Joker and len(unique) == 3 and jokers + max([cards.count(i) for i in unique]) == 4):
            return 6
        else:
            return 5
    if len(unique) == 3 or (jokers > 0 and len(unique) == 4):
        if 3 in [cards.count(i) for i in unique] or (jokers > 0 and len(unique) == 4):
            return 4
        else:
            return 3
    if len(unique) == 4 or jokers > 0:
        return 2
    return 1
    
    


def main():
    # Read in input
    data = input()
    points = winnings(data, False)
    points2 = winnings(data, True)
    print(points)
    print(points2)


if __name__ == "__main__":
    main()