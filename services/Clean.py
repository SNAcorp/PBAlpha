from storage.Storage import Storage
import RPi.GPIO as GPIO

class ProgramExitManager:
    __Button = None
    __RFID = None
    __Recipt = None
    __DrinkDispenser = None

    def __new__(cls):
        """
        Создание нового экземпляра класса (синглтон).
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProgramExitManager, cls).__new__(cls)
        return cls.instance

    @property
    def Button(self):
        """
        Getter для свойства Button.
        """
        return self.__Button

    @Button.setter
    def Button(self, ButtonReader):
        """
        Setter для свойства Button.
        """
        self.__Button = ButtonReader

    @property
    def RFID(self):
        """
        Getter для свойства RFID.
        """
        return self.__RFID

    @RFID.setter
    def RFID(self, RFIDReader):
        """
        Setter для свойства RFID.
        """
        self.__RFID = RFIDReader

    @property
    def Receipt(self):
        """
        Getter для свойства Receipt.
        """
        return self.__Receipt

    @Receipt.setter
    def Receipt(self, ReceiptModel):
        """
        Setter для свойства Receipt.
        """
        self.__Receipt = ReceiptModel

    @property
    def DrinkDispenser(self):
        """
        Getter для свойства DrinkDispenser.
        """
        return self.__DrinkDispenser

    @DrinkDispenser.setter
    def DrinkDispenser(self, DrinkDispenser):
        """
        Setter для свойства DrinkDispenser.
        """
        self.__DrinkDispenser = DrinkDispenser

    def clean_RFID(self):
        """
        Очистка ресурсов RFID.
        """
        if self.__RFID is not None:
            self.__RFID.clean()

    def clean_Button(self):
        """
        Очистка ресурсов кнопки.
        """
        if self.__Button is not None:
            self.__Button.clean()

    def clean_Receipt(self):
        """
        Очистка ресурсов чека.
        """
        if self.__Receipt is not None:
            self.__Receipt.clean()

    def clean_DrinkDispenser(self):
        """
        Очистка ресурсов автомата с напитками.
        """
        if self.__DrinkDispenser is not None:
            self.__DrinkDispenser.clean()

    def clean_all(self):
        """
        Очистка всех ресурсов.
        """
        self.clean_RFID()
        self.clean_Button()
        self.clean_Receipt()
        self.clean_DrinkDispenser()

    def pin_extra_clean(self):
        """
        Дополнительная очистка пинов GPIO.
        """
        GPIO.setmode(GPIO.BOARD)
        for bpin, lpin, ppin in zip(Storage.button_pin, Storage.led_pin, Storage.pump_list):
            GPIO.cleanup(bpin)
            GPIO.cleanup(lpin)
            GPIO.cleanup(ppin)

    def clean(self):
        """
        Полная очистка всех свойств.
        """
        self.__Button = None
        self.__RFID = None
        self.__Receipt = None
        self.__DrinkDispenser = None



