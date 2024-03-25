import time
from storage.Storage import Storage
import os
import json
import requests


class Swap:
    __storage = Storage()
    __file = __storage.get_swap_file_path
    __server = __storage.server_url

    def __init__(self):
        if os.path.isfile(self.__file):
            with open(self.__file, 'r') as files:
                data = json.load(files)
                for key in data.keys():
                    while True:
                        json1 = data[key]
                        response = requests.put(Storage().server_url, json=json1)
                        if response.status_code == 200:
                            break
                        else:
                            time.sleep(5)
                            continue
            os.remove(self.__file)
            
        else:
            pass
