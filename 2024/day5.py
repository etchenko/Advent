from shared.shared import read_input
import math

def process_input(file):
    lines = read_input(file)
    rules = {}
    data = []
    ordering = True
    for line in lines:
        if line == '\n':
            ordering = False
            continue

        if ordering:
            first, second = line.replace('\n','').split('|')
            if first not in rules:
                rules[first] = [second]
            else:
                rules[first].append(second)
        else:
            data.append(line.replace('\n','').split(','))
    return rules, data
            
    
def sol(rules, data):
    sum = 0
    sum_incorrect = 0
    for line in data:
        valid = True
        for i, item in enumerate(line):
            if item in rules and valid:
                for rule in rules[item]:
                    if rule in line and line.index(rule) < i:
                        valid = False
                        break
        if valid:
            sum += int(line[math.floor(len(line)/2)])
        else:
            # Inefficient but works
            incorrect = True
            while incorrect:
                swapped = False
                for i, item in enumerate(line):
                    if item in rules and not swapped:
                        for rule in rules[item]:
                            if rule in line and line.index(rule)< i and not swapped:
                                line.insert(line.index(rule), line.pop(i))
                                swapped = True
                if not swapped:
                    incorrect = False
            sum_incorrect += int(line[math.floor(len(line)/2)])
    return sum, sum_incorrect
    
def main():
    # Read in input
    rules, data = process_input('day5.txt')
    out, out2 = sol(rules, data)
    print(out, out2) 

if __name__ == "__main__":
    main()