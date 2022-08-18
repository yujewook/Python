#함수 Funtcion

"""
    C언어
        일반함수 멤버함수(클래스내에 선언한 함수)
        일반함수
        반환형(void) 함수명(매개변수){
            실행문;
            return;
        }
        멤버함수
        public :
            반환형(void) 함수명(매개변수){
            실행문;
            return;
        }
    
    javascript
        일반함수 멤버함수(클래스내에 선언한 함수)
        일반함수
        function 함수명(매개변수){
            실행문;
            return;
        }
        
        멤버함수 
        함수명 = function (매개변수){
            실행문;
            return;
        }
    
    java -> 일반함수 없음, 멤버함수만 존재
        public 반환형 함수명(매개변수){
            실행문;
            return;
        }
    
    python -> 일반함수, 멤버함수 존재
        def 함수명(매개변수){
            실행문
            return
        }
                 java에서 this    
        def 함수명(self,매개변수){
            실행문
            return
        }
    
    
"""

# 반복되는 내용을 묶어서 처리
# 선언 구현 호출해서 사용
# 반드시 호출한 자리도 돌아온다
# 모든 함수는 return이 있다 생략되도 있다 하나만 줄 수 있다.

# print("hello python!!!")
# print("hello python!!!")
# print("hello python!!!")

def hello():                    #선언 함수를 알려주는 것
    print ("hello python!!")    #구현 함수의 정의
    return                      #return 생략
hello()                         #호출 함수를 사용한다.


#매개변수
#파이썬에서 if의 끝을 elif로 끝내도 가능  
# def max(a,b):
#     if a>b:
#         return a 
#     elif b>a :
#         return b
#     elif b==a:
#         return "같다"
# print (max(5,2) )

"""
    오버로드
    함수의 이름은 같아도 매개변수 자료형이 다르거나 개수가 다르거나 순서가 다를 경우 다른 함수로 취급
    
    c는 오버로드가 안됨 -> 매개변수에 초기값을 줄 수 있다.
    int hap(int a , int b){return a+b}
    int hap(double a , double b){return a+b} 이 안된다.
    
    c++ 초기값 o 오버로드 o
    
    java     오버로드o 초기값 x
    public int hap (int a , int b) {return a+b}
    public int hap (double c , double d) {return a+b}
                    
                    
                    이것은 배열이다
    public int hap (int ... args){
        for (int a : args){
        }
    }
    
"""

def hap (a,b):
    return a+b
print ( hap(5,2))
print ( hap(5.5,2.5))

def cha(a,b,c=0):
    return (a-b-c)
print(cha(5,3))

#def gop(a,b=0,c): #초기값을 시작한 부분 부터 뒤에 모든 매개변수에 줘야한다.
def gop(a, b=4, c=3):    
    return(a*b*c)
print(gop(2,5))
print(gop(2))
#하나도 값을 안주면 에러 print(gop())

#VarArgs -> 리스트 
def avg(*args): #튜플로 받는다
    sum = 0
    for a in args:
        sum += a
    print(sum/len(args))
avg(1,2,3) 
avg(1,2,6,4,8,10,9)

#args는 맨 끝으로 설정해야 한다. 
#def (a,*args, *argss) 도 안된다.
def sum(a,b,*args):
    print(a,b,args)
#   a  b  나머지 args-> 튜플로 받는다
sum(10,20,30,40,50)

#키워드 인수
def add(a,b,c=0):
    print(a+b+c)
add(2,5,7)    
add(2,5)   
#함수의 매개변수 이름과 맞춰주면 순서랑 상관 없이 사용한다. 
add(a=5,b=7)
add(b=5,a=9)
add(5,b=2,c=10)
add(10,b=20)
#add(a=10 , 20) 에러
#add(a=10)
#add(10,c=20)b가 값이 없어서 안된다.
#            딕션러리로 넘어온다(MAP)
def insert(a,**params):
    #print(type(params))
    print (a,end=" ")
    for key, value in params.items():
        print(key,value,end=" ")
print()
insert(10, b=10)
insert(20, b=20, c=30)
#insert(b=20, 10 , c=30) 에러가 난다.
insert(b=20,c=30,a=10) #가능하다.


def hap1(a=10,*args,**param):
    print("a :" ,end="")
    #a라는 변수있기때문에 다른 변수줘야한다
    for i in args:
        print ( i , end="")
    for key, value in param.items():
        print(key,value,end=" ") #end는 **param으로 줄려고 쓴다.
    print()
    
hap1(1,"a","b","c")
hap1(20,"a","b",b=20,c=30)
hap1(20, b=20,c=30)
#하나는 a에 들어간다.
hap1(20, 30, 50)
#param
hap1(b=20, c=30, d=50)
#hap1("a","b","c",a=20) a라는 방에 두개가 들어가기 때문에. 에러

print()

#지역변수/ 전역변수
#변수는 자기가 잡힌 영역에만 사용가능
b = 10
b = 100
print("b",b) #인터프리터 마지막 것이 된다.


a =10       # 전역 변수 모든 영역에서 사용가능
def display():
  
    a = 100 #지역변수 -> 할당된 영역에서만 사용
    print("a:",a)
    print("b : ",b) # 전역변수의 b를 사용
    
    
    
display()#지역변수 사용
print(a)

def display1():
  #전역변수를 사용 하고 싶을때 global 하지만 맨처음에 나와야한다.
    global a # a라는 변수가 전체가 바뀐다. -> 전역변수도 값이 변한다.
    print("전역변수 a:",a) #전역변수를 사용한다
    
    a =10
    print("지역변수 a",a)
    

    
    
display1()
print(a)

#지역 변수 보다 편하게 전역 변수로 취한다
#a,b=5,2

def ha(a,b): #()매개변수 인수 인자 argument parameter라고 한다.
    # a=5
    # b=2#지역변수 
    return a+b
def ch(a,b):
    # a=5
    # b=2#지역변수 
    return a-b
def go(a,b):
    # a=5
    # b=2#지역변수 
    return a*b
def mo(a,b):
    # a=5
    # b=2#지역변수 
    return a/b

print(ha(5,2))
print(ch(5,2))
print(go(5,2))
print(mo(5,2))

#내장함수 
#절대값 구하는 것
print(abs(10))
print(abs(-10))

#전부다 참일때 
print(all([1,2,3])) #True
print(all([1,2,0])) #false

#하나라도 참이면 참이다
print(any([0,"",False]))
print(any ([1]) )

#현재 dir다르게 한다.
print(dir())
aaaaa = 10
del aaaaa
print(dir())
# 특정 모듈안에 있는 특정 함수들 
import sys
print (dir(sys))

#나눗셈 몫하고 나머지 같이 준다
print(divmod(7,3))

#eval 
print("1+2")        #연산안해줌
print(eval("1+2"))  #연산해줌

a=10
print(id(a))
print(id(10))

b=a
print(id(b))

print(min("python"))    #가장작은값
print(max("python"))    #가장큰값
print(min([1,5,3,7,9])) #열거형이 들어 갈 수 있다.

print(pow(4,2))         #제곱해주는 함수

m = [10,30,50,40,20]
m.sort()                #sort는 원본을 바꿔 버림 return이 없음
m=sorted(m)             #원본을 바꾸지는 않음 return이 있음 m에다 다시 넣어줘야함

print(m)

print(zip([1,2,3],[4,5,6])) #객체의 주소가 출력됨 1,4 한쌍 2,5 한쌍 3,6 한쌍으로 묶어준다
#리스트로 바꿔서 출려해야함
print(list(zip([1,2,3],[4,5,6]))) #리스트 안에 튜플이 생김

#람다함수
def add1(a,b):
    return a+b
print(add1(3,7))
#    매개변수  retrun
add2 = lambda a,b : a+b #익명함수 -> 이름주기 add2=
print(add2(2,3))
print(( lambda a,b: a+b)(5,20))

#filter (function ,list) 골라낼 조건을 function으로 만들어 준다
#대량의 데이터
def even(a):
    return a%2==0
print(even(20))

print(filter(even,range(10)) ) #객체가 출력

print( list(filter(even,range(10))) ) #객체가 출력->리스트로 바꿔서 출력 true 인 것만 골라냄

print(list(filter(lambda x: x%2==0, range(10) ) ))

#map(function , list)
print (map( lambda x : x*2, range(10) ) ) #객체가 출력
print (list( map( lambda x : x*2, range(10) ) ) ) #각각의 요소에 출력값을 묶어서 나올때


#reduce(function , list)
from functools import reduce
print(reduce (lambda x,y:x+y,range(10)) )

