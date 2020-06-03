import serial

komunikacija = serial.Serial("/dev/ttyUSB0", 115200)

sifra = 2
komunikacija.write(sifra.encode("UTF-8"))