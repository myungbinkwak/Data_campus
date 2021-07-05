a = [200,250,300,280,500]

def modify(values, factor):
    for i in range(len(5)):
        values[i] = values[i] * factor

print("인상전", a) 
modify(a, 1.3)
print("인상후", a)       

[i for i in range(100)
    if i % 2==0 and i % 3==0]

list1=[10, 20, 30, 40, 50]
list2 = [sum(list1[0:x+1])for x in range(0, len(list1))] 

print("원래 리스트", list1)
print("새로운리스트: ",list2)

list_ex1 = ['risk', 'issue', 'test', 'maintenance', 'maturity']
list_ex2 = ['security', 'plan', 'design', 'systematic', 'safety']
list_ex3 = ['maintenance', 'verification', 'validation']

if ('maintenance' in list_ex1) and (len(list_ex1) >= 5) :
    print('list_ex1 will be tested')
elif ('maintenance' in list_ex2) and (len(list_ex2) >= 5) :
     print('list_ex2 will be tested')
elif ('maintenance' in list_ex3) and (len(list_ex3) >= 5) :
    print('list_ex3 will be tested')
else :
     print('There is no available test list')


n1 = 10
n2 = 90
n1, n2 = (n2, n1) 

fruits =["apple","banana","grape"]
for index, value in enumerate(fruits):
    print(index, value)

fruits ={"apple","banana","grape"}
for x in sorted(fruits):
    print(x, end=" ")

A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}
if A == B :
    print("A와 B는 같습니다.")
else :
    print("A와 B는 같지 않습니다.")

list1 =[1,2,3,4,5,1,2,4 ]
len(set(list1)) # set 중복하지않은것의 개수(서로다른 정수)

list1 =[1,2,3,4,5 ]
list2 =[3,4,5,6,7 ]
set(list1)&set(list2) # 공통

S1 = "Hello World!"
S2 = "How are you?"

list1 = list(set(S1) & set(S2))

print("\n공통적인 글자:", end"")

for i in list1:
    print(i, end="")

"I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low"
#사용된 단어의 개수= 17
{"be", "and", "shall", "low", "have", "made", "one", "exalted", "every", 
"mountain", "I", "that", "valley", "hill", "day", "a", "dream"}    

txt = input("입력 텍스트:  ")
words = txt.split(" ")
unique = set(words)
len(unique)

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"}
print( capitals["Korea"])
# print( capitals[“France”]) 존재x -> 에러

capitals ={}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"
print(capitals)

city = capitals.pop("UK") #삭제

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
    print( key,":", capitals[key])

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key, value in capitals.items():
    print( key,":", value )

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"}
print( capitals.keys()) # key 
print( capitals.values()) # value

dic ={ i:str(i) for i in [1,2,3,4,5]}
print( dic )

fruits =["apple","orange","banana"]
dic ={ f:len(f) for f in fruits }
print( dic )

score_dic = { 
"Kim":[99,83,95],
"Lee":[68,45,78],
"Choi":[25,56,69]
}

text_data ="Create the highest, grandest vision possible for your life, because you become what you believe"
word_dic = {} # 단어들과 출현 횟수를 저장하는 딕셔너리를 생성
for w in text_data.split():
    if w in word_dic:
        word_dic[w] +=1
    else:
        word_dic[w] = 1
for w, count in sorted(word_dic.items()): # 키와 값을 정렬하여 반복 처리한다. 
    print(w, "의 등장횟수=", count)

