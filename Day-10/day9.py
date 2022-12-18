import numpy as np

def input():
    '''
    Read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    data = []
    for i in lines:
        data.append(i[0:-1])
    return data

def cycles(data):
    output = [1]
    i = 0
    for row in data:
        instr = row.split(' ')
        if instr[0] == 'noop':
            output.append(output[i])
            i += 1
        elif instr[0] == 'addx':
            output.append(output[i])
            output.append(output[i + 1] + int(instr[1]))
            i += 2
    return output

def count_strength(cycles):
    return cycles[19]*20 + cycles[59]*60 + cycles[99]*100 + cycles[139]*140 + cycles[179]*180+cycles[219]*220

def draw_sprite(cycles):
    output = ''
    for i, cycle in enumerate(cycles):
        if i%40 == 0:
            output = output + '\n'
        if i%40 >= cycle - 1 and i%40 <= cycle + 1:
            output = output + '.'
        else:
            output = output + '#'
    return output

def main():
    '''
    Main method to get the solution
    '''
    cyc = cycles(input())
    # Solution 1
    sol_1 = count_strength(cyc)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = draw_sprite(cyc)
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()
