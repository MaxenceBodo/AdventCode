#Premiere partie
with open('./input/input1.txt') as file :
   text = file.read()

floor = 0

for char in text:
  floor +=1 if char=="(" else -1

print(floor)

#Deuxième partie
floor = 0

for position, char in enumerate(text, start=1):
    floor += 1 if char == "(" else -1
    if floor == -1:
        break

print(position)