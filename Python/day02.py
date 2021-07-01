# for
for i in range(0, 3, 1):
    print("%d : 안녕")

for i in range(1,6,1) : 
    print('%d'%i, end="")

# for을 이용해 10까지 합계
i, hap =0,0
for i in range(1, 11, 1):
    hap = hap + i
print("1부터 10까지 합계: %d"%hap)    

# 500-1000사이의 합계
i, hap = 0, 0
for i in range(501, 1001, 2):
    hap = hap + i
print("500부터 1000까지 홀수의 합계: %d"%hap)    

# 키보드로 입력한 값까지의 합계
i, hap = 0, 0
a = int(input("숫자를 입력하세요:"))
for i in range(0, a, 1):
    hap = hap + i
print("합계: %d"%(hap))    

i, dan =0, 0
dan = int(input("단:"))
for i in range(1, 10, 1):
    print("%d X %d = %2d" % (dan, i , dan*i))

i, dan =0, 0
for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("%d x %d = %2d"% (i, k, i*k))
    print("")        
i, hap=0,0
i=1
while i < 11:
    hap = hap+i
    i=i+ 1
print("합계:%d"%hap)    

hap = 0
a,b =0,0 

while True:
    a = int(input("첫번째 수:"))
    if a ==0:
        break
    b = int(input("두번째 수:"))
    hap = a+b
    print("%d+%d = %d"% a+b)

for y in range(1, 6):
    for x in range(y):
        print("$", end="")
    print("")    

a = int(input("정수를 입력하세용: "))
for a in range(1, a+1):
    for k in range(1, k+1):
        print(a, end="")
    print("") 

#약수
a = int(input("정수를 입력하세용: "))
for i in range(1, a+1):
    if a % i ==0:
        print(i, end="")
print()            

#최대공약수
a = int(input("정수를 입력하세용: "))
result = 0
for i in range(1, a+1):
        result += i**2

hap, i = 0,0

for i in range(1, 101):
    if i % 3 == 0:
        continue

    hap += i


def get_area(radius):
    area = 3.14*radius**2
    return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)

def calc(v1, v2, op):
    result = 0
    if op =='+':
        result = v1+v2
    elif op == '-':
        result == v1-v2
    elif op == '*':
        result == v1*v2
    elif op == '/':
        result == v1/v2

    return result            

res = 0 
va1, var2, oper = 0,0,""

oper = input("계산을 입력하세요(+,-,*,/):")
var1 = int(input("첫번째 수를 입력하세요 :"))
var2 - int(input("두번째 수를 입력하세요:"))

res = calc(var1, var2, oper)

print("##계산기 : %d%s%d =%d"%(var1, oper, var2, res))


import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))

    t.forword(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end.fill()


def func1():
    global a
    a = 10
    print("func1()에서 a값 %d"%a)

def fun2():
    print("func2()에서 a값%d" %a)


# 함수변수 선언부분

a=20

#메인코드 부분
func1()
func2()


## 너무 어렵고...