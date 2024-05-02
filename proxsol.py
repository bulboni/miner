import socket
import threading
from multiprocessing import Process

def handle_client(client_socket, remote_host, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    
    def forward(src, dst):
        while True:
            try:
                data = src.recv(8192)  # Mengatur ukuran buffer menjadi 4096 byte
                if not data:
                    print("[*] Connection closed by client")
                    break
                dst.send(data)
            except BrokenPipeError:
                print("[*] Broken pipe error occurred")
                break
    
    client_thread = threading.Thread(target=forward, args=(client_socket, remote_socket))
    remote_thread = threading.Thread(target=forward, args=(remote_socket, client_socket))
    
    client_thread.start()
    remote_thread.start()
    
    # Wait for the threads to finish
    client_thread.join()
    remote_thread.join()
    
    # Close sockets after threads are finished
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
