# numpy패키지

import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from pandas.core.frame import DataFrame
from pandas.core.groupby.generic import AggScalar
plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4])
X = [1,2,3,4,5,6,7]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

plt.plot(X,Y)
plt.show()
X = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

plt.plot(X,Y)
plt.xlabel("day")
plt.ylabel("temperature")
plt.show()
X = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [20, 23, 24, 25, 19.2, 28.3, 25.9]
plt.plot(X,Y1, X, Y2,)
plt.xlabel("day")
plt.ylabel("temperature")
plt.show()
plt.legend(loc="upper left")
plt.title("Temperatures of Cities")
plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4], ":+", color="red")
import numpy as np
ftemp = [ 63, 73, 80, 86, 84, 78, 66, 54, 45, 63 ]
F = np.array(ftemp)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[0][2]
b[1][1]

heights = [ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ]
weights = [ 86, 74, 59, 95, 80, 68 ]

np_heights = np.array(heights)
np_weights = np.array(weights)
import matplotlib.pyplot as plt
A = np.arange(1, 10, 2)
plt.plot(A)
plt.show()

A = np.linspace(0, 10, 100)
import matplotlib.pyplot as plt
plt.plot(A)
plt.show()
np.random.seed(100)
np.random.randn(5)
np.random.randn(5, 4)
m, sigma = 10, 2
m + sigma*np.random.randn(5)
mu, sigma = 0, 0.1
np.random.normal(mu, sigma, 5)

import numpy as np
import matplotlib.pyplot as plt

Pure = np.linspace(0, 10, 100)# 1부터 10까지 100개의 데이터 생성
noise =np.random.normal(0, 1, 100)
 # 평균이 0이고 표준편차가 1인 100개의 난수 생성

signal = Pure + noise

plt.plot(signal)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
numbers = np.random.normal(size=10000)
plt.hist(numbers) #히스토 그램
plt.xlabel("value")
plt.ylabel("freq")
plt.show()
#number안에 들어 있는
#10000개의 난수에 대하여 각 구간별로 몇 개의 난수가 들어 있는지 계산하
#여 히스토그램으로 그린다


numbers = np.random.normal(size=10000)
noise =np.random.normal(10, 2, 10000)
 # 평균이 10이고 표준편차가 2인 10000개의 난수 생성

plt.hist(numbers, bins = 20)
plt.hist(noise, bins = 20)
plt.show()
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
a = np.linspace(-2*np.pi,2*np.pi,100)

y1 = np.sin(a)
y2 = 3*np.sin(a)

plt.plot(a,y1,a,y2)
plt.show()

ypred=np.array([1,0,0,0,0])
y=np.array([0,1,0,0,0])
n = 5
mse = (1/n)*np.sum(np.square(ypred-y))
print(mse)

ypred = np.array

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a[0:3, 0:2]
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a > 5
s = np.array([220,250,230])
s = s+100
s

x = np.arange(0, 10)
x1 = np.ones(10)
x2 = x
x3 = np.square(x)

plt.plot(x,x1,x,x2,x,x3)

plt.show()

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.transpose()


a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
x
# 0부터 8까지 3행3열 생성
a = np.arange(0,9).reshape((3,3))
a

x = np.ones((10,10))
x[1:-1,1:-1]=0
print(x)

a = np.arange(0, 10)
a[5:9]*-1

a = np.arange(0,9).reshape((3,3))

np.sum(a)
np.sum(a, axis = 0)
np.sum(a, axis = 1)

a = [2,0,3,6,4,6,8,12,10,9,18,20,22]
plt.plot(a)
plt.show()

import pandas as pd
titanic = pd.read_csv('titanic.csv')
a = titanic["Age"]
max(a)
titanic.describe()

data = {'name': ['kim', 'park',' lee', 'choi'],'age':[20,23,21,26]}
df = pd.DataFrame(data, index=["학번1", "학번2", "학번3", "학번4"])
df

ser = pd.Series(data)

titanic = pd.read_csv('titanic.csv', index_col=0)
titanic.head(8)

df = pd.DataFrame(np.random.randint(0, 100, size=(5,4)), columns=list('ABCD')

con = pd.read_csv('countries.csv')

ages = titanic["Age"]
ages.head()

titanic[["Name", "Age", "Sex"]]
#20세미만의 승객이름
titanic.loc[titanic["Age"] < 20, "Name"]
titanic[titanic["Pclass"].isin([1, 2])]
#20~23행 5~7열
titanic.iloc[20:23, 5:7]
# 데이터 정렬
titanic.sort_values(by="Age").head()

#클래스와 연령에 따라 내림차순
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

# 데이터 프레임 만들기
data = {
    "city": ["aaa","bbb","ccc","ddd"],
    "name": ["김", "이", "박","최"],
    "job" : ["학생1", "학생2", "학생3", "학생4"],
    "age" : [11,23,42,53]
}

df = pd.DataFrame(data)
df.loc[2] # 3번줄 데이터

df.name.loc[2]