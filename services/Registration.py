from storage.Storage import Storage
import requests
import json
import os
import time


class TerminalRegistration:
    def __init__(self):
        self.path = Storage().get_tech_file_path
        self.link = Storage().get_link_for_registration
        self.__info = {}
        self.__info['terminal_id'], self.__info['terminal_name'] = self.__load_terminal_info()

    def __load_terminal_info(self):
        # Проверяем, существует ли файл с ID терминала
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                terminal_info = json.load(file)
                return terminal_info["id"], terminal_info["name"]
        else:
            return self.__register_terminal()

    def __register_terminal(self):
        while True:
            response = requests.put(self.link)
            if response.status_code == 200:
                terminal_name = response.json()['terminal']['name']
                terminal_id = response.json()['terminal']['id']
                self.__save_terminal_id(terminal_id, terminal_name)
                self.__terminal_id = terminal_id
                return terminal_id, terminal_name
            else:
                time.sleep(2)

    def __save_terminal_id(self, terminal_id, terminal_name):
        with open(self.path, 'w+') as file:
            json.dump({"id": terminal_id, "name": terminal_name}, file)
    
    @property
    def terminal_id(self):
        return self.__info['terminal_id']
    
    @property
    def terminal_name(self):
        return self.__info['terminal_name']