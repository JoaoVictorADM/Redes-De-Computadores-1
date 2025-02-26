# Aplicação Cliente-Servidor para Cálculo de Endereços IP

Esta é uma pequena aplicação cliente-servidor que permite calcular informações sobre endereços IP, como a quantidade de endereços úteis, o primeiro e o último endereço útil em uma rede. O servidor processa as requisições do cliente, que envia comandos e recebe os resultados.

## Descrição dos Arquivos

### `Servidor.py`

O servidor é responsável por:
1. Escutar conexões TCP na porta `5000`.
2. Autenticar o cliente com um usuário e senha (`admin/admin`).
3. Oferecer um menu de opções para o cliente:
   - Calcular informações sobre endereços IPv4.
   - Calcular informações sobre endereços IPv6.
   - Sair da aplicação.
4. Processar a entrada do cliente (endereço IP e máscara) e retornar informações sobre a rede, como:
   - Número de endereços úteis.
   - Primeiro endereço útil.
   - Último endereço útil.

### `Cliente.py`

O cliente é responsável por:
1. Conectar-se ao servidor no endereço local `127.0.0.1` e porta `5000`.
2. Enviar as credenciais de login (usuário e senha) para autenticação.
3. Interagir com o servidor por meio de um menu de opções:
   - Solicitar cálculos de endereços IPv4 ou IPv6.
   - Encerrar a conexão.
4. Exibir os resultados recebidos do servidor.

## Como Funciona a Aplicação

1. **Autenticação**:
   - O cliente se conecta ao servidor e envia um nome de usuário e senha.
   - O servidor verifica as credenciais e permite o acesso apenas se forem corretas.

2. **Menu de Opções**:
   - Após a autenticação, o servidor envia um menu de opções para o cliente.
   - O cliente escolhe uma opção (calcular IPv4, calcular IPv6 ou sair).

3. **Cálculo de Endereços IP**:
   - Se o cliente escolher calcular IPv4 ou IPv6, o servidor solicita o endereço IP e a máscara.
   - O servidor calcula e retorna:
     - Número de endereços úteis.
     - Primeiro endereço útil.
     - Último endereço útil.

4. **Encerramento**:
   - O cliente pode escolher a opção de sair, encerrando a conexão com o servidor.
