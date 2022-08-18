# 추상화 abstract
from abc import abstractmethod , ABCMeta
from _ast import Break


class Animal( metaclass=ABCMeta) : #추상클래스
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    @abstractmethod
    def disp(self): #추상 -> 구현을 하지말자 ->어차피 다시 재정의된다 (오버로딩)
        pass # 내용이 없을때 pass
    
#animal = Animal() 추상클래스는 객체를 생성할 수 없다. -> 상속을 받아서 사용 해야한다.

#상속
class Dog(Animal):
    #def __init__(self,): 부모쪽 생성자를 사용한다
        #Animal.__init__(self, name, age) 부모쪽 생성자를 받는 방법 java에서 super
    #상속 받을때에만 생성자를 안만들어도 된다.
    #부모쪽 추상화된 메소드 -> 반드시 구현 해야 한다.
    #오버로딩 되므로 재정의가 된다 -> 자식꺼만 실행
    def disp(self):
        print(self.name,self.age) 

class Cat(Animal):
    def disp(self):
        print(self.name,self.age)
    
dog = Dog("규호",2)
dog.disp()
cat = Cat("중성화규호",2)
cat.disp()


#예외처리
#syntax error 문법이 틀린경우
#semantic error 예외, 실행중에 문제가 생기는 경우
#순서가 중요 예외가 있을때만 예외처리 해야함 
import traceback
try :
    #a = 4/0
    a = 4/"양"
#0으로 나눌때
except ZeroDivisionError :
    print("0으로 나누면 안됩니다.")
#타입
except TypeError :
    print("정수로만 나누세요")
#모든걸 예외처리
except Exception:
    traceback.print_exc()#실행할때 오류를 찾아라
else:#예외가 없을때 
    print("값 :", a)
finally:
    print("프로그램 끝")
    
#사용자 예외정의

#예외 클래스 정의하기 -> 구현은 안해도 된다.
class NumberException (Exception):
    pass
class InputException (Exception):
    pass

#print (a)
# a 입력값이 숫자냐?
# try:
#     a = input("단 : ")
#     if not a.isdigit():
#         #강제 예외 발생시키기
#         raise NumberException()
#     if int(a)<2 or int(a)>9:
#         raise InputException()
#
# except NumberException :
#     print ("숫자만 입력하세요")
# except InputException :
#     print ("2~9까지 입력")
# else :
#     for i in range(1,10):
#         print(a,"*",i,"=", int(a)*i)
# finally:
#     print("프로그램 끝")  


import simple.module.mymodule

#함수 사용하기
simple.module.mymodule.hello()
simple.module.mymodule.bye()

#함수 사용하기
user = simple.module.mymodule.User("홍길동",30)
print(user.getName())
print(user.getAge())

#간단한 방법으로 불러오기1
import simple.module.mymodule as my
#함수 사용하기
my.hello()
my.bye()
#클래스 사용하기
user = my.User("임두혁",20)
print(user.getName())
print(user.getAge())

#간단한 방법으로 불러오기2
from simple.module import mymodule
#함수 사용하기
mymodule.hello()
mymodule.bye()
#클래스 사용하기
user = my.User("김영식",20)
print(user.getName())
print(user.getAge())

#원하는 것만 import 해오기 
from simple.module.mymodule import hello ,bye ,User
#함수 사용하기
hello()
bye()

#클래스 사용하기
user = my.User("김영식",20)
print(user.getName())
print(user.getAge())

# 클래스 별칭으로 해서 임포트 하는 방법            
from simple.module.mymodule import User as U
user = U("양규호",10)
print(user.getName())
print(user.getAge())

#자주 사용하는 모듈
import os
# print(os.__doc__)
# print( help(os) )
# print(help(os.mkdir))
#cmd 창에서 python -m pydoc -p 3333 으로 찾는다


path ="c:/"
for file in os.listdir(path):
    if os.path.isdir(path + file):
        print("폴더 :" ,file)
    else:
        print("파일 :" , file)
    print(os.path.split(path + file))
    print(os.path.join(path + file)) #하나의 파일경로로 합쳐줌
print(os.path.abspath(path))
        
if os.path.exists("test"): 
    os.mkdir("test")        #현재 폴더에 test라는 폴더 만들어주는것
if os.path.exists("test"): 
    os.mkdir("test")        #현재 폴더에 test라는 폴더 삭제해주는것

import sys
print(sys.exc_info())
#sys.exit(0) 프로그램 강제종료
print(sys.modules)          #현재 모듈들어와 있는 모듈 알려줌
print(sys.path)             #현재 모듈들 경로
print(sys.version)          #version
print(sys.version_info)     


import logging, platform
print( platform.platform() )
if platform.platform().startswith( "Window" ) :
    # 윈도우인 경우
    logfile = os.path.join( os. getenv( "HOMEDRIVE" ), os.getenv( "HOMEPATH" ), "test.log" )
else :
    # 윈도우가 아닌 경우
    logfile = os.path.join( os.getenv( "HOME" ), "test.log" )
print( logfile )    
logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s : %(levelname)s : %(message)s",
        filename=logfile,
        filemode="w"
    )
logging.debug( "디버그" )
logging.info( "정보" )
logging.warning( "경고" )
logging.error( "에러" )
logging.critical( "크리티컬" )

#시간 사용하기위한 모듈
from datetime import date,time,datetime,timedelta

now = date.today()
print (now)
print (now.year ,"년" , now.month,"월",now.day,"일")

#백만분의 일초
now = datetime.today()
print(now)
print(now.year ,"년" , now.month,"월",now.day,"일",
      now.hour,":" , now.minute ,":", now.microsecond )


