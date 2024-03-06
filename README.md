# Проект BPAlpha

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

## Краткое описание класса `RFIDUtil`

`RFIDUtil` - класс для управления операциями с RFID.

### Инициализация

Конструктор принимает объект RFID и инициализирует переменные для управления RFID тегом.

### Методы

- `block_addr(sector, block)`: Вычисляет адрес блока по заданным сектору и блоку.
- `sector_string(block_address)`: Возвращает строку, представляющую сектор и блок блока по его адресу.
- `set_tag(uid)`: Устанавливает тег для дальнейших операций, вызывает `deauth()` при уже установленном теге.
- `auth(auth_method, key)`: Устанавливает информацию аутентификации для текущего тега.
- `deauth()`: Сбрасывает информацию аутентификации, останавливает криптографию, если RFID в режиме аутентификации.
- `is_tag_set_auth()`: Проверяет, установлен ли тег и предоставлена ли информация аутентификации.
- `do_auth(block_address, force=False)`: Вызывает `card_auth()` с сохраненной информацией аутентификации при необходимости.
- `write_trailer(sector, key_a, auth_bits, user_data, key_b)`: Записывает секторный трейлер заданного сектора, требуется установленный тег и аутентификация.
- `rewrite(block_address, new_bytes)`: Перезаписывает блок новыми данными, сохраняя старые, если передан None, требуется установленный тег и аутентификация.
- `read_out(block_address)`: Выводит номер сектора/блока и содержимое блока, требуется установленный тег и аутентификация.
- `get_access_bits(c1, c2, c3)`: Вычисляет биты доступа для секторного трейлера на основе условий доступа.
- `dump(sectors=16)`: Читает и выводит содержимое блока для заданного количества секторов.

## Класс `RFIDReader`

###Этот код содержит класс `RFIDReader`, предназначенный для чтения RFID меток и отправки данных на сервер для проверки доступа.

### Методы класса

- **`__init__(self)`**: Инициализирует объект класса, устанавливает свойства и начальные параметры.
- **`end_read(self, signal, frame)`**: Функция для корректного завершения чтения RFID меток.
- **`send_to_server(self, uid)`**: Отправляет UID метки на сервер для проверки доступа. Возвращает ответ сервера в виде JSON.
- **`start_reading(self)`**: Основная функция для считывания RFID меток. Ожидает метку, отправляет её UID на сервер для проверки доступа. Если доступ разрешен, передает данные в модель `Recipt`. Возвращает `True` если доступ разрешен, иначе `False`.

### Вспомогательные методы и свойства

- **`signal`**: Сигнал для корректного завершения чтения.
- **`frame`**: Фрейм для корректного завершения чтения.
- **`run`**: Переменная для управления циклом чтения меток.
- **`rdr`**: Объект для работы с RFID считывателем.
- **`util`**: Утилита для работы с RFID.
- **`server_url`**: URL сервера для отправки запроса с UID метки.


## Файл __init__

###Данный код выполняет операции считывания RFID меток и управления насосами для наливки напитков. Вот пошаговое описание его функциональности:

1. **Импорт необходимых модулей и классов**: Код начинается с импорта классов `Recipt`, `Storage`, `RFIDReader`, `ButtonReader` и модуля `RPi.GPIO`.

2. **Инициализация экземпляров классов**: Создаются экземпляры классов `Storage` и `Recipt`.

3. **Основной цикл**: Бесконечный цикл `while True`, который выполняется постоянно.

4. **Вложенный цикл для считывания RFID меток**: Внутренний цикл `while True` выполняется до тех пор, пока не будет считана RFID метка. После этого начинается операция наливки напитка.

5. **Запуск таймера**: После считывания RFID метки запускается таймер для отслеживания времени начала операции.

6. **Считывание номера выбранной бутылки**: Получается номер выбранной бутылки с помощью метода `get_bottle_number` из объекта `recipt`.

7. **Инициализация считывателя кнопок**: Создается экземпляр класса `ButtonReader` с указанием пинов для светодиода и кнопки налива соответствующей бутылки. Затем вызывается метод `setup()` для настройки считывателя кнопок, и метод `wait_for_events()` для ожидания событий.

8. **Ожидание завершения налива**: После нажатия кнопки налива начинается ожидание завершения налива напитка с помощью переменной `storage.result`.

9. **Формирование и отправка данных на сервер**: По завершении налива напитка, останавливается таймер, формируется модель чека и данные отправляются на сервер.

10. **Сброс результатов**: Переменная `storage.set_result` устанавливается в `False` для подготовки к новой операции считывания RFID метки.

    

## Класс `ButtonReader`

###Этот файл содержит класс `ButtonReader`, который отвечает за считывание нажатия кнопки и управление насосами для наливки напитков.

- **`__init__(self, led_pin: int, button_pin: int)`**: Конструктор класса инициализирует переменные для пина светодиода и пина кнопки.

- **`button_callback(self, pin: int) -> bool`**: Метод, вызываемый при нажатии кнопки. Создает экземпляр класса `DrinkDispenser` для управления насосами, ждет завершения налива, а затем выключает подсветку и завершает работу.

- **`setup(self)`**: Метод настройки пинов взаимодействия с кнопкой и подсветкой.

- **`wait_for_events(self)`**: Метод ожидания нажатия кнопки. Выполняет бесконечный цикл, в котором проверяет состояние кнопки и вызывает `button_callback` при нажатии.

  

