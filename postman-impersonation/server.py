import os
import socket
import sys
import re

'''
# Visit https://edstem.org/au/courses/8961/lessons/26522/slides/196175 to get
PERSONAL_ID = ''
PERSONAL_SECRET = ''
# Just a comment

def main():
    # TODO
    pass


if __name__ == '__main__':
    main()
'''

def analyze_config(conf):

    config = [-1,-1,"","",""]

    if os.path.exists(conf):
        with open(conf) as f:
            lines = f.readlines()
            lines = list(map(lambda x:x.strip(),lines))
    else:
        exit(1)

    for line in lines:

        if line.startswith("server_port"):
            config[0] = int(line.split("=",1)[1])
            if config[0] < 1024:
                exit(2)
        if line.startswith("client_port"):
            config[1] = int(line.split("=",1)[1])
            if config[1] < 1024:
                exit(2)
        if line.startswith("inbox_path"):
            config[2] = line.split("=",1)[1]
        if line.startswith("send_path"):
            config[3] = line.split("=",1)[1]
        if line.startswith("spy_path"):
            config[4] = line.split("=",1)[1]

    if config[0] == -1: exit(2)
    if config[0] == config[1]: exit(2)
    if config[2] == "": exit(2)
    #if config[2] == config[3] or config[2] == config[4]:exit(2)

    
    '''
    #print(send_path)
    #print(os.path.expanduser(send_path))
    # Check if folder exist
    #print(os.path.exists(send_path))
    if os.path.exists(os.path.expanduser(send_path)) is True or os.path.exists(send_path) is True:
        #print("Victoria")
        # Check if folder has read permisions
        if (os.access(os.path.expanduser(send_path),os.R_OK)) is True:
            send_path = os.path.expanduser(send_path)
        else:
            exit(2)
    else:
        exit(2)
    '''
    return config



def enviar(msg):
    msg = msg+"\r\n"
    print("S:", msg, flush=True, end='')
    conn.send(msg.encode())

def recibir():
    msg =conn.recv(1024).decode()
    msg_out = re.sub(r'\r\n', '', msg)
    print("C:",msg,flush=True, end='')
    return msg_out

def ignition():
    enviar("220 Service ready")
    recibir()
    enviar("250 127.0.0.1")
    enviar("250 AUTH CRAM-MD5")

def server_program(params):
    # get the hostname
    host = socket.gethostname()
    port = params[0]  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    global conn
    conn, address = server_socket.accept()  # accept new connection

    # Initialize the server
    #ignition()
    enviar("220 Service ready")
    #recibir()
    while True:
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = recibir()
        if not data:
            # if data is not received break
            break
        elif data == "QUIT":
            enviar("221 Service closing transmission channel")
            break
        else:
            enviar("501 Syntax error in parameters or arguments")


    conn.close()  # close the connection
    print("Byeeeeee")


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 2:exit(1)
    params = analyze_config(sys.argv[1])
    while True:
        server_program(params)