import serial
# the serial library is used for reading serial data

# change ACM number as found from ls /dev/tty/ACM#
ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
    # send an angle number as an array of num characters
    angle = str(120)
    ser.write(angle)