## Класс `DrinkDispenser`

###Этот файл содержит класс `DrinkDispenser`, который отвечает за управление насосами для налива напитков.

- **`res`**: Статическая переменная, отвечающая за цикл проверки нажатия кнопки.

- **`__init__(self)`**: Конструктор класса инициализирует экземпляры классов `Recipt` и `Storage`, а также определяет номер выбранной бутылки, порцию вина и пин для насоса.

- **`result(self)`**: Метод для передачи флага об окончании работы класса.

- **`dispense_drink(self, index, duration)`**: Основная функция класса, отвечающая за налив напитка. Включает насос на указанном пине на заданное время, затем выключает насос, устанавливает флаг окончания работы класса и устанавливает флаг для всех классов. 

- **`run(self)`**: Метод для запуска основной функции класса. Вызывает метод `dispense_drink` с номером бутылки и порцией вина. В случае возникновения исключения, выводит сообщение о завершении программы и очищает настройки GPIO.



## Класс `Recipt`

###Этот код содержит класс `Recipt`, предназначенный для формирования модели чека и отправки данных на сервер.

### Переменные класса

- **`_final_order_id`**: ID заказа.
- **`_start_time`**: Время начала обслуживания.
- **`_end_time`**: Время окончания обслуживания.
- **`_final_volume`**: Время работы насоса.
- **`_final_number_of_bottle`**: Номер выбранной бутылки.
- **`_final_uid`**: UID.

### Методы класса

- **`__new__(cls)`**: Создает единственный экземпляр класса для обеспечения синглтона.
- **`get_bottle_number`**: Getter для получения номера выбранной бутылки.
- **`get_volume`**: Getter для получения времени работы насоса.
- **`start_time`**: Getter/Setter для времени начала обслуживания.
- **`number_of_bottle`**: Getter/Setter для номера выбранной бутылки.
- **`end_time`**: Getter/Setter для времени окончания обслуживания.
- **`volume`**: Getter/Setter для времени работы насоса.
- **`order_id`**: Getter/Setter для ID заказа.
- **`uid`**: Getter/Setter для UID.
- **`__clean`**: Метод для очистки всех полей временного хранилища.
- **`total_create`**: Метод для формирования модели чека и отправки данных на сервер. Возвращает 1 в случае успешной отправки и 0 в случае ошибки.



## Класс `Storage`

###Этот код содержит класс `Storage`, который предназначен для хранения данных и настроек, таких как пины GPIO, время работы насоса, результат работы программы и другие.

### Переменные класса

- **`__button_pins_led`**: Словарь с пинами подсветки кнопок.
- **`__button_pins`**: Словарь с пинами для взаимодействия с кнопками.
- **`__pump_pins`**: Словарь с пинами для управления насосами (диспенсером).
- **`__pump_pins_list`**: Список пинов насосов.
- **`__times_for_pumps`**: Словарь с временем работы насоса для различных режимов.
- **`result_of_program`**: Результат работы программы.
- **`__names_of_vine`**: Словарь с наименованиями вин.
- **`__server_url`**: URL сервера.

### Методы класса

- **`__new__(cls)`**: Создает единственный экземпляр класса для обеспечения синглтона.
- **`get_volume(volume: str) -> int`**: Возвращает количество секунд для работы насоса по переданному режиму.
- **`get_dispander_pin(number_of_bottle: int) -> int`**: Возвращает номер пина нужного насоса.
- **`led_pin(number_of_button: int) -> int`**: Возвращает ID пина подсветки кнопки по номеру кнопки.
- **`button_pin(number_of_button: int) -> int`**: Возвращает ID пина по номеру кнопки.
- **`pump_list() -> list`**: Возвращает список пинов всех насосов.
- **`result(value: bool)`**: Метод для изменения промежуточного результата.
- **`get_vine_name(bottle_number) -> str`**: Получает наименование вина для формирования модели чека.
- **`server_url()`**: Получение ссылки на сервер.



## Класс `SessionMonitor`

### Описание
`SessionMonitor` представляет собой класс, предназначенный для мониторинга состояния сессии на удаленном сервере.

### Атрибуты
- `server_url`: строка, URL сервера, к которому производится запрос для проверки состояния сессии.
- `last_status`: переменная, хранящая последнее известное состояние сессии.

### Методы
1. `__init__(self, server_url)`: конструктор класса, инициализирует атрибут `server_url` и устанавливает `last_status` в `None`.
   
2. `check_session_status(self) -> bool`: метод для проверки состояния сессии. Отправляет GET-запрос к серверу, получает данные в формате JSON и извлекает статус сессии. Возвращает `True`, если сессия активна, и `False` в противном случае. Если произошла ошибка во время запроса или обработки данных, возвращает `None`.

3. `monitor_session(self) -> bool`: метод для мониторинга состояния сессии. В бесконечном цикле вызывает `check_session_status`, обновляет `last_status` и проверяет, если сессия неактивна (`last_status == False`), то возвращает `False`. Перед каждой проверкой статуса сессии делается задержка в 5 секунд.

### Использование
```python
# Создание экземпляра класса SessionMonitor
monitor = SessionMonitor("http://example.com/session")

# Мониторинг состояния сессии
if not monitor.monitor_session():
    print("Сессия неактивна.")
```

### Зависимости
- `requests`: используется для отправки HTTP-запросов.
- `time`: используется для задержки между проверками состояния сессии.


## Версия
Текущая версия проекта: 0.1.1
