# Import the socket module for network communication
import socket

# Define a function named client_program
def client_program():
    # Define the server's IP address and port number
    host = "127.0.0.1"
    port = 5002

    # Create a socket object using the default socket family (AF_INET) and socket type (SOCK_STREAM)
    client_socket = socket.socket() 

    # Connect to the server using the provided host and port
    client_socket.connect((host, port))

    # Receive data (up to 1024 bytes) from the server, decode it from bytes to string
    data = client_socket.recv(1024).decode() 

    # Print the received data from the server
    print('Received from server: ' + data)

    # Prompt the user to enter a polynomial key in binary
    key=input("enter polynomial key in binary: ")

    # Call the crc function with the received data and the entered key
    crc(data,key)

    # Create a string to send to the server indicating that there was no error
    stringg="recived string without error"

    # Encode the string and send it to the server
    client_socket.send(stringg.encode())

    # Close the client socket
    client_socket.close() 

# Define a function named xor that performs a bitwise XOR operation on two binary strings
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# Define a function named mod2div that performs modulo-2 division (CRC division)
def mod2div(dividend, divisor):
    div= len(divisor)
    temp=dividend[0:div]
    zero_xor='0'*div
    while div<len(dividend):
        if temp[0]=='1':
            temp=xor(divisor,temp)+dividend[div]
        else:
            temp=xor(zero_xor,temp)+dividend[div]
        div+=1
    if temp[0]=='1':
        temp=xor(divisor,temp)
    else:
        temp=xor(zero_xor,temp)
        
    return temp

# Define a function named crc that calculates the CRC bits and checks for errors
def crc(data,key):
    no_zero=len(key)-1
    crc_bits=mod2div(data,key)
    if ('0'*no_zero)==(crc_bits):
        print("remainder after decoding: ",crc_bits)
        print("No error has occurred")

# Call the client_program function to run the client
client_program()
