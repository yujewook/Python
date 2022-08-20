from socket import socket , AF_INET , SOCK_STREAM

clientSock = socket(AF_INET,SOCK_STREAM)
#포트 연결
clientSock.connect(("localhost",3000))#튜플로 준다
print("연결")
clientSock.send("i am a client".encode("utf-8"))
print("메세지를 보냈습니다")
data = clientSock.recv(1024)
print("받은데이터",data.decode("utf-8"))