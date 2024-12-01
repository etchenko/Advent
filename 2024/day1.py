from shared.shared import read_input
def process_input():
    lines = read_input('day1.txt')
    output = [item.split('   ') for item in lines]
    return [int(x[0]) for x in output], [int(x[1]) for x in output]
    
def sol1(data1, data2):
    data1.sort()
    data2.sort()
    return sum([abs(x - y) for x,y in zip(data1,data2)])

def sol2(data1, data2):
    return sum([data2.count(x)*x for x in data1])

def main():
    # Read in input
    data1, data2 = process_input()
    # Solution 1
    out = sol1(data1, data2)
    # Solution 1
    print(out) 
    # Get second calibration
    out2 = sol2(data1, data2)
    # Solution 2s
    print(out2)

if __name__ == "__main__":
    main()