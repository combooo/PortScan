
# Author: Stanislav Kvitko

import socket # socket module provides low-level networking interface operations
from tqdm import tqdm # module that adds a progress bar to loops

HOST = 'localhost' # target machine
PORT_COUNT = 2 ** 16 # total number of ports to scan

def is_port_open(port): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #Creates a TCP socket
        return not sock.connect_ex((HOST, port)) 
        # tries to connect to the specified port on the target host.connect_ex() 
        # returns 0 if successful, meaning the port is open, and a non-zero value otherwise.
    
for port in tqdm(range(1, PORT_COUNT), total=PORT_COUNT-1, desc=f'Scanning {HOST}'):
    if is_port_open(port):
        print(f'Port {port} is opened')