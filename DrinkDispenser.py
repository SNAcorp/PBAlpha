from Storage import Storage
from ReciptModel import Recipt
import RPi.GPIO as GPIO
import time

class DrinkDispenser:
    
    """ Переменная ответственная за цикл в котором идет проверка нажатия кнопки"""
    res = 0
    
    def __init__(self):
        self.recipt = Recipt() """ Экземляр класса Recipt """
        self.storage = Storage() """  Экземляр класса Storage """
        self.index = self.recipt.get_bottle_number """ Номер выбранной бутылки """
        self.volume = self.storage.get_volume(self.recipt.get_volume) """ Порция вина """ 
        
        self.pin = self.storage.get_dispander_pin(self.index) """ Пин на котором нужно включить насос """
        
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
        
        """ Включение и выключение насоса спустя отведенное время порцией """
        GPIO.output(self.pin, GPIO.LOW)
        print(f"На пине {self.pin} включен насос")
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.HIGH)
        print(f"На пине {self.pin} выключен насос")
        
        """ Меняем флаг на завершение программы """
        self.res = 1
        
        """ Ставим флаг для всех классов """
        self.storage.result_of_program = True
        
        """ Отчищаем уставленные настройки """
        GPIO.cleanup()
        return 1

    def run(self):
        try:
            """ Запускаем основную функцию """
            self.dispense_drink(self.index, self.volume)
            return 1
            
        except Exception:
            print("Программа завершена.")
            GPIO.cleanup()
        
