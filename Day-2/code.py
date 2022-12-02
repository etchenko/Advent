def input():
    result = []
    with open('input.txt','r') as f:
        lines = f.readlines()
        result = [x for x in lines]
    return result

def get_round_score(row):
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
    hands = {'A':0,'B':1,'C':2}
    opp = hands[row[0]]
    me = row[2]

    if me == 'X':
        return ((opp - 1)%3) + 1
    if me == 'Y':
        return opp + 4
    if me == 'Z':
        return ((opp + 1)%3) + 7



def get_total_score(data):
    total = 0
    for i in data:
        total += get_round_score_2(i)
    return total



def main():
    data = input()
    print(get_total_score(data))


if __name__ == "__main__":
    main()