#This is a comment
print("Hello world")
x = 10
y = 15
print(x)
print(y+x)
print(y)
a = str(3)
b= float(12)
print(a)
print(b)
print(type(a))
print(type(b))

#global variables
a = "Awesome"

def myFunc():
    print("python is " + a)
myFunc()
#local variables

def Myfunc():
    global z
    z = "Awesome"
    print("Python is " + z)
Myfunc()
print("python is " + z)


w  ="Banana"
for x in w:
    print(x)
print(len(w))

txt = "The Best Things In Life Are Free"
word = "free"
if word in txt:
    print("Yes the word" + word+ " Is present 👍👍👍")
else:
    print("The given word,"+word+"  is not present 😒😒😒")

c= "Hello world"
print(c[2:5])
print(c.upper())
print(c.capitalize())
print(c.casefold())
print(c.encode())
print(c.strip())

age = int(input("What is your age"))
if age >= 18:
    print("You are allowed to proceed")
else:
    print("you are still an underage")

a= "to create "
b= "Worldwide"
c= "strong business"
myOrder = "I want {} a {} recognized {}"
print(myOrder.format(a, b, c))

MyList = ["Apple", "Avacado", "Cherry"]
for x in MyList:
    print(x)
print(MyList)
print(len(MyList))