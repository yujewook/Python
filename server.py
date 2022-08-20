from socket import socket ,AF_INET,SOCK_STREAM

serverSocket=socket (AF_INET , SOCK_STREAM)
                    #포트
serverSocket.bind(("",3000))#튜플로 준다
serverSocket.listen(1)
# 클라이언트 안에 소켓도 있다.
connectionSocket , addr  = serverSocket.accept()
print(str(addr),"님이 접속했습니다.")
data = connectionSocket.recv(1024)
print("받은메세지" , data.decode("utf-8"))
#다시 보내버린다                    인코드를 해야한다
connectionSocket.send("i am a server".encode("utf-8"))
print("메세지를 보냈습니다")