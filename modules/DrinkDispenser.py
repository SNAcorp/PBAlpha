from storage.Storage import Storage
from storage.ReciptModel import Recipt
from services.Log import Log
import time
import datetime
import RPi.GPIO as GPIO

class DrinkDispenser:
    
    """ Переменная ответственная за цикл в котором идет проверка нажатия кнопки"""
    res = 0
    
    def __init__(self):
        """ Экземляр класса Recipt """
        self.recipt = Recipt()
        """  Экземляр класса Storage """
        self.storage = Storage()
        """ Номер выбранной бутылки """
        self.index = self.recipt.get_bottle_number
        """ Порция вина """
        self.volume = self.storage.get_volume(self.recipt.get_volume) 
        """ Пин на котором нужно включить насос """
        self.pin = self.storage.get_dispander_pin(self.index)
        self.log = Log()
        
        GPIO.setmode(GPIO.BOARD) 
        
        """ Настройка пина насоса """
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
            
    """ Функция для передачи флага об окончании работы класса """
    def result(self):
        return self.res
    
    """ Основная функция """
    def dispense_drink(self, index, duration):
        """ Провверка на неправильный индекс """
        if index < 0 or index > 4:
            print("Недопустимый индекс насоса", index)
            return 0
        self.log.number_of_dispanser = index
        self.log.start_time_of_dispanser = datetime.datetime.now().strftime("%H:%M:%S.%f")
        """ Включение и выключение насоса спустя отведенное время порцией """
        print(f"На пине {self.pin} включен насос")
        GPIO.output(self.pin, GPIO.LOW)
        self.log.is_dispanser_turn_on = True
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.HIGH)
        self.log.end_time_of_dispanser = datetime.datetime.now().strftime("%H:%M:%S.%f")
        print(f"На пине {self.pin} выключен насос")
        
        """ Меняем флаг на завершение программы """
        self.res = 1
        
        """ Ставим флаг для всех классов """
        self.storage.result_of_program = True
        
        """ Отчищаем уставленные настройки """
        GPIO.cleanup()
        return 1
    
    def clean(self):
        self.res = 1
        GPIO.cleanup(self.pin)
        
    def run(self):
        try:
            """ Запускаем основную функцию """
            self.dispense_drink(self.index, self.volume)
            return 1
            
        except Exception:
            print("Программа завершена.")
            
        finally:
            GPIO.cleanup()
        
