num=input("enter number")
l=[]

for i in num:
    l.append(eval(i))

x=0
for i in range(len(l)-1):
    if(((l[i]-l[i+1])==(-1)) or ((l[i]-l[i+1])==(1)) ):
        x=x+1

if (x+1==len(l)):
    print("it is step number")
else:
    print("it is not step number")