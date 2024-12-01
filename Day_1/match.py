def makeArray(file, list1, list2):
    with open(file, 'r') as file:
        for line in file:
            splitted = line.strip().split('   ')
            list1.append(int(splitted[0]))
            list2.append(int(splitted[1]))
    
def findDistance(file):
    list1 = []
    list2 = []
    makeArray(file, list1, list2)
    list1.sort()
    list2.sort()

    distance = 0

    for _ in range(0, len(list1)):
        distance += abs(list1[_] - list2[_])

    return distance

def findSimilarity(file):
    list1 = []
    list2 = []
    score = 0
    makeArray(file, list1, list2)
    for _ in range(0, len(list1)):
        num = list2.count(list1[_])
        score += (num * list1[_])

    return score

print(findDistance('input.txt'))
print(findSimilarity('input.txt'))