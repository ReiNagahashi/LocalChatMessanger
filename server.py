import os
import socket
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "/tmp/udp_socket_file"
print(f"Server is running on {server_address}")

# Unixドメインソケットのみ、すでに存在するソケットファイルを削除する必要がある
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

while True:
    print('\nwaiting to recieve massege')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        fake = Faker()
        response = fake.text().encode('utf-8')
        sent = sock.sendto(response, address)
        print('sent {} bytes back to {}'.format(sent, address))
