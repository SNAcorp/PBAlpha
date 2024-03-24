from storage.ReciptModel import Recipt
from storage.Storage import Storage
from modules.RFIDReader import RFIDReader
from modules.ButtonReader import ButtonReader
from services.Clean import ProgramExitManager
from services.Registration import TerminalRegistration
from services.Logger import Logger
from services.SessionLoader import SessionMonitor
from services.Log import Log
import datetime
import time
import threading

def Analyze_logs():
    formate_logs.analyze_logs()

def Monitor_starting():
    status = req.monitor_session()
    print("Serser status: ", status)
    if status == True:
        print("online")
    else:
        print("ofline")
        time.sleep(5)
                    
def Program_starting():
    try:
        while True:
            while True:
                rfid_reader = RFIDReader()
                exit_manager.rfid = rfid_reader

                rfid = rfid_reader.start_reading()
                if rfid:

                    recipt.start_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

                    """ 1. ID чека к которому прикрепить заказ
                    2. Номер выбранной бутылки
                    3. Объем, который необходимо налить"""
                    """ После завершения считывания RFID метки начинаем считывание кнопок """
                    bot = recipt.get_bottle_number
                    #                print(bot)
                    report.start_time_of_button = datetime.datetime.now().strftime("%H:%M:%S.%f")
                    button_reader = ButtonReader(storage.led_pin(bot),
                                                     storage.button_pin(bot))
                    report.number_of_button = bot
                    button_reader.setup()
                    button_reader.wait_for_events()
                    while 1:
                        time.sleep(1)
                        """Ждем конца работы насосов"""
                        if storage.result == True:
                            time.sleep(3)
                        break

                    """ Формируем модель чека и отправляем данные на сервер """
                    recipt.end_time = datetime.datetime.now().strftime("%H:%M:%S")
                    recipt.total_create
                    time.sleep(2)

                    report.current_time_of_end = datetime.datetime.now().strftime("%H:%M:%S.%f")
                    storage.set_result = False
            break

    except:

        raise "Ошибка в основной программе"

    finally:
        exit_manager.clean_all
        exit_manager.pin_extra_clean
        exit_manager.clean
        time_program_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
        formate_logs.log({'time_of_program_start': time_program_start,
                          'time_of_program_end': time_program_end},
                         storage.get_system_log_file_path)

        print("GOOD")

    formate_logs.result_log(report)       
        

if __name__ == "__main__":
    time_program_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
    
    registration = TerminalRegistration()
    req = SessionMonitor()
    
    storage = Storage()
    recipt = Recipt()
    exit_manager = ProgramExitManager()
    
    exit_manager.clean_all
    exit_manager.pin_extra_clean
    exit_manager.clean
    
    formate_logs = Logger()
    report = Log()

    # analyze_starting = threading.Thread(target=Analyze_logs())
    monitor_starting = threading.Thread(target=Monitor_starting)
    program_starting = threading.Thread(target=Program_starting)

    monitor_starting.start()

    # analyze_starting.start()
    # analyze_starting.join()

    while True:
        if monitor_starting == True:
            program_starting.start()
            program_starting.join()
        else:
            time.sleep(5)









