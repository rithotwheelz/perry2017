"""
Program is used to decode the data from CAN bus messages originating from the 
BMS. Program takes in a large string containing bytes in hex form. Multiple CAN 
bus messages are contained in this string. Each CAN bus message is 36 bytes long. 
Program updates paramter values for the BMS from these CAN bus messages and 
also prints any detected faults to the command line.

"""
from Definitions import *

def decoder(message):
    """
    Function to decode a large byte hex string. The BMS data parameters are 
    overwritten after each message is decoded. Faults are printed to the 
    console. Function only recognizes 2 message IDs in each message.

    Input: message (str) - A large byte string containing hex values. This
                            string contains multiple can bus messages

    Output: none.

    """

    #Number indicating the index of the first important hex value in each
    # can bus message.
    first = 48

    #Number indicating the index of the last important hex value in each 
    # can bus message
    last = 72

    #The number of CAN messages which will be read in each message string. Each 
    # can bus message is 36 bytes. The first number of messages will be read. #The rest will be ignored.
    line_num = 3

    #Variable to keep track of the current can bus message index in each 
    # message string
    line_count = 1

    #Variable containing current index of first important hex value in each 
    # can bus message
    min_idx = line_count * first

    #Variable containing current index of last important hex value in each 
    # can bus message
    max_idx = line_count * last

    #Loop through the number of indicated CAN messages in each message string, 
    # decoding each message, either a data message or a fault message
    while line_count <= (line_num + 1):

        #Use the current first and last indices to get the CAN ID and data 
        # bytes for the current 36 byte CAN bus message
        good = message[min_idx:max_idx]

        #Check if the current CAN ID matches the BMSDataID in order to use the 
        # corresponding data bytes to update the dictionary values. Store 
        # the hex values in decimal
        if good[0:8] == BMSDataID:

            BMSParameters["Pack Current"] = int(good[8:12], 16)
            BMSParameters["Pack Voltage"] = int(good[12:16], 16)
            BMSParameters["Pack SOC"] = int(good[16:18], 16)
            BMSParameters["High Temp"] = int(good[18:20], 16)
            BMSParameters["Low Temp"] = int(good[20:22], 16)
            BMSParameters["Average Temp"] = int(good[22:24], 16)

        #Else if the CAN ID matches the BMSFaultID, then check the 
        # corresponding data bytes to find faults. Each byte in the data 
        # section is converted to binary. Each bit in each byte corresponds 
        # to a fault. A '1' indicates a fault, '0' indicates normal operation. 
        # Print each detected fault to the command line
        elif good[0:8] == BMSFaultID:

            #convert bytes to binary
            binary0 = hextobin(good[8:10])
            binary1 = hextobin(good[10:12])
            binary2 = hextobin(good[12:14])

            #Variable to keep track of index of current bit in each byte
            i = 0

            #Loop through each byte and check for active faults. Print them
            while i < 8:
                if binary0[i] == "1":
                    print(BMSFaultList0[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    print(BMSFaultList1[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 5:
                if binary2[i] == "1":
                    print(BMSFaultList2[i] + " Fault")
                #Increment index variable
                i += 1

            #Last 3 bits of third byte correspond to current battery level
            # (e.g. If 5th index is high, battery level is high)
            # Battery levels stored in BMS data parameter dictionary. 
            # High: 3, Medium: 2, Low: 1
            if binary2[5] == "1":
                BMSParameters["Battery Level"] = 3
            if binary2[6] == "1":
                BMSParameters["Battery Level"] = 2
            if binary2[7] == "1":
                BMSParameters["Battery Level"] = 1
        
        elif good[0:8] == controllerData0:

            controllerParams["Capacitor Voltage"] = int(good[8:12], 16)
            controllerParams["Motor RPM"] = int(good[12:16], 16)
            controllerParams["Motor Temp"] = int(good[16:20], 16)
            controllerParams["Controller Current"] = int(good[20:24], 16)

        elif good[0:8] == controllerData1:

            controllerParams["Controller Temp"] = int(good[8:12], 16)
            controllerParams["Speed"] = int(good[12:16], 16)
            controllerParams["Acceleration"] = int(good[16:20], 16)
            controllerParams["KSI Voltage"] = int(good[20:24], 16)

        elif good[0:8] == controllerFaults:

            binary0 = hextobin(good[8:10])
            binary1 = hextobin(good[10:12])
            binary2 = hextobin(good[12:14])
            binary3 = hextobin(good[14:16])
            binary4 = hextobin(good[16:18])
            binary5 = hextobin(good[18:20])
            binary6 = hextobin(good[20:22])
            binary7 = hextobin(good[22:24])

            #Variable to keep track of index of current bit in each byte
            i = 0

            #Loop through each byte and check for active faults. Print them
            while i < 8:
                if binary0[i] == "1":
                    print(controllerFaults0[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    print(controllerFaults1[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary2[i] == "1":
                    print(controllerFaults2[i] + " Fault")
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    print(controllerFaults3[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary2[i] == "1":
                    print(controllerFaults4[i] + " Fault")
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    print(controllerFaults5[i] + " Fault")
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary2[i] == "1":
                    print(controllerFaults6[i] + " Fault")
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    print(controllerFaults7[i] + " Fault")
                #Increment index variable
                i += 1



        #Increment counter variable
        line_count += 1

        #Increase index for first important hex value in each message
        min_idx = (line_count * first) + 24

        #Increase index for last important hex value in each message
        max_idx = line_count * last


def hextobin(hexval):
    '''
    Takes a string representation of hex data with
    arbitrary length and converts to string representation
    of binary.  Includes padding 0s
    '''

    thelen = len(hexval) * 4
    binval = bin(int(hexval, 16))[2:]
    while len(binval) < thelen:
        binval = '0' + binval
    return binval


def main(data):
    # data = input("Enter value: ")
    decoder(data)
    for a, b in BMSParameters.items():
        print(a, b)

# main()
