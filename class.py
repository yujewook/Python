#클래스
#캡슐화 상속 다형성



#private __ 하면 프라이빗
__a = 10 #일반변수
def getA():
    return __a
print(getA())


class P :
    __a = 10  # 프라이빗
    b = 20
    def getA(self): #무조건 self를 사용해야 한다.
        return  self.__a #self를 꼭 명시해야한다.
    def getB(self):
        return self.b
    
    #1.데이터 대신 넣어주는 함수
    def setA(self,a):
        self.__a = a
        
        
        
p = P() #객체생성
print(p.b)
#print(p.__a) 프라이빗이라서 접근 불가 -> 메소드로 접근가능

#프라이빗을 접근하기 위해 함수를 사용
print(p.getA())
#프라이빗 변수 접근하는 방법2 private으로 완벽한 캡슐화는 불가능하다. 밑줄한칸 _클래스명__변수명
print(p._P__a) 

#프라이빗 변수 바꾸는 방법
p.__a = 100 # 안된다
#1. 함수를 만들어 준다음에
p.setA(100)
print(p.getA())



#캡술화
class Person:
    __name=""
    __age=0
    __height=0.0
    
    def setName(self,name):
        #조건문 만들기
        if len(name)>10 or name =="":
            print("이름을 바르게 입력하세요")
        else:    
            self.__name = name
    def setAge(self,age):
        if age < 1 or age > 140:
            print("나이를 바르게 넣어줘라") 
        else:
            self.__age = age
    def setHeight(self,height):
        if height < 40 or height>200:
            print("키를 바르게 입력하세요")
        else:    
            self.__height = height
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getHeight(self):
        return self.__height

#비정상적 데이터
kim = Person()
kim.setName("홍길리릴리ㅣㄹ동")
kim.setAge(150)
kim.setHeight(350)

print("이름 : "  ,kim.getName() )
print("나이 : "  ,kim.getAge() )
print("키 : "  ,kim.getHeight() )

#정상적 데이터
lee = Person()
lee.setName("이순신")
lee.setAge(25)
lee.setHeight(180)

print("이름 : "  ,lee.getName() )
print("나이 : "  ,lee.getAge() )
print("키 : "  ,lee.getHeight() )



#생성자 생성자 없을시 변수를 직접 만들어야 한다 -> 생성자가 변수를 만들어준다 /자바는 다 만들어야한다.

class User:
    def __init__(self,name="",age=0,tel=""):
        self.name = name
        self.age = age 
        self.tel = tel
        print("생성자")
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel
    
    # def __del__(self):
    #     print("소멸자")
        
        
#초기값이 있어서 파라미터를 다 맞출 필요는 없다
#객체마다 생성자 , 객체마다 소멸자 -> 스택영역이라 
lee = User()
kim = User("광명 피바라기 영식햄")
hong = User( age=20,tel="1111-2222" )

print("이름 :" , hong.getName() )
print("나이 :" , hong.getAge() )
print("전화 :" , hong.getTel() )


#static -> 자바에서 모든 객체가 공유 -> 메모리 영역중 static 영역에 할당 -> 메모리는 하나만 할당 ->먼저할당 한다
#but 파이썬에는 static을 명시 할 필요가 없다
class Member :
      #생성자와 그냥 변수와 차이점이 있다
    name = "수원통김영식"        # 멤버변수 클래스변수 static변수
    count = 0 #static 
    def __init__(self, age=0, cnt=0 ): #지역변수 -> 객체생성을 해야한다.
        self.age = age
        self.cnt = cnt
        Member.count += 1
        self.cnt += 1;
    def getcnt(self):
        return self.cnt
    def getCount(self):
        return Member.count

#static 변수 객체생성을 안해도 된다.         
print( Member.name ) # static은 객체생성 안해도 사용할 수 있다
# print( Member.age )
#Member에 변수를 바꾸면 한번에 다 바뀜
Member.name = "이순신"

lee = Member()
print( lee.name )
print( lee.getCount )
print( lee.getcnt() )

hong = Member()



class Customer :
    name = "홍길동"
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name    
    
    #static 메소드 만들기
    #@staticmethod static어노테이션으로 사용한다. 또는 disp함수명()
    def dispName():
        return Customer.name
    # static 메소드 만들기
    dispName = staticmethod(dispName)
    
    
