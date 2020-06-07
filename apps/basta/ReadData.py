import time, requests, serial

#serijski port za arduino:
#ser = serial.Serial("/dev/ttyUSB0", 115200)


#primanje podataka sa arduina:

#while True:
    #response = ser.readline().decode("UTF-8")
    #vlaznost_zemljista = response.split(';')[0]
    #kisa = response.split(';')[1]
    #temp = response.split(';')[2]
    #vlaznost_vazduha = response.split(';')[3]
    #zalivanje = response.split(';')[4]
    #otvoren_prozor = response.split(';')[5]
    #radi_ventilator = response.split(';')[6]
    #print(response)



url = 'http://172.20.222.226:8000/basta/read_data'
values = {"temp": 25, "vlaznost_vazduha": 15, "vazdusni_pritisak":18, "vlaznost_zemljista": 46}


    #values = {'vlaznost_zemljista': 2, 'kisa':3, 'temp': 4,
             #'vlaznost_vazduha': 6, 'zalivanje': 1, 'otvoren_prozor': 1,
             #'ventilator': 1}

response = requests.post(url=url, json=values)
if response.status_code == 200:
    print("Podaci uspesno sacuvani u bazi")
else:
    print(response.text)
    #time.sleep(10)