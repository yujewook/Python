a = 10
print(a)
# 영역 표시가 안되고 들여쓰기가 필요하다.
print("hello python") 

import keyword
print (keyword.kwlist)
#  길이 구하기
print (len(keyword.kwlist))
#타입 주는것
print ( type(10) )
print ( type(10.5) )
print ( type("ABC") )
print ( type('ABC') )
#복소수
print( type(10+10j) )
#float
print( type(5/2) ) #2.5

#컴마 떄문에 안됨 
#a = 10, b =20
# 이건 가능
a,b = 10, 20
print(a,b)
#교환  이것이 튜플덕분임
a ,b = b,a
#여러개 출력 
print(a,b)
#지우는 것
del a,b 
#print(a,b)

print("우리 나라 \
역슬레시로 한줄(코딩내에서) 뛰는것 에러 안나오게 만들기 ")

a="""
  대량의 문자열 만들게 하기
  문자열 인식하게 
  하는 방법
"""

print(a)

#형변환
print ( type( int(10.5) ))
print ( type( float(10) ))
#print ( type( int(에러임) ))
print(type(int("123") ))
print(type(str(123) ))

#2진수 변환 
print(int("1111" , 2 ) )
#16진수
print(int("ff" , 16 ) )
#8진수
print(oct(20))
#16진수
print(hex(20))
#2진수
print(hex(20))
#띄어쓰기
print("ABC","DEF")
print("ABC"+"DEF")
#오버라이드이 안되기 때문이다.
#print("ABC" + 10)
#{0}의 자리 "abc" {1}의 자리 "def"
print("{0}{1}".format("abc","def"))
#자리 바꿈
print("{1}{0}".format("abc","def"))

print("{0:10s}{0:10s}".format("abc","def"))

#소수점 자리 설정 0:.2 두번째 숫자가중요 소수점 2번째자리 표시 
print("{0:.2f}".format(123.4567))

#연산자
a=10
print(a**2)
print(5/2)
#자동형 변환으로 인해서 int / float -> 더큰 것 float을 따라간다.
print(5.0/2)
print(5//2) #2
print(5.0//2) #2.0
#and 둘이 참일때만 참 / / or 하나만 참이여도 참
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)

print(False or False)
print(False or True)
print(True or False)
print(True or True)
#"Hello" 안에 H존재 유주 확인
print("H"in"Hello") #True
print("f"in"Hello") #False

a="hello"
b="hello"
print(a is b)
print(a == b)
a += "python!"
b += "python!"

#is는 주소 비교
print(a is b)
# == 같은거 인지 비교 
print(a == b)

#산술 대입연산자
a=10
a+=10; print(a)
a-=10; print(a)
a*=10; print(a)
a/=10; print(a)
a%=10; print(a)

