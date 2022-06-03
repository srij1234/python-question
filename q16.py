z=int(input("enter number of test cases"))
for pqr in range(z):
    n=int(input("enter n"))

    x=1
    y=1
    p=0
    while(x!=n+1):
        y=y+1
        p=0
        for i in range(2,y):
            if(y%i==0):
                p=p+1
        if(p==0):
            print(y,"is a prime")
            x=x+1