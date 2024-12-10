import socket

#criando o servidor socket om o AF_INET (1pv4) e o SOCK_STREAM (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#pegando o hostname ou seja o ip
host = "127.0.0.1"
#definindo a porta de conexao
port = 1234
#fazendo uma conexao do host com a porta
server_socket.bind((host, port))

#definindo quantos listeners o server vai ouvir
server_socket.listen(3)

while True:
    #Atribuindo o client socket e o endereco, se a conexao acontecer
    client_socket, address = server_socket.accept()
    #printando a mensagem apos o server aceitar a conexao
    print(f"Receive connection from {str(address)}")
    #manda uma mensagem
    message = 'Thank you for connecting to the server' + '\r\n'
    client_socket.send(message.encode('ascii'))
    #fechando o servidor
    client_socket.close()