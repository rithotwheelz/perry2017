'''    Simple socket server using threads
'''
from flask import Flask
from flask import render_template
from flask import jsonify
# import num
import socket
import sys
import codecs
import threading
import Decoder

##DEFINITIONS
HOST = '192.168.1.25'   # Symbolic name, meaning all available interfaces
PORT = 50000            # Arbitrary non-privileged port

BMSParameters = {"Pack Current": 0, "Pack Voltage": 0, "Pack SOC": 0, "High Temp": 0, 
                 "Low Temp": 0, "Average Temp": 0, "Battery Level": 0}

controllerParams = {"Capacitor Voltage": 0, "MotorRPM": 0, "Motor Temp": 0, "Controller Current": 0, "Controller Temp": 0, "Speed": 0, "Acceleration": 0, "KSI Voltage": 0}

contFaults = []
bmsFaults = []

app = Flask(__name__)

def listen(args, threadEnder):
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
        print("listener ready. starting server...")
        server.start()
        print ('Connected with ' + addr[0] + ':' + str(addr[1]))
        print (str(conn) + "\n" + str(addr))
        while (not threadEnder.is_set()):
            mess = conn.recvfrom(1024)
            # print ("Message:", repr(mess))
            raw_message = codecs.encode(mess[0], 'hex')
            clean_message = raw_message.decode("utf8")
            # print ("Message:", repr(clean_message))
            # bmsUpdate(Decoder.BMS(clean_message))
            # contUpdate(Decoder.Controller(clean_message))
            allThem = Decoder.updateAll(clean_message)
            bmsUpdate(allThem[0])
            contUpdate(allThem[2])
            faultsUpdate(allThem[1], allThem[3])
            
    except socket.timeout as msg:
        print ('Socket has timed out. No messages received')
        listener.join()
        sys.exit()
    print ('listener finished')
    s.close()

def bmsCurr():
    return BMSParameters["Pack Current"]

def bmsVolt():
    return BMSParameters["Pack Voltage"]

def bmsSOC():
    return BMSParameters["Pack SOC"]

def bmsHTemp():
    return BMSParameters["High Temp"]

def bmsLTemp():
    return BMSParameters["Low Temp"]

def bmsATemp():
    return BMSParameters["Average Temp"]

def bmsLvl():
    return BMSParameters["Battery Level"]

def contCap():
    return controllerParams["Capacitor Voltage"]

def contRpm():
    return controllerParams["MotorRPM"]

def contMtemp():
    return controllerParams["Motor Temp"]

def contCur():
    return controllerParams["Controller Current"]

def contTemp():
    return controllerParams["Controller Temp"]

def contSpeed():
    return controllerParams["Speed"]

def contAcc():
    return controllerParams["Acceleration"]

def contKsi():
    return controllerParams["KSI Voltage"]

def bmsUpdate(data):
    # current, voltage, soc, hTemp, aTemp, lTemp, lvl
    BMSParameters["Pack Current"] = data[0]
    BMSParameters["Pack Voltage"] = data[1]
    BMSParameters["Pack SOC"] = data[2]
    BMSParameters["High Temp"] = data[3]
    BMSParameters["Average Temp"] = data[4]
    BMSParameters["Low Temp"] = data[5]
    BMSParameters["Battery Level"] = data[6]

def contUpdate(data):
    controllerParams["Capacitor Voltage"] = data[0]/64
    controllerParams["MotorRPM"] = data[1]
    controllerParams["Motor Temp"] = (data[2]/100)*(9/5)+32
    controllerParams["Controller Current"] = data[3]/1000
    controllerParams["Controller Temp"] = (data[4]/100)*(9/5)+32
    controllerParams["Speed"] = data[5]/100
    controllerParams["Acceleration"] = data[6]/1000
    controllerParams["KSI Voltage"] = data[7]/100

def faultsUpdate(bms, cont):
    bmsFaults = bms
    contFaults = cont

def run(args, threadEnder):
    if (not threadEnder.is_set()):
        print("starting server run")
        app.run()
    else:
        print("exiting server run")
        sys.exit()

threadEnder = threading.Event()
listener = threading.Thread(target=listen, args=(1, threadEnder))
server = threading.Thread(target=run, args=(2, threadEnder))

listener.daemon = False
server.daemon = False

try:
    print("starting listener...")
    listener.start()

    # print("listener ready. starting server...")
    # server.start()
    while True:
        pass

except KeyboardInterrupt:
    print ("Closing program...")
    threadEnder.set()
    print("Bye.")

@app.route('/')
def hello():
    return render_template("table.html")

@app.route('/_thing', methods= ['GET'])
def thing():
    capVolt = contCap()
    RPM = contRpm()
    motorTemp = contMtemp()
    contCurr = contCur()
    cTemp = contTemp()
    speed = contSpeed()
    accel = contAcc()
    ksi = contKsi()

    packVolt = bmsVolt()
    packCurr = bmsCurr()
    soc = bmsSOC()
    hTemp = bmsHTemp()
    aTemp = bmsATemp()
    lTemp = bmsLTemp()
    bLev = bmsLvl()

    return jsonify(capVolt=capVolt, RPM=RPM, motorTemp=motorTemp, contCurr=contCurr, cTemp=cTemp, speed=speed, accel=accel, ksi=ksi, packVolt=packVolt, packCurr=packCurr, soc=soc, hTemp=hTemp, aTemp=aTemp, lTemp=lTemp, bLev=bLev, contFaults=contFaults, bmsFaults=bmsFaults)
