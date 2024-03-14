class Log:
    
    __is_global_server_online = True
    
    __current_time_of_start = None
    __current_time_of_end = None
    
    
    __number_of_bottle = 0
    __check_id = 0
    __value_for_dispanser = ""
    __is_uid_valid = False
    
    __is_result_of_request_is_rfid_true = False
    __is_the_rfid_turn_on = False
    __uid = ""
    __start_time_of_rfid = 0
    __end_time_of_rfid = 0
    
    __is_the_button_led_turn_on = False
    __is_the_button_turn_on = False
    __number_of_button = 0
    __start_time_of_button = 0
    __end_time_of_button = 0
    
    __is_dispanser_turn_on = False
    __number_of_dispanser = 0
    __start_time_of_dispanser = 0
    __end_time_of_dispanser = 0
    
    __is_recipt_send_to_bd = False
    __is_recipt_full = False
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance

    @property
    def report(self):
        return {'is_global_server_online': self.__is_global_server_online, 
                'start_time': self.__current_time_of_start, 
                'end_time': self.__current_time_of_end, 
                'number_of_bottle': self.__number_of_bottle, 
                'check_id': self.__check_id, 
                'value_for_dispenser': self.__value_for_dispanser, 
                'is_uid_valid': self.__is_uid_valid, 
                'is_result_of_request_rfid_true': self.__is_result_of_request_is_rfid_true, 
                'is_the_rfid_turn_on': self.__is_the_rfid_turn_on, 
                'uid': self.__uid, 
                'start_time_of_rfid': self.__start_time_of_rfid, 
                'end_time_of_rfid': self.__end_time_of_rfid, 
                'is_the_button_led_turn_on': self.__is_the_button_led_turn_on, 
                'is_the_button_turn_on': self.__is_the_button_turn_on, 
                'number_of_button': self.__number_of_button, 
                'start_time_of_button': self.__start_time_of_button, 
                'end_time_of_button': self.__end_time_of_button, 
                'is_dispenser_turn_on': self.__is_dispanser_turn_on, 
                'number_of_dispenser': self.__number_of_dispanser, 
                'start_time_of_dispenser': self.__start_time_of_dispanser, 
                'end_time_of_dispenser': self.__end_time_of_dispanser, 
                'is_receipt_send_to_db': self.__is_recipt_send_to_bd,
                'is_receipt_full': self.__is_recipt_full}

    def reset(self):
        self.__is_global_server_online = True
        self.__current_time_of_start = None
        self.__current_time_of_end = None
        self.__number_of_bottle = 0
        self.__check_id = 0
        self.__value_for_dispanser = ""
        self.__is_uid_valid = False
        self.__is_result_of_request_is_rfid_true = False
        self.__is_the_rfid_turn_on = False
        self.__uid = ""
        self.__start_time_of_rfid = 0
        self.__end_time_of_rfid = 0
        self.__is_the_button_led_turn_on = False
        self.__is_the_button_turn_on = False
        self.__number_of_button = 0
        self.__start_time_of_button = 0
        self.__end_time_of_button = 0
        self.__is_dispanser_turn_on = False
        self.__number_of_dispanser = 0
        self.__start_time_of_dispanser = 0
        self.__end_time_of_dispanser = 0
        self.__is_recipt_send_to_bd = False
        self.__is_recipt_full = False
    
    @property
    def is_global_server_online(self):
        return self.__current_time_of_start

    @is_global_server_online.setter
    def is_global_server_online(self, value):
        self.__is_global_server_online = value
    
    @property
    def current_time_of_start(self):
        return self.__current_time_of_start

    @current_time_of_start.setter
    def current_time_of_start(self, value):
        self.__current_time_of_start = value

    @property
    def current_time_of_end(self):
        return self.__current_time_of_end

    @current_time_of_end.setter
    def current_time_of_end(self, value):
        self.__current_time_of_end = value

    @property
    def number_of_bottle(self):
        return self.__number_of_bottle

    @number_of_bottle.setter
    def number_of_bottle(self, value):
        self.__number_of_bottle = value

    @property
    def check_id(self):
        return self.__check_id

    @check_id.setter
    def check_id(self, value):
        self.__check_id = value

    @property
    def value_for_dispanser(self):
        return self.__value_for_dispanser

    @value_for_dispanser.setter
    def value_for_dispanser(self, value):
        self.__value_for_dispanser = value

    @property
    def is_uid_valid(self):
        return self.__is_uid_valid

    @is_uid_valid.setter
    def is_uid_valid(self, value):
        self.__is_uid_valid = value

    @property
    def is_result_of_request_is_rfid_true(self):
        return self.__is_result_of_request_is_rfid_true

    @is_result_of_request_is_rfid_true.setter
    def is_result_of_request_is_rfid_true(self, value):
        self.__is_result_of_request_is_rfid_true = value

    @property
    def is_the_rfid_turn_on(self):
        return self.__is_the_rfid_turn_on

    @is_the_rfid_turn_on.setter
    def is_the_rfid_turn_on(self, value):
        self.__is_the_rfid_turn_on = value

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, value):
        self.__uid = value

    @property
    def start_time_of_rfid(self):
        return self.__start_time_of_rfid

    @start_time_of_rfid.setter
    def start_time_of_rfid(self, value):
        self.__start_time_of_rfid = value

    @property
    def end_time_of_rfid(self):
        return self.__end_time_of_rfid

    @end_time_of_rfid.setter
    def end_time_of_rfid(self, value):
        self.__end_time_of_rfid = value

    @property
    def is_the_button_led_turn_on(self):
        return self.__is_the_button_led_turn_on

    @is_the_button_led_turn_on.setter
    def is_the_button_led_turn_on(self, value):
        self.__is_the_button_led_turn_on = value

    @property
    def is_the_button_turn_on(self):
        return self.__is_the_button_turn_on

    @is_the_button_turn_on.setter
    def is_the_button_turn_on(self, value):
        self.__is_the_button_turn_on = value

    @property
    def number_of_button(self):
        return self.__number_of_button

    @number_of_button.setter
    def number_of_button(self, value):
        self.__number_of_button = value

    @property
    def start_time_of_button(self):
        return self.__start_time_of_button
    
    @start_time_of_button.setter
    def start_time_of_button(self, value):
        self.__start_time_of_button = value

    @property
    def end_time_of_button(self):
        return self.__end_time_of_button

    @end_time_of_button.setter
    def end_time_of_button(self, value):
        self.__end_time_of_button = value

    @property
    def is_dispanser_turn_on(self):
        return self.__is_dispanser_turn_on

    @is_dispanser_turn_on.setter
    def is_dispanser_turn_on(self, value):
        self.__is_dispanser_turn_on = value

    @property
    def number_of_dispanser(self):
        return self.__number_of_dispanser

    @number_of_dispanser.setter
    def number_of_dispanser(self, value):
        self.__number_of_dispanser = value

    @property
    def start_time_of_dispanser(self):
        return self.__start_time_of_dispanser

    @start_time_of_dispanser.setter
    def start_time_of_dispanser(self, value):
        self.__start_time_of_dispanser = value

    @property
    def end_time_of_dispanser(self):
        return self.__end_time_of_dispanser

    @end_time_of_dispanser.setter
    def end_time_of_dispanser(self, value):
        self.__end_time_of_dispanser = value

    @property
    def is_recipt_send_to_bd(self):
        return self.__is_recipt_send_to_bd

    @is_recipt_send_to_bd.setter
    def is_recipt_send_to_bd(self, value):
        self.__is_recipt_send_to_bd = value

    @property
    def is_recipt_full(self):
        return self.__is_recipt_full

    @is_recipt_full.setter
    def is_recipt_full(self, value):
        self.__is_recipt_full = value
    
    