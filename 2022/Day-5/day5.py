import copy

# The initial arrangement of stacks
STACKS = [
    ['D', 'L', 'J','R','V','G','F'],
    ['T', 'P', 'M','B','V','H','J', 'S'],
    ['V', 'H', 'M','F','D','G','P', 'C'],
    ['M', 'D', 'P','N','G','Q'],
    ['J', 'L', 'H','N','F'],
    ['N', 'F', 'V','Q','D','G','T', 'Z'],
    ['F', 'D', 'B','L'],
    ['M', 'J', 'B','S','V','D','N'],
    ['G', 'L', 'D']]

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

def follow_instruction(array, instr, crane):
    '''
    Follow a crane instruction to move crates from one stack to the next

    crane: 
        Move all at once if 9001
        Move one by one if 9000
    '''
    # Get the instructions
    words = instr.split(' ')
    count, start, end = [int(i) - 1 for i in words[1::2]]
    count += 1

    # Get all the crates from the starting stack
    crates = array[start][-count:]
    array[start] = array[start][:-count]
    
    # If moving one by one, reverse the order to add back
    if crane == 9000:
        crates.reverse()
    # Add creates to final stack
    array[end].extend(crates)
    return array

def move_crates(instr, crane):
    '''
    Move all of the crates based on the list of instructions
    '''
    array = copy.deepcopy(STACKS)
    for i in instr:
        follow_instruction(array, i, crane)
    return array

def get_tops(array):
    '''
    Return the top crate from each stack
    '''
    output = ''
    for row in array:
        output += row[-1]
    return output


def main():
    data = input()
    # Solution 1
    sol_1 = get_tops(move_crates(data, 9000))
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = get_tops(move_crates(data, 9001))
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()