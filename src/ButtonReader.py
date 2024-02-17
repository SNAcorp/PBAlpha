
import requests
import RPi.GPIO as GPIO

class ButtonReader:
    BUTTON_PINS = [1, 2, 3, 4]
    drinks = {1: "Franch Vine", 2: "Russian Vine", 3: "Italaian Vine", 4: "Other Vine"}
    __check_id = ""
    __order = ""

    def __init__(self, server_url, check_id):
        self.run = True
        self.server_url = server_url
        self.__check_id = check_id

    @property
    def check_id(self):
        return self.__check_id

    @property
    def order(self):
        return self.__order

    @check_id.setter
    def check_id(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")

        self.__check_id = value.strip()

    def button_callback(self, pin):
        #print(f"Button {pin} pressed")
        # Отправляем информацию о нажатой кнопке на сервер
        response = requests.post(self.server_url, json={'id': self.check_id,'vendor_code': self.drinks[pin]})
        if response.status_code == 200:
            #print(f"Button {pin} sent to server successfully.")
            self.__order = self.drinks[pin]
            return 1
        else:
            #print(f"Failed to send button {pin} to server.")
            return 0

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.BUTTON_PINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: self.button_callback(pin), bouncetime=200)

    def wait_for_events(self):
        #print("Starting button reading")
        try:
            while self.run:
                pass
        except Exception:
            print("Error in Button event")
        finally:
            GPIO.cleanup()