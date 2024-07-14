import socket
import threading

# Função para lidar com conexões de clientes
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Cliente disse: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

# Função para enviar a mensagem para todos os clientes
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Função para remover a conexão do cliente
def remove(connection):
    if connection in clients:
        clients.remove(connection)

# Configuração do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(100)

clients = []

print("Servidor está escutando...")

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    print(f"Conexão estabelecida com {client_address}")

    threading.Thread(target=handle_client, args=(client_socket,)).start()
