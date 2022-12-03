def input():
    '''
    Read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines

def get_item(row):
    row = row[0:-1]
    first = row[0:int(len(row)/2)]
    second = row[int(len(row)/2):]
    for i in first:
        if i in second:
            print(i)
            return i
    return None

def score(data):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    for row in data:
        item = get_item(row)
        sum+= letters.index(item) + 1
    return sum

def get_badge(rows):
    for i in rows[0]:
        if (i in rows[1]) and i in rows[2]:
            return i

def badge_total(data):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    for i in range(0, len(data), 3):
        items = data[i:i+3]
        item = get_badge(items)
        sum += letters.index(item) + 1
    return sum


def main():
    data = input()
    # Solution 1
    sol_1 = score(data)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = badge_total(data)
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()