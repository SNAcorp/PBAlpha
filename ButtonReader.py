import RPi.GPIO as GPIO
import time
from DrinkDispenser import DrinkDispenser

class ButtonReader:
    
    def __init__(self, led_pin: int, button_pin: int):
        self.__run = True
        self.__led_pin = led_pin
        self.__button_pin = button_pin
    
    """Функция которая исполняется когда нажали кнопку"""
    def button_callback(self, pin: int) -> bool:
        
        """ Доп. Проверка нажатия кнопки """ 
        if GPIO.input(pin):
            #print('yes ', pin)
            """ Создание экземпляра класса для управления насосами """
            dispenser = DrinkDispenser()
            dispenser.run()
            
            """ Ждем, пока насосы завершат свою работу, чтобы выключить подстветку """
            if dispenser.result() == 1:
                self.__run = False
                GPIO.cleanup()
                return True
            
        return False

    """ Функция настройки пинов взаимодейтсвия с кнопкой и подствеки """
    def setup(self):
        
        """ Раскладка пинов "BOARD" """
        GPIO.setmode(GPIO.BOARD)
        
        """ Настройка пина подстветки """
        GPIO.setup(self.__led_pin, GPIO.OUT)
        GPIO.output(self.__led_pin, GPIO.HIGH)
   
        """ НАстройка пина входа"""
        GPIO.setup(self.__button_pin, GPIO.IN)
    

    """ Функция ожидания события """
    def wait_for_events(self):
        
        
            
            """ Бесконечный цикл слежения за нажатием """
            while self.__run:
                
                """ Проверка не нажата ли кнопка """
                if GPIO.input(self.__button_pin) == GPIO.LOW:
                    
                    """ Задержка для компенсации дрибезжания кнопок"""
                    time.sleep(0.11)
                    self.button_callback(self.__button_pin)
                    
                else:
                    """ Задержка для компенсации дрибезжания кнопок"""
                    time.sleep(0.11)
        
        
            