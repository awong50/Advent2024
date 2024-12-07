def makeArray(file):
    list1 = []
    with open(file, 'r') as file:
        for line in file:
            splitted = line.strip()
            list1.append(splitted)
    return list1

def makeSplitArray(file):
    list1 = []
    with open(file, 'r') as file:
        for line in file:
            splitted = line.strip()
            splitArray = []
            for _ in splitted:
                splitArray.append(_)
            list1.append(splitArray)
    return list1


def hFindXMAS(file):
    map = makeArray(file)

    sum = 0

    for _ in map:
        sum += _.count("XMAS")
        sum += _.count("SAMX")

    return sum

def vFindXMAS(file):
    map = makeSplitArray(file)
    
    sum = 0

    for col in range(len(map[0])):
        column = "".join([map[row][col] for row in range(len(map))])
        sum += column.count("XMAS")
        sum += column.count("SAMX")
    return sum       

def dFindXMAS(file):
    map = makeSplitArray(file)
    sum = 0
    rows, cols = len(map), len(map[0])
    
    for row in range(rows - 3):
        for col in range(cols - 3):
            substring = "".join(map[row + i][col + i] for i in range(4))
            if substring == "XMAS" or substring == "SAMX":
                sum += 1
    
    for row in range(rows - 3):
        for col in range(3, cols):
            substring = "".join(map[row + i][col - i] for i in range(4))
            if substring == "XMAS" or substring == "SAMX":
                sum += 1

    return sum

def findXMASB(file):
    map = makeSplitArray(file) 
    sum = 0
    rows, cols = len(map), len(map[0])

    if rows < 3 or cols < 3:
        return 0

    for row in range(rows - 2): 
        for col in range(cols - 2):  
            forward_slash = map[row][col] + map[row + 1][col + 1] + map[row + 2][col + 2]
            backward_slash = map[row][col + 2] + map[row + 1][col + 1] + map[row + 2][col]
            
            if forward_slash == "MAS" and backward_slash == "MAS":
                sum += 1
            elif forward_slash == "SAM" and backward_slash == "SAM":
                sum += 1
            elif forward_slash == "MAS" and backward_slash == "SAM":
                sum += 1
            elif forward_slash == "SAM" and backward_slash == "MAS":
                sum += 1

    return sum


print(dFindXMAS('input.txt') + hFindXMAS('input.txt') + vFindXMAS('input.txt'))

print(findXMASB('input.txt'))


    