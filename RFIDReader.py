import signal
import sys
import time
import requests
from pirc522 import RFID
import RPi.GPIO as GPIO
from Storage import Storage
from ReciptModel import Recipt
class RFIDReader:

    def __init__(self):
        self.storage = Storage()
        self.recipt = Recipt()
        self.run = True
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        self.server_url = self.storage.server_url

        signal.signal(signal.SIGINT, self.end_read)
            
    """ Фнкция для корректного завершения чтения """
    def end_read(self, signal, frame):
        self.run = False
        self.rdr.cleanup()
        sys.exit()
    
    """ Отправка запроса на сервер нашего UID """
    def send_to_server(self, uid):
        """ Отправляем UID метки на сервер для проверки """
        response = requests.post(self.server_url, json={'uid': uid})
        if response.status_code == 200:
            print("RFID метка успешно отпрвлена")
            return response.json()  """Возвращаем ответ сервера в виде JSON """
        else:
            print("Ошибка в отпрвке RFID метки")
            return None
        return {'order_id': "10", 'access_granted': True, "volume": "test_cup", "number_of_bottle": 2}

    def start_reading(self):
        """ Основная функция для считывания меток """
        while self.run:
#             print("Начали читать RFID")
            self.rdr.wait_for_tag()
            
            """ Применяем встроеную функцию в библиотеку для отправки запроса """
            (error, data) = self.rdr.request()
             #if not error:
             #    print("\nDetected: " + format(data, "02x"))
            """ Избегаем колизии """
            (error, uid) = self.rdr.anticoll()
            """ Если нет ошибок, то выполняем программу далее """
            if not error:
                #print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

                """Отправляем UID метки на сервер """
                response = self.send_to_server(uid)
                
                """ Если запрос прошел успешно"""
                if response:
                    """ Выбираем поле с валидностью """
                    access_granted = response["access_granted"]#.get("access_granted", False)
                    
                    """ Если доступ разрешен """
                    if access_granted:
#                         print("rfid yes")
                        """ Передаем данные в модель """
                        self.recipt.uid = str(uid)
                        self.recipt.order_id = response["order_id"] #.get("order_id", "")
                        self.recipt.number_of_bottle = response["number_of_bottle"] #.get("number_of_bottle", -1)
                        self.recipt.volume = response["volume"] #.get("volume", "")
                        return access_granted
                        
                    else:
                        print("rfid no")
                        return access_granted
                        """ Здесь мы можем выполнить какие-то действия при отказе в доступе """