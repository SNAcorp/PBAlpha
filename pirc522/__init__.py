from RFIDReader import RFIDReader
from ButtonReader import ButtonReader

if __name__ == "__init__":
    server_url = "http://example.com/api"
    rfid_reader = RFIDReader(server_url)
    rfid = rfid_reader.start_reading()
    check_id = rfid[0]
    if rfid_reader.start_reading()[1]:
        # После завершения считывания RFID метки начинаем считывание кнопок
        button_reader = ButtonReader(server_url, check_id)
        button_reader.setup()
        button_reader.wait_for_events()
