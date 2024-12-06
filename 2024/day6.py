from shared.shared import read_input
    
def sol1(data, guard):
    return len(traverse(data, guard, (-1,0))[0])

# BRUTE FORCE. VERY SLOW
def sol2(data, starting):
    visited, _ = traverse(data, starting, (-1,0))
    sum_loops = 0
    for (i, j) in visited:
        if data[i][j] != "^" and data[i][j] != "#":
            current = data.copy()
            current[i] = current[i][:j] + "#" + current[i][j+1:]
            _, looped = traverse(current, starting, (-1,0))
            sum_loops += 1 if looped else 0
    return sum_loops
    
def find_guard(data):
    # Find the guard in the array (Not the most efficient way)
    for i, line in enumerate(data):
        for j, char in enumerate(line.replace('\n','')):
            if char == "^":
                return (i,j)
            
# returns the number of visited cells and whether the guard has looped
def traverse(data, guard, direction):
    visited, visited_dir = set(), set()

    while guard[0] > -1 and guard[1] > -1:
        if (guard[0], guard[1], direction[0], direction[1]) in visited_dir:
            return len(visited), True
        visited.add(guard)
        visited_dir.add((guard[0], guard[1], direction[0], direction[1]))
        new_location = tuple(map(sum, zip(guard, direction)))
        try:
            assert(new_location[0] > -1 and new_location[1] > -1)
            if data[new_location[0]][new_location[1]] == "#":
                direction = (direction[1], -direction[0])
            else:
                guard = new_location
        except:
            break
    return visited, False

def main():
    # Read in input
    data = read_input('day6.txt')
    guard = find_guard(data)
    # Solution 1
    out = sol1(data, guard)
    print(out) 
    # Solution 2
    out2 = sol2(data, guard)
    print(out2)

if __name__ == "__main__":
    main()