# 문제 3
import random
from typing import MutableMapping

def dice_game():
    human = random.randint(1,6)
    print("인간: 주사위값 = ", human)
    ai = random.randint(1,6)
    print("컴퓨터: 주사위값 = ", ai)
    if human > ai : 
        print("인간승리")
    elif human == ai:
        print("동점")
    else:
        print("컴퓨터 승리")
while True:
    dice_game()
    user = input("중단 할까요? y/n")
    if user == "Y" or user == "y":
    break;

def change_meter(meter):
    feet = float(meter / 0.305)
    yard = float(meter * 1.0936)
    print(meter "미터는" feet, "피트" yard "야드입니다")
meter = float(input('meter입력: '))
change_meter(meter)


def checkPW(passwd):
    if len(passwd)>=9:
        ans = "good"
    elif len(passwd) >=5:
        ans = 'nomal'
    else:
        ans = "bad"
    return(ans)

passwd = int(input('비밀번호 길이입력해주세요...: '))

def objection(o):
    if( o == '춘천'):
        a = 5000
    elif( o == '서울'):
        a = 50000    
#---------------------------------------------------------------------------
## List 

temps = [28, 31, 33, 35, 27, 26, 25]

#리스트 변경
temps[3] = 36 # 4번째 있는것을 36으로 변경
temps   

temps[7] = 29 #오류 6번까지 있기때문에

temps
for i in range(len(temps)):
    print(temps[i], end='')

#---

questions =['name','quest','color']
answers =['Kim','파이썬','blue']
for q, a in zip(questions, answers):
    print(f"What is your {q}? It is {a}")


#---------- append 리스트에 추가하는거

heroes = [ ] # 공백 리스트를 생성한다. 
heroes.append("아이언맨") # 리스트에 ”아이언맨“을 추가한다. 
heroes.append("토르") # 리스트에 ”토르“를 추가한다. 
print(heroes)
heroes.insert(1, '스파이더맨')
print(heroes)
n = heroes.index('스파이더맨') #제일 첫번째꺼
heroes.pop(1) # 1에 해당하는것 제거

heroes.remove(" ")# 삭제하고 싶은것 넣기
if '토르' in heroes:
    heroes.remove('토르')  # 토르 삭제


myList=[30,10,20]
print("현재 리스트: %s" % myList)
myList.append(40)
print('append(40)후의 리스트: %s' % myList)
myList.pop(3)
print('pop(3)후의 리스트: %s' % myList)
myList.sort()
print('sort()후의 리스트: %s' % myList)
myList.reverse()
print('reverse()후의 리스트: %s' % myList)
myList.index(20)
print('20값의 위치: %s' % myList.index(20))
myList.insert(2, 222)
print('insert후의 리스트: %s' % myList)
myList.remove(222)
print('remove(222)후의 리스트: %s' % myList)
myList.extend([77,88,77])
print('extend([77,88,77])후의 리스트: %s' % myList)
print('77의개수: %s' % myList.count(77))

##-----
student = 5
lst = []
count = 0

for i in range(student):
    value = int(input("성적: "))
    lst.append(value)

print("\n성적평균 =", sum(lst) / len(lst))

for score in lst:
    if score >= 80:
        count += 1
print("80점 이상=", count)        
   
heroes1 = [ "아이언맨", "토르" ]
heroes2 = [ "헐크", "스칼렛 위치" ]
avengers = heroes1 + heroes2 
# avengers는 ['아이언맨', '토르', '헐크', '스칼렛 위치']가 된다. 

string=['happy', 'love', 'dog', 'cat']
num = [1,2,6,3,9,5]
empty = []
mix = [4,0,'hi', 1, 'sun','x']

len(string)+len(num)+len(empty)+len(mix)

temps = [28, 31, 33, 35, 27, 26, 25] 
values = temps
print(temps) # temps 리스트 출력
values[3] = 39 # values 리스트 변경
print(temps) # temps 리스트가 변경되었다. 

temps = [28, 31, 33, 35, 27, 26, 25] 

values = list(temps)

numbers = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
 numbers[:: -1]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']
lst
['white', 'blue', 'red', 4, 5, 6, 7, 8]

numbers = list(range(0, 10)) # 0에서 시작하여 9까지를 저장하는 리스트
print(numbers)
del numbers[-1] # 마지막 항목을 삭제한다. 
print(numbers)

s = "Monty Python"
print(s[0]) # M
print(s[6:10]) # Pyth
print(s[-12:-7]) # Mont

squares = []
for x in range(10):
    squares.append(x*x)

prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
mprices

words = ["All", "good", "things", "must", "come", "to", "an", "end."]
letters = [ w[0] for w in words ]
letters

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
numbers


