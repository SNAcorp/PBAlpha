import signal
import sys
import time
import requests
from pirc522 import RFID
import RPi.GPIO as GPIO

class RFIDReader:

    __check_id = ""

    def __init__(self, server_url, check_id):
            self.run = True
            self.rdr = RFID()
            self.util = self.rdr.util()
            self.util.debug = True
            self.server_url = server_url
            self.__check_id = check_id

            signal.signal(signal.SIGINT, self.end_read)

    @property
    def check_id(self):
        return self.__check_id

    @check_id.setter
    def check_id(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")

        self.__check_id = value.strip()

    def end_read(self, signal, frame):
        self.run = False
        #print("\nCtrl+C captured, ending read.")
        self.rdr.cleanup()
        sys.exit()

    def send_to_server(self, uid):
        # Отправляем UID метки на сервер для проверки
        response = requests.post(self.server_url, json={'uid': uid})
        if response.status_code == 200:
            #print("RFID tag sent to server successfully.")
            return response.json()  # Возвращаем ответ сервера в виде JSON
        else:
            #print("Failed to send RFID tag to server.")
            return None

    def start_reading(self):
        #print("Starting RFID reading")
        while self.run:
            self.rdr.wait_for_tag()

            (error, data) = self.rdr.request()
            #if not error:
                #print("\nDetected: " + format(data, "02x"))

            (error, uid) = self.rdr.anticoll()
            if not error:
                #print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

                # Отправляем UID метки на сервер
                response = self.send_to_server(uid)
                if response:
                    access_granted = response.get("access_granted", False)
                    check_id = response.get("check_id", 0)
                    if access_granted:
                        return [check_id, access_granted]
                        # Здесь вы можете продолжить выполнение программы, т.к. метка допущена
                    else:
                        return [check_id, access_granted]
                        # Здесь вы можете выполнить какие-то действия при отказе в доступе