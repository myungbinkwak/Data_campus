## 결측값

z <- c(1,2,3,NA,5,NA,8)      # 결측값이 포함된 벡터 z
sum(z)                       # 정상 계산이 되지 않음
is.na(z)                     # NA 여부 확인
sum(is.na(z))                # NA의 개수 확인
sum(z, na.rm=TRUE)           # NA를 제외하고 합계를 계산

z1 <- c(1,2,3,NA,5,NA,8)      # 결측값이 포함된 벡터 z1
z2 <- c(5,8,1,NA,3,NA,7)      # 결측값이 포함된 벡터 z2
z1[is.na(z1)] <- 0            # NA를 0 로 치환 
z1                            
z3 <- as.vector(na.omit(z2))  # NA를 제거하고 새로운 벡터 생성
z3

# NA를 포함하는 test 데이터 생성
x <- iris
x[1,2]<- NA; x[1,3]<- NA
x[2,3]<- NA; x[3,4]<- NA  
head(x)

# for를 이용한 방법
for (i in 1:ncol(x)) {
  this.na <- is.na(x[,i]) 
  cat(colnames(x)[i], '\t', sum(this.na), '\n')
}

# apply를 이용한 방법
col_na <- function(y) {
  return(sum(is.na(y)))
}

na_count <-apply(x, 2, FUN=col_na)
na_count

rowSums(is.na(x))            # 행별 NA 개수  
sum(rowSums(is.na(x))>0)     # NA가 포함된 행의 개수 
sum(is.na(x))                # 데이터셋 전체에서 NA 개수

head(x)
x[!complete.cases(x),]              # NA가 포함된 행들을 나타냄
y <- x[complete.cases(x),]          # NA가 포함된 행들을 제거
head(y)                             # 새로운 데이터셋 y의 내용 확인

v1 <- c(1,7,6,8,4,2,3)
v1 <- sort(v1)                  # 오름차순
v1
v2 <- sort(v1, decreasing=T)    # 내림차순 
v2

name <- c('정대일','강재구','신현석','홍길동')
sort(name)                      # 오름차순
sort(name, decreasing=T)        # 내림차순 

name <- c('정대일','강재구','신현석','홍길동')
order(name)                            # 오름차순
order(name, decreasing=T)              # 내림차순

idx <- order(name)
name[idx]                              # 오름차순 정렬

head(iris)
order(iris$Sepal.Length)
iris[order(iris$Sepal.Length),]                   # 오름차순으로 정렬
iris[order(iris$Sepal.Length, decreasing=T),]     # 내림차순으로 정렬
iris.new <- iris[order(iris$Sepal.Length),]       # 정렬된 데이터를 저장
head(iris.new)
iris[order(iris$Species, decreasing=T, iris$Petal.Length),]     # 정렬 기준이 2개

x <- 1:100
y <- sample(x, size=10, replace=FALSE)    # 비복원 추출
y

idx <- sample(1:nrow(iris), size=50, replace=F)
iris.50 <- iris[idx,]      # 50개의 행 추출
dim(iris.50)               # 행과 열의 개수 확인
head(iris.50)

sample(1:20, size=5)
sample(1:20, size=5)
sample(1:20, size=5)

set.seed(100)
sample(1:20, size=5)
set.seed(100)
sample(1:20, size=5)
sample(1:20, size=5)

combn(1:5,3)              # 1~5에서 3개를 뽑는 조합 

x = c("red","green","blue","black","white")
com <- combn(x,2)         # x의 원소를 2개씩 뽑는 조합 
com

for(i in 1:ncol(com)) {    # 조합을 출력
  cat(com[,i], "\n")
}

agg <- aggregate(iris[,-5], by=list(iris$Species), 
                 FUN=mean)
agg

agg <- aggregate(iris[,-5], by=list(품종=iris$Species), 
                 FUN=sd)
agg

head(mtcars)
agg <- aggregate(mtcars, by=list(cyl=mtcars$cyl,
                                 vs=mtcars$vs),FUN=max)
agg

###LAB


install.packages("carData")

# (1)
library(carData)
str(UN)         # 요약 정보 확인

# (2)
col_na <- function(y) {
  return(sum(is.na(y)))
}

apply(UN, 2, FUN=col_na)

# (3)
mean(UN$lifeExpF, na.rm=T)   # NA 제외하고 계산

