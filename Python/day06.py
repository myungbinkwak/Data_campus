from abc import abstractproperty


x = 25
y = 98
prod = x * y
print(x, "과", y, "의 곱은", prod)

word = input("문자열을 입력하세요: ")

if word[:1] == word[-1:]:
    print("회문입니다.")
else:
    print("아니에요")

phrase = "North Atlantic Treaty Organization"
acronym = ""
for word in phrase.upper().split():
   acronym += word[0]

print(acronym) 

address = input("메일주소:")
(id, domain) = address.split("@")

sentence = "A picture is worth a thousand words."
table ={"alphas":0,"digits":0,"spaces":0 }

for i in sentence:
    if i.isalpha():
        table["alphas"]+=1
    if i.isdigit():
        table["digits"]+=1
    if i.isspace():
        table["spaces"]+=1            

print(table)

t = "Python is very easy and powerful!"
length = len(t.split(" "))
print(length)

# otp
import random
s = "0123456789" # 대상 문자열
passlen = 4 # 패스워드 길이
p = "".join(random.sample(s, passlen))
print(p)

a = "abcder g"
b = "bcd h"

set1=set(a)
set2=set(b)
print(set1 & set2)

def censor_string(txt, lst, character):
    for word in list:
        txt = txt.replace(word, character*len(word))
    return txt

s = input("문자열:")
f = input("금칙어:").split()

print(censor_string(s, f, "*"))


class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
a = Counter()
a.increment()
print("카운터의 값=", a.count)

class Counter:
    def __init__(self, initValue=0) :
        self.count = initValue
def increment(self) :
    self.count += 1
a = Counter(0) # 계수기를 0으로 초기화한다. 
b = Counter(100) # 계수기를 100으로 초기화한다.

class Student:
    def __init__(self, name=None, age=0):
        self.__name = name # __가 변수 앞에 붙으면 외부에서 변경 금지
        self.__age = age # __가 변수 앞에 붙으면 외부에서 변경 금지

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
            self.__age = age

    def setName(self, name):
            self.__name = name        


        
obj=Student("홍", 20)
obj.getName()

class Circle:
        ...
        def __eq__(self, other):
                return self.radius == other.radius
c1 = Circle(10)
c2 = Circle(10)
if c1 == c2:
    print("원의 반지름은 동일합니다. ")

   

class Cat:
    def __init__(self, name= age=0):
        self.__name = name # __가 변수 앞에 붙으면 외부에서 변경 금지
        self.__age = age # __가 변수 앞에 붙으면 외부에서 변경 금지

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
            self.__age = age

    def setName(self, name):
            self.__name = name        


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)
print (missy.getName(), missy.getAge())
print (lucky.getName(), lucky.getAge())             


class Rocket():
    def__init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

my_rocket = Rocket()
print("로켓의 높이:", my_rocket.y)

my_rocket.move_up()
print("로켓의 높이:", my_rocket.y)

class Triangle():
    def__init__(self,angle1, angle2, angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

    numberOfSides=3
    def checkAngles(self):
        if self.angle1+self.angle12+self.angle1==180:
            return True
        else:
            return False
        
TriangleTriangle=(90,30,60)

# abs() 절대값 반환

f = -30.92 
abs(f)

mylist = [1, 3, 4, 6] # 모든 값이 참이다. 
all(mylist)

invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
sum(persons)

any(persons)
all(persons)
max(persons)

import copy
colors = ["red", "blue", "green"]
clone = copy.deepcopy(colors)
clone[0] = "white"
print(colors)
print(clone)

import random
print(random.randint(1, 6))

print(random.randint(1, 6))

import random
print(random.random()*100)

myList = [ "red", "green", "blue" ]
random.choice(myList)

import calendar
cal = calendar.month(2021, 7)
print(cal)