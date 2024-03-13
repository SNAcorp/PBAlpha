from ReciptModel import Recipt
from Storage import Storage
from RFIDReader import RFIDReader
from ButtonReader import ButtonReader
from Clean import ProgramExitManager
from SessionLoader import SessionMonitor
import datetime
import time

import RPi.GPIO as GPIO

monitor = SessionMonitor()
storage = Storage()
recipt = Recipt()
exit_manager = ProgramExitManager()
exit_manager.recipt = recipt

exit_manager.clean_all
exit_manager.pin_extra_clean
exit_manager.clean

def main():

    try:
        while monitor.monitor_session() == True:
            try:
                while True:
                    rfid_reader = RFIDReader()
                    exit_manager.rfid = rfid_reader

                    rfid = rfid_reader.start_reading()
                    if rfid:
                        recipt.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        """ 1. ID чека к которому прикрепить заказ
                        2. Номер выбранной бутылки
                        3. Объем, который необходимо налить"""

                        """ После завершения считывания RFID метки начинаем считывание кнопок """
                        bot = recipt.get_bottle_number
                        print(bot)

                        button_reader = ButtonReader(storage.led_pin(bot), storage.button_pin(bot))
                        exit_manager.Button = button_reader
                        button_reader.setup()
                        button_reader.wait_for_events()

                        while 1:
                            time.sleep(1)
                            """Ждем конца работы насосов"""
                            if storage.result == True:
                                time.sleep(3)
                                break

                        """ Формируем модель чека и отправляем данные на сервер """
                        recipt.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        recipt.total_create
                        time.sleep(2)

                    storage.set_result = False
                    exit_manager.clean

            #print("GOOD")

            except:
                print("Ошибка в исполнении основной программы:")

    finally:
        exit_manager.clean_all
        exit_manager.pin_extra_clean
        exit_manager.clean


while monitor.monitor_session() == False:
    time.sleep(5)
    main()









