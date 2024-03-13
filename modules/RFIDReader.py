from pirc522 import RFID
from services.Log import Log
from storage.Storage import Storage
from storage.ReciptModel import Recipt
import signal
import sys
import datetime



class RFIDReader:

    def __init__(self):
        self.storage = Storage()
        self.recipt = Recipt()
        self.run = True
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        self.server_url = self.storage.server_url
        self.log = Log()

        signal.signal(signal.SIGINT, self.clean)
            
    """ Фнкция для корректного завершения чтения """
    def clean(self, signal, frame):
        self.run = False
        self.rdr.cleanup()
        sys.exit()
        
    """ Преобразуем UID из списка в строку """
    def reformat_uid(self, uid):
        result = ""
        for number in uid:
            result += str(number)
        return result
    
    """ Отправка запроса на сервер нашего UID """
    def send_to_server(self, uid):
#         """ Отправляем UID метки на сервер для проверки """
#         response = requests.post(self.server_url, json={'uid': uid})
#         if response.status_code == 200:
#             print("RFID метка успешно отпрвлена")
#             """Возвращаем ответ сервера в виде JSON """
#             return response.json()  
#         else:
#             print("Ошибка в отпрвке RFID метки")
#             return None
        return {'order_id': "10", 'access_granted': True, "volume": "test_cup", "number_of_bottle": 4}

    def start_reading(self):
        """ Основная функция для считывания меток """
        while self.run:
#             print("Начали читать RFID")
            self.log.start_time_of_rfid = datetime.datetime.now().strftime("%H:%M:%S.%f")
            self.rdr.wait_for_tag()
            self.log.is_the_rfid_turn_on = True
            
            """ Применяем встроеную функцию в библиотеку для отправки запроса """
            (error, data) = self.rdr.request()
             #if not error:
             #    print("\nDetected: " + format(data, "02x"))
            """ Избегаем колизии """
            (error, uid) = self.rdr.anticoll()
            """ Если нет ошибок, то выполняем программу далее """
            print(uid)
            if not error:
                print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                self.log.current_time_of_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
                self.log.end_time_of_rfid = datetime.datetime.now().strftime("%H:%M:%S.%f")
                """ Форматируем UID """
                uid = self.reformat_uid(uid)

                """Отправляем UID метки на сервер """
                response = self.send_to_server(uid)
                
                """ Если запрос прошел успешно"""
                if response:
                    """ Выбираем поле с валидностью """
                    access_granted = response["access_granted"]#.get("access_granted", False)
                    self.log.is_uid_valid = response["access_granted"]#.get("access_granted", False)
                    """ Если доступ разрешен """
                    if access_granted:
                        self.log.is_result_of_request_is_rfid_true = True
#                         print("rfid yes")
                        """ Передаем данные в модель """
                        self.recipt.uid = str(uid)
                        self.log.uid = str(uid)
                        self.recipt.order_id = response["order_id"]  #.get("order_id", "")
                        self.log.check_id = response["order_id"] #.get("order_id", "")
                        self.recipt.number_of_bottle = response["number_of_bottle"] #.get("number_of_bottle", -1)
                        self.log.number_of_bottle = response["number_of_bottle"]
                        self.recipt.volume = response["volume"] #.get("volume", "")
                        self.log.value_for_dispanser = response["volume"] #.get("volume", "")
                        return access_granted
                        
                    else:
                        print("rfid no")
                        return access_granted
                        """ Здесь мы можем выполнить какие-то действия при отказе в доступе """