array = []
games = []
counter = 0

class Game:
    plays = []

with open("input.txt", "r") as file:
    for line in file:
        games.append({"red": 0,"green": 0,"blue": 0,"id": counter+1})
        array.append(line.split(':', 1))
        aux = array[counter][1].split(';')

        for i in aux:
            plays = i.split(',')
            for play in plays:
                throw = play.split(' ')

                # Remove white space
                throw.pop(0)

                # Remove \n
                throw[1] = throw[1].replace("\n", "")
        
                

                # Get the minimum number
                if (games[counter][throw[1]] < int(throw[0])):
                    games[counter][throw[1]] = int(throw[0])

        counter+=1

total = 0
for game in games:
    power = game["red"] * game["green"] * game["blue"]
    total += power


print(total)