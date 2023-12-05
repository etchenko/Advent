import re

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def getPoints(data):
    tot = 0
    for line in data:
        tot += getCardPoints(line)
    return tot

def getCardPoints(line):
    tot = 0
    numbers = line[:-1].split(':')[1]
    winning = numbers.split('|')[0].split(' ')
    got = numbers.split('|')[1].split(' ')
    for number in got:
        if number != '':
            if number in winning:
                tot = tot*2 if tot > 0 else 1
    return tot

def getMatches(line):
    tot = 0
    numbers = line[:-1].split(':')[1]
    winning = numbers.split('|')[0].split(' ')
    got = numbers.split('|')[1].split(' ')
    for number in got:
        if number != '':
            if number in winning:
                tot += 1
    return tot


def getPoints2(data):
    copies = {i:1 for i in range(len(data))}
    for line in data:
        cardNum = int(line.split(':')[0].split(' ')[-1]) - 1
        matches = getMatches(line)
        for i in range(cardNum + 1, cardNum + matches + 1):
            current = copies[cardNum]
            if i in copies.keys():
                copies[i] = copies[i] + current
    return sum(copies.values())


def main():
    # Read in input
    data = input()
    points = getPoints(data)
    points2 = getPoints2(data)
    print(points)
    print(points2)


if __name__ == "__main__":
    main()