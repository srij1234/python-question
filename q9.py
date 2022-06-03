s=input("enter string")
l=[]
for i in s:
    l.append(i)
l.sort()
for i in l:
    print(i,end="")