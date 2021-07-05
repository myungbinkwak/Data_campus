score <- c(76, 84, 69, 50, 95, 60, 82, 71, 88, 84)
which(score==69) # 성적이 69인 학생은 몇 번째에 있나?
which(score>=85) # 성적이 85 이상인 학생은 몇 번째에 있나?
max(score) # 최고 점수는 몇 점인가?
which.max(score) # 최고 점수는 몇 번째에 있나?
min(score) # 최저 점수는 몇 점인가?
which.min(score) # 최저 점수는 몇 번째에 있나?

score <- c(76, 84, 69, 50, 95, 60, 82, 71, 88, 84)
idx <- which(score<=60) # 성적이 60 이하인 값들의 인덱스
score[idx] <- 61 # 성적이 60 이하인 값들은 61점으로 성적 상향조정
score # 상향조정된 성적 확인
idx <- which(score>=80) # 성적이 80 이상인 값들의 인덱스
score.high <- score[idx] # 성적이 80 이상인 값들만 추출하여 저장
score.high # score.high의 내용 확인

idx <- which(iris$Petal.Length>5.0) # 꽃잎 길이가 5.0 이상인
idx
iris.big <- iris[idx,] # 인덱스에 해당하는 값만 추출하여 저장
iris.big

score <- c(60,40,95,80)
names(score) <- c('John','Jane','Tom','David')
score # 성적 데이터 출력
idx <- which.max(score)
names(score)[idx] # 성적이 제일 좋은 학생의 이름

install.packages('Stat2Data')
library(Stat2Data)
data(ChildSpeaks)
str(ChildSpeaks)

idx <- which(ChildSpeaks$Age < 9)
ChildSpeaks[idx, 'm1'] <- 5
idx <- which(ChildSpeaks$Age >= 9 & ChildSpeaks$Age < 15 )
ChildSpeaks[idx, 'm1'] <- 4
idx <- which(ChildSpeaks$Age >= 15 & ChildSpeaks$Age < 21 )
ChildSpeaks[idx, 'm1'] <- 3
idx <- which(ChildSpeaks$Age >= 21 & ChildSpeaks$Age < 27 )
ChildSpeaks[idx, 'm1'] <- 2
idx <- which(ChildSpeaks$Age >= 27 )
ChildSpeaks[idx, 'm1'] <- 1

idx <- which(ChildSpeaks$Gesell < 70)
ChildSpeaks$m2[idx] <- 1
idx <- which(ChildSpeaks$Gesell >= 70 & ChildSpeaks$Gesell < 90 )
ChildSpeaks$m2[idx] <- 2
idx <- which(ChildSpeaks$Gesell >= 90 & ChildSpeaks$Gesell < 110 )
ChildSpeaks$m2[idx] <- 3
idx <- which(ChildSpeaks$Gesell >= 110 & ChildSpeaks$Gesell < 130 )
ChildSpeaks$m2[idx] <- 4
idx <- which(ChildSpeaks$Gesell >= 130 )
ChildSpeaks$m2[idx] <- 5

ChildSpeaks$total <- ChildSpeaks$m1 + ChildSpeaks$m2

idx <- which(ChildSpeaks$total < 3)
ChildSpeaks$result[idx] <- '매우느림'
idx <- which(ChildSpeaks$total >= 3 & ChildSpeaks$total < 5 )
ChildSpeaks$result[idx] <- '느림'
idx <- which(ChildSpeaks$total >= 5 & ChildSpeaks$total < 7 )
ChildSpeaks$result[idx] <- '보통'
idx <- which(ChildSpeaks$total >= 7 & ChildSpeaks$total < 9 )
ChildSpeaks$result[idx] <- '빠름'
idx <- which(ChildSpeaks$total >= 9 )
ChildSpeaks$result[idx] <- '매우빠름'

ChildSpeaks
ChildSpeaks[which.min(ChildSpeaks$total),]

## 데이터시각화
favorite <- c('WINTER', 'SUMMER', 'SPRING', 'SUMMER', 'SUMMER',
              'FALL', 'FALL', 'SUMMER', 'SPRING', 'SPRING')   # 자료 입력
favorite                            # favorite의 내용 출력
table(favorite)                     # 도수분포 계산

