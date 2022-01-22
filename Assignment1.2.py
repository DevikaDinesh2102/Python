#1
#LIST

list=['a','b','c','d']
print(list)
#index
a=list[1]
print(a)
list1=['a','b','a','c','d',"apple",21]
print(list1)
#length
print(len(list))
print(len(list1))
#type
print(type(list))
#access items
print(list1[2:7])
print(list[1:4])
#change item
list[1] = "e"
print(list)
#add item
list1.append("pencil")
print(list1)
#extend list
list.extend(list1)
print(list)
#remove item
list.remove("e")
print(list)
#remove specific item
list.pop(2)
print(list)
#loop
for i in range(len(list)):
  print(list[i])
  
#copy
list2= list.copy()
print(list2)
#reverse the list
list.reverse()
print(list)

#2
#STRING
x=("hello world")
print(x)
#capitalize the first word
print(x.capitalize())
#returns a string where all the characters are lower casereturns a string where all the characters are lower case
print(x.casefold())
#align to centre
#y=x.centre(20)
#print(y)

#index
print(x.index("world"))
#count the number of times a word occurs
x=('hello world hello python hello coding')
print(x.count("hello"))
x=("hello world.")
#Returns an encoded version of the string
print(x.encode())
# to return true if the string ends with the specified value
print(x.endswith("."))
#to Searches the string for a specified value and returns the position of where it was found
print(x.find("world"))
#to Formats specified values in a string
x="i study {subject}"
print(x.format(subject="python"))
#Check if all the characters in the text are alphanumeric
print(x.isalnum())
#Check if all the characters in the text are letter
x=("helloworld")
print(x.isalpha())
#Check if all the characters in the unicode object are decimals
print(x.isdecimal())
#to check of it follows the title rule
x=("Hello World")
print(x.istitle())
#tocheck if all the characters are upper case
x=("HELLO")
print(x.isupper())
#to convert to lower case
print(x.lower())
#to Returns a left trim version of the string
y=x.lstrip()
print("hi",y,"how are you")
#to replace a character with other
x=("hello world")
y=x.maketrans("h", "b")
print(x.translate(y))
# to splits the string into a tuple containing three elements.
x=("i study python")
print(x.partition("study"))
#to replace a word
print(x.replace("python","mathematics"))
print(x)
#to check Where in the text is the last occurrence of  word
print(x.rfind("python"))
print(x.rindex("python"))
#to convert to upper case
print(x.upper())
#to convert first letter of each word in title format
print(x.title())
#to Fills the string with a specified number of 0 values at the beginning
x='10'
print(x.zfill(10))
x=("Hello World")
#Make the lower case letters upper case and the upper case letters lower case
print(x.swapcase())
#to Check if the string starts with a specified character
print(x.startswith("Hello"))
#Check if the string starts
x=("hi there/how are you")
print(x.splitlines())
x=("hi there ")
#split a string into a list
print(x.split())

print(x.rsplit())
print(x)
#right align the string
y=x.rjust(10)
print(y,"how are you")

#3
list=[1,2,3,4,5,6]
print(list[2])
print(list[-2])
print(list[-1])

#negative index gives the item by counting it from the end,
# -1 will give the the last item while , -2 will give the second last item

