import time, binascii, requests, serial

#serijski port za arduino:
#ser = serial.Serial('smth')

#primanje podataka sa arduina:

while True:
    #response = ser.readline()
    #pocetak = 'Humidity:'

    #if response[0:9] == pocetak:
        #trenutna_vlaznost_zemljista = binascii.b2a_qp(response).split(',')[0]
        #trenutna_temperatura = binascii.b2a_qp(response).split(',')[1]
        # dodati/izmeniti senzore

    #vlaznost_zemljista = trenutna_vlaznost_zemljista[10:15]
    #temperatura = trenutna_temperatura[14:19]

    url = 'http://localhost:8000/basta/read_data'
    temperatura = 24
    vlaznost_vazduha = 30
    vazdusni_pritisak = 20
    vlaznost_zemljista = 35

    values = {'temp': temperatura, 'vlaznost_vazduha': vlaznost_vazduha, 'vazdusni_pritisak': vazdusni_pritisak,
              'vlaznost_zemljista': vlaznost_zemljista}

    response = requests.post(url=url, json=values)
    if response.status_code == 200:
        print("Podaci uspesno sacuvani u bazi")
    else:
        print(response.text)
    time.sleep(10)




