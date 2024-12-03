def makeArray(file):
    list1 = []
    with open(file, 'r') as file:
        for line in file:
            splitted = line.strip().split(' ')
            list1.append([int(x) for x in splitted])
    return list1

def checkDifference(list2):
    for _ in range(len(list2) - 1):
        difference = abs(list2[_] - list2[_ + 1])
        if difference > 3 or difference < 1:
            return False
    return True

def checkAscending(list2):
    for _ in range(len(list2) - 1):
        if list2[_] > list2[_ + 1]:
            return False
    return True

def checkDescending(list2):
    for _ in range(len(list2) - 1):
        if list2[_] < list2[_ + 1]:
            return False
    return True


def safteyTest(file):
    list1 = makeArray(file)
    safe = 0
    for _ in list1:
        if checkDifference(_) and (checkAscending(_) or checkDescending(_)):
            safe += 1
    return safe

def checkSafteyWithDamp(list2):
    if checkDifference(list2) and (checkAscending(list2) or checkDescending(list2)):
        return True
    
    for _ in range(len(list2)):
        modified = list2[:_] + list2[_ + 1:]
        if checkDifference(modified) and (checkAscending(modified) or checkDescending(modified)):
            return True
        
    return False
    
def safteyTestWithDamp(file):
    list1 = makeArray(file)
    safe = 0
    for _ in list1:
        if checkSafteyWithDamp(_):
            safe += 1
    return safe
        
            
print(safteyTest('input.txt'))
print(safteyTestWithDamp('input.txt'))