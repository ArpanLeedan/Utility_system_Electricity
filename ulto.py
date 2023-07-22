n=eval(input("Enter list "))
l=[]
for i in n:
    if(n.count(i)>1):
        if(i in l):
            continue
        else:
            n.remove(i)
            l.append(i)
print(n)