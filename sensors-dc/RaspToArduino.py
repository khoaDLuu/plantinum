import serial  # Khai báo thưu viện serial
ser = serial.Serial(/dev/ttyUSBx,9600)  # Lưu ý x là số cổng USB 
while 1:
 ser.write("1") #gửi số qua arduino thông qua serial