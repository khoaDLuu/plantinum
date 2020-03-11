import serial  # Khai báo thưu viện serial
ser = serial.Serial(/dev/ttyUSBx,9600)  # Lưu ý x là số cổng USB 
While 1:
 ser.readline() #Đọc số từ arduino gửi qua