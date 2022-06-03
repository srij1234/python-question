import random
l=[]
for i in range(100):
    l.append(random.randint(1,100))
new=[]
for i in l:
    if i not in new:
        new.append(i)
for i in new:
    x=0
    for j in l:
        if(i==j):
            x=x+1
    if(x>1):
        print(i,"has repeated",x+1,"times")