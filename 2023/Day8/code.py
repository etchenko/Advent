from math import gcd
from functools import reduce

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def path(instructions, paths, start):
    current = start
    it = 0
    while current[2] != 'Z':
        instr = getInstruction(it, instructions)
        current = paths[current][0] if instr == 'L' else paths[current][1]
        it += 1
    return it

def path2(instr, paths):
    currents = [k for k in paths.keys() if k[2] == 'A']
    lens = []
    for curr in currents:
        lens.append(path(instr, paths, curr))
    return reduce(lambda a,b: a*b // gcd(a,b), lens)

def getData(data):
    instructions = ''
    paths = {}
    for line in data:
        if '=' not in line and len(line) > 2:
            instructions = line[:-1]
        elif '=' in line:
            start = line.split(' ')[0]
            left = line.split('(')[1].split(',')[0]
            right = line.split(',')[1][1:].split(')')[0]
            paths[start] = (left,right)
    return instructions, paths

def getInstruction(it, instr):
    return instr[it % len(instr)]


def main():
    # Read in input
    data = input()
    instr, paths = getData(data)
    steps = path(instr, paths, 'AAA')
    steps2 = path2(instr, paths)
    print(steps)
    print(steps2)


if __name__ == "__main__":
    main()