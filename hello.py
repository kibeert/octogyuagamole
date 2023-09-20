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