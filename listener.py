'''    Simple socket server using threads
'''
import socket
import sys
import codecs
import Decoder
HOST = '192.168.1.25'   # Symbolic name, meaning all available interfaces
PORT = 50000            # Arbitrary non-privileged port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Test created')

#Bind socket to local host and port
try:
    s.bind((HOST,PORT))
    print ('Socket bind complete')
    s.settimeout(50)
    #Stamfsdfjdsoirt listening on socket
    s.listen(1)
    print ('Socket now listening')
    #now keep talking with the client
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg) + ' Message ')
    sys.exit()

#while 1:
    #wait to accept a connection - blocking call
try:
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    print (str(conn) + "\n" + str(addr))
    while 1:
        mess = conn.recvfrom(4096)
        # print ("Message:", repr(mess))
        raw_message = codecs.encode(mess[0], 'hex')
        clean_message = raw_message.decode("utf8")
        # print ("Message:", repr(clean_message))
        Decoder.main(clean_message)
        
except socket.timeout as msg:
    print ('Socket has timed out. No messages received')
    sys.exit()
print ('finish')
s.close()
