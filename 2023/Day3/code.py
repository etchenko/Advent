import re

def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines   

def partSum(data, symbols):
    tot = 0
    numLocs = {}
    i,j=0,0
    while i < len(data):
        while j < len(data[i]):
            if re.search("[1-9]",data[i][j]):
                j2 = j + 1
                while j2 < len(data[i]) and re.search("[0-9]",data[i][j2]):
                    j2 += 1
                done = False
                for k in range(j,j2):
                    if not done and (i,k) in symbols:
                        tot += int(data[i][j:j2])
                        done = True
                    numLocs[i,k] = (j,int(data[i][j:j2]))
                j = j2
            else:
                j += 1
        j = 0
        i += 1
    return tot,numLocs

def getSymbolLocs(data):
    symbols = {}
    gears = {}
    for i,line in enumerate(data):
        for j,ele in enumerate(line):
            if j < len(data[i]) - 1 and not re.search("[.|0-9]",ele):
                symbols[i-1,j]=1
                symbols[i+1,j]=1
                symbols[i-1,j-1]=1
                symbols[i+1,j-1]=1
                symbols[i-1,j+1]=1
                symbols[i+1,j+1]=1
                symbols[i,j+1]=1
                symbols[i,j-1]=1
            if ele == "*":
                gears[i,j]=1
    return symbols,gears

def gearRatios(symbols,locs):
    tot = 0
    for i,j in symbols.keys():
        valid,ratio = checkGear(i,j,locs)
        if valid:
            tot += ratio
    return tot

def checkGear(i,j,locs):
    tot = 0
    ratio = 1
    iss = [i-1,i,i+1]
    jss = [j-1,j,j+1]
    for i in iss:
        found = []
        for j in jss:
            if (i,j) in locs:
                first,num = locs[i,j]
                if not first in found:
                    tot +=1
                    ratio = ratio*num
                    found.append(first)
    return tot == 2,ratio


def main():
    # Read in input
    data = input()
    symbols,gears = getSymbolLocs(data)
    res1,locs = partSum(data,symbols)
    print(res1)
    print(gearRatios(gears,locs))


if __name__ == "__main__":
    main()