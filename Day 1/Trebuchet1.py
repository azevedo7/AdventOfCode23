total = 0
with open("input.txt", "r") as file1:
    for line in file1: 
        aux = []
        for char in line:
            if (char.isnumeric()):
                aux.append(char)
        first = int(aux[0])
        last = int(aux[-1])
        total += first * 10 + last

print(total)