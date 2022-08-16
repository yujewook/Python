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
def max(a,b):
    if a>b:
        return a 
    elif b>a :
        return b
    elif b==a:
        return "같다"
print (max(5,2) )

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
add(10 , b=20)
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
    print("a : " ,end="")
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


 