# (4)
tmp <- UN[,c('pctUrban','infantMortality')]
tmp <- tmp[complete.cases(tmp),]    # NA 제거
colMeans(tmp)

# (5)
tmp <- subset(UN, region=='Asia')   # 아시아 국가 추출
mean(tmp$fertility, na.rm=T)

##---------------------------------------------------
# (1)
library(carData)
str(Highway1)

# (2)
Highway1[order(Highway1$rate, decreasing = T),]

# (3)
tmp <- Highway1[order(Highway1$len, decreasing = T),'len']
tmp             # 구간별 길이를 내림차순으로 정렬한 결과
sum(tmp[1:10])  # 상위 10개 구간의 총 길이

# (4)
tmp <- Highway1[order(Highway1$adt),c('adt','rate')]
tmp             
tmp[1:10,]

# (5)
tmp <- Highway1[order(Highway1$slim, decreasing = T),c('len','adt','rate')]
tmp             
tmp[1:5,]
##---------------------------------------------------
# (1)
library(carData)
str(KosteckiDillon)

# (2)
tot.mean <- mean(KosteckiDillon$dos)
tot.mean

# (3)
for (rate in (1:5)*0.1) {
  set.seed(100)
  idx <- sample(nrow(KosteckiDillon), nrow(KosteckiDillon)*rate)
  sam.data <- KosteckiDillon[idx,'dos']  # 샘플링 자료 추출
  tmp.mean <- mean(sam.data)             # 샘플링 자료 평균
  cat('Diff:', rate, tot.mean-tmp.mean, '\n')
}  

# (4)
cbn <- combn(1:5, 3)
cbn
ncol(cbn)     # 조합의 개수
##---------------------------------------------------

# (1)
library(carData)
data('CES11')        # 데이터셋 불러오기
str(CES11)

# (2)
table(CES11$abortion)              # 반대, 찬성 인원수
table(CES11$abortion)/nrow(CES11)  # 반대, 찬성 비율

# (3)
agg <- aggregate(CES11[,'abortion'], by=list(성별=CES11$gender), FUN=table)
agg.2 <- agg[,2]                       # Yes/No 빈도수 부분만 추출
agg.2[1,] <- agg.2[1,]/sum(agg.2[1,])  # female Yes/No 비율 계산
agg.2[2,] <- agg.2[2,]/sum(agg.2[2,])  # male Yes/No 비율 계산
rownames(agg.2) <- agg[,1]
agg.2

# (4)
agg <- aggregate(CES11[,'abortion'], by=list(지역=CES11$urban), FUN=table)
agg.2 <- agg[,2]                       # Yes/No 빈도수 부분만 추출
agg.2[1,] <- agg.2[1,]/sum(agg.2[1,])  # 도시외 지역 Yes/No 비율 계산
agg.2[2,] <- agg.2[2,]/sum(agg.2[2,])  # 도시지역 Yes/No 비율 계산
rownames(agg.2) <- agg[,1]
agg.2

##--------------------------------------------------
# (1)
library(carData)
help(Chile)       # 데이터셋에 대한 도움말 확인
str(Chile)

# (2)
sum(is.na(Chile))                    # 결측값 개수 확인, 295개의 결측값 존재
ch <- Chile[complete.cases(Chile),]  # 결측값 제거

# (3)
idx <- sample(nrow(ch), nrow(ch)*.6)   # 60% 샘플링
ch60 <- ch[idx, ]
dim(ch60)

# (4)
agg <- aggregate(ch60[,'population'], by=list(지역=ch60$region), sum)
agg[order(agg$x, decreasing = T),]

# (5)
table(ch60$vote)

# (6)
no.people <- table(ch60$sex)               # 여성, 남성 응답자수     
tmp    <- subset(ch60, vote=='Y')          # 찬성만 추출 
agg <- aggregate(tmp[,'vote'], by=list(성별=tmp$sex), length)
yes.ratio <- agg$x / no.people             # 찬성 비율 계산
yes.ratio

# (7)
no.region <- table(ch60$region)            # 지역별 응답자수     
tmp    <- subset(ch60, vote=='Y')          # 찬성만 추출 
agg <- aggregate(tmp[,'vote'], by=list(지역=tmp$region), length)
yes.ratio <- agg$x / no.region             # 찬성 비율 계산
yes.ratio

