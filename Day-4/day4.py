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

def unwrap(row):
    '''
    Unwrap each row of input to get the pair of ranges
    '''
    cols = row.split(',')
    first, second = cols[0], cols[1]
    first = first.split('-')
    second = second.split('-')
    return first, second

def pair_comparison(first, second, comp_type):
    '''
    Compare to range pairs based on the comparison type

    Parameter comp_type: a sting describing the comparison to be made
        'contain': Check if one range contains the other
        'overlap': Check if one range overlaps with the other
    '''
    op = 0 if (comp_type == 'contain') else 1
    # Check first pair compared to second
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[(1 - op)]):
        return True
    # Check second pair compared to first
    elif int(first[0]) >= int(second[0]) and int(first[(1 - op)]) <= int(second[1]):
        return True
    return False

def ranges_count(data, comp_type):
    '''
    Count the number of range pairs where the chosen comparison is true

    Parameter comp_type: a sting describing the comparison to be made
        'contain': Check if one range contains the other
        'overlap': Check if one range overlaps with the other
    '''
    sum = 0
    for row in data:
        first, second = unwrap(row)
        if pair_comparison(first, second, comp_type):
            sum += 1
    return sum

def main():
    data = input()
    # Solution 1
    sol_1 = ranges_count(data, 'contain')
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = ranges_count(data, 'overlap')
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()