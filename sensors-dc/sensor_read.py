import serial

# change ACM number as found from ls /dev/tty/ACM*
ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600

def read_sensor():
    str_temp = ser.readline()
    temp = float(str_temp.split(b'\\')[0])
    
    str_humi = ser.readline()
    humi = float(str_humi.split(b'\\')[0])
    
    str_light = ser.readline()
    light = int(str_light.split(b'\\')[0])
    
    str_mois = ser.readline()
    mois = int(str_mois.split(b'\\')[0])

    return temp, humi, light, mois
    


