def fun(l,com):
    if(com=='asc'):
        l.sort()
        return l
    if(com=='desc'):
        l.sort()
        l.reverse()
        return l
    if(com=='none'):
        return l
    
        
li=eval(input('enter list'))
com=input('enter command')
print(fun(li,com))