import socket
import struct
import random
import numpy as np
import threading
from concurrent.futures import ThreadPoolExecutor

# ----------- CLIENT -----------
def generate_matrix(rows, cols):
    return np.random.randint(0, 100, (rows, cols)).tolist()

def client():
    HOST = '127.0.0.1'
    PORT = 65432
    
    # Генерація розмірів матриць
    N = random.randint(1001, 1100)
    M = random.randint(1001, 1100)
    L = random.randint(1001, 1100)
    
    print(f"Matrix A: {N}x{M}, Matrix B: {M}x{L}")
    
    matrix_a = generate_matrix(N, M)
    matrix_b = generate_matrix(M, L)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Надсилаємо розміри матриць
        s.sendall(struct.pack('iii', N, M, L))
        
        # Надсилаємо матриці
        for row in matrix_a:
            s.sendall(struct.pack(f'{M}i', *row))
        for row in matrix_b:
            s.sendall(struct.pack(f'{L}i', *row))
        
        # Отримання результату
        result = []
        for _ in range(N):
            row_data = s.recv(4 * L)
            row = struct.unpack(f'{L}i', row_data)
            result.append(row)
        
        print("Result received:")
        for row in result:
            print(row)

# ----------- SERVER -----------
def multiply_matrices(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b).tolist()

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        # Отримання розмірів матриць
        data = conn.recv(12)
        N, M, L = struct.unpack('iii', data)
        
        matrix_a = []
        matrix_b = []
        
        for _ in range(N):
            row_data = conn.recv(4 * M)
            row = struct.unpack(f'{M}i', row_data)
            matrix_a.append(row)
        
        for _ in range(M):
            row_data = conn.recv(4 * L)
            row = struct.unpack(f'{L}i', row_data)
            matrix_b.append(row)
        
        # Обчислення
        result = multiply_matrices(matrix_a, matrix_b)
        
        # Відправлення результатів
        for row in result:
            conn.sendall(struct.pack(f'{L}i', *row))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def server():
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is listening...")
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            while True:
                conn, addr = s.accept()
                executor.submit(handle_client, conn, addr)

# ----------- MAIN -----------
if __name__ == '__main__':
    choice = input("Run as (server/client): ").strip().lower()
    if choice == 'server':
        server()
    elif choice == 'client':
        client()
    else:
        print("Invalid choice")
