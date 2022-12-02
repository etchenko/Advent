def input():
    '''
    Read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines

def get_round_score(row):
    '''
    Get the score of a round given the first rule
    '''
    hands = {'X':0,'Y':1,'Z':2,'A':0,'B':1,'C':2}
    opp = hands[row[0]]
    me = hands[row[2]]

    if opp == me:
        return me + 1 + 3
    if (opp + 1)%3 == me:
        return me + 1 + 6
    else:
        return me + 1

def get_round_score_2(row):
    '''
    Get the score of the round given the second rule
    '''
    hands = {'A':0,'B':1,'C':2}
    opp = hands[row[0]]
    me = row[2]

    if me == 'X':
        return ((opp - 1)%3) + 1
    if me == 'Y':
        return opp + 4
    if me == 'Z':
        return ((opp + 1)%3) + 7

def get_total_score(data, rules):
    '''
    Get the total score of the game given the rule
    '''
    total = 0
    for i in data:
        if rules == 1:
            total += get_round_score(i)
        else:
            total += get_round_score_2(i)
    return total

def main():
    data = input()
    # Solution 1
    print(f'Solution 1: {get_total_score(data, 1)}')
    # Solution 2
    print(f'Solution 2: {get_total_score(data, 2)}')


if __name__ == "__main__":
    main()