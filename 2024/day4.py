from shared.shared import read_input
    
def sol1(data):
    sum = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "X":
                sum += find_word(i,j,data,"XMAS")
    return sum

def sol2(data):
    sum = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "A" and i > 0 and i < len(data)-1 and j > 0 and j < len(line)-2:
                sum += find_cross(i,j,data)
    return sum

def find_word(i,j,data,word):
    sum = 0
    for dir in range(8):
        valid = True
        for k in range(len(word)):
            row,col = get_coords(i,j,k,dir)
            if row < 0 or col < 0:
                valid = False
                break
            try:
                if data[row][col] != word[k]:
                    valid = False
                    break
            except:
                valid = False
                break
        if valid:
            sum += 1
    return sum

def find_cross(i,j,data):
    try:
        diag1 = data[i-1][j-1]+ data[i][j]+data[i+1][j+1]
        diag2 = data[i-1][j+1]+ data[i][j]+data[i+1][j-1]
        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            return 1
    except:
        pass
    return 0

def get_coords(i,j,k,dir):
    if dir == 0:
        return i+k,j
    elif dir == 1:
        return i,j+k
    elif dir == 2:
        return i+k,j+k
    elif dir == 3:
        return i+k,j-k
    elif dir == 4:
        return i,j-k
    elif dir == 5:
        return i-k,j
    elif dir == 6:
        return i-k,j-k
    else:
        return i-k,j+k
    
def main():
    # Read in input
    data = read_input('day4.txt')
    # Solution 1
    out = sol1(data)
    # Solution 1
    print(out) 
    # Get second solution
    out2 = sol2(data)
    # Solution 2
    print(out2)

if __name__ == "__main__":
    main()