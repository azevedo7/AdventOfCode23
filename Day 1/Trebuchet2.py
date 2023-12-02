total = 0
word_to_number = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("input.txt", "r") as file1:
    for line in file1:
        lastNumber = True
        counterStart = 0
        counterEnd = 0
        words = []
        aux = []
        for char in line:
            if(char == '\n'):
                break
            if (char.isnumeric()):
                aux.append(char)
                if(not lastNumber):
                    counterStart = counterEnd + 1
                    counterEnd+=1
                lastNumber = True
            else:
                words.append(char)
                if(not lastNumber):
                    for i in range(counterStart, counterEnd + 1):
                        words[i] += char
                        if words[i] in word_to_number:
                            aux.append(word_to_number[words[i]])
                    counterEnd+=1
                lastNumber = False
                    
        first = int(aux[0])
        last = int(aux[-1])
        total += first * 10 + last

print(total)