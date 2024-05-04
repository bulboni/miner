import socket
from multiprocessing import Process

def handle_client(client_socket, remote_host, remote_port):
    try:
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((remote_host, remote_port))
        
        while True:
            data = client_socket.recv(8192)
            if not data:
                break
            remote_socket.send(data)
            
            data = remote_socket.recv(8192)
            if not data:
                break
            client_socket.send(data)
    except Exception as e:
        print(f"[*] Error: {e}")
    finally:
        client_socket.close()
        remote_socket.close()

def main():
    local_host = "0.0.0.0"  # Bind to all available interfaces
    local_port = 4052  # Change to desired local port
    remote_host = "rx.unmineable.com"  # Change to target server address
    remote_port = 3333  # Change to target server port
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(100)
    
    print(f"[*] Listening on {local_host}:{local_port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_process = Process(target=handle_client, args=(client_socket, remote_host, remote_port))
        client_process.start()

if __name__ == "__main__":
    main()
