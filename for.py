# java int m []={10,20,30,40}
# m = [10,20,30,40,50] 대괄호를 사용한다
# MAP에 중괄호를 사용한다. 파이썬은 여러 자료형을 사용할 수있다/ 자바는 한가지 자료형만 사용가능
# 슬라이싱 인덱싱은 안된다.
from _ast import Pass, Break
kim ={"name":"김유신" , "age":30 , "tel":"1111-2222"}
print(kim)
# 데이터 꺼내는 방법
print(kim["name"])
print(kim.get("name"))

# 키만 뽑는 방법
keys = kim.keys()
print ( type(keys))
# 값만 뽑는 방법
values = kim.values()
print ( type(values))

#데이터 넣는 방법
if "id" not in kim.keys() :
    #id라는 방을 만들어서 "aaa"를 넣어라 , 조건문 없이 map에 넣을려고 하면 수정이 되어 버린다.
    kim["id"] = "aaa"
    #바꾸는 것으로 인식한다.
    kim["id"] = "bbb"
print (kim)

#튜플로 return 시켜준다.items()
for key, value in kim.items():
    print(key,value)
    
#지우는 방법
del kim["id"]
print(kim)
    
# 인덱싱 안된다 print (kim[1])
# 슬라이싱 안된다 print (kim[1:3])


#입력해주는것
#a = input("정수 : ")
#print(a)
#print(type(a))

#강제 형변환
#a = int( input ("정수 한개 :"))
#b = int(input ("정수 한개 :"))
#print(a+b)
#a= eval(input("정수"))
#b= eval(input("정수"))
#print (a+b)


#조건문

#a= eval(input("단 : "))
#if a >=2 and a <= 9:
    #pass
#    for i in range(1,10) :#range 마지막 값 end value-1 이다.
#        print(a,"*",i,"=",a*i)
#else :
#   print("잘못입력")    

#age = eval(input("나이 :"))
#if age <= 20:
    #print ("어린이")
#elif age <= 40:
    #print("청년") 
#elif age <= 60:
    #print("중년") 
#else :
#    print("노년") 


# 삼항연산
# 조건? 참 : 거짓 
a=6
        #참        조건        거짓
print ( "짝수" if a%2==0  else "홀수")
 
# 반복문
for i in range(10):
    print (i, end="")
print()

for i in range(1,11):
    print(i , end="") 
print() 
 
 
#증가값     start end 증가  
for i in range(0,10, 2):
    print (i,end= " ")
print()
#감소값 
for i in range(10,0, -1):
    print (i,end= " ")
print()

#나열형
m = [10,20,30,40,50]
print (type(m))
for a in m:
    print (a,end=" ")
print()

#튜플
m=(10,20,30,40,50)
print (type(m))
for a in m:
    print (a,end=" ")
print()

#문자열
m = "abcde"
print (type(m))
for a in m:
    print (a,end=" ")
print()


#set은 중복이 안된다. 집합연산, 차집합 할때 사용
m = set ([10,20,30,40,50])
print (type(m))
for a in m:
    print(a, end=" ")
print()
 
#map
m={"kim":"김유신", "lee":"이순신" , "hong":"홍길동"}
print(type(m))
for key, value in m.items():
    print (key, value)
print()
 
#리스트안에 튜플을 받을떄 for문 
m=[(1,2),(3,4),(5,6)]
print(type(m))
for a in m :
    print(a[0], a[1])
print()
 
for a,b in m :
    print(a,b)
print()
 
#리스트 반복문으로 만들기 i값을 갖고 리스트 만들어라

m = [ i for i in range(1,101) ]
m =[ i*2 for i in range (1,101)]
#            조건문                 반복문
m =[ "짝수" if i %2==0 else "홀수" for i in range(1,10)] 
print (m) 
 
# 60점 이상이면 합격 아니면 불합격

score = {"kim":89,"lee":65,"jung":96,"park":45,"choi":55,
         "cho":89,"hong":89,"hwang":60,"ki":87,"sung":35} 
for key, value in score.items():
    if value >= 60 :
         print (key, value ,"합격")
    else:
        print (key, value ,"불합격")
 
i = 0
while (i<3):
    print(i) 
    i+=1
print()


i = 0
while True : #while 다음 (조건 언제까지 돌아라)
    i += 1
    if i >10:
        break
    print(i , end=" ")   
print()

# 인덱스를 강제로 만들어주는것

users = {"kim": "김유신", "lee":"이순신" ,"hong":"홍길동"}
for i, user in enumerate(users): #enumerate  키값만 나온다.
     print(i, user ,users[user] )
     print (i, user, users.get( user ))