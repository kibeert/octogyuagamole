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
print(MyList[2])
MyList[1] = "mango"
print(MyList)
for i in range(len(MyList)):
    print(i)
MyList.sort()
print(MyList)
thisDict={
    "firstname": "collins",
    "lastname": "koech",
    "age" : 20,

}
print(thisDict)
print(thisDict["firstname"])
print(len(thisDict))
print(thisDict.get(age))
for x in thisDict:
    print(x)

family = {
    "father":{
        "name":"Shadrack",
        "gender": "male",
        "age": 56,
    },
    "mother":{
        "name":"Rose",
        "gender":"female",
        "age": 50
    },
    "child1":{
        "name":"manu",
        "gender":"male",
        "age":25
    }
}
print(family)
for i in family:
    print(i)

print(family["child1"]["name"])

grade = int(input("What was your score"))
if grade<=100 and grade>90:
    print("A good work")
elif grade<=89  and grade>70:
    print("B")
elif grade<=79 and grade>60:
    print("c")
elif grade<=59 and grade>50:
    print("D")
elif grade<=49 and grade>40:
    print("D")
else:
    print("F fail")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    for y in adj:
        print(y,x)

def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example results")
tri_recursion(9)

myTuple = ("Apple", "Banana", "Cherry")
myit = iter(myTuple)

for x in myTuple:
    print(x)

class myNumbers():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x= self.a
        self.a +=1
        return x
    
myclass = myNumbers()
myIter = iter(myclass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

x = "Hello World"

print(len(x))
