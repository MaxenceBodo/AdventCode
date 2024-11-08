with open('./input/input3.txt') as file : 
    text = file.read()

#Partie 1
x, y = 0, 0
totalMaison = set()

for char in text : 
    if char == '^':
        x += 1
    elif char == 'v':
        x -= 1
    elif char == '>':
        y += 1
    elif char == '<':
        y -= 1
    totalMaison.add((x,y))
print(len(totalMaison))

#Partie 2
xs,ys = 0,0
xr,yr = 0,0

i=0

totalMaison = set()

for char in text : 
    if i%2==0:  
        
        if char=="^" :
            xs=xs+1
        if char==">" :
            ys=ys+1
        if char=="<" :
            ys=ys-1
        if char=="v" :
            xs=xs-1
        totalMaison.add((xs,ys))

    else :  
        if char=="^" :
            xr=xr+1
        if char==">" :
            yr=yr+1
        if char=="<" :
            yr=yr-1
        if char=="v" :
            xr=xr-1
        totalMaison.add((xr,yr))
    i +=1

print(len(totalMaison))