s=input("enter:")
x=0
for i in range(len(s)//2):
    if(s[i]==s[len(s)-1-i]) :
        x=x+1
if(x==len(s)//2):
    print("it is a palindrome")
else:
    print("it is not a palindrome")