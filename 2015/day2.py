with open('./input/input2.txt') as file : 
    text = file.readlines()

#Partie 1
paper = 0
for line in text : 
    l,w,h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    paper = paper + 2*l*w+2*w*h+2*h*l+min(l*w,w*h,h*l)
    

print(paper)

#Partie 2
ribbon = 0
for line in text : 
    l,w,h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    smallest = sorted([l,w,h])[:2]

    ribbon = ribbon + 2*smallest[0]+2*smallest[1] + l*w*h

print(ribbon)