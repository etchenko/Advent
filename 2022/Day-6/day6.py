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

def process(lines, chars):
    line = lines[0]
    buffer = []
    for i, letter in enumerate(line):
        if len(buffer) < chars:
            buffer.append(letter)
        if (len(set(buffer)) == len(buffer)) and len(buffer) ==chars:
            return i + 1
        if len(buffer) == chars:
            buffer.pop(0)
    return 0


def main():
    data = input()
    # Solution 1
    sol_1 = process(data, 4)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = process(data, 14)
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()