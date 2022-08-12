#열거형 나열형
from audioop import reverse


name = "홍길동"
age= 20
print( "name:" + name +"age : "+ str(age))
#파이썬은 ,를 많이 사용한다.
print("="*100)
print("name: %s age: %d" %(name, age))
print("name: {0} age: {1}".format(name, age))

#함수의 매개변수를 지정할 수 있다.
print("name: {name} age: {age}".format(name="홍길동", age=30) )

a = "hello"
print ("{0:10}".format(a))
#왼쪽 정렬
print ("{0:<10}".format(a))
#오른쪽 정렬
print ("{0:>10}".format(a))
#가운데 정렬
print ("{0:^10}".format(a))
print("{0:-^10}".format(a))
#빈칸을 x 로 채워라
print("{0:x^10}".format(a))

#문자열 관련함수
a = "hello Python"
print(a.lower() )
print(a.upper() )
print(a.title() )
print(a.swapcase() )
#전부다 소문자냐?
print(a.islower() )
#전부다 대문자냐?
print(a.isupper() )
#여기안에 특정문자열 몇개있나?
print(a.count("h") )
print(a.find("d") )
#인덱스는 못찾으면 예외가 나온다
#print(a.index("d") )
#a에게 컴마 넣기
print(",".join(a) )
b = "     b    b      b     "
#왼쪽띄어쓰기를 지워라
print(b.lstrip(" "))
#오른쪽띄어쓰기를 지워라
print(b.rstrip(" "))
#바꾸기
print(a.replace("o","a" ) )
#나누기 
print(a.split())
#특정문자를 주면 그문자를 기준으로 짜른다
print(a.split("o"))


#앞에 띄어쓰기는 전부 false
c="aaddfvc123"
#전부다 알파벳/숫자냐?
print(c.isalnum())
#전부다 알파벳이냐
print(c.isalpha())
#
print(c.isidentifier())#식별자
print(c.isdigit())#숫자

print("="*100)
print("0abc".isidentifier())
print(" 0abc".isidentifier())
print("_abc".isidentifier())
print("a+bc".isidentifier())
print("a$b".isidentifier())
print("가나다".isidentifier())


#문자열 난 ㅇ인덱싱
# 0 1 2 3 4 5 6 7 8 9 10 11 12 
#|h|e|l|l|o| |p|y|t|h| o| n|\0| #파이썬은 리스트
#                           {12}문자열은 끝을 알려주기 때문에 사용된다. 

print(a[0])
print(a[11])

#슬라이싱 가로로 자르는것 
print(a[:])#전체출력
print(a[3:])#3번쨰 부터
print(a[:11])#처음부터 10번쨰 까지 끝인덱스는 -1
print(a[2:10])
print(a[:-1])
print(a[:-2])

#리스트
print()
fruits = ["banana","apple", "orange", "pear", "grape"]
print("banana" in fruits )
print("melon" in fruits )

print(fruits[3])
fruits[3]="melon"
print(fruits)
#전체 다 찍기
print(fruits[:])
print(fruits[2:])
print(fruits[:3]) #end index는 -1 
print(fruits[:-2])
print(fruits[1][3])

print(len(fruits))#데이터 개수
print(max(fruits))#문자열 첫번째 자리꺼 큰거가 나옴
fruits.append("pear")#append (리스트 뒤에 추가)는 return 값이 없어서 print 하면 안됨
print(fruits)
fruits.insert(2,"watermelon")
print(fruits)
#fruits.extend("apple")
print(fruits)
print(fruits.count("apple"))#apple가 몇개인가?

print(fruits.pop())#맨끝에것 꺼내라
fruits.remove("apple")
print(fruits)
#내림차순
fruits.sort(reverse=True)#원본이 바뀜
print(fruits)

shop =["라면", "햇반" , "김치"]
shoplist = [fruits,shop]
print(shoplist) 

print(shoplist[1][1])
print(shoplist[1][1][1])
#슬라이싱
print(shoplist[1][:2])
shoplist[1].append("달걀")
print(shoplist)
            #앞에서 여러개를 뽑아내면 뒤에도 행을 또 뽑아낸다 앞에 나오고 뒤에를 연산한다
print(shoplist[:2][:2])
print(shoplist[0][:len(shoplist[0])])

#튜플
print()
#각각의 데이터를 받겠다
a,b =(10,20)
print(a,b)
# 데이터 하나에 전부 넣는다.
zoo = ("dog","cat","monkey","snake")
#하나씩 꺼내는 법 변수만큼 줘야한다.
a,b,c,d = zoo
print(a)
#인덱싱
print( zoo[0] )
#슬라이싱
print( zoo[0:2] )
print(len(zoo))

#list와 튜플은 서로 교환이 가능하다.
z = list(zoo)
z.sort()
z.append("tiger")
print(z)
print(type(z))

t = tuple(z)
max(t)
print(t)
print(t)
print(type(t))

def clac(a,b):
    return(a+b, a-b, a*b,a/b)
values = clac(5,2)
print(values[0])
a,b,c,d = clac(5,2) 
print(a,b,c,d)

#Set 함수 
        #리스트로 줘야한다.
country =set(["korea","japan","china","russia","taiwan"])
print(type(country))
country.add("korea")#안들어감
print(country)
nation = country.copy()
nation.add("USA")#하나만 줄 수 있다.
nation.add("Uk")#하나만 줄 수 있다.
print(nation)
print(nation - country)#차집합 중복값 제거
print(nation | country)#합집합
print(nation & country)#교집합
print()
print(nation.difference(country) )
print(nation.union(country) )
print(nation.intersection(country) )

nation.pop()#아무거나 꺼내서 지운다.

print(nation.symmetric_difference(country)) #교집합이 아닌값

print("korea" in nation)
print("korea" not in nation)