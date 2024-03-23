from storage.Storage import Storage
import RPi.GPIO as GPIO

class ProgramExitManager:
    __Button = None
    __RFID = None
    __Recipt = None
    __DrinkDispenser = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProgramExitManager, cls).__new__(cls)
        return cls.instance

    @property
    def Button(self):
        return self.__Button

    @Button.setter
    def Button(self, ButtonReader):
        self.__Button = ButtonReader

    @property
    def rfid(self):
        return self.__RFID

    @rfid.setter
    def rfid(self, RFIDReader):
        self.__RFID = RFIDReader

    @property
    def recipt(self):
        return self.__Recipt

    @recipt.setter
    def recipt(self, ReciptModel):
        self.__Recipt = ReciptModel

    @property
    def drink_dispenser(self):
        return self.__DrinkDispenser

    @drink_dispenser.setter
    def drink_dispenser(self, DrinkDispenser):
        self.__DrinkDispenser = DrinkDispenser

    def clean_rfid(self):
        if self.__RFID != None:
            self.__RFID.clean

    def clean_button(self):
        if self.__Button != None:
            self.__Button.clean

    def clean_recipt(self):
        if self.__Recipt == None:
            self.__Recipt.clean

    def clean_drinkdispanser(self):
        if self.__DrinkDispanser != None:
            self.__DrinkDispenser.clean

    def clean_all(self):
        self.clean_rfid
        self.clean_button
        self.clean_recipt
        self.clean_drinkdispanser

    def pin_extra_clean(self):
        GPIO.setmode(GPIO.BOARD)
        for bpin, lpin, ppin in zip(Storage.button_pin, Storage.led_pin, Storage.pump_list):
            GPIO.cleanup(bpin)
            GPIO.cleanup(lpin)
            GPIO.cleanup(ppin)

    def clean(self):
        self.__Button = None
        self.__RFID = None
        self.__Recipt = None
        self.__DrinkDispenser = None



