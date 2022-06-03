l=eval(input("enter array"))
p=[]

for i in l:
    if i not in p:
        p.append(i)
x=0
k=0
for i in p:
    y=0
    
    for j in l:
        if(j==i):
            y=y+1
    if(y>x):
        x=y
        k=i
print("highest frequency=",k)