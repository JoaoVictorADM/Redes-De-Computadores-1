import socket

HOST = '127.0.0.1'  # Endereço IP do Servidor
PORT = 5000         # Porta que o Servidor está escutando

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

tcp.connect(destino)

while True:

    mensagemUsuario = tcp.recv(1024).decode()
    tcp.send(input(mensagemUsuario).encode())

    mensagemSenha = tcp.recv(1024).decode()
    tcp.send(input(mensagemSenha).encode())

    retorno = tcp.recv(1024).decode() 

    if retorno == '1':
        break

    print("\nDados Incorretos!\n")

print("\nLogado com sucesso!\n")

while True:

    mensagemMenu = tcp.recv(1024).decode()
    op = input(mensagemMenu)
    tcp.send(op.encode())

    if op == '3':
        print(tcp.recv(1024).decode())
        break

    if op != '1' and op != '2':
        print(tcp.recv(1024).decode())
        continue

    mensagemIP = tcp.recv(1024).decode()
    tcp.send(input(mensagemIP).encode())

    print(tcp.recv(1024).decode())

tcp.close()
