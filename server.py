import socket 
import threading

HEADER = 64
PORT = 5050
# my linux laptop: 192.168.1.45
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    #keep the line open as long as client is connected
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # if we recieve a message
        if msg_length:
            # this can crash the thread, but this is just a prototype anyways
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                #connected = False
                break
            # what's the network information of the client who connected
            print(f"[addr: {addr}] msg: {msg}")
            try:
                # check if the message (not the header) is an int 
                output = int(msg)
            except:
                if output == DISCONNECT_MESSAGE:
                    output = 'disconnecting you...'
                else:
                    output = "Error: not an integer"
            # if it is an int, square it
            else:
                output *= output
                output = str(output)
            
            #send the output back to the client
            conn.send(output.encode(FORMAT))
    #close connection if connected is no longer True
    conn.close()
        
#initiate and maintain the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        #use threading so we can handle multiple clients cleanly.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()