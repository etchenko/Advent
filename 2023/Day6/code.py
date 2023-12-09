import re

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def ways(data, kerning = False):
    raceTimes = []
    distances = []
    for line in data:
        if line.split(':')[0] == 'Time':
            raceTimes = readNums(line, kerning)
        else:
            distances = readNums(line, kerning)
    sums = [1 for i in range(len(raceTimes))]
    for i, distance in enumerate(distances):
        sumDistance = 0
        race = int(raceTimes[i])
        for mills in range(0,race):
            if (race - mills)*mills > int(distance):
                sumDistance += 1
        sums[i] = sumDistance
    mult = 1
    for i in sums:
        mult = mult*i
    return mult



def readNums(line, kerning = False):
    nums = []
    data = line.split(':')[1]
    currNum = ''
    for char in data:
        if char in '0123456789':
            currNum += char
        else:
            if currNum != '':
                if not kerning:
                    nums.append(currNum)
                    currNum = ''
    if kerning:
        nums.append(currNum)
    return nums



def main():
    # Read in input
    data = input()
    points = ways(data)
    points2 = ways(data, True)
    print(points)
    print(points2)


if __name__ == "__main__":
    main()