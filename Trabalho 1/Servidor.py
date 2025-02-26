import socket
import ipaddress

HOST = '127.0.0.1'  # Endereço IP do Servidor
PORT = 5000         # Porta que o Servidor está escutando

# Credenciais de login
USUARIO = 'admin'
SENHA = 'admin'

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

# Colocando um endereço IP e uma porta no Socket
tcp.bind(origem)

# Colocando o Socket em modo de escuta
tcp.listen()

print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

# Aceitando uma nova conexão
conexao, cliente = tcp.accept()
print('\nConexão realizada por:', cliente)


def calcularIps(endereco):
    try:
        # Cria a rede com base no IP/máscara informado
        rede = ipaddress.ip_network(endereco, strict=False)
        
        num_uteis = rede.num_addresses   
        primeiro_util = rede.network_address
        ultimo_util = rede.broadcast_address
        
        # Calcula o número de endereços úteis (ignora rede e broadcast para IPv4)
        if isinstance(rede, ipaddress.IPv4Network):
            num_uteis = num_uteis - 2
            primeiro_util = primeiro_util + 1
            ultimo_util = ultimo_util - 1

        return {
            "enderecos_uteis": num_uteis,
            "primeiro_util": str(primeiro_util),
            "ultimo_util": str(ultimo_util),
        }
        
    except ValueError:
        return "Erro: Endereço IP ou máscara inválidos."


while True:

    conexao.send("Usuário: ".encode())
    usuario = conexao.recv(1024).decode()

    conexao.send("Senha: ".encode())
    senha = conexao.recv(1024).decode()

    if usuario == USUARIO and senha == SENHA:
        conexao.send("1".encode())
        break

    conexao.send("0".encode())

while True:
    # Menu de opções
    menu = ("Menu de Escolha:\n" + \
           "1 - Calcular IPv4\n" + \
           "2 - Calcular IPv6\n" + \
           "3 - Sair\n" + \
           "Escolha uma opção: ").encode()

    conexao.send(menu)
    opcao = conexao.recv(1024).decode()

    if opcao == '1' or opcao == '2':
        conexao.send("\nDigite o endereço IP e a máscara (ex: 192.168.0.1/24): ".encode())
        endereco = conexao.recv(1024).decode()

        resultado = calcularIps(endereco)
        
        if isinstance(resultado, dict):
            resposta = f"\nQuantidade de endereços úteis: {resultado['enderecos_uteis']}\n" + \
                       f"Primeiro endereço útil: {resultado['primeiro_util']}\n" + \
                       f"Último endereço útil: {resultado['ultimo_util']}\n"
        else:
            resposta = resultado
        
        conexao.send(resposta.encode())
    
    else:

        if opcao == '3':
            conexao.send("\nSaindo\n".encode())
            break

        conexao.send("\nOpção inválida\n".encode())

    

print('Finalizando conexão do cliente', cliente)
conexao.close()


