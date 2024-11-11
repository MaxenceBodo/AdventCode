import re

with open('./input/input5.txt') as file : 
    text = file.readlines()

#Partie 1
def partie1() :
    nombreDeMatch = 0

    for line in text : 
        if len(re.findall(r"[aeiou]",line))>=3  :
            if re.search(r"(.)\1",line) :
                if not re.search(r"ab|cd|pq|xy",line) :
                    nombreDeMatch+=1
    return(nombreDeMatch)

#Partie 2 :
def partie2() :
    nombreDeMatch = 0    
    pair_pattern = r"(..).*\1"
    repeat_pattern = r"(.).\1"
    for line in text : 
        if re.search(pair_pattern, line) and re.search(repeat_pattern, line)  :
                nombreDeMatch+=1
    return(nombreDeMatch)

print(partie1())
print(partie2())