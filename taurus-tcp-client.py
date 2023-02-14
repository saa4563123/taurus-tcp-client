import socket
from threading import Thread

version = '1.0'

# 서버 아이피 & 포트
HOST = 'local.nura.kr'
PORT = 9009

def setup():
    print('===========================================================')
    print('[TAURUS] 서버 클라이언트 Version - %s' % version)
    print('[TAURUS] 서버 호스트 도메인 - %s' % HOST)
    print('[TAURUS] 서버 호스트 포트 - %s' % PORT)
    print('[TAURUS] Create by - Lee SeungHwan. KNUT TAURUS 2023')
    print('===========================================================')

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass

def ipset():
    print('===========================================================')
    print('[TAURUS] 접속할 서버 아이피를 입력해주세요.')
    print('[TAURUS] Create by - Lee SeungHwan. KNUT TAURUS 2023')
    print('===========================================================')
    subHOST = str(input())

    return subHOST

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            sock.send(msg.encode())

            if msg == '/quit':
                break

HOST = ipset()
setup()
runChat()
