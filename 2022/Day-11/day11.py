import numpy as np
import math

class Monkeys():
    def __init__(self, verbose, worry) -> None:
        self.monkeys = {}
        self.verbose = verbose
        self.worry = worry
    
    def create_monkeys(self, input):
        i = 0
        while i < len(input):
            id = int(input[i].split(' ')[1].split(':')[0])
            self.add_monkey(id)
            items = [int(j[1:]) for j in input[i + 1].split(':')[1].split(',')]
            self.monkeys[id].add_items(items)
            self.monkeys[id].create_operation(input[i + 2])
            test = int(input[i + 3].split(':')[1].split(' ')[3])
            first = int(input[i + 4].split(':')[1].split(' ')[4])
            second = int(input[i + 5].split(':')[1].split(' ')[4])
            self.monkeys[id].create_test(test, first, second)
            i += 7
        cycle = np.prod([monkey.test for monkey in self.monkeys.values()])
        for monk in self.monkeys.values():
            monk.set_cycle(cycle)

    def add_monkey(self, id):
        self.monkeys[id] = Monkey(id, self.verbose, self.worry)
    
    def round(self):
        for i in range(max(self.monkeys.keys()) + 1):
            items = self.monkeys[i].operations()
            self.throw_items(items)
    
    def throw_items(self, items):
        for id, item in items:
            self.monkeys[id].add_item(item)
    
    def rounds(self, num):
        for i in range(num):
            self.round()
        
    def monkey_business(self):
        bus = []
        for id, monkey in self.monkeys.items():
            bus.append(monkey.thrown)
        bus.sort()
        print(bus)
        return bus[-1]*bus[-2]

class Operation():
    def __init__(self, text) -> None:
        self.ops = {'+': lambda x, y: x + y,
                        '-': lambda x, y: x - y,
                        '*': lambda x, y:x * y,
                        '/': lambda x, y: x/y}
        self.operation = text.split(' ')[6]
        self.mod = text.split(' ')[-1]
        self.self_mod = False
        if self.mod == 'old':
            self.self_mod = True
        else:
            self.mod = int(self.mod)
    
    def __call__(self, nums):
        other = nums if self.self_mod else self.mod
        return self.ops[self.operation](nums,other)                         
        

class Monkey():
    def __init__(self, id, verbose, worry) -> None:
        self.id = id
        self.items = []
        self.thrown = 0
        self.verbose = verbose
        self.worry = worry
    
    def add_items(self, items):
        for item in items:
            self.items.append(item)
        
    def add_item(self, item):
        self.items.append(item)
    
    def create_operation(self, text):
        self.op = Operation(text)
    
    def create_test(self, test, first, second):
        self.test = test
        self.first = first
        self.second = second
    
    def set_cycle(self, cycle):
        self.cycle = cycle

    def __item_operation(self, item):
        changed = self.op(item)
        if not self.worry:
            return changed
        else:
            return changed // 3
    
    def __throw_item(self, item):
        self.thrown += 1
        item = item % self.cycle
        if item%self.test == 0:
            if self.verbose:
                print(f'        Current worry level is divisible by {self.test}')
            return (self.first, item)
        else:
            if self.verbose:
                print(f'        Current worry level is not divisible by {self.test}')
            return (self.second, item)
    
    def operations(self):
        if self.verbose:
            print(f'Monkey {self.id}:')
        thrown = []
        while len(self.items) > 0:
            item = self.items.pop(0)
            inspected = self.__item_operation(item)
            monk_id, item_new = self.__throw_item(inspected)
            thrown.append((monk_id, item_new))
            if self.verbose:
                print(f'    Monkey inspects an item with a worry level of {item}')
                print(f'        Current Worry Level {inspected}')
                print(f'        Item with worry level {inspected} is thrown to monkey {monk_id}')
        return thrown

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




def main():
    '''
    Main method to get the solution
    '''
    monkeys = Monkeys(verbose = False, worry = True)
    monkeys.create_monkeys(input())
    monkeys.rounds(20)
    # Solution 1
    sol_1 = monkeys.monkey_business()
    print(f'Solution 1: {sol_1}')
    # Solution 2
    monkeys_no_worry = Monkeys(verbose = False, worry = False)
    monkeys_no_worry.create_monkeys(input())
    monkeys_no_worry.rounds(10000)
    sol_2 = monkeys_no_worry.monkey_business()
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()
