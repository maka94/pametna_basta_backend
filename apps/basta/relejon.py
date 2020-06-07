import serial, time

#komunikacija = serial.Serial("/dev/ttyUSB0", 115200)


def komanda(sifra):
    time.sleep(5)
    #komunikacija.write(str(sifra).encode("UTF-8"))