#1
for i in range(1,10,2):
    print(i)


#2
l=[1]
for x in l:
    l.append(x+1)
    print(x)
    
#3
A = ("a", "b", "c")
a=list(A)
a.append("d")
print(a)
A=tuple(a)
print(A)


