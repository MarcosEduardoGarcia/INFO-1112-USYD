import os
import socket
import sys

'''
# Visit https://edstem.org/au/courses/8961/lessons/26522/slides/196175 to get
PERSONAL_ID = 'EC27EF'
PERSONAL_SECRET = '54a1c6ce84f1b6e7eec12f5dc5b79481'


def main():
    # TODO
    pass


if __name__ == '__main__':
    main()
'''


# Parameters

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

    '''
    config[0] = server_port 
    config[1] = client_port
    config[2] = inbox_path
    config[3] = send_path
    config[4] = spy_path
    '''

    if config[0] == -1: exit(2)
    if config[0] == config[1]: exit(2)
    if config[3] == "": exit(2)
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
    print("C:", msg, flush=True, end='')
    client_socket.send(msg.encode())

#Aqui
def recibir():
    print("S:", client_socket.recv(1024).decode(),flush=True, end='')

def ignition():
    recibir()
    enviar("EHLO 127.0.0.1")
    recibir()
    recibir()

def client_program(params):
    print("Entro aqui", flush=True)
    global client_socket
    host = socket.gethostname() # as both code is running on same pc
    port = params[0]  # socket server port number
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    ignition()

    message = input("C: ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('S: ' + data)  # show in terminal

        message = input("C: ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 2:exit(1)
    params = analyze_config(sys.argv[1])
    client_program(params)