from storage.Storage import Storage
import requests


class SessionMonitor:
    def __init__(self):
        """Установка URL сервера"""
        self.server_url = Storage().get_link_for_session_control
        """ Инициализация переменной для хранения последнего состояния сессии """ 
        self.last_status = None
        
    def check_session_status(self):
        try:
            """ Отправка GET-запроса к серверу """
            response = requests.get(self.server_url)
            """ Отправка GET-запроса к серверу """
            if response.status_code == 200:
                return True
            else:
                """ Вывод сообщения об ошибке, если запрос неудачен """
                return response.status_code
                #print("Failed to fetch data from server. Status code:", response.status_code)
        except Exception as e:
            """ Вывод сообщения об ошибке, если произошла исключительная ситуация """
            print("An error occurred:", str(e))
            """ В случае ошибки возвращаем None """
            return None 

    def monitor_session(self):
        """ Бесконечный цикл для мониторинга состояния сессии """
        while True:
#             """ Получение текущего статуса сессии """
#             current_status = self.check_session_status()
#             """ Проверка наличия статуса сессии """
#             if current_status is not None:
#                 """ Обновление последнего известного статуса сессии"""
#                 self.last_status = current_status
#                 if self.last_status == False:
#                     
                     return True
#             """ Задержка перед следующей проверкой статуса сессии (5 секунд) """
#             time.sleep(5) 
