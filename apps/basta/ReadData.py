import time, binascii, requests, serial

#serijski port za arduino:
ser = serial.Serial("/dev/ttyUSB0", 115200)

#primanje podataka sa arduina:

while True:
    response = ser.readline().decode("UTF-8")
    vlaznost_zemljista = response.split(';')[0]
    kisa = response.split(';')[1]
    temp = response.split(';')[2]
    vlaznost_vazduha = response.split(';')[3]
    zalivanje = response.split(';')[4]
    otvoren_prozor = response.split(';')[5]
    radi_ventilator = response.split(';')[6]
    print(response)



    #url = 'http://localhost:8000/basta/read_data'


    #values = {'vlaznost_zemljista': vlaznost_zemljista, 'kisa':kisa, 'temp': temperatura,
             # 'vlaznost_vazduha': vlaznost_vazduha, 'zalivanje': zalivanje, 'otvoren_prozor': otvoren_prozor,
             # 'ventilator': radi_ventilator}

    #response = requests.post(url=url, json=values)
    #if response.status_code == 200:
        #print("Podaci uspesno sacuvani u bazi")
    #else:
       # print(response.text)
    time.sleep(10)





