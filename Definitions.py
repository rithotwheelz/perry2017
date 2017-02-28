"""
Defintions1.py

File containing definitions to use in BMSDecoder.py and ControllerDecoder.py files. Programs 
to decode BMS messages coming from the BMS and controller on RIT Hot Wheelz Phoebe 2.0 
race car.

"""

#BMS mailbox IDs
BMSDataID = "0000003b"
BMSFaultID = "000003cc"

#Controller mailbox IDs
controllerData0 = "00000033"
controllerData1 = "00000034"
controllerFaults = "00000035"

#Dictionary holding BMS data parameters
BMSParameters = {"Pack Current": 0, "Pack Voltage": 0, "Pack SOC": 0, "High Temp": 0, 
				 "Low Temp": 0, "Average Temp": 0, "Battery Level": 0}

#Dictionary containing controller data parameters
controllerParams = {"Capacitor Voltage": 0, "MotorRPM": 0, "Motor Temp": 0, "Controller Current": 0, "Controller Temp": 0, "Speed": 0, "Acceleration": 0, "KSI Voltage": 0}

#Array containing list of BMS faults for first byte. Corresponds to Custom Flag #0 in the BMS CAN bus settings
BMSFaultList0 = ["Internal Communication", "Internal Conversion", "Weak Cell", "Low Cell Voltage", "Open Wiring", "Current Sensor", "Pack Voltage Sensor", "Weak Pack"]

#Array containing list of BMS faults for second byte. Corresponds to Custom Flag #1 in the BMS CAN bus settings
BMSFaultList1 = ["Voltage Redundancy", "Fan Monitor", "Thermistor", "CANBUS Communication", "Always-On Supply", "High Voltage Isolation", "12V Power Supply", "Charge Limit Enforcement"]

#Array containing list of BMS faults for third byte. Corresponds to Custom Flag #2 in the BMS CAN bus settings
BMSFaultList2 = ["Discharge Limit Enforcement", "Charger Safety Relay", "Internal Memory", "Internal Thermistor", "Internal Logic"]

#Array containing list of controller faults for first byte. Corresponds to controller Status1 variable
controllerFaults0 = ["Main Contactor Welded", "Main Contactor Did Not Close", "Pot Low Overcurrent", "Throttle Wiper Low",
					 "Throttle Wiper High", "Pot2 Wiper Low", "Pot2 Wiper High", "EEPROM Failure"]

#Array containing list of controller faults for second byte. Corresponds to controller Status2 variable
controllerFaults1 = ["HPD/Sequencing Fault", "Severe B+ Undervoltage", "Severe B+ Overvoltage", "B+ Undervoltage Cutback",
					 "B+ Overvoltage Cutback", "Not Used", "Controller Overtemp Cutback", "Controller Severe Undertemp"]

#Array containing list of controller faults for third byte. Corresponds to controller Status3 variable
controllerFaults2 = ["Controller Severe Overtemp", "Coill Driver Open/Short", "Coi12 Driver Open/Short", "Coil3 Driver Open/Short",
					 "Coi14 Driver Open/Short", "PD Open/Short", "Main Open/Short", "EMBrake Open/Short"]

#Array containing list of controller faults for fourth byte. Corresponds to controller Status4 variable
controllerFaults3 = ["Precharge Failed", "Digital Out 6 Overcurrent", "Digital Out 7 Overcurrent", "Controller Overcurrent",
					 "Current Sensor Fault", "Motor Temp Hot Cutback", "Parameter Change Fault", "Motor Open"]

#Array containing list of controller faults for fifth byte. Corresponds to controller Status5 variable
controllerFaults4 = ["External Supply Out of Range", "Motor Temp Sensor Fault", "VCL Run Time Error", "+5V Supply Failure",
					 "OS General", "PDO Timeout", "Encoder Fault", "Stall Detected"]

#Array containing list of controller faults for sixth byte. Corresponds to controller Status6 variable
controllerFaults5 = ["Not Used", "Not Used", "Not Used", "Not Used", "Motor Type Fault", "Supervisor Fault",
					 "Motor Characterization Fault", "Pump Hardware Fault"]

#Array containing list of controller faults for seventh byte. Corresponds to controller Status7 variable
controllerFaults6 = ["Not Used", "VCL/OS Mismatch", "EM Brake Failed to Set", "Encoder LOS (Limited Operating Strategy)",
					 "Not Used", "Dual Severe Fault", "Fault On Other Traction Controller", "Illegal Model Number"]

#Array containing list of controller faults for eighth byte. Corresponds to controller Status8 variable
controllerFaults7 = ["Pump Overcurrent", "Pump BDI", "Pump HPD", "Dualmotor Parameter Mismatch", "Severe KSI Undervoltage",
					 "Severe KSI Overvoltage", "Insulation Resistance Low", "Encoder Pulse Count Fault"]
