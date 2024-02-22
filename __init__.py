from ReciptModel import Recipt
from Storage import Storage
from RFIDReader import RFIDReader
from ButtonReader import ButtonReader
import time
import RPi.GPIO as GPIO


storage = Storage()
recipt = Recipt()

while True:
    while True:
        rfid_reader = RFIDReader()
        rfid = rfid_reader.start_reading()
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
            
            while 1:
                time.sleep(1)
                """Ждем конца работы насосов"""
                if storage.result == 1:
                    time.sleep(3)
                    break
                
            """ Формируем модель чека и отправляем данные на сервер """
            recipt.end_time = time.time()
            recipt.total_create
            time.sleep(2)
            
        
        storage.set_result = False
        
        #print("GOOD")
    
    
    
    
