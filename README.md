# Проект RFID Python

Этот проект представляет собой набор Python скриптов и классов для работы с RFID считывателем на Raspberry Pi.

## Установка

Для использования этого проекта вам понадобится Raspberry Pi с установленной ОС Raspbian или подобной, а также RFID считыватель, подключенный к вашему Raspberry Pi.

1. Сначала убедитесь, что у вас установлен Python 3.x на вашем Raspberry Pi.

2. Установите необходимые зависимости с помощью pip:

```bash
pip install spidev RPi.GPIO
git clone https://github.com/your_username/rfid_project.git
```
## Использование

### 1. Код модуля RFID
Код модуля RFID состоит из трех файлов: rfid.py, rfid_util.py и __init__.py.

rfid.py: Этот файл содержит основной класс RFID, который предоставляет методы для работы с RFID считывателем, такими как инициализация, аутентификация, чтение и запись данных с карт.
rfid_util.py: Этот файл содержит класс RFIDUtil, который предоставляет удобные методы для работы с RFID тегами, такие как аутентификация, запись и чтение данных из блоков.
__init__.py: Этот файл используется для объединения модулей в пакет.

### 2. Пример использования
Приведенный ниже код демонстрирует пример использования модуля RFID для считывания и записи данных с RFID тегов:

```python
import signal
import time
import sys

from rfid.rfid import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\n Ctrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        print("Setting tag")
        util.set_tag(uid)
        print("\nAuthorizing")
        util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
        util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        print("\nReading")
        util.read_out(4)
        print("\nDeauthorizing")
        util.deauth()

        time.sleep(1)
```

Этот код инициализирует RFID считыватель, ожидает считывания тега, а затем аутентифицирует, читает и деаутентифицирует данные на блоке 4 RFID тега.

## Методы

### В модуле RFID (rfid.py):
  1. RFID.wait_for_tag(timeout=0): Ожидает считывания RFID тега.
  2. RFID.request(): Отправляет запрос на считывание тега.
  3. RFID.anticoll(): Обнаруживает идентификатор тега.
  4. RFID.auth(auth_mode, key, uid): Аутентифицирует использование указанного адреса блока.
  5. RFID.read(block_address): Считывает данные из указанного блока.
  6. RFID.write(block_address, data): Записывает данные в указанный блок.
  7. RFID.cleanup(): Очищает GPIO и завершает работу с RFID.
  8. В модуле RFIDUtil (rfid_util.py):
  9. RFIDUtil.set_tag(uid): Устанавливает тег для дальнейших операций.
  10. RFIDUtil.auth(auth_method, key): Устанавливает информацию аутентификации для текущего тега.
  11. RFIDUtil.deauth(): Сбрасывает информацию аутентификации.
  12. RFIDUtil.read_out(block_address): Печатает содержимое блока с указанным адресом.
  13. RFIDUtil.write_trailer(sector, key_a, auth_bits, user_data, key_b): Записывает трейлер указанного сектора.
  14. RFIDUtil.rewrite(block_address, new_bytes): Перезаписывает блок новыми байтами.
  15. RFIDUtil.get_access_bits(c1, c2, c3): Вычисляет биты доступа для трейлера сектора.
  16. RFIDUtil.dump(sectors): Выводит содержимое всех блоков указанного количества секторов.

## Версия
Текущая версия проекта: 0.1.0
