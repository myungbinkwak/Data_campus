price = 12345
tax = price * 0.075
tax = round(tax, 2)
print(tax)

x = input("첫 번째 정수를 입력하시오:")
y = input("두 번째 정수를 입력하시오:")
sum = x + y
print("합은 ", sum)

x = 100
y = 200
print(x, "와 ", y, "의 합=", x+y)

##
#	이 프로그램은 사용자와 친근하게 대화한다. 
#
print("안녕하세요?")
name = input("이름이 어떻게 되시나요? ")
print("만나서 반갑습니다. " + name + "씨")

print("이름의 길이는 다음과 같군요:", len(name))

age = int(input("나이가 어떻게 되나요? "))
print("내년이면 "+ str(age+1) + "이 되시는군요.")


###

x = 100
tax = x*0.1
total = x+tax
print(total)

#### 
x= int(input("닭의 수:"))
y= int(input("돼지의 수:"))
z= int(input("소의 수:"))
leg = print(x*2+y*4+z*4)

### 조건문

a = 99
if a < 100: 
    print("100보다 작군요")

a = 200
if a < 100:
    print("100보다 작군요")
else:
    print("100보다 크군요")

###  

a = int(input("정수를 입력하세요: "))
if a % 2 == 1 :
    print("홀수를 입력했군요.")
else: 
    print("짝수를 입력했군요.")    

import random

numbers = []
for num in range(0, 10):
    numbers.append(random.randrange(0, 10))

print("생선된 리스트", numbers)

for num in range(0, 10):
    if num not in numbers:
        print("숫자 %d는 리스트에 없네요" %num)


a = int(input("정가를 입력하시오: "))

if a < 1000000:
    a*0.9   
else:
    a*1.15    


price = int(input("가격:"))
card = int(input("카드:"))
if price > 20000 and card == 'python':
    print("배송료가 없습니다.")
else:
    print("배송료는 3000원입니다.")

import random

print("동전던지기")
coin = random.randrange(2)

if coin == 0:
    print("앞")
else:
    print("뒤")

print("게임이 종료") 

at = float(input("리히터 규모를 입력하시오"))

if at > 9.0:
    print("대부분의 구조물이 파과")
elif at > 8.0:
    print("지표면에 균열")
elif at > 7.0:
    print("큰 피해")
elif at > 4.0:
    print("흔들림")    
else:
    print("감지 o")    

###
print("========================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("========================")

selection = int(input("메뉴를 선택하세요:"))

if selection >= 1 and  selection <= 3:
    print("메뉴", selection
else:
    print("잘못 입력했어...")

# 어렵네...