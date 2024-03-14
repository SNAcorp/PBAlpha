from storage.Storage import Storage
import datetime
import os
import json

class Logger:
    storage = Storage()
    __log_file =  storage.get_log_file_path

    def log(self, log_message: dict, file = __log_file):
        # with open(self.__log_file, 'a') as file:
        #     json.dump({self.__log_num: log_message}, file)
        #     file.write('\n')
        current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
        log_message['time'] = current_time
        if os.path.isfile(file):
            with open(file, 'r') as files:
                data = json.load(files)
            if len(data.keys()) != 0:
                data.update({max(map(int, data.keys())) + 1: log_message})
            
            else:
                data.update({"0": log_message})

            with open(file, 'w') as filer:
                json.dump(data, filer, indent=4)

        else:
            with open(file, 'w+') as file:
                json.dump({"0": log_message}, file, indent=4)

    def result_log(self, log_instance):
        log_msg = log_instance.report
        log_message = {'info': log_msg}
        self.log(log_message)

    def analyze_logs(self):
        six_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)
        logs = []
        with open(self.__log_file, 'r') as file:
            for line in file:
                log = json.loads(line)
                log_time_str = log['time']
                log_time = datetime.datetime.strptime(log_time_str, "%d.%m.%Y %H:%M:%S.%f")
                if log_time >= six_months_ago:
                    logs.append(log)
        with open(self.__log_file, 'w') as file:
            json.dump(logs, file)
