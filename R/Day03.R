##Day03 

dim(iris) # 행과 열의 개수 보이기
nrow(iris) # 행의 개수 보이기
ncol(iris) # 열의 개수 보이기
colnames(iris) # 열 이름 보이기, names() 함수와 결과 동일
head(iris) # 데이터셋의 앞부분 일부 보기
tail(iris) # 데이터셋의 뒷부분 일부 보기
str(iris) # 데이터셋 요약 정보 보기
iris[,5] # 품종 데이터 보기
levels(iris[,5]) # 품종의 종류 보기(중복 제거)
table(iris[,"Species"]) # 품종의 종류별 행의 개수 세기
colSums(iris[,-5]) # 열별 합계 / 5번째는 factor라서 제외
colMeans(iris[,-5]) # 열별 평균
rowSums(iris[,-5]) # 행별 합계
rowMeans(iris[,-5]) # 행별 평균
z <- matrix(1:20, nrow=4, ncol=5)
z
t(z) # 행과 열 방향변환

IR.1 <- subset(iris, Species=='setosa')
IR.1
IR.2 <- subset(iris, Sepal.Length>5.0 & Sepal.Width>4.0)
IR.2
IR.2[, c(2,4)] # 2열과 4열의 값만 추출

a <- matrix(1:20,4,5) # 1~20까지 4행 5열
b <- matrix(21:40,4,5)
a
b
2*a # 매트릭스 a에 저장된 값들에 2를 곱하기
a+b
a <- a*3
b <- b-5

#자료구조 확인
class(iris) # iris 데이터셋의 자료구조 확인
class(state.x77) # state.x77 데이터셋의 자료구조 확인
is.matrix(iris) # 데이터셋이 매트릭스인지 확인하는 함수
is.data.frame(iris) # 데이터셋이 데이터프레임인지 확인하는 함수
is.matrix(state.x77)
is.data.frame(state.x77)

# 매트릭스를 데이터프레임으로 변환
is.matrix(state.x77)
st <- data.frame(state.x77)
head(st)
class(st)
# 데이터프레임을 매트릭스로 변환
is.data.frame(iris[,1:4])
iris.m <- as.matrix(iris[,1:4])
head(iris.m)
class(iris.m)

iris[,"Species"] # 결과가 벡터-매트릭스, 데이터프레임 모두 가능
iris[,5] # 결과가 벡터-매트릭스, 데이터프레임 모두 가능
iris["Species"] # 결과가 데이터프레임-데이터프레임만 가능
iris[5] # 결과가 데이터프레임-데이터프레임만 가능
iris$Species # 결과가 벡터-데이터프레임만 가능


#① 직경(Girth)은 화원에서 보유한 벚나무의 평균보다 커야 한다.
#② 높이(Height)는 80보다 커야 한다.
#③ 부피(Volume)는 50보다 커야 한다.

class(trees)
str(trees)

grith.mean <- mean(trees$Girth)

candidate <- subset(trees, Girth > grith.mean & Height > 80 & Volume > 50)
candidate
nrow(candidate)

library(reshape2)
tips
table(tips$day)

dinner <- subset(tips, time == 'Dinner')
lunch <- subset(tips, time == 'Lunch')
table(dinner$day)
table(lunch$day)

colMeans(dinner[c('total_bill', 'tip', 'size')])
colMeans(lunch[c('total_bill', 'tip', 'size')])
tip.rate <- tips$tip/tips$total_bill # 손님별 팁의 비율
mean(tip.rate) # 평균 팁의 비율

#데이터 입출력

