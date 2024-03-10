from ReciptModel import Recipt
from Storage import Storage
from RFIDReader import RFIDReader
from ButtonReader import ButtonReader
from Clean import ProgramExitManager
import time
import RPi.GPIO as GPIO


storage = Storage()
recipt = Recipt()
exit_manager = ProgramExitManager

try:
    exit_manager.pin_extra_clean()
    while True:
        while True:
            rfid_reader = RFIDReader()
            rfid = rfid_reader.start_reading()
            rfid_exit = exit_manager.clean_rfid()
            if rfid:
                recipt.start_time = time.time()

                """ 1. ID чека к которому прикрепить заказ
                2. Номер выбранной бутылки
                3. Объем, который необходимо налить"""

                """ После завершения считывания RFID метки начинаем считывание кнопок """
                bot = recipt.get_bottle_number
                print(bot)

                button_reader = ButtonReader(storage.led_pin(bot),
                                         storage.button_pin(bot))
                button_reader.setup()
                button_reader.wait_for_events()
                button_exit = exit_manager.clean_button()

                while 1:
                    time.sleep(1)
                    """Ждем конца работы насосов"""
                    if storage.result == 1:
                        time.sleep(3)
                    break

                """ Формируем модель чека и отправляем данные на сервер """
                recipt.end_time = time.time()
                recipt.total_create
                recipt_clean = exit_manager.clean_recipt()
                time.sleep(2)


            storage.set_result = False

except Exception as fail:
    print(fail)
    exit_manager.pin_extra_clean()

finally:
    exit_manager.clian()
        #print("GOOD")



