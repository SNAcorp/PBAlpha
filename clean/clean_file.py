from RFIDReader import RFIDReader
from ButtonReader import ButtonReader
from DrinkDispenser import DrinkDispenser
from ReciptModel import Recipt
from SessionLoader import SessionMonitor


class ProgramExitManager:
    def __init__(self, led_pin, button_pin, monitor_session):
        self.clean_but = button_pin
        self.clean_led = led_pin
        self.clean_monitor_session = monitor_session

    def clean_RFID(self, RFIDReader):
        self.clean_RFID.end_read

    def check_order_status(self, RFIDReader):
        if not self.clean_monitor_session.monitor_session():
            self.clean_but.end_read
            self.clean_led.end_read
            return False
