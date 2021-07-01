d <- c(1,2,3,4,5,6,7,8,9,10)
sum(d)
sum(2*d)
length(d)
mean(d[1:5])
max(d)
min(d)
sort(d) # 오름차순 정렬
sort(d, decreasing = FALSE) # 오름차순 정렬
sort(d, decreasing = TRUE) # 내림차순 정렬
v1 <- median(d)
v1
v2 <- sum(d)/length(d) # 벡터 d의 길이(값의 개수)
v2


d <- 1:9
d>=5 # d 원소 각각이 >=5인지 검사
d[d>5] # 6 7 8 9
sum(d>5) # 5보다 큰 값의 개수를 출력
sum(d[d>5]) # 5보다 큰 값의 합계를 출력
d==5
condi <- d > 5 & d < 8 # 조건을 변수에 저장
d[condi] # 조건에 맞는 값들을 선택
d

espresso <- c(4, 5, 3, 6, 5, 4, 7)
americano <- c(63, 68, 64, 68, 72, 89, 94)
latte <- c(61, 70, 59, 71, 71, 92, 88)


sale.espresso <- 2 * espresso
sale.americano <- 2.5 * americano
sale.latte <- 3.0 * latte

sale.espresso <- 2 * espresso
sale.americano <- 2.5 * americano
sale.latte <- 3.0 * latte

bt <- c('A', 'B', 'B', 'O', 'AB', 'A') # 문자형 벡터 bt 정의
bt.new <- factor(bt) # 팩터 bt.new 정의
bt # 벡터 bt의 내용 출력
bt.new # 팩터 bt.new의 내용 출력
bt[5] # 벡터 bt의 5번째 값 출력
bt.new[5] # 팩터 bt.new의 5번째 값 출력
levels(bt.new) # 팩터에 저장된 값의 종류를 출력
as.integer(bt.new) # 팩터의 문자값을 숫자로 바꾸어 출력
bt.new[7] <- 'B' # 팩터 bt.new의 7번째에 'B' 저장
bt.new[8] <- 'C' # 팩터 bt.new의 8번째에 'C' 저장
bt.new # 팩터 bt.new의 내용 출력

h.list <- c('balling', 'tennis', 'ski') # 취미를 벡터에 저장
person <- list(name='Tom', age=25, student=TRUE, hobby=h.list) # 리스트 생성
person # 리스트에 저장된 내용을 모두 출력
person[[1]] # 리스트의 첫 번째 값을 출력
person$name # 리스트에서 값의 이름이 name인 값을 출력
person[[4]] # 리스트의 네 번째 값을 출력

cafe <- list(espresso = c(4, 5, 3, 6, 5, 4, 7),
             americano = c(63, 68, 64, 68, 72, 89, 94),
             latte = c(61, 70, 59, 71, 71, 92, 88),
             price = c(2.0, 2.5, 3.0),
             menu = c('espresso','americano','latte'))

cafe$menu <- factor(cafe$menu)

names(cafe$price) <- cafe$menu

sale.espresso <- cafe$price['espresso'] * cafe$espresso
sale.americano <- cafe$price['americano'] * cafe$americano
sale.latte <- cafe$price['latte'] * cafe$latteo

sale.day <- sale.espresso + sale.americano + sale.latte # 요일별 매출액
names(sale.day) <- c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
sum(sale.day) # 총 매출액
sale.mean <- mean(sale.day) # 평균 매출액
names(sale.day[sale.day >= sale.mean])

accident <- c(31,26,42,47,50,54,70,66,43,32,32,22)
names(accident) <- c('M1','M2','M3','M4','M5','M6','M7','M8',
                     'M9','M10','M11','M12')
accident

sum(accident)

max(accident)
min(accident)

accident*0.9

accident[accident>=50]

month.50 <- accident[accident >= 50]   # 사고 건수 50이 넘는 달만 추출
names(month.50)  
names(accident[accident >= 50])        # 이렇게 실행해도 됨                  

length(accident[accident<50])

M6.acc <- accident[6]
accident[accident > M6.acc]
# 다음과 같이 한 줄 명령어로도 처리 가능
accident[accident > accident[6]]


z <- matrix(1:20, nrow=4, ncol=5)
z2 <- matrix(1:20, nrow=4, ncol=5, byrow=T)


x <- 1:4 # 벡터 x 생성
y <- 5:8 # 벡터 y 생성
z <- matrix(1:20, nrow=4, ncol=5) # 매트릭스 z 생성
m1 <- cbind(x,y) # x와 y를 열 방향으로 결합하여 매트릭스 생성
m1 # 매트릭스 m1의 내용을 출력
m2 <- rbind(x,y) # x와 y를 행 방향으로 결합하여 매트릭스 생성
m2 # 매트릭스 m2의 내용을 출력
m3 <- rbind(m2,x) # 매트릭스 m2와 벡터 x를 행 방향으로 결합
m3 # 매트릭스 m3의 내용을 출력
m4 <- cbind(z,x) # 매트릭스 z와 벡터 x를 열 방향으로 결합
m4 # 매트릭스 m4의 내용을 출력

z <- matrix(1:20, nrow=4, ncol=5) # 매트릭스 z 생성
z # 매트릭스 z의 내용 출력
z[2,1:3] # 2행의 값 중 1~3열에 있는 값
z[1,c(1,2,4)] # 1행의 값 중 1, 2, 4열에 있는 값
z[1:2,] # 1~2행에 있는 모든 값
z[,c(1,4)] # 1, 4열에 있는 모든 값


score <- matrix(c(90,85,69,78,85,96,49,95,90,80,70,60), nrow=4)
score
rownames(score) <- c('John','Tom','Mark','Jane')
colnames(score) <- c('English','Math','Science')
score


city <- c("Seoul","Tokyo","Washington") # 문자로 이루어진 벡터
rank <- c(1,3,2) # 숫자로 이루어진 벡터
city.info <- data.frame(city, rank) # 데이터프레임 생성
city.info


iris[,c(1:2)] # 1~2열의 모든 데이터
iris[,c(1,3,5)] # 1, 3, 5열의 모든 데이터
iris[,c("Sepal.Length","Species")] # 1, 5열의 모든 데이터
iris[1:5,] # 1~5행의 모든 데이터
iris[1:5,c(1,3)] # 1~5행의 데이터 중 1, 3열의 데이터

kcal <- c(514, 533, 566)
na <- c(917, 853, 888)
fat <- c(11, 13, 10)
menu <- c('새우', '불고기', '치킨')

burger <- data.frame(kcal, na, fat, menu)
