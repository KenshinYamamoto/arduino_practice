import matplotlib.pyplot as plt
import serial
import time

ser = serial.Serial('/dev/cu.usbmodem11301', 9600)
not_used = ser.readline()
s_time = time.time()

xs = []
y = []
counts = 0

fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 1024)

while time.time() - s_time < 10:
    counts += 1
    val_arduino = ser.readline()
    
    xs.append(counts)
    y.append(int(str(val_arduino).split("'")[1].split('\\')[0]))
    
    plt.pause(0.001)
    print(int(str(val_arduino).split("'")[1].split('\\')[0]))
    

plt.plot(xs, y)
plt.savefig('arduino_to_pc.png')
ser.close()