ds <- table(favorite)                      # 도수분포표 저장
ds                                         # 도수분포표 내용 확인     
barplot(ds, main='favorite season')        # 막대그래프 작성

age.A <- c(13709, 10974, 7979, 5000, 4250)
age.B <- c(17540, 29701, 36209, 33947, 24487)
age.C <- c(991, 2195, 5366, 12980, 19007)

ds <- rbind(age.A, age.B, age.C)
colnames(ds) <- c('1970','1990','2010','2030','2050')  
ds

# 그래프의 작성
barplot(ds, main='인구 추정')    

#색깔
barplot(ds, main='인구 추정', 
        col=c('green','blue','yellow'))

#범례
barplot(ds, main='인구 추정', 
        col=c('green','blue','yellow'),
        beside=TRUE)    

# 무엇을 의미하는지
barplot(ds, main='인구 추정', 
        col=c('green','blue','yellow'),
        beside=TRUE,
        legend.text=T)

# 빈영역을 찾아서 정하기
par(mfrow=c(1, 1), mar=c(5, 5, 5, 7))
barplot(ds, main='인구 추정', 
        col=c('green','blue','yellow'),
        beside=TRUE,
        legend.text=T,
        args.legend = list(x='topright', bty='n', inset=c(-0.25,0)))


par(mfrow=c(1, 1), mar=c(5, 5, 5, 7))        # 그래프 윈도우 설정
barplot(ds, main='인구 추정', 
        col=c('green','blue','yellow'),
        beside=TRUE,
        legend.text=c('0~14세','15~64세','65세 이상'), #범례내용 변경
        args.legend = list(x='topright', bty='n', inset=c(-0.25,0)))
par(mfrow=c(1, 1), mar=c(5,4,4,2)+0.1)      # 그래프창 설정 해제

#히스토그램
head(cars)                    
dist <- cars[,2]              # 자동차 제동거리
dist
hist(dist,                    # data
     main='Histogram for 제동거리',   # 제목
     xlab ='제동거리',        # x축 레이블              
     ylab='빈도수',           # y축 레이블                     
     border='blue',           # 막대 테두리색  
     col='green',             # 막대 색
     las=2,                   # x축 글씨 방향(0~3) 
     breaks=5)                # 막대 개수 조절

result <- hist(dist,                    # data
               main='Histogram for 제동거리',    # 제목
               breaks=5)                # 막대 개수 조절
result
freq <- result$counts                   # 구간별 빈도수 저장
names(freq) <- result$breaks[-1]        # 구간값을 이름으로 지정
freq                                    # 구간별 빈도수 출력

par(mfrow=c(2,2), mar=c(3,3,4,2))     # 화면 분할(2x2)               

hist(iris$Sepal.Length,               # 그래프 1
     main='Sepal.Length',
     col='orange')             

barplot(table(mtcars$cyl),            # 그래프 2
        main='mtcars',
        col=c('red','green','blue'))              

barplot(table(mtcars$gear),           # 그래프 3
        main='mtcars',
        col=rainbow(3),               # 레인보우 팔레트 사용
        horiz=TRUE)              

pie(table(mtcars$cyl),                # 그래프 4
    main='mtcars',
    col=topo.colors(3),           # topo 팔레트 사용
    radius=2)              

par(mfrow=c(1,1), mar=c(5,4,4,2)+.1)  # 화면 분할 취소 

##DIA
library(Stat2Data)
data(Diamonds)
ds <- Diamonds$PricePerCt  # 캐럿당 가격

hist(ds, main = '캐럿당 가격 분포',
     breaks = 9)

hist(ds, main = '캐럿당 가격 분포',
     breaks = 9,
     xlab = '캐럿당 가격($)', ylab = '빈도수', las = 1)

color <- rep('#a8dadc', 9)
color[3] <- '#1d3557'

hist(ds, main = '1캐럿당 가격 분포',
     breaks = 9,
     xlab = '캐럿당 가격($)', ylab = '빈도수', las = 1,
     col = color,
     border = '#457b9d')

## CARDATA
library(carData)
ds <- Chile
colors = rainbow(20)     # 레인보우 팔레트에서 20색 선택

par(mfrow = c(2,3))

