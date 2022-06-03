x=input("enter number")
for i in range(len(x)-5):
    print("*",end='')
for i in range(len(x)-4,len(x),1):
    print(x[i],end='')    