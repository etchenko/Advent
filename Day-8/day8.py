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

def create_array(data):
    '''
    Create the numpy array of trees
    '''
    array = []
    for line in data:
        array.append([int(i) for i in line])
    a=  np.array(array, np.int32)
    return a

def check_subset(sub, i):
    '''
    Check if the tree is visible from this direction
    '''
    for j in sub:
        if j >= i:
            return False
    return True

def check_tree(array, i, j):
    '''
    Check if a tree is visible
    '''
    tree = array[i,j]
    row = array[i,:]
    column = array[:,j]
    left, right, above, below = row[:j], row[j + 1:], column[:i], column[i + 1:]
    if check_subset(left, tree) or check_subset(right, tree) or check_subset(above, tree) or check_subset(below, tree):
        return True
    return False

def count_forest(data):
    '''
    Count the amount of visible trees in the forest
    '''
    sum = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            if check_tree(data, i, j):
                sum += 1
    return sum

def scenic_score(array, i, j):
    '''
    Get the scenic score of a tree
    '''
    tree = array[i,j]
    row = array[i,:]
    column = array[:,j]
    left, right, above, below = row[:j][::-1], row[j + 1:], column[:i][::-1], column[i + 1:]
    return check_score_dir(left, tree)*check_score_dir(right, tree)*check_score_dir(above, tree)*check_score_dir(below, tree)

def check_score_dir(row, item):
    '''
    Get the scenic score in a given direction
    '''
    if len(row) == 0:
        return 0
    found = False
    i = 0
    for i, tree in enumerate(row):
        if tree >= item:
            return i + 1
    return len(row)

def find_best_tree(array):
    '''
    Get the max scenic score
    '''
    best = 0
    for i, row in enumerate(array):
        for j, tree in enumerate(row):
            score = scenic_score(array, i, j)
            best = max(score, best)
    return best

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
