def input():
    '''
    Method to read in the input
    '''
    with open('input.txt','r') as f:
        lines = f.readlines()
    return lines


def calibration(data,clean = False):
    '''
    Count the sum of the calibration
    '''
    total = 0
    for line in data:
        line = clean_line(line) if clean else line
        first = find_int(line)
        last = find_int(line,True)
        total += int(first + last)
    return total

def find_int(line, reverse = False):
    '''
    Find the first (or last) int in the line
    '''
    line = line [::-1] if reverse else line
    for i in line:
        if i.isdigit():
            return i
    return ""

def clean_line(line):
    '''
    Clean the line, converting written numbers to integers
    '''
    nums = ['one','two','three','four','five','six','seven','eight','nine']
    num_conv = ['o1e','t2o','t3e','f4r','f5e','s6x','s7n','e8t','n9e']
    for i,num in enumerate(nums):
        line = line.replace(num,num_conv[i])
    return line
    

def main():
    # Read in input
    data = input()
    # Get the calibration
    cal_sum = calibration(data)
    # Solution 1
    print(cal_sum) 
    # Get second calibration
    cal_sum2 = calibration(data,True)
    # Solution 2
    print(cal_sum2)


if __name__ == "__main__":
    main()