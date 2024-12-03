import re
## Trying to write shortest code (even if it's ugly)

def process_input():
    with open('day3.txt', 'r') as f:
        content = f.read()
    return content

def handle_insts(content, inst, func, en="", dis=""):
    x = re.findall(inst + ('' if not en else '|'+en+'|'+dis), content)
    active, sum = 1, 0
    for i in x:
        active = 1 if i == en.replace('\\','') else 0 if i == dis.replace('\\','') else active
        if active and re.match(inst,i):
            sum += func(i)
    return sum

def get_mul(inst):
    x,y = re.findall('[0-9]{1,3}', inst)
    return int(x) * int(y)

def main():
    data = process_input()
    print(handle_insts(data,'mul\([0-9]{1,3},[0-9]{1,3}\)',get_mul))
    print(handle_insts(data,'mul\([0-9]{1,3},[0-9]{1,3}\)',get_mul,'do\(\)','don\'t\(\)'))

if __name__ == "__main__":
    main()