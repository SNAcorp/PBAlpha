from storage.Storage import Storage
import datetime
import os
import json


class Logger:
    storage = Storage()
    __log_file = storage.get_log_file_path

    """Метод для записи сообщения в журнал"""
    def log(self, log_message: dict, file=__log_file):
        """Получение текущего времени"""
        current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")

        """Добавление времени к сообщению в журнале"""
        log_message['time'] = current_time

        """Проверка существования файла"""
        if os.path.isfile(file):
            with open(file, 'r') as files:
                data = json.load(files)

            if len(data.keys()) != 0:
                """Обновление данных в файле"""
                data.update({max(map(int, data.keys())) + 1: log_message})

            else:
                """Добавление первой записи, если файл пуст"""
                data.update({"0": log_message})

            with open(file, 'w') as filer:
                json.dump(data, filer, indent=4)  # Запись данных в формате JSON с отступами

        else:
            """ Если файл не существует. Создание нового файла"""
            with open(file, 'w+') as file:

                """Запись первой записи в новый файл"""
                json.dump({"0": log_message}, file, indent=4)

    def result_log(self, log_instance):
        """Получение экземпляра класса log, и вызов свойства report для получения полного отчета"""
        log_msg = log_instance.report

        """Создание словаря с информацией о результате"""
        log_message = {'info': log_msg}
        self.log(log_message)

    def analyze_logs(self):
        """Расчет даты шести месяцев назад"""
        six_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)

        """Список для хранения журнальных записей"""
        logs = []
        with open(self.__log_file, 'r') as file:
            for line in file:
                log = json.loads(line)
                log_time_str = log['time']
                log_time = datetime.datetime.strptime(log_time_str, "%d.%m.%Y %H:%M:%S.%f")
                if log_time >= six_months_ago:  # Проверка, была ли запись сделана не позже чем шесть месяцев назад
                    logs.append(log)  # Добавление записи в список
        with open(self.__log_file, 'w') as file:  # Открытие файла журнала на запись
            json.dump(logs, file)  # Запись анализированных данных в файл
