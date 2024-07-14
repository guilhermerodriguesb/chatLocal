import socket
import threading

# Função para receber mensagens do servidor
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"Servidor disse: {message}")
        except:
            print("Erro ao receber mensagem.")
            client.close()
            break

# Função para enviar mensagens ao servidor
def send():
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

# Configuração do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Criando threads para enviar e receber mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
