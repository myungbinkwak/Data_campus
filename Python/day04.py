a = [200,250,300,280,500]

def modify(values, factor):
    for i in range(len(5)):
        values[i] = values[i] * factor

print("�λ���", a) 
modify(a, 1.3)
print("�λ���", a)       

[i for i in range(100)
    if i % 2==0 and i % 3==0]

list1=[10, 20, 30, 40, 50]
list2 = [sum(list1[0:x+1])for x in range(0, len(list1))] 

print("���� ����Ʈ", list1)
print("���ο��Ʈ: ",list2)

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
    print("A�� B�� �����ϴ�.")
else :
    print("A�� B�� ���� �ʽ��ϴ�.")

list1 =[1,2,3,4,5,1,2,4 ]
len(set(list1)) # set �ߺ������������� ����(���δٸ� ����)

list1 =[1,2,3,4,5 ]
list2 =[3,4,5,6,7 ]
set(list1)&set(list2) # ����

S1 = "Hello World!"
S2 = "How are you?"

list1 = list(set(S1) & set(S2))

print("\n�������� ����:", end"")

for i in list1:
    print(i, end="")

"I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low"
#���� �ܾ��� ����= 17
{"be", "and", "shall", "low", "have", "made", "one", "exalted", "every", 
"mountain", "I", "that", "valley", "hill", "day", "a", "dream"}    

txt = input("�Է� �ؽ�Ʈ:  ")
words = txt.split(" ")
unique = set(words)
len(unique)

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"}
print( capitals["Korea"])
# print( capitals[��France��]) ����x -> ����

capitals ={}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"
print(capitals)

city = capitals.pop("UK") #����

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
word_dic = {} # �ܾ��� ���� Ƚ���� �����ϴ� ��ųʸ��� ����
for w in text_data.split():
    if w in word_dic:
        word_dic[w] +=1
    else:
        word_dic[w] = 1
for w, count in sorted(word_dic.items()): # Ű�� ���� �����Ͽ� �ݺ� ó���Ѵ�. 
    print(w, "�� ����Ƚ��=", count)

