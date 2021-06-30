# day01

# 산술연산자 
7+4
log(10)+5 # 로그함수
sqrt(25) # 제곱근
max(5, 3, 2) # 최댓값

# 반지름이 10인 원의 면적
10*10*3.14

# 5시간 48분 32초로 환산
5*60*60 + 48*60 + 32

# 패키지 install.packages(), library()
# ggplot2 패키지
# install.packages('ggplot2')
library(ggplot2)
ggplot(data = iris, aes(x = Petal.Length, y = Petal.Width)) + geom_point()

## cowsay packages
install.packages('cowsay')
library(cowsay)
say('Hello world!', by='cat')
say('좋은 아침', by = 'snowman')

Sys.time()

# 생일 맞추기석준이의 생일을 맞아 친한 친구 5명이 모였다. 그중 평소 퀴즈를 좋아하는 민철이가다음과 같이 문제를 냈다. “우리 다섯 명의 생일을 맞춰보자! 단, 내가 설명하는 방식으로 계산해서 알아내야 해. 먼저 태어난 달에 4를 곱하고, 그 결과에 9를 더하고, 다시 그 결과에 25를 곱하고, 마지막으로 다시 그 결과에 태어난 날짜를 더하는 거야.” 친구들의 계산 결과가 다음과 같을 때 각자의 생일을 구해보시오

# 소윤이 태어난 날
(931 - 225) %% 100
# 소윤이 태어난 달
((931 - 225) - ((931 - 225) %% 100)) /100

# 변수

total <- 5050 # 5050을 변수 total에 저장
total # 방법 1
print(total) # 방법 2
cat('합계 :', total) # 방법 3

abc <- 850 # 어떤 작업을 하려는 것인지 알기 어렵다.
mid.sum <- 850 # 중간 합계로 850을 저장하려는 것임을 예상할 수 있다.

5 > 3 # 비교연산
2 > 7 # 비교연산
TRUE + TRUE # 산술연산에서 TRUE는 1 FALSE는 0
a <- TRUE # a에 논리값 TRUE 저장
b <- F # b에 논리값 FALSE 저장
a # a의 내용 출력
b # b의 내용 출력
a + b # 논리값의 산술연산 결과

salt <- 50
water <- 100
result <- salt / (salt + water) *100
cat("소금 =", salt, ", 물 =", water, " : 농도 =", result, "%")

salt <- 70
water <- 110
result <- salt / (salt + water) *100
cat("소금 =", salt, ", 물 =", water, " : 농도 =", result, "%")

#벡터
score.1 <- 68; score.2 <- 95; score.3 <- 83; score.4 <- 76; 
score.5 <- 90
score.6 <- 80; score.7 <- 85; score.8 <- 91; score.9 <- 82; 
score.10 <- 70
total <- score.1 + score.2 + score.3 + score.4 + score.5 +
  score.6 + score.7 + score.8 + score.9 + score.10
avg <- total / 10 # 10명의 평균 계산
avg # 평균 출력

score <- c(68, 95, 83, 76, 90, 80, 85, 91, 82, 70)
mean(score)


x <- c(1,2,3) # 숫자형 벡터
y <- c('a','b','c') # 문자형 벡터
z <- c(TRUE,TRUE,FALSE,TRUE) # 논리형 벡터
x # 벡터 x에 저장된 값을 출력
y # 벡터 y에 저장된 값을 출력
z # 벡터 z에 저장된 값을 출력

v3 <- seq(1,101,3)
v3

absent <- c(8,2,0,4,1) # absent 벡터에 결근 인원수 저장
absent # absent 벡터의 내용 출력
names(absent) # absent 벡터의 값들의 이름을 확인
names(absent) <- c('Mon','Tue','Wed','Thu','Fri') # 값들의 이름
absent # absent 벡터의 내용 출력
names(absent) # absent 벡터의 값들의 이름을 확인

sales <- c(640,720,680,540) # 1~4월 매출액
names(sales) <- c('M1','M2','M3','M4') # 매출액에 월을 이름으로 붙임
sales # 1~4월 매출액 출력
sales[1] # 1월 매출액 출력
sales['M2'] # 2월 매출액 출력
sales[c('M1','M4')] # 1월, 4월 매출액 출력

v1 <- c(1,5,7,8,9)
v1
v1[2] <- 3 # v1의 두 번째 값을 3으로 변경
v1
v1[c(1,5)] <- c(10,20) # v1의 1, 5번째 값을 각각 10, 20으로 변경
v1
v1 <- c(100,200,300) # v1의 내용을 100, 200, 300으로 변경

customer <- c('kim', 'lee', 'park', 'choi', 'seo')
deposit <- c(5000000, 4500000, 4000000, 5500000, 6000000)
rate <- c(3.5, 3, 4, 5, 4.5)
period <- c(2, 2, 5, 7, 4)

names(deposit) <- customer
names(rate) <- customer
names(period) <- customer

who <- 'kim'

sum <- deposit[who] * ( 1 + rate[who] / 100)^ period[who]
sum

lab <- data.frame(customer, deposit, rate, period)
lab

# 함수
#매개변수 = 함수의 입력값을 받는 변수
d <- c(1,7,4,2,3) # 벡터 d에 5개의 값을 저장
sort(d) # 벡터 d의 값들을 오름차순으로 정렬하여 출력
sort(d,decreasing=TRUE) # 벡터 d의 값들을 내림차순으로 정렬하여 출력

str <- paste('good', 'morning', sep=' / ')
str

sales <- c(750,740,760,680,700,710,850,890,700,720,690,730)
names(sales) <- paste(1:12, '월', sep="")
sales
#상반기 합계
sum(sales[1:6])
