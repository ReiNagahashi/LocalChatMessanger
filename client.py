import socket
import sys
import os
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/udp_socket_file'

address = '/tmp/udp_client_socket_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

user_input = input('Enter your message: ')
message = user_input.encode('utf-8')

# sys.stdout.flush()

sock.bind(address)

try:
    print('sending{!r}'.format(message))
    sent = sock.sendto(message, server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()
