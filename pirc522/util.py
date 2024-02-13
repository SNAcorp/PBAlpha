
class RFIDUtil(object):
    rfid = None
    method = None
    key = None
    uid = None
    last_auth = None

    debug = False

    def __init__(self, rfid):
        self.rfid = rfid

    def block_addr(self, sector, block):
        """
        Возвращает адрес блока спецификации. блок в спец. сектор.
        """
        return sector * 4 + block

    def sector_string(self, block_address):
        """
        Возвращает сектор и его блочное представление адреса блока, например.
        S01B03 для прицепа во втором секторе.
        """
        return "S" + str((block_address - (block_address % 4)) / 4) + "B" + str(block_address % 4)

    def set_tag(self, uid):
        """
        Устанавливает тег для дальнейших операций.
        Вызывает deauth(), если карта уже установлена.
        Вызывает RFID select_tag().
        Возвращает вызванное состояние ошибки select_tag().
        """
        if self.debug:
            print("Selecting UID " + str(uid))

        if self.uid != None:
            self.deauth()

        self.uid = uid
        return self.rfid.select_tag(uid)

    def auth(self, auth_method, key):
        """
        Устанавливает информацию аутентификации для текущего тега
        """
        self.method = auth_method
        self.key = key

        if self.debug:
            print("Изменение используемого ключа аутентификации на " + str(key) + " используя метод " + ("A" if auth_method == self.rfid.auth_a else "B"))

    def deauth(self):
        """
        Сбрасывает информацию аутентификации. Вызывает stop_crypto(),
        если RFID находится в состоянии аутентификации
        """
        self.method = None
        self.key = None
        self.last_auth = None

        if self.debug:
            print("Изменение ключа и метода аутентификации на None")

        if self.rfid.authed:
            self.rfid.stop_crypto()
            if self.debug:
                print("Остановка crypto1")

    def is_tag_set_auth(self):
        return (self.uid != None) and (self.key != None) and (self.method != None)

    def do_auth(self, block_address, force=False):
        """
        При необходимости вызывает RFID card_auth() с сохраненной информацией аутентификации.
        Возвращает состояние ошибки из вызова метода.
        """
        auth_data = (block_address, self.method, self.key, self.uid)
        if (self.last_auth != auth_data) or force:
            if self.debug:
                print("Вызов card_auth по UID " + str(self.uid))

            self.last_auth = auth_data
            return self.rfid.card_auth(self.method, block_address, self.key, self.uid)
        else:
            if self.debug:
                print("Не вызываю card_auth - уже авторизован")
            return False

    def write_trailer(self, sector, key_a=(0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF), auth_bits=(0xFF, 0x07, 0x80), 
                      user_data=0x69, key_b=(0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF)):
        """
        Записывает трейлер указанного сектора.
        Тег и авторизация должны быть установлены - авторизация выполняется.
        Если значение равно None, значение байта сохраняется.
        Возвращает состояние ошибки.
        """
        addr = self.block_addr(sector, 3)
        return self.rewrite(addr, key_a[:6] + auth_bits[:3] + (user_data, ) + key_b[:6])

    def rewrite(self, block_address, new_bytes):
        """
        Перезаписывает блок новыми байтами, сохраняя старые, если не передано None.
        Тег и авторизация должны быть установлены - авторизация выполняется.
        Возвращает состояние ошибки.
        """
        if not self.is_tag_set_auth():
            return True

        error = self.do_auth(block_address)
        if not error:
            (error, data) = self.rfid.read(block_address)
            if not error:
                for i in range(len(new_bytes)):
                    if new_bytes[i] != None:
                        if self.debug:
                            print("Изменение позиции " + str(i) + " с текущим значением " + str(data[i]) + " к " + str(new_bytes[i]))

                        data[i] = new_bytes[i]

                error = self.rfid.write(block_address, data)
                if self.debug:
                    print("Запись " + str(data) + " на " + self.sector_string(block_address))

        return error

    def read_out(self, block_address):
        """
        Печатает номер сектора/блока и содержимое блока.
        Тег и авторизация должны быть установлены - авторизация выполняется.
        """
        if not self.is_tag_set_auth():
            return True

        error = self.do_auth(block_address)
        if not error:
            (error, data) = self.rfid.read(block_address)
            print(self.sector_string(block_address) + ": " + str(data))
        else:
            print("Error on " + self.sector_string(block_address))

    def get_access_bits(self, c1, c2, c3):
        """
        Вычисляет биты доступа для трейлера сектора на основе условий доступа к ним.
        c1, c2, c3, c4 — это кортежи из 4 элементов, содержащие значения для каждого блока.
        возвращает 3 байта для трейлера сектора
        """
        byte_6 = ((~c2[3] & 1) << 7) + ((~c2[2] & 1) << 6) + ((~c2[1] & 1) << 5) + ((~c2[0] & 1) << 4) + \
                 ((~c1[3] & 1) << 3) + ((~c1[2] & 1) << 2) + ((~c1[1] & 1) << 1) + (~c1[0] & 1)
        byte_7 = ((c1[3] & 1) << 7) + ((c1[2] & 1) << 6) + ((c1[1] & 1) << 5) + ((c1[0] & 1) << 4) + \
                 ((~c3[3] & 1) << 3) + ((~c3[2] & 1) << 2) + ((~c3[1] & 1) << 1) + (~c3[0] & 1)
        byte_8 = ((c3[3] & 1) << 7) + ((c3[2] & 1) << 6) + ((c3[1] & 1) << 5) + ((c3[0] & 1) << 4) + \
                 ((c2[3] & 1) << 3) + ((c2[2] & 1) << 2) + ((c2[1] & 1) << 1) + (c2[0] & 1)
        return byte_6, byte_7, byte_8

    def dump(self, sectors=16):
        for i in range(sectors * 4):
            self.read_out(i)