barplot(table(ds$region), main = '지역별 분포', col=colors[1:5])
barplot(table(ds$sex), main = '성별 분포', , col=colors[6:7])
barplot(table(ds$education), main = '교육수준별 분포', col=colors[8:10])

hist(ds$age, breaks = 6, main = '연령', xlab = 'age', col=colors[1:6])
hist(ds$income, breaks = 4, main = '수입', xlab = 'income', 
     col=colors[11:14])
hist(ds$statusquo, breaks = 9, main = '정책 지지도', xlab = 'support', 
     col=colors[15:20]) 

par(mfrow = c(1,1))

#PIE
favorite <- c('WINTER', 'SUMMER', 'SPRING', 'SUMMER', 'SUMMER',
              'FALL', 'FALL', 'SUMMER', 'SPRING', 'SPRING')   # 자료 입력
ds <- table(favorite)                                         # 도수분포 계산
ds                
pie(ds, main='선호 계절',                                     # 원그래프 작성
    radius=1)                                   
#색
pie(ds, main='선호 계절',
    col=c('brown','green','red','black'),    # 파이의 색 지정
    radius=1 )                               # 파이의 크기 지정 

# 3차원 원그래프
#install.packages('plotrix')
library(plotrix)
pie3D(ds, main='선호 계절',
      labels=names(ds),                              # 파이별 레이블지정
      labelcex=1.0,                                  # 레이블의 폰트크기
      explode=0.1,                                   # 파이 간 간격
      radius=1.5,                                    # 파이의 크기 
      col=c('brown','green','red','yellow'))         # 파이의 색 지정

#꺾은선 그래프
month = 1:12                             # 자료 입력
late  = c(5,8,7,9,4,6,12,13,8,6,6,4)     # 자료 입력      
plot(month,                              # x data
     late,                               # y data
     main='지각생 통계',                 # 제목 
     type='l',                           # 그래프의 종류 선택(알파벳) 
     lty=1,                              # 선의 종류(line type) 선택
     lwd=1,                              # 선의 굵기 선택
     xlab='Month',                       # x축 레이블
     ylab='Late cnt'                     # y축 레이블
)


#데이터가 2개
month = 1:12
late1  = c(5,8,7,9,4,6,12,13,8,6,6,4)
late2  = c(4,6,5,8,7,8,10,11,6,5,7,3)
plot(month,                                # x 데이터
     late1,                                # y 데이터
     main='Late students',
     type='b',                             # 그래프의 종류 선택(알파벳)
     lty=1,                                # 선의 종류(line type) 선택
     col='red',                            # 선의 색깔 선택          
     xlab='Month',                         # x축 레이블
     ylab='Late cnt'                       # y축 레이블
)
lines(month,                               # x 데이터
      late2,                               # y 데이터
      type='b',                            # 선의 종류(line type) 선택
      col='blue')                          # 선의 색깔 선택

#BOX Plot
dist <- cars[,2]                      # 자동차 제동거리 (단위: 피트)
boxplot(dist, main='자동차 제동거리')

boxplot.stats(dist)

boxplot(Petal.Length~Species,            # 자료와 그룹 정보
        data=iris,                       # 자료가 저장된 자료구조
        main='품종별 꽃잎의 길이',       # 그래프의 제목    

                col=c('green','yellow','blue'))  # 상자들의 색

# 산점도
wt <-mtcars$wt                   # 중량 자료
mpg <- mtcars$mpg                # 연비 자료
plot(wt, mpg,                    # 2개 변수(x축, y축)     
     main='중량-연비 그래프',    # 제목
     xlab='중량',                # x축 레이블
     ylab='연비(MPG)',           # y축 레이블
     col='red',                  # point의 color
     pch=19)                     # point의 종류 


vars <- c('mpg','disp','drat','wt')    # 대상 변수 
target <- mtcars[,vars]                # 대상 자료 생성  
head(target)
pairs(target,                          # 대상 자료     
      main='Multi plots') 

iris.2 <- iris[,3:4]                # 데이터 준비
levels(iris$Species)                # 그룹 확인
group <- as.numeric(iris$Species)   # 점의 모양과 색
group                               # group 내용 출력
color <- c('red','green','blue')    # 점의 컬러
plot(iris.2, 
     main='Iris plot',
     pch=c(group),
     col=color[group]) 

plot(iris.2, 
     main='Iris plot',
     pch=c(group),
     col=color[group]) 

legend(x='bottomright',               # 범례의 위치  
       legend=levels(iris$Species),   # 범례의 내용
       col=c('red','green','blue'),   # 색 지정
       pch=c(1:3))                    # 점의 모양 


##---- 10----------------------------

#install.packages("carData")
library(carData)

# (1) 자료 준비
room.class <- TitanicSurvival$passengerClass  # 선실 정보
room.class                

# (2) 도수분포 계산
tbl <- table(room.class)   
tbl
sum(tbl)                                      # 전체 탑승객수 

# (3) 막대그래프 작성
barplot(tbl, main='선실별 탑승객',       
        xlab='선실 등급',
        ylab='탐승객수',
        col=c('blue', 'green', 'yellow'))                    

#(4) 원그래프 작성
tbl/sum(tbl)                                 # 선실별 탑승객 비율
par(mar=c(1,1,4,1))                     
pie(tbl, main='선실별 탑승객',       
    col=c('blue', 'green', 'yellow'))                    
par(mar=c(5.1,4.1,4.1,2.1))

##----------
# (1) 자료 준비
grad <- state.x77[,'HS Grad']   # 주별 고등학교 졸업율
grad                

# (2) 사분위수
summary(grad)
var(grad)                # 분산
sd(grad)                 # 표준 편차

# (3) 히스토그램
hist(grad, main='주별 졸업율',
     xlab='졸업율',
     ylab='주의 개수',
     col='orange')

# (4) 상자그림
boxplot(grad, main='주별 졸업율',
        col='orange')

# (5) 졸업율이 가장 낮은 주
idx <- which(grad==min(grad))
grad[idx]

# (6) 졸업율이 가장 높은 주
idx <- which(grad==max(grad))
grad[idx]

# (7) 졸업율이 평균 이하인 주
idx <- which(grad<mean(grad))
grad[idx] 
##----------------------
# (1) 자료 준비
ds <- read.csv('fdeaths.csv', row.names='year')
ds

#(2) 선그래프 작성
my.col <- c('black', 'blue','red', 'green','purple','dark gray')
my.lty <- 1:6

plot(1:12,                       # x data
     ds[1,],                     # y data(1974년 자료)
     main='월별 사망자 추이',    # 그래프 제목
     type='b',                   # 그래프 종류
     lty=my.lty[1],              # 선의 종류
     xlab='Month',               # x축 레이블
     ylab='사망자수',            # y축 레이블
     ylim=c(300,1200),           # y축 값의 범위   
     col=my.col[1]               # 선의 색
)

for( i in 2:6) {
  lines(1:12,                      # x data
        ds[i,],                    # y data(1975~1979)
        type='b',                  # 그래프 종류
        lty=my.lty[i],             # 선의 종류
        col=my.col[i]              # 선의 색
  )
}

legend(x='topright',               # 범례의 위치
       lty=my.lty,                 # 선의 종류
       col=my.col,                 # 선의 색
       legend=1974:1979            # 범례의 내용
)

##--------------------
# (1) 자료 확인
head(pressure)

# (2) 산점도 작성
plot(pressure$temperature,     # x축 자료
     pressure$pressure,        # y축 자료
     main='온도와 기압',       # 그래프 제목
     xlab='온도(화씨)',        # x축 레이블
     ylab='기압',              # y축 레이블
)
##--------------------
#(1) 자료의 확인
head(cars)

#(2) 산점도의 작성
plot(cars$speed,                        # x축 자료
     cars$dist,                         # y축 자료
     main='자동차 속도와 제동거리',     # 그래프 제목
     xlab='속도',                       # x축 레이블
     ylab='제동거리',                   # y축 레이블
)

#(3) 상관계수 
cor(cars$speed, cars$dist)
##------------------
# (1) 자료 확인
st <- data.frame(state.x77)     # 매트릭스를 데이터프레임으로 변환 
head(st)

# (2) 다중 산점도 작성
plot(st)

# (3) 다중 상관계수
cor(st)

##너무 많은데