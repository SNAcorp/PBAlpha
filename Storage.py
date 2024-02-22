class Storage:
    """ Пины подсветки кнопок """ 
    __button_pins_led = {1: 16, 2: 13, 3: 15, 4: 11}
    
    """ Пины для взимодействия с сигналом кнопок """
    __button_pins = {1: 33, 2: 31, 3: 32, 4: 29}
    
    """ Пины для управления насосами (диспенсером) """
    __pump_pins = {1: 36, 2: 38, 3: 40, 4: 37}
    
    """ Пины насосов в формате списка """
    __pump_pins_list = [36, 38, 40, 37]
    
    """ Словарь для установки времени работы насоса """
    __times_for_pumps = {'full_cup': 9, 'test_cup': 3}
    
    """ Результат работы программы """
    result_of_program = False

    """ Словарь с наименованиями вин """
    __names_of_vine = {1: "1 Vine", 2: "2 Vine", 3: "3 Vine", 4: "4 Vine"}
    
    """"""
    __server_url = "https://example.com/api"
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
        return cls.instance
    
    def get_volume(self, volume: str) -> int:
        """
        Возвращаем кол-во секунд для работы насоса
        """
        return self.__times_for_pumps.get(volume)
    
    
    def get_dispander_pin(self, number_of_bottle: int) -> int:
        """
        Возвращаем номер пина нужного нам насоса
        """
        return self.__pump_pins.get(number_of_bottle)
    
    def led_pin(self, number_of_button: int) -> int:
        """
        ID нужного нам пина подстветки по номеру кнопки (по раскладке BOARD) 
        """
        print(self.__button_pins_led.get(number_of_button))
        return self.__button_pins_led.get(number_of_button)
    
    def button_pin(self, number_of_button: int) -> int:
        """
        ID пина по номеру кнопки
        """
        return self.__button_pins.get(number_of_button)
    
    def pump_list(self) -> list:
        """
        Возвращаем список пинов всех насосов
        """
        return self.__pump_pins_list
    
    @property
    def result(self) -> bool:
        """
        Резултат работы одного цикла программы
        """
        return self.result_of_program
    
    @result.setter
    def result(self, value: bool):
        """
        Изменение промежуточного результата
        """
        self.result_of_program = value
    
        
    def get_vine_name(self, bottle_number) -> str:
        """
        Получение наименования вина для формирования модели чека
        """
        return self.__names_of_vine.get(bottle_number)
    
    
    
    @property
    @staticmethod
    def server_url(self) -> str:
        """
        Получение ссылки на сервер
        """
        return self.__server_url
    