import time 
print(time.time())
print(time.gmtime(time.time()))
t=time.gmtime(time.time())
print(t.tm_hour+9,"시")

#날짜계산 할때 쓰는 것 timedelta
#print(now + 30 ) error -> 
print(now + timedelta(30)) #날짜 연산
print(now.strftime("%y:년 %m:월 %H:시간 %M :분: %S :초 ")) #날짜 문자열로 변환
s = "2022-8-18 13:05:30"
                    # s라고 데이터를 줘야한다. "%Y-%m-%d %H:%M:%S" 형식을 맞춰야 한다.
print(datetime.strptime(s,"%Y-%m-%d %H:%M:%S")) 
t = datetime

#random

import random
#실행 할때 마다 바뀌지 않았으면 좋겠어
#random.seed(0) # 고정된 렌덤값이 나온다.
#for i in range(6):
#    print(int(random.random()*100)) # 1- 100 까지 만든것
#    print(int(random.random()*45)+1) # 1- 45 까지 만든것 6개
                #sample 중복 안되는값 하지만 리스트로 줘야한다.
lotto = random.sample(range(1, 46),6) #중복 안나오게
# print( lotto.sort() ) 
print( sorted( lotto ) )   
random.shuffle( lotto )
print( lotto )
for i in range( 6 ) :
    # print( random.randint( 1, 45 ) )
    print( random.uniform( 1, 45 ) )
    
    
    
    
    
# 파일 입출력
#경로를 다른 컴퓨터에도 되게 할려면 realpath를 사용해야한다.

#연결 쓰기모드
f = open("a.txt","w",encoding="utf-8")   
#파일에 출력
for i in range(1,11):
    f.write(str(i)) #문자열만 출력한다.
f.write("\r\n")#줄바꿔라
print("파일생성 완료")        
f.close() #파일 닫음


# #연결 읽기모드
# f = open("a.text","r",encoding="utf-8")
# while True:
#     data = f.read() #한줄씩
#     if data == "":
#         break
#     print( data , end="")
#
#
# f.close()
#
# f = open("a.text" , "r",encoding="utf-8")
# while True:
#     line = f.readline() # 여러줄
#     if line =="":
#         break
#     print(line)
#
# f.close()
#
# f = open("a.text" , "r",encoding="utf-8")
# for line in f :
#     print(line)
# f.close()

with open("a.txt" ,"r" , encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines :
        print(line)

    
    
#csv
with open("lotto.csv", "w") as f :
    for i in range(10):
        
        #충돌 발생 안하게 하는것
        m = random.sample(range(1,46),6)
        m.sort()
        for i,a in enumerate(m): #데이터 튜플로
            f.write(str(a))
            if(i<len(m)-1):
                f.write(",")#컴마를 꼭 해줘야 csv에서 사용해야한다. 데이터에는 띄어쓰기 주면 안된다.
        f.write("\n")   
        
        
with open("lotto.csv", "r") as f:
    for line in f :
        for a in line.split(",") :
            print(a , end="\t")
        print()


#pickling 객체단위 입출력 -> 자바에서 Dto 같은 것 -> 클래스로 만들어 줘야한다 
class User :
    def __init__ (self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel

import pickle    
#직렬화
hong = User("홍길동",20,"1111-2222")
                    # 바이러리로 저장
with open("user.txt","wb") as f:
    pickle.dump(hong,f)
    
with open("user.txt","rb") as f :
    user = pickle.load(f)
    print(user.getName(), user.getAge(), user.getTel())
    #리스트
users = [
        User("양규호",20,"1111-2222"),
        User("임두혁",20,"2222-2222"),
        User("수원통",25,"1111-3222"),
    ]

with open ("users.txt", "wb") as f:
    pickle.dump(users,f)
    
with open("users.txt","rb") as f :
    us = pickle.load(f)
    print(type(us))
    for u in us : 
        print(u.getName(), u.getAge() , u.getTel() )



#정규표현식 Regular Expression
import re

p = re.compile("[a-z]+")
print(p.match(""))  #none
print(p.match(" ")) #none
print(p.match("a")) #<re.Match object; span=(0, 1), match='a'>
print(p.match("python!!!"))
print(p.match("Python!!!")) #첫문자가 대문자라서 매칭 안됨
print(p.match("pyThon!!!")) #py까지만 찾음
print(p.match(" python!!!"))

print(p.search(""))
print(p.search(" "))
print(p.search("a "))
print(p.search("python!!"))
print(p.search("Python!!")) #대문자를 뺴고 찾음
print(p.search("pyThon!!")) #py만 찾음
print(p.search(" python"))

word = p.search(" python!!")
print(word.start())
print(word.end())
print(word.span())
print(word.group())


s = "life is too short"
print(p.match(s))
print(p.search(s))
print(p.findall(s))#리스트로 return
print(p.finditer(s)) #객체로 만들어 준다.

for word in p.finditer(s):
    print(word.group())
    
p = re.compile("a.b") 
print(p.search("ab")) #none
print(p.search("ac")) #none
print(p.search("acb"))
print(p.search("a0b"))
print(p.search("a&b"))
print(p.search("a\tb"))
print(p.search("a\nb")) #none
print(p.search("acdb")) #none
s="""
    abc acb acccb a
    cb a\nb a0b a\tb
"""

print(p.findall(s))
p = re.compile("a.b",re.DOTALL) #re.S \n도 가능
print(p.findall(s))

p = re.compile("[A-Z]+" , re.IGNORECASE) #re.I 대소문자 상관없이
print(p.findall(s))

s = """python one
pythontwo
python
study python
python
life is too short"""

p = re.compile("^python\s\w+")
print(p.findall(s))
p = re.compile("^\python\s\w+", re.MULTILINE)
print(p.findall(s))