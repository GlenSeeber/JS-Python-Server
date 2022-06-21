import socket

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# what is the IP address to the server you are connecting to?
# if you're running this locally, you'll need the private IP
SERVER = "172.16.225.152"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    #send_length is your header
    send_length = str(msg_length).encode(FORMAT)
    # add padding
    send_length += b' ' * (HEADER - len(send_length))
    #send header
    client.send(send_length)
    #send message
    client.send(message)
    # print what you recieve back from your client
    print(client.recv(2048).decode(FORMAT))

while True:
    # get user input
    myMsg = input("Send Message:\n> ")
    #if they say 'quit' or 'q', disconnect them
    if myMsg in ("quit", "q"):
        break
    # otherwise, send the message
    send(myMsg)

#when they exit the loop, discconect them
send(DISCONNECT_MESSAGE)