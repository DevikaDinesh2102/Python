#1
#DICTIONARY
a={"pet":"dog","name":"ruby","age":"1"}
print(a)
#to clear the elements of dict
print(a.clear())

#to Returns a copy of the dictionary
a={"pet":"dog","name":"ruby","age":"1"}
print(a.copy())
#method returns a dictionary with the specified keys and the specified value
y=dict.fromkeys(a)
print(y)
#to get the value of the specified key
print(a.get("name"))
print(a.get("age"))
#to Return the dictionary's key-value pairs
print(a.items())
# to return the key
print(a.keys())
#to pop a specific item
a.pop("pet")
print(a)
#to pop the last item
a.popitem()
print(a)
a={"pet":"dog","name":"ruby","age":"1"}
#Returns the value of the specified key
print(a.setdefault("color", "white"))
print(a)
# to inserts the specified items to the dictionary
a.update({"type":"cute"})
print(a)
#to return a list of all the values in the dictionary
print(a.values())

#2
#SET
setA={"python","java","html","c++"}
print(setA)
set1=set(("python","java","html","c++"))
print(set1)
set2=set(["python","java","html","c++"])
print(set2)



#sorted function
func=("90","11","2","58","32")
x=sorted(func,reverse=True)
print(x)

#5
#calculator
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
x=int(input("Choose option "))

if x==1:
    a=int(input("A="))
    b=int(input("B="))
    c=a+b
    print("Sum = ",c)
elif x==2:
    a=int(input("A="))
    b=int(input("B="))
    c=a-b
    print("Difference = ",c)
elif  x==3:
    a=int(input("A="))
    b=int(input("B="))
    c=a*b
    print("Product = ",c)
elif x==4:
    a=int(input("A="))
    b=int(input("B="))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid")