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

def main():
    '''
    Main method to get the solution
    '''
    data = create_array(input())
    # Solution 1
    sol_1 = count_forest(data)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = find_best_tree(data)
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()
