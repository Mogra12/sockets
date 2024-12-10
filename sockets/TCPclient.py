import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 1234

client_socket.connect((host,port))

#definindo o maximo de dados que podem ser enviados pela conexao
message = client_socket.recv(1024)

client_socket.close()

# decodando a mensagem que veio em ascii
print(message.decode('ascii'))