kim = Customer()
kim.setName("임두혁")
print(kim.getName())            #임두혁 지역변수 사용
print(Customer.dispName() )     #홍길동 static 변수 사용

print()
class Car :
    cc="2000cc"
    @staticmethod
    def getStatic():
        return Car() #Car라는 객체가 생긴다
    @classmethod
    def getClass(cls):
        return cls() #cls라는 객체 만든다 -> 해당클래스가 넘어 온다. 한마디로 cls 클래스를 매개변수로 전달
    def getCc(self):
        return self.ccs
class Truck(Car):
    cc="3000cc"
    
a = Car.getStatic() #car 클래스 객체
b = Car.getClass()  #car 클래스 객체이다 Car.로 객채를 만들었기 때문 -> Car클래스로 만들어진다.
print(a.getCc())    #2000cc
print(b.getCc())    #2000cc   

c = Truck.getStatic() #car 클래스 객체
d = Truck.getClass()  #클래스 메소드로 객체를 만들어서 -> truck클래스로 객체를 만들어진다 <1.번과비교>
print(c.getCc()) #2000cc
print(d.getCc()) #3000cc

#상속
#코드재활용
# class Animal:
#     def __init__(self,name=""):
#         self.name = name
#         print("Animal 생성자")
#     def getName(self):
#         return self.name
#
# class Cat(Animal) :
#     # def __init__(self,name=""):
#     #     Animal.__init__(self,name) 이 부분은 없어도 알아서 잘 생성된다.
#     None
# class Dog(Animal) :
#     def __init__(self,name=""):
#         Animal.__init__(self,name)
#         print("cat 생성자")
#
# cat = Cat("양양양야")
# print(cat.getName())
# dog = Dog("규호규호")
# print(dog.getName())
        

#다중 상속        
class Animal:
    def __init__(self,name):
        self.name= name       
        
    def getName(self):
        return self.name
    
class Pet:
    def __init__(self,kind):
        self.kind=kind
    
    def getKind(self):
        return self.kind

class Dog(Animal,Pet):
    def __init__(self,name,kind,color):
        Animal.__init__(self, name)
        Pet.__init__(self,kind)
        self.color=color
    
    def getColor(self):
        return self.color
    #오버라이드
    def getKind(self):
        return "품종 :" + self.kind
        
        
dog =Dog("규호규호","규호종","핑크색")
print (dog.getName())
print (dog.getKind())
print (dog.getColor())



#다형성 중요도가 떨어짐
class Bread :
    def __init__(self,name=""):
        self.name = name
    def getName(self):
        return "Bread : " + self.name 
    #다형성 그나마 제대로 할려면
    @classmethod #클래스가 들어가는 공간 cls / msg-> 넘어간 단어로 만들어준다
    def getClass(cls ,msg):
        return cls(msg)
    
class Toast(Bread):
    def getName(self):
        return "Toast : " +self.name
class Cake(Bread):
    def getName(self):
        return "Cake : " +self.name
class RedBeanBread(Bread):
    def getName(self):
        return "RedBeanBread : " +self.name
#자바    
#Bread bread = new Cake(); getName을 하면 cake의 이름이 나온다
#Bread bread = new Toast();
#Bread bread = new RedBeanBread();
toast = Toast("토스트")
print (toast.getName())
cake =Cake("케이크")
print (cake.getName())
redbeanbread = RedBeanBread("팥빵")
print (redbeanbread.getName())

print()
#객체를 브래드로 만든다
bread = Bread()
toast = Toast.getClass("ㅌ토스트")#msg 파라메터 설정후 사용가능
print(toast.getName()) #토스트의 객체가 만들어짐
cake = Cake.getClass("@케이크")
print(cake.getName()) 
redbeanbread  = RedBeanBread.getClass("v팥")#
print(redbeanbread.getName()) 



#property 어노테이션으로도 사용 가능 @
class Gamer :
    __name = ""
    __age = 0
    def setName(self,name) :
        self.__name = name
    def setAge(self, age) :
        self.__age = age
    def getName(self) :
        return self.__name
    def getAge(self) :
        return self.__age
    name = property(getName,setName)
    age =property(getAge,setAge)
       
gamer = Gamer()
gamer.setName("양규호")
gamer.setAge("10")
print(gamer.getName())
print(gamer.getAge())

#print (grammer.__name)
gamer.name ="이순신"
gamer.age= 40
print(gamer.name)
print(gamer.age)


