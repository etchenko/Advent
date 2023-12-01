class Storage:
    '''
    A class specifying a storage system
    '''
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
    
class File(Storage):
    '''
    A file class meant to represent a file
    '''
    def __init__(self, name, size, parent):
        super().__init__(name, size, parent)

class Directory(Storage):
    '''
    A directory class, which can contain other directories or files
    '''
    def __init__(self, name, parent):
        super().__init__(name, 0, parent)
        self.children = []
        self.child_names = []
    
    def update(self):
        ''' 
        Update the size value of the directory, as well as all of the parent directories
        '''
        self.size = 0
        for child in self.children:
            self.size += child.size
        if self.parent:
            self.parent.update()
    
    def __add_child(self, child):
        ''' 
        Add a child to the directory
        '''
        self.children.append(child)
        self.child_names.append(child.name)
        self.update()
        return child
    
    def child_exists(self, child):
        '''
        Check if the name is in the directory
        '''
        return child in self.child_names
    
    def add_dir(self, name):
        '''
        Add a directory as a child
        '''
        if name in self.child_names:
            return self.__get_child(name)
        else:
            child = Directory(name, self)
            return self.__add_child(child)

    def __get_child(self, name):
        '''
        Return the child Storage object with the given name
        '''
        return self.children[self.child_names.index(name)]
    
    def add_file(self, filename, size):
        '''
        Add a file to the children of the directory
        '''
        if filename in self.child_names:
            return self.__get_child(filename)
        else:
            child = File(filename, size, self)
            return self.__add_child(child)
    
    def get_root(self):
        '''
        Get back to the root directory
        '''
        if self.parent:
            return self.parent.get_root()
        else:
            return self
    
    def move_to_child(self, instr):
        '''
        Return the desired child directory if exists, otherwise create it and return it
        '''
        if self.child_exists(instr):
            return self.__get_child(instr)
        else:
            return self.add_dir(instr)
    
    def get_child_directories(self):
        '''
        Get a list of all the child directories
        '''
        items = []
        for i in self.children:
            if type(i) == Directory:
                items.append(i)
        return items



class Command:
    def __init__(self, curr):
        self.dir = curr

class CD(Command):
    '''
    The 'cd' command
    '''
    def __init__(self, curr, instr):
        super().__init__(curr)
        self.dest = instr
    
    def perform_command(self):
        '''
        Return the directory which we are moving to
        '''
        if self.dest == '..':
            return self.dir.parent
        elif self.dest == '/':
            return self.dir.get_root()
        else:
            return self.dir.move_to_child(self.dest)

class LS(Command):
    '''
    The 'ls' command
    '''
    def __init__(self, curr, items):
        super().__init__(curr)
        self.items = items
    
    def perform_command(self):
        '''
        Create all of the directories and files which are returned by the ls command
        '''
        for item in self.items:
            (first, name) = item.split(' ')
            if first != 'dir':
                self.dir.add_file(name, int(first))
            else:
                self.dir.add_dir(item)
            

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

def instantiate_storage(instructions):
    '''
    Create the storage tree system based on the input received
    '''
    # Instantiate root directory
    root = Directory('/', None)
    curr = root
    i = 0
    while i < len(instructions):
        inst = instructions[i].split(' ')
        if inst[1] == 'cd':
            cd = CD(curr, inst[2])
            curr = cd.perform_command()
            i+= 1
        elif inst[1] == 'ls':
            command = False
            items = []
            i += 1
            while not command and i < len(instructions):
                if instructions[i][0] == '$':
                    command = True
                else:
                    items.append(instructions[i])
                    i += 1
            LS(curr, items).perform_command()
    return root

def get_sizes_100000(root):
    '''
    Get the total size of all the directories with a size smaller than 100000
    '''
    total = 0
    if root.size <= 100000:
        total += root.size
    for i in root.get_child_directories():
        total += get_sizes_100000(i)
    return total

def get_smallest_removable(root):
    '''
    Get the size of the smallest directory which when deleted would leave at least 30000000 space
    '''
    items = [root]
    items.extend(get_smallest_help(root))
    sizes = [i.size for i in items]
    sizes.sort()
    left = 70000000 - root.size
    for i in sizes:
        if i + left > 30000000:
            return i

def get_smallest_help(root):
    '''
    Helper function which returns a list of all directories
    '''
    items = root.get_child_directories()
    for i in items:
        items.extend(get_smallest_help(i))
    return items

def main():
    data = input()
    # Solution 1
    root = instantiate_storage(data)
    sol_1 = get_sizes_100000(root)
    print(f'Solution 1: {sol_1}')
    # Solution 2
    sol_2 = get_smallest_removable(root)
    print(f'Solution 2: {sol_2}')


if __name__ == "__main__":
    main()