# 데이터 입력
age <- c(28, 17, 35, 46, 23, 67, 30, 50)
age
# 정보 추출
young <- min(age)
old <- max(age)
# 처리 결과 출력
cat('가장 젊은 사람의 나이는', young, '이고,’,
"가장 나이든 사람의 나이는', old, '입니다. \n')

x <- scan()
y <- scan(what="")

df <- data.frame()
exam = edit(df) #데이터프레임 편집기
exam

#화면에서 데이터 입력받기
install.packages('svDialogs') # 패키지 설치
library(svDialogs)
user.input <- dlgInput('Input income')$res 
user.input
income <- as.numeric(user.input) # 문자열을 숫자로
income
tax <- income * 0.05 # 세금 계산
cat('세금: ', tax)

#체질량지수 구하기
height <- dlgInput('Input height(cm)')$res
weight <- dlgInput('Input weight(kg)')$res

height <- as.numeric(height)
weight <- as.numeric(weight)

height <- height /100
bmi <- weight/(height^2)
cat('입력한 키는 ', height*100, 'cm, 몸무게는 ', weight,'kg 입니다. \n',sep = "")
cat('BMI는 ', bmi, '입니다.', sep = "")


#파일 읽기 / 저장
getwd()
air <- read.csv('airquality.csv', header = T)
head(air)

my.iris <- subset(iris, Species == "Setosa")
my.iris

write.csv(my.iris, 'my_iris.csv', row.names = F) # CSV파일에 저장하기

#install.packages('xlsx')  패키지 설치하기
library(xlsx) # 패키지 불러오기
air <- read.xlsx('airquality.xlsx', header=T, sheetIndex=1) # .xlsx 파일 읽기 header = T파일의 첫번쨰 행은 데이터 값이 아닌 열이름이라는 뜻
head(air)

# 엑셀쓰기
library(xlsx) # 패키지 불러오기
my.iris <- subset(iris, Species=='setosa') # setosa 품종 데이터만 추출
write.xlsx(my.iris, 'my_iris.xlsx', row.names=F) # 파일에 저장하기

# ggplot2
library(ggplot2)
str(diamonds) 
diamonds.new <- subset(diamonds, cut == 'Premium' & carat >= 2)
write.csv(diamonds.new, 'shiny_diamonds.csv', row.names = F)
diamonds.load <- read.csv('shiny_diamonds.csv', header = T)
diamonds.new <- subset(diamonds.load, color != 'D')
library(xlsx)
write.xlsx(diamonds.new, 'shiny_diamonds.xlsx', row.names = F)



print('Begin work') # 화면으로 출력
a <- 10; b <- 20
sink('result.txt', append=T) # 파일로 출력 시작
cat('a+b=', a+b, '\n')
sink( ) # 파일로 출력 정지
cat('hello world \n') # 화면으로 출력
sink('result.txt', append=T) # 파일로 출력 시작
cat('a*b=', a*b, '\n')
sink( ) # 파일로 출력 정지
print("End work") # 화면으로 출력

sink('bmi.txt', append = T) # append = T : 새로운 결과를 이어붙이기
cat(height*100, weight, bmi)
cat('\n') # 줄바꿈을 위한 입력
sink( )

# 조건
job.type <- 'A'
if (job.type == 'B') {
  bonus <- 200 # 직군이 B일 때 실행
} else {
  bonus <- 100 # 직군이 B가 아닌 나머지 경우 실행
}
print(bonus)

# else가 생략된 if문
job.type <- 'A'
bonus <- 100
if (job.type == 'B') {
  bonus <- 200 # 직군이 B일 때 실행
}
print(bonus)
# -------------------
a <- 10
if (a<5) {
  print(a)
} else {
  print(a*10)
  print(a/10)
}

# -------------------
a <- 10
b <- 20
if (a>5 & b>5) { # and
  print(a+b)
}
if (a>5 | b>30) { # or
  print(a*b)
}

# if-else를 이용한 처리 ###############
a <- 10
b <- 20
if (a>b) {
  c <- a
} else {
  c <- b
}
print(c)
# ifelse를 이용한 처리 ###############
a <- 10
b <- 20
c <- ifelse(a>b, a, b)
print(c)

#num 12 설정
#num이 홀수이면 'odd' 출력, 
#num이 짝수인지 'even' 출력
num = 12
if (num/2 ==0){
  print('even')
} else {
  print('odd')
}
#-----------------------------------------
num <- 12
if(num %% 2 == 0) {
  type <- 'even'
} else {
  type <- 'odd'
}
print(type)


##--------------
library(svDialogs)
purchase <- dlgInput('Enter the purchase amount')$res
purchase <- as.numeric(purchase )

type <- NULL
ratio <- NULL

if (purchase >= 300000) {
  type <- '플래티넘'
  ratio <- 0.07
} else if (purchase >=200000) {
  type <- '골드'
  ratio <- 0.05
} else if (purchase >= 100000) {
  type <- '실버'
  ratio <- 0.03
} else {
  type <- '프렌즈'
  ratio <- 0.01
}
cat('고객님은', type, '회원으로 구매액의', ratio*100, '%가 적립됩니다.')

i <- 1
while (i<=10){
  print(i)
  i <- i+1
}

#for(반복변수 in 반복범위){
#    반복할 명령문
#}

for(i in 1:5) {
  print('*')
}

for(
  i in 6:10) {
  print(
    i
  )
}
for(i in 1:9) {
  cat('2 *', i,'=', 2*i,'\n')
}

for(i in 1:20) {
  if(i%%2==0) { # 짝수인지 확인
    cat(i, ' ')
  }
}


for(i in 1:50){
  if(i %% 3 == 0 | i %% 4 == 0){
    cat(i, ' ')
  }
}


sum <- 0
for(i in 1:100) {
  sum <- sum + i # sum에 i 값을 누적
}
print(sum)

# apply

apply(iris[,1:4], 1, mean) # 행 방향으로 함수 적용
apply(iris[,1:4], 2, mean) # 열 방향으로 함수 적용

sub1 <- c(14, 16, 12, 20, 8, 6, 12, 18, 16, 10)
sub2 <- c(18, 14, 14, 16, 10, 12, 10, 20, 14, 14)
sub3 <- c(44, 38, 30, 48, 42, 50, 36, 52, 54, 32)
score <- data.frame(sub1, sub2, sub3)

total <- apply(score, 1, sum)
scoreset <- cbind(score, total)

result <- c( )
for(i in 1:nrow(scoreset)){
  if(scoreset[i,1] < 20*0.4 | scoreset[i,2] < 20*0.4 | 
     scoreset[i,3] < 60*0.4){
    result[i] <- '불합격'
  }else if(scoreset[i,4] >= 60){
    result[i] <- '합격'
  }else{
    result[i] <- '불합격'
  }
  cat(i, '번째 응시생은', result[i],'입니다.\n')
}

## Day03







































