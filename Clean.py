from RFIDReader import RFIDReader
from ButtonReader import ButtonReader
from DrinkDispenser import DrinkDispenser
from ReciptModel import Recipt

class ProgramExitManager:
    def __init__(self, led_pin, button_pin,  ):
        self.clean_but = button_pin
        self.clean_led = led_pin
    
    def clean_button(self):
        self.clean_RFID.end_read
        
    def 
    
    """
        ТЗ:
        У нас есть класс SessionMonitor в файле SessionLoader,
        который принимает в качестве аргумента URL на сервер.
        
        В нем есть метод monitor_session, который запускает
        контроль активности заказа с сервера, если заказ отменен,
        то метод возвращает 'False'.
    
    """
        