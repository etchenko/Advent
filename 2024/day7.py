from shared.shared import read_input
    
def operations(lines, ops):
    total = 0
    for line in lines:
        target, value = int(line.split(':')[0]), [int(x) for x in line.split(' ')[1:]]
        total += test(value[0], value[1:], target, ops)
    return total

def test(total, items, target, ops):
    if len(items) < 1: return target if total == target else 0
    if total > target: return 0
    for op in ops:
        if op == '+': temp = total + items[0]
        if op == '*': temp = total * items[0]
        if op == "||": temp = int(str(total) + str(items[0]))
        if test(temp, items[1:], target, ops): return target
    return 0

def main():
    data = read_input('day7.txt')
    print(operations(data, ['+','*']), operations(data, ['+','*',"||"]))

if __name__ == "__main__":
    main()