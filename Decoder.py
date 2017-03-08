"""
Program is used to decode the data from CAN bus messages originating from the 
BMS. Program takes in a large string containing bytes in hex form. Multiple CAN 
bus messages are contained in this string. Each CAN bus message is 36 bytes long. 
Program updates paramter values for the BMS from these CAN bus messages and 
also prints any detected faults to the command line.

"""
from defTest import *

bmsData = [0, 0, 0, 0, 0, 0, 0]
bmsFaults = [0, 0, 0, 0, 0, 0, 0]
contData = [0, 0, 0, 0, 0, 0, 0, 0]
contFaults = [0, 0, 0, 0, 0, 0, 0]


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

            bmsData[0] = int(good[8:12], 16)
            bmsData[1] = int(good[12:16], 16)
            bmsData[2] = int(good[16:18], 16)
            bmsData[3] = int(good[18:20], 16)
            bmsData[5] = int(good[20:22], 16)
            bmsData[4] = int(good[22:24], 16)

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

            #Clear previous bms faults
            reset(bmsFaults)

            #Loop through each byte and check for active faults. Print them
            while i < 8:
                if binary0[i] == "1":
                    for j in range(0,7):
                        if bmsFaults[j] == 0:
                            bmsFaults[j] = BMSFaultList0[i]
                            break
                else:
                    try:
                        bmsFaults.remove(BMSFaultList0[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8: 
                if binary1[i] == "1":
                    for j in range(0,7):
                        if bmsFaults[j] == 0:
                            bmsFaults[j] = BMSFaultList1[i]
                            break
                else:
                    try:
                        bmsFaults.remove(BMSFaultList1[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 5:
                if binary2[i] == "1":
                    for j in range(0,7):
                        if bmsFaults[j] == 0:
                            bmsFaults[j] = BMSFaultList2[i]
                            break
                else:
                    try:
                        bmsFaults.remove(BMSFaultList2[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Last 3 bits of third byte correspond to current battery level
            # (e.g. If 5th index is high, battery level is high)
            # Battery levels stored in BMS data parameter dictionary. 
            # High: 3, Medium: 2, Low: 1
            if binary2[5] == "1":
                bmsData[6] = 3
            elif binary2[6] == "1":
                bmsData[6] = 2
            elif binary2[7] == "1":
                bmsData[6] = 1
        
        elif good[0:8] == controllerData0:
            con0 = good[10:12] + good[8:10]
            con1 = good[14:16] + good[12:14]
            con2 = good[18:20] + good[16:18]
            con3 = good[22:24] + good[20:22]
            contData[0] = int(con0, 16)
            contData[1] = int(con1, 16)
            contData[2] = int(con2, 16)
            contData[3] = int(con3, 16)

        elif good[0:8] == controllerData1:
            con4 = good[10:12] + good[8:10]
            con5 = good[14:16] + good[12:14]
            con6 = good[18:20] + good[16:18]
            con7 = good[22:24] + good[20:22]
            contData[4] = int(con4, 16)
            contData[5] = int(con5, 16)
            contData[6] = int(con6, 16)
            contData[7] = int(con7, 16)

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

            #Clear previous controller faults
            reset(contFaults)

            #Loop through each byte and check for active faults. Print them
            while i < 8:
                if binary0[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults0[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults0[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary1[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults1[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults1[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary2[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults2[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults2[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary3[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults3[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults3[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary4[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults4[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults4[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary5[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults5[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults5[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

            #Reset index variable
            i = 0

            while i < 8:
                if binary6[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults6[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults6[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

                #Reset index variable
            i = 0

            while i < 8:
                if binary7[i] == "1":
                    for j in range(0,7):
                        if contFaults[j] == 0:
                            contFaults[j] = controllerFaults7[i]
                            break
                else:
                    try:
                        contFaults.remove(controllerFaults7[i])
                    except ValueError:
                        pass
                #Increment index variable
                i += 1

        #Increment counter variable
        line_count += 1

        #Increase index for first important hex value in each message
        min_idx = (line_count * first) + 24

        #Increase index for last important hex value in each message
        max_idx = line_count * last

def reset(f):
    # Reset the faults
    for x in range(0,7):
        f[x] = 0

def hextobin(hexval):
    '''
    Takes a string representation of hex data with
    arbitrary length and converts to string representation
    of binary.  Includes padding 0s.
    Returns binary in reverse
    '''

    thelen = len(hexval) * 4
    binval = bin(int(hexval, 16))[2:]
    while len(binval) < thelen:
        binval = '0' + binval
    return binval[::-1]

def updateAll(message):
    decoder(message)
    return [bmsData, bmsFaults, contData, contFaults]
