s=input("enter string:")

x=0
y=0
z=0
for i in s:
    if ((ord(i)>47) and (ord(i)<58)):
        x=x+1
        
    elif (((ord(i)<91) and (ord(i)>64)) or ((ord(i)>96) and (ord(i)<123))):
        y=y+1
        
    else:
        z=z+1
print("number of int =",x)
print("number of alfabet =",y)        
print("number of special char =",z)        
    