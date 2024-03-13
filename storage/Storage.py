class Storage:
    """ Пины подсветки кнопок """ 
    __button_pins_led = {1: 13, 2: 16, 3: 15, 4: 11}
    
    """ Пины для взимодействия с сигналом кнопок """
    __button_pins = {1: 31, 2: 33, 3: 32, 4: 29}
    
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
    
    """"""
    __path_to_log_file = "technical_information/log.json"

    __path_to_tech_file = "technical_information/terminal_info.json"

    __link_for_registration = "https://wine.mag.tc/api/terminals/register"

    __link_for_session_control = "https://wine.mag.tc"

    __path_to_system_file = "technical_information/system_info.json"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
        return cls.instance
    
    @property
    def get_log_file_path(self) -> str:
        """
        Возвращаем путь к файлу с логами
        """
        return self.__path_to_log_file

    @property
    def get_system_log_file_path(self):
        """
        Возвращаем путь к файлу с логами циклов перезапуска программы
        """
        return self.__path_to_system_file

    @property
    def get_link_for_registration(self) -> str:
        """
        Возвращаем ссылку на api регистрации в с системе
        """
        return self.__link_for_registration

    @property
    def get_link_for_session_control(self) -> str:
        """
        Возвращаем ссылку на api регистрации в с системе
        """
        return self.__link_for_session_control
    
    def get_volume(self, volume: str) -> int:
        """
        Возвращаем кол-во секунд для работы насоса
        """
        return self.__times_for_pumps.get(volume)
    @property
    def get_tech_file_path(self) -> str:
        """
        Возвращаем путь к файлу с технической информацией
        """
        return self.__path_to_tech_file
    
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
             