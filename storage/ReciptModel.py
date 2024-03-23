from storage.Storage import Storage
from services.Logger import Logger
from services.Log import Log
import requests
import time


class Recipt:
    logger = Logger()
    storage = Storage()
    log = Log()
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

    """Счетчик заполнености чека"""
    _count = 0

    """Сколько должно быть заполнено полей"""
    _result_count = sum(1 for attr in vars() if attr.startswith('_')) - 3

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
        self._count += 1
        self._start_time = str(time)

    @property
    def number_of_bottle(self):
        """ Getter для получения номера выбранной бутылки """
        return self._final_number_of_bottle

    @number_of_bottle.setter
    def number_of_bottle(self, value):
        """ Setter для номера выбранной бутылки """
        self._count += 1
        self._final_number_of_bottle = value

    @property
    def end_time(self):
        """ Getter для получения времени окончания обслуживания """
        return self._end_time

    @end_time.setter
    def end_time(self, time):
        """ Setter для времени окончания обслуживания """
        self._count += 1
        self._end_time = str(time)

    @property
    def volume(self):
        """ Getter для получения времени работы насоса """
        return self._final_volume

    @volume.setter
    def volume(self, value: str):
        """ Setter для времени работы насоса """
        self._count += 1
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
        self._count += 1
        self._final_order_id = value

    @property
    def uid(self):
        """ Getter для получения UID """
        return self._final_uid

    @uid.setter
    def uid(self, value: str):
        """ Setter для UID """
        self._count += 1
        self._final_uid = value

    @property
    def clean(self):
        """ Функция для очистки всех полей временного хранилища """
        self._final_order_id = ""

        self._start_time = ""
        self._end_time = ""

        self._final_volume = ""
        self._final_number_of_bottle = -1

        self._final_uid = ""

        self._count = 0

    @property
    def total_create(self):
        if self._count == self._result_count:
            self.log.is_recipt_full = True

        """ Формирование модели """
        json1 = {"uid": self._final_uid,
                 "state":{
                 "order_id": self._final_order_id,
                 "start_time": self._start_time,
                 "end_time": self._end_time,
                 "volume": self._final_volume,
                 "name_of_bottle": self.storage.get_vine_name(self._final_number_of_bottle)}}

        response = requests.put(Storage().server_url, json=json1)
        """ Проверяем успешно ли ушли данные """
        if response.status_code == 200:
            """Все успешно отправлено"""
            self.log.is_recipt_send_to_bd = True
            self.clean
            return 1
        else:
            """Произошла ошибка при отправке"""
            time.sleep(5)
            """ Повторная попытка отправки данных """
            response = requests.put(Storage().server_url, json=json1)
            if response.status_code == 200:
                """Все успешно отправлено"""
                self.log.is_recipt_send_to_bd = True
                self.clean
                return 1
            else:
                """Сервер не принимает наши данные"""
                self.log.is_recipt_send_fail = True
                """Записываем данные в файл swap'a.
                    Считаем что сервер оффлайн и уходим в режим ожидания"""
                self.logger.log(json1, self.storage.get_swap_file_path)
                self.log.is_recipt_write_to_swap = True
                self.clean
                return 0

