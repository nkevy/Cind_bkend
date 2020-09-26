import logging
import socket 

BUFFER_SIZE = 1

# a server listenting to a port
# takes json input from port
class CindServer():
    def __init__(self,host:str,port:int):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def trigger(self,msg:str):
        pass

    def start(self):
        with (self.soc) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(((self.host,self.port))
            s.listen()
            while True:
                conn, addr = s.accept()
                msgdata = []
                while True:
                    buff = conn.recv(BUFFER_SIZE)
                    buff.decode()
                    if buff == ";":
                        conn.close()
                        trigger(msgdata)
                    elif buff:
                        msgdata.append(buff)
                    else:
                        break


## todo: switch to bottlepy
if __name__ == '__main__':
    csr = CindServer('127.0.0.1',8000)
    csr.start()
