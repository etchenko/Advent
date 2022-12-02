def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines


def count_elf_food(data):
    '''
    Count the amount of food each elf has, and return the array
    '''
    elf_food = [0]
    j = 0
    for line in data:
        if line != '\n':
            elf_food[j] += int(line)
        else:
            j += 1
            elf_food.append(0)
    return elf_food

def max_index(data):
    '''
    Find the index of the elf with the most food
    '''
    maxi = 0
    max_loc = 0
    for i, num in enumerate(data):
        if num > maxi:
            maxi = num
            max_loc = i
    return max_loc


def main():
    # Read in input
    data = input()
    # Get the total food for each elf
    food_array = count_elf_food(data)
    # Sort the array
    food_array.sort()
    # Solution 1
    print(food_array[-1]) 
    # Solution 2
    print(sum(food_array[-3:]))


if __name__ == "__main__":
    main()