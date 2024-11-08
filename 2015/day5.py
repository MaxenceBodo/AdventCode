import re

with open('./input/input5.txt') as file : 
    text = file.readlines()

nombreDeMatch = 0

for line in text : 
    if len(re.findall(r"[aeiou]",line))>=3  :
        if re.search(r"(.)\1",line) :
            if not re.search(r"ab|cd|pq|xy",line) :
                nombreDeMatch+=1

print(nombreDeMatch)