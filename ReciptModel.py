from Storage import Storage
class Recipt:
    """ID Заказа """
    _final_order_id = ''
    
    """Время начала обслуживания """
    _start_time = ''
    """ Время окончания """
    _end_time = ''
    
    """ Время работы насоса """
    _final_volume = ''
    """Номер бутылки """
    _final_number_of_bottle = -1
    
    """UID"""
    _final_uid = ''
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Recipt, cls).__new__(cls)
        return cls.instance
    
    @property
    def get_bottle_number(self) -> int:
        """ Getter для получения номера выбранной бутылки """
        return self._final_number_of_bottle
    
    @property
    def get_volume(self) -> str:
        """ Getter для получения времени работы насоса """
        return self._final_volume
    
    @property
    def start_time(self):
        """ Getter для получения времени начала обслуживания """
        return self._start_time
    
    @start_time.setter
    def start_time(self, time):
        """ Setter для времени начала обслуживания """
        self._start_time = str(time)
        
    @property
    def number_of_bottle(self):
        """ Getter для получения номера выбранной бутылки """
        return self._final_number_of_bottle
    
    @number_of_bottle.setter
    def number_of_bottle(self, value):
        """ Setter для номера выбранной бутылки """
        self._final_number_of_bottle = value    
        
    @property
    def end_time(self):
        """ Getter для получения времени окончания обслуживания """
        return self._end_time
    
    @end_time.setter
    def end_time(self, time):
        """ Setter для времени окончания обслуживания """
        self._end_time = str(time)
    
    @property
    def volume(self):
        """ Getter для получения времени работы насоса """
        return self._final_volume
    
    @volume.setter
    def volume(self, value: str):
        """ Setter для времени работы насоса """
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self._final_volume = value
    
    @property
    def order_id(self):
        """ Getter для получения ID заказа """
        return self._final_order_id
    
    @order_id.setter
    def order_id(self, value: str):
        """  Setter для id заказа """
        self._final_order_id = value
        
    @property
    def uid(self):
        """ Getter для получения UID """
        return self._final_uid
  
    @uid.setter
    def uid(self, value: str):
        """ Setter для UID """
        self._final_uid = value
    
    
    @property
    def __clean(self):
        """ Функция для очистки всех полей временного хранилища """
        self._fianl_order_id = ""
    
        self._start_time = ""
        self._end_time = ""
        
        self._fianl_volume = ""
        self._fianl_number_of_bottle = -1
        
        self.fianl_uid = ""
    
    @property
    def total_create(self):
        """ Формирование модели """
        response = requests.post(Storage().server_url, json={"order_id": self._fianl_order_id,
                                                             "uid": self._fianl_uid,
                                                             "start_time": self._start_time,
                                                             "end_time": self._end_time,
                                                             "volume": self._fianl_volume,
                                                             "name_of_bottle": Storage().get_vine_name(self._final_number_of_bottle)})
        """ Проверяем успешно ли ушли данные """
        if response.status_code == 200:
            print("Все успешно отправлено")
            return 1
        else:
            print("Произошла ошибка при отправке")
            """ Здесь планируется долписать метод сохранения модели с повторной отправкой """
            return 0
#         print({"order_id": self._final_order_id, "uid": self._final_uid, "start_time": self._start_time,
#                "end_time": self._end_time,"volume": self._final_volume,
#                "name_of_bottle": Storage().get_vine_name(self._final_number_of_bottle)})
        self.__clean
        