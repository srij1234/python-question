
l=[]
p=int(input("enter number of elements:"))
for i in range(p):
    a=input("enter element:")
    l.append(a)
print("initial array:",l)
x=0
y=0
for i in l:
    if(i=="north"):
        x=x+1
    if(i=="south"):
        x=x-1
    if(i=="west"):
        y=y+1
    if(i=="east"):
        y=y-1
a=[]
if(x<0):
    for i in range(abs(x)):
        a.append("south")

elif(x>0):
    for i in range(abs(x)):
        a.append("north")
if(y>0):
    for i in range(abs(y)):
        a.append("west")
elif(y<0):
    for i in range(abs(y)):
        a.append("east")
print("final array:",a)
