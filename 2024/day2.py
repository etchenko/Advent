from shared.shared import read_input

def process_input():
    lines = read_input('day2.txt')
    return [[int(num) for num in item.split(' ')] for item in lines]
    
def sol1(data):
    safe_count = 0
    for report in data:
        safe_count += get_report_safety(report)
    return safe_count

def sol2(data):
    safe_count = 0
    for report in data:
        safe = get_report_safety(report)
        if not safe:
            for i, _ in enumerate(report):
                copy = report.copy()
                del copy[i]
                if get_report_safety(copy):
                    safe = 1
                    continue
        safe_count += safe
    return safe_count

def get_report_safety(report):
    safe = 1
    cur = 0
    sign = get_sign(report[1] - report[0])
    while cur < (len(report) - 1) and safe:
        diff = report[cur + 1] - report[cur]
        if abs(diff) < 1 or abs(diff) > 3:
            safe = 0
        cur += 1
        if get_sign(diff) != sign:
            safe = 0
    return safe

def get_sign(number):
    if number > 0:
        return 1
    return -1

def main():
    # Read in input
    data = process_input()
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