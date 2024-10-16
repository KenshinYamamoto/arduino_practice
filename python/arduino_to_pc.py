import serial
ser = serial.Serial('/dev/cu.usbmodem11301', 9600)
not_used = ser.readline()
while True:
    val_arduino = ser.readline()
    print(int(str(val_arduino).split("'")[1].split('\\')[0]))
    

ser.close()