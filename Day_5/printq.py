def makeArrays(file):
    rulesArray = []
    sections = []
    combined = []

    with open(file, 'r') as file:
        for line in file:
            if '|' in line:
                x, y = map(int, line.split('|'))
                rulesArray.append([x, y])
            elif line.strip():
                sections.append(list(map(int, line.strip().split(','))))
        combined.append(rulesArray)
        combined.append(sections)
    
    return combined

def checkValid(section, rules):
    sectionMap = {page: idx for idx, page in enumerate(section)}
    for x, y in rules:
        if x in sectionMap and y in sectionMap:
            if sectionMap[x] > sectionMap[y]:
                return False
    return True


def findSums(file):
    combined = makeArrays(file)
    rules = combined[0]
    sections = combined[1]
    sum = 0

    for i in range(len(sections)):
        if checkValid(sections[i], rules):
            sum += sections[i][len(sections[i]) // 2]
    
    return sum

def reSort(section, rules):
    sectionsBefore = {sectionN: 0 for sectionN in section}

    for x, y in rules:
        if x in section and y in section:
            sectionsBefore[y] += 1

    sorted = []

    while len(sorted) < len(section):
        for sectionN in section:
            if sectionsBefore[sectionN] == 0:
                sorted.append(sectionN)
                sectionsBefore[sectionN] = -1

                for x, y in rules:
                    if x == sectionN and y in sectionsBefore:
                        sectionsBefore[y] -= 1

    return sorted[len(sorted) // 2]

def findMoreSums(file):
    combined = makeArrays(file)
    rules = combined[0]
    sections = combined[1]
    sum = 0

    for i in range(len(sections)):
        if not checkValid(sections[i], rules):
            sum += reSort(sections[i], rules)
    return sum

print(findSums('input.txt'))
print(findMoreSums('input.txt'))

