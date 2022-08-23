import cx_Oracle
import os
location ="C:\oraclexe\instantclient_21_6"
os.environ["PATH"] =location +";"+os.environ["PATH"]
#오라클 하고 연결
dsn = cx_Oracle.makedsn("localhost","1521","xe")
con = cx_Oracle.connect("bit","bit",dsn)
cursor = con.cursor()

#데이터 인서트 하기
# sql = "insert into dbtest values( :1 , :2 ,:3 , :4 , sysdate)"
# user = ("ADF","999","양규호","999-9999")
# result = cursor.execute(sql,user)
# if result ==0 :
#     print("가입실패")
# else :
#     print("가입성공")

#select 
sql = "select * from dbtest"
cursor.execute(sql) #커서가 데이터를 갖고 있는다
# for row in cursor :
#     #print(row) 튜플로 갖고 온다
#     for column in row :
#         print(column, end="\t")
#     print()

rows = cursor.fetchall() #여러줄 꺼내기 위와 결과는 똑같지만 가공이 가능하다.
print(rows[0]) # 튜플로 갖고 온다 
print(rows[1])
for row in rows :
    for column in row :
        print(column , end ="\t")
    print()

#회원수 찍기
sql = "select count(*) from dbtest"
cursor.execute(sql)
count = cursor.fetchall()[0]        #데이터가 튜플로 넘어온다. 데이터를 꺼내기위해 [0]
print("회원수 :" , count)

#한줄만 갖고오는 경우
sql = "select * from dbtest where id=:idx"
cursor.execute(sql, idx="aaa" ) # aaa 를 튜플로 줘야한다.
user = cursor.fetchone() #하나만 뽑아오기
print(user)







#delete
id = "ADF"
passwd = "999"
#비밀번호 확인
sql = "select * from dbtest where id=:idx"
cursor.execute(sql, idx=id)
user = cursor.fetchone()
if user == None :
    print("아이디가 없습니다")
else:
    if passwd == user[1]:
        sql =  "delete * from dbtest where id=:idx"
        result = cursor.execute(sql , idx = id)
        if result == 0 :
            print("탈퇴 실패")
        else: 
            print("탈퇴 성공:" ,id,"를 삭제했습니다.")
    else:
        print("비밀번호가 틀림")









con.commit()
con.close()