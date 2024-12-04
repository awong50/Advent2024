def makeString(file1):
    with open(file1, 'r') as file:
        text = ""
        for line in file:
            text += line
    return text.strip().replace('\n', '')

def multiply(file1):
    text = makeString(file1)
    sum = 0
    for _ in range(0, len(text) - 3):
        if text[_:_+4] == 'mul(':
            numberstr = ""
            numbers = []
            i = _ + 4
            while i < len(text) and text[i] != ')':
                if text[i].isdigit():  
                    numberstr += text[i]
                elif text[i] == ',' and numberstr:  
                    numbers.append(int(numberstr))
                    numberstr = ''
                else:  
                    numberstr = ""
                    numbers = []
                    break
                i += 1
            
            if numbers != []:
                numbers.append(int(numberstr))
                sum += (numbers[0] * numbers[1])
                numbers = []
                numberstr = ""
            
    
    return sum

def restrictedMultiply(file1):
    text = makeString(file1)
    sum = 0
    enabled = True
    for _ in range(0, len(text) - 3):
        if text[_:_+4] == 'mul(':
            if enabled:
                numberstr = ""
                numbers = []
                i = _ + 4
                while i < len(text) and text[i] != ')':
                    if text[i].isdigit():  
                        numberstr += text[i]
                    elif text[i] == ',' and numberstr:  
                        numbers.append(int(numberstr))
                        numberstr = ''
                    else:  
                        numberstr = ""
                        numbers = []
                        break
                    i += 1
                
                if numbers != []:
                    numbers.append(int(numberstr))
                    sum += (numbers[0] * numbers[1])
                    numbers = []
                    numberstr = ""
        elif text[_:_+4] == "do()":
            enabled = True
        elif text[_:_+7] == "don't()":
            enabled = False
            
    return sum

print(multiply('input.txt'))
print(restrictedMultiply('input.txt'))

