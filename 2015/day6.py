import numpy as np

with open('./input/input6.txt') as line : 
    text = line.readlines()

light = np.zeros((999,999))

def togleLight(grille,action,positionDepart, positionArrive) :
    if action =="turn on" :
        grille[positionDepart[0]:positionDepart[1],positionArrive[0]:positionArrive[1]]=1
    elif action =="toggle" :
        for i in range(positionDepart[1], positionArrive[1]) :
            grille[positionDepart[0]:positionDepart[1],positionArrive[0]:positionArrive[1]]^=1
    elif action =="turn off" :
        grille[positionDepart[0]:positionDepart[1],positionArrive[0]:positionArrive[1]]=1

for line in text :
    