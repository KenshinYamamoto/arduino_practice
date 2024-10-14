import serial
ser = serial.Serial('/dev/cu.usbmodem11301', 9600)
not_used = ser.readline()
while True:
    val_arduino = ser.readline()
    # val_decoded = float(repr(val_arduino.decode())[1:-5])
    val_decoded = val_arduino
    print(val_decoded.decode())
    

ser.close()