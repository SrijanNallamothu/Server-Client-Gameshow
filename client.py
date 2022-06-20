
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IPaddress = str(sys.argv[1])

Port = int(sys.argv[2])

server.connect((IPaddress, Port))

while True:

    sockets = [sys.stdin, server] # from which inputs come

    readsockets,writesocket, errorsocket = select.select(sockets,[],[]) # used to read messages from sockets.

    for s in readsockets:

        if s == server:
            text = s.recv(2048)
            print text

	    if text == "BYE!!" :
			server.close()
                        sys.exit()
			
        else:

            text = sys.stdin.readline()
            server.send(text)
            sys.stdout.flush()

server.close()
sys.exit()
