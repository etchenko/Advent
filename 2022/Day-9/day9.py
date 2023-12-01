import numpy as np
import math

def input():
    '''
    Read in the input
    '''
    with open('input2.txt','r') as f:
        lines = f.readlines()
    data = []
    for i in lines:
        data.append(i[0:-1])
    return data

def rope_pair(first, second):
    hi, hj = first[0], first[1]
    ti, tj = second[0], second[1]
    if tj != hj and hi != ti:
        if hi > ti + 1 or hi < ti - 1 or hj > tj + 1 or hj < tj - 1:
            ti += math.copysign(1, hi - ti)
            tj += math.copysign(1, hj - tj)
    elif hi > ti + 1:
        ti += 1
    elif hi < ti - 1:
        ti -= 1
    elif hj > tj + 1:
        tj += 1
    elif hj < tj - 1:
        tj -= 1
    return [ti, tj]

def long_rope(data):
    knots = [[0,0]]*10
    locations = [[0,0]]
    for row in data:
        direction, quant = row.split(' ')
        for i in range(int(quant)):
            if direction == 'R':
                knots[0][0] += 1
            elif direction == 'U':
                knots[0][1] += 1
            elif direction =='D':
                knots[0][1] -= 1
            elif direction == 'L':
                knots[0][0] -= 1
            for j in range(len(knots) - 1):
                knots[j + 1] = rope_pair(knots[j], knots[j + 1])
            locations.append(knots[9])
    return locations


def rope_simulation(data):
    hi, hj = 0, 0
    ti, tj = 0, 0
    locations = [(0,0)]
    for row in data:
        direction, quant = row.split(' ')
        for i in range(int(quant)):
            if direction == 'R':
                hi += 1
            elif direction == 'U':
                hj += 1
            elif direction =='D':
                hj -= 1
            elif direction == 'L':
                hi -= 1
            if tj != hj and hi != ti:
                if hi > ti + 1 or hi < ti - 1:
                    ti += (hi - ti)/2
                    tj += hj - tj
                if hj > tj + 1 or hj < tj - 1:
                    tj += (hj- tj)/2
                    ti += hi - ti
            elif hi > ti + 1:
                ti += 1
            elif hi < ti - 1:
                ti -= 1
            elif hj > tj + 1:
                tj += 1
            elif hj < tj - 1:
                tj -= 1
            locations.append((ti, tj))
    return locations

def unique_locations(loc):
    unique = [list(x) for x in set(tuple(x) for x in loc)]
    return len(unique)
        

def main():
    '''
    Main method to get the solution
    '''
    locations = rope_simulation(input())
    # Solution 1
    sol_1 = unique_locations(locations)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = long_rope(input())
    print(f'Solution 2: {unique_locations(sol_2)}')


if __name__ == "__main__":
    main()
