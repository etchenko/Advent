import re

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def sumPossibles(data):
    tot = 0
    for line in data:
        valid = True
        line = line[:-1]
        game,rounds = line.split(':')
        game = game.split(' ')[1]
        rounds = rounds.split(';')
        for round in rounds:
            valid = valid and checkRound(round)
        if valid:
            tot += int(game)
    return tot

def checkRound(round):
    limits = {'green': 13, 'red': 12, 'blue':14}
    colors = round.split(',')
    for color in colors:
        colorSplit = color.split(' ')
        if limits[colorSplit[2]] < int(colorSplit[1]):
            return False
    return True

def sumPowers(data):
    tot = 0
    for line in data:
        valid = True
        line = line[:-1]
        game,rounds = line.split(':')
        game = game.split(' ')[1]
        tot += getPowerRounds(rounds)
    return tot

def getPowerRounds(rounds):
    maxs = {'red':0,'green':0,'blue':0}
    cubes = re.split(',|;',rounds)
    for cube in cubes:
        _,num,color = cube.split(' ')
        if maxs[color] < int(num):
            maxs[color] = int(num)
    return maxs['green']*maxs['blue']*maxs['red']
    


def main():
    # Read in input
    data = input()
    print(sumPossibles(data))
    print(sumPowers(data))


if __name__ == "__main__":
    main()