# Документация проекта PBAlpha

Добро пожаловать в документацию проекта! Здесь вы найдете подробное описание структуры проекта, его компонентов и функциональности. Проект представляет собой программное обеспечение, разработанное для управления автоматизированным диспенсером напитков с использованием различных модулей, сервисов и технических средств.

Структура проекта организована в несколько директорий и файлов, каждый из которых выполняет определенную роль в функционировании системы. В документации предоставлено подробное описание каждого компонента, а также инструкции по его использованию и взаимодействию с другими частями проекта.

Мы надеемся, что данная документация поможет вам лучше понять функциональность проекта и успешно использовать его в ваших задачах. Если у вас возникнут вопросы или замечания, не стесняйтесь обращаться к разработчикам.

Приступим к рассмотрению каждого компонента проекта подробнее.

# <a id="content">Содержание</a>

- [Иерархия файлов проетка](#files_structures) /
  * [Вид иерархии проекта](#hierarchy)
- [Главная функция " init.py "](#init)
- [Рассмотрение компонентов проекта](#components) /
  * [ButtonReader.py](#button)
  * [DrinkDispenser.py](#dispenser)
  * [RFIDReader.py](#rfid_reader)
- [Services](#service) /
  * [Clean.py](#clean)
  * [Log.py](#log_file)
  * [Logger.py](#logger)
  * [Registration.py](#registration)
  * [SessionLoader.py](#sessionloader)
- [Storage](#storage) /
  * [ReciptModel.py](#recipt)
  * [Storage.py](#storage)
- [Создание файлов в директории " technical_information "](#technical_info) /
  * [Первый запуск программы](#first_start)
  * [Дальнейшее использование файлов](#using_files)
- [Завершение проекта](#end)



# <a id="files_structures">Файловое строение проекта</a>

Проект организован в виде иерархии директорий и файлов, обеспечивающих модульность, читаемость и удобство разработки. В центре структуры находится главный исполнительный класс программы, расположенный в файле `__init__.py`. Внутри этой директории размещены все компоненты, необходимые для функционирования программы.

Для лучшей организации проекта используются три основные директории:

1. **modules**: Здесь содержатся модули, отвечающие за взаимодействие с различными аппаратными компонентами, такими как считыватели кнопок, диспенсеры напитков и считыватели RFID.

2. **services**: В этой директории находятся служебные модули, предназначенные для обработки данных, ведения журналов, регистрации и других сервисных функций.

3. **storage**: Здесь располагаются модели данных и инструменты для работы с хранилищем информации.

Кроме того, проект содержит вспомогательную директорию `pirc522`, которая представляет собой пакет для работы с RFID-считывателем.

И, наконец, директория `technical_information` содержит техническую информацию, такую как логи выполнения программы, информацию о регистрации терминала и времени включения и выключения системы.

Эта структура проекта обеспечивает четкое разделение функциональности, что упрощает разработку, отладку и поддержку проекта. Далее мы рассмотрим каждую директорию и ее содержимое более подробно.

##<a id="hierarchy">Вид иерархии проекта:</a>

[Возврат к содержанию](#content)

- modules/
  - ButtonReader.py
  - DrinkDispanser.py
  - RFIDReader.py

- services/
  - Clean.py
  - Log.py
  - Logger.py
  - Registration.py
  - SessionLoader.py

- storage/
  - ReciptModel.py
  - Storage.py

- pirc522/
  - rfid.py
  - util.py

- technical_information/
  - log.json
  - terminal_info.json
  - system_info.json
  - swap.json

- \_\_init\_\_.py

# <a id="init">Главная функция "__init__.py"</a>

[Возврат к содержанию](#content)

Эта функция является центральной точкой нашего приложения. Она выполняет инициализацию и управление основными компонентами, а также контролирует основной поток программы.

### Импорты:
- `from storage.ReciptModel import Recipt`: Импорт класса `Recipt` из модуля `ReciptModel`, который отвечает за создание временного хранилища данных (чек).
- `from storage.Storage import Storage`: Импорт класса `Storage` из модуля `Storage`, который содержит основные параметры и методы для взаимодействия с хранилищем данных.
- `from modules.RFIDReader import RFIDReader`: Импорт класса `RFIDReader` из модуля `RFIDReader`, отвечающего за считывание RFID меток.
- `from modules.ButtonReader import ButtonReader`: Импорт класса `ButtonReader` из модуля `ButtonReader`, который обрабатывает нажатия кнопок.
- `from services.Clean import ProgramExitManager`: Импорт класса `ProgramExitManager` из модуля `Clean`, который управляет очисткой ресурсов и завершением программы.
- `from services.Registration import TerminalRegistration`: Импорт класса `TerminalRegistration` из модуля `Registration`, который регистрирует терминал на сервере.
- `from services.Logger import Logger`: Импорт класса `Logger` из модуля `Logger`, отвечающего за ведение логов.
- `from services.SessionLoader import SessionMonitor`: Импорт класса `SessionMonitor` из модуля `SessionLoader`, который мониторит состояние сессии.
- `from services.Log import Log`: Импорт класса `Log` из модуля `Log`, который формирует логи программы.

### Функции и переменные:
- `analyze_logs()`: Функция для анализа логов, вызывает метод `analyze_logs` у экземпляра `formate_logs`.
- `time_program_start`: Переменная, содержащая время начала выполнения программы.
- `registration`: Экземпляр класса `TerminalRegistration`, отвечающий за регистрацию терминала на сервере.
- `req`: Экземпляр класса `SessionMonitor`, мониторящий состояние сессии.
- `storage`: Экземпляр класса `Storage`, предоставляющий основные методы для работы с хранилищем данных.
- `recipt`: Экземпляр класса `Recipt`, предоставляющий временное хранилище данных (чек).
- `exit_manager`: Экземпляр класса `ProgramExitManager`, управляющий завершением программы и очисткой ресурсов.
- `formate_logs`: Экземпляр класса `Logger`, отвечающего за форматирование логов.
- `report`: Экземпляр класса `Log`, формирующий логи программы.
- `storage.server_url = registration.terminal_id`: Эта строка кода устанавливает URL сервера, используемый для взаимодействия программы с сервером, путем присвоения переменной `storage.server_url` значения идентификатора терминала, полученного из регистрационных данных из файла, в частности, идентификатора терминала. Таким образом, данная операция позволяет программе настроить связь с сервером на основе данных, считанных из файла регистрации.

### Основной блок кода:
- Основной цикл программы, который выполняется бесконечно, пока программа не завершится или не произойдет ошибка.
- Внутренний цикл, в котором осуществляется мониторинг состояния сессии и считывание RFID меток.
- Обработка нажатий кнопок и формирование чека.
- Завершение работы программы и очистка ресурсов.
- Запись логов и времени выполнения программы.

### Обработка ошибок и завершение:
- Обработка исключений с выводом сообщения о возникшей ошибке.
- Завершение программы с очисткой ресурсов и записью времени выполнения программы.



#<a id="components">Рассмотрение компонентов проекта</a>

[Возврат к содержанию](#content)

После обзора общей структуры проекта мы перейдем к более детальному рассмотрению каждого компонента. Для каждой директории мы приведем список файлов с кратким описанием их функциональности. Далее мы рассмотрим каждый файл подробно, описывая его назначение, структуру и примеры использования.

Цель этого раздела - предоставить полное понимание работы проекта и его компонентов, а также помочь вам успешно внедрить его в ваши задачи. Начнем с рассмотрения модулей, затем перейдем к служебным сервисам и инструментам хранения данных, и закончим с вспомогательными файлами, содержащими техническую информацию.

Далее приступим к подробному рассмотрению каждого файла в проекте.

## <a id="button">ButtonReader.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `ButtonReader`, предназначенный для управления кнопкой на Raspberry Pi.

### Назначение

Класс `ButtonReader` реализует функционал считывания нажатия кнопки и управления подсветкой. Он предоставляет методы для настройки взаимодействия с кнопкой, ожидания нажатия и выполнения определенных действий при его обнаружении.

### Импорты

- `Log`: Класс для ведения журнала событий.
- `DrinkDispenser`: Класс для управления диспенсером напитков.
- `ProgramExitManager`: Класс для управления завершением программы.
- `RPi.GPIO`: Библиотека для взаимодействия с GPIO на Raspberry Pi.
- `time`: Модуль для работы со временем.
- `datetime`: Модуль для работы с датой и временем.

### Методы

#### def \_\_init\_\_()

Конструктор класса `ButtonReader`, инициализирует объект.

---

#### def button_callback()

Метод, вызываемый при нажатии кнопки. Инициирует запуск диспенсера напитков и ожидает завершения его работы.

---

#### def setup()

Метод для настройки пинов GPIO для взаимодействия с кнопкой и подсветкой.

---

#### def wait_for_events()

Метод, ожидающий нажатия кнопки и вызывающий метод `button_callback` при обнаружении события.

---

#### def clean()

Метод для завершения работы программы и освобождения ресурсов GPIO.

## <a id="dispenser">DrinkDispenser.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `DrinkDispenser`, отвечающий за управление диспенсером напитков.

### Назначение

Класс `DrinkDispenser` реализует функционал управления диспенсером напитков. Он предоставляет методы для инициализации диспенсера, выдачи напитка определенного объема и завершения его работы.

### Импорты

- `Storage`: Класс для работы с хранилищем данных.
- `Recipt`: Класс модели чека.
- `Log`: Класс для ведения журнала событий.
- `time`: Модуль для работы со временем.
- `datetime`: Модуль для работы с датой и временем.
- `RPi.GPIO`: Библиотека для взаимодействия с GPIO на Raspberry Pi.

### Методы

#### def \_\_init\_\_()

Конструктор класса `DrinkDispenser`, инициализирует объект и настраивает пин насоса.

---

#### def result()

Метод для передачи флага об окончании работы класса.

---

#### def dispense_drink()

Основной метод класса, предназначенный для выдачи напитка определенного объема. Включает насос на заданное время, затем выключает его.

---

#### def clean()

Метод для завершения работы программы и освобождения ресурсов GPIO.

---

#### def run()

Метод для запуска основной функции выдачи напитка с заданным объемом.

## <a id="rfid_reader">RFIDReader.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `RFIDReader`, предназначенный для работы с считывателем RFID на Raspberry Pi.

### Назначение

Класс `RFIDReader` реализует функционал считывания меток RFID и отправки их на сервер для проверки. Он предоставляет методы для начала чтения меток, обработки полученных данных и отправки запроса на сервер для проверки валидности метки.

### Импорты

- `RFID`: Класс для работы с считывателем RFID.
- `Log`: Класс для ведения журнала событий.
- `Storage`: Класс для работы с хранилищем данных.
- `Recipt`: Класс модели чека.
- `signal`: Модуль для обработки сигналов.
- `sys`: Модуль для работы с системными функциями.
- `datetime`: Модуль для работы с датой и временем.

### Методы

#### def \_\_init\_\_()

Конструктор класса `RFIDReader`, инициализирует объект и настраивает считыватель RFID.

---

#### def clean()

Метод для корректного завершения работы чтения меток.

---

#### def reformat_uid()

Метод для преобразования UID из списка в строку.

---

#### def send_to_server()

Метод для отправки UID метки на сервер для проверки валидности.

---

#### def start_reading()

Метод для начала чтения меток. Ожидает появления метки, отправляет ее на сервер и обрабатывает результат.

### Пример ответа от сервера (json)
```json
{
    "order_id": "10",
    "access_granted": true,
    "volume": "test_cup",
    "number_of_bottle": 4
}
```

#<a id="service">Services</a>

[Возврат к содержанию](#content)

Продолжая наше рассмотрение файлов в директории services, мы сосредоточимся на компонентах, отвечающих за выполнение различных служебных функций в приложении. В этой директории могут находиться файлы, реализующие логирование, управление сеансами, взаимодействие с внешними сервисами и другие служебные задачи. Давайте начнем анализ собранных файлов в этой директории, начиная с файла ```SessionLoader.py```.

## <a id="clean">Clean.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `ProgramExitManager`, отвечающий за корректное завершение программы и освобождение ресурсов.

### Назначение

Класс `ProgramExitManager` предоставляет методы для освобождения ресурсов и завершения работы всех компонентов программы при выходе из программы. Он обеспечивает правильное завершение работы считывателя кнопки, считывателя RFID, модели чека и диспенсера напитков, а также освобождение GPIO-пинов.

### Импорты

- `Storage`: Класс для работы с хранилищем данных.

### Методы

#### def \_\_new\_\_()

Метод для реализации синглтона - создает только один экземпляр класса.

---

#### def Button()

Свойство для получения и установки считывателя кнопки.

---

#### def rfid()

Свойство для получения и установки считывателя RFID.

---

#### def recipt()

Свойство для получения и установки модели чека.

---

#### def drink_dispenser()

Свойство для получения и установки диспенсера напитков.

---

#### def clean_rfid()

Метод для корректного завершения работы считывателя RFID.

---

#### def clean_button()

Метод для корректного завершения работы считывателя кнопки.

---

#### def clean_recipt()

Метод для корректного завершения работы модели чека.

---

#### def clean_drinkdispanser()

Метод для корректного завершения работы диспенсера напитков.

---

#### def clean_all()

Метод для корректного завершения работы всех компонентов.

---

#### def pin_extra_clean()

Метод для освобождения GPIO-пинов.

---

#### def clean()

Метод для сброса всех компонентов и очистки объекта.


## <a id="log_file">Log.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `Log`, предназначенный для ведения журнала событий программы.

### Назначение

Файл Log.py играет важную роль в программе, собирая данные о состоянии сервера, времени работы программы, операциях с бутылками, диспенсером, кнопками и считывателем RFID, а также о состоянии отправки чека в базу данных. Эти данные собираются из различных компонентов программы и позволяют эффективно отслеживать работу приложения, контролировать его производительность и обеспечивать надежность работы системы.


### Методы/Свойства

#### def \_\_new\_\_()

Метод для реализации синглтона - создает только один экземпляр класса.

#### reset()

Метод для сброса всех параметров журнала.



### Свойства:

#### report

Свойство для получения текущего отчета о состоянии журнала.

---

#### is_global_server_online

Свойство для установки/получения состояния глобального сервера.

---

#### current_time_of_start

Свойство для установки/получения текущего времени начала работы программы.

---

#### current_time_of_end

Свойство для установки/получения текущего времени завершения работы программы.

---

#### number_of_bottle

Свойство для установки/получения номера бутылки.

---

#### check_id

Свойство для установки/получения ID чека.

---

#### value_for_dispanser

Свойство для установки/получения значения для диспенсера.

---

#### is_uid_valid

Свойство для установки/получения состояния валидности UID.

---

#### is_result_of_request_is_rfid_true

Свойство для установки/получения результата запроса к RFID.

---

#### is_the_rfid_turn_on

Свойство для установки/получения состояния считывателя RFID.

---

#### uid

Свойство для установки/получения UID.

---

#### start_time_of_rfid

Свойство для установки/получения времени начала работы считывателя RFID.

---

#### end_time_of_rfid

Свойство для установки/получения времени завершения работы считывателя RFID.

---

#### is_the_button_led_turn_on

Свойство для установки/получения состояния светодиода кнопки.

---

#### is_the_button_turn_on

Свойство для установки/получения состояния кнопки.

---

#### number_of_button

Свойство для установки/получения номера кнопки.

---

#### start_time_of_button

Свойство для установки/получения времени начала работы кнопки.

---

#### end_time_of_button

Свойство для установки/получения времени завершения работы кнопки.

---

#### is_dispanser_turn_on

Свойство для установки/получения состояния диспенсера.

---

#### number_of_dispanser

Свойство для установки/получения номера диспенсера.

---

#### start_time_of_dispanser

Свойство для установки/получения времени начала работы диспенсера.

---

#### end_time_of_dispanser

Свойство для установки/получения времени завершения работы диспенсера.

---

#### is_receipt_send_to_bd

Свойство для установки/получения состояния отправки чека в базу данных.

---

#### is_receipt_send_fail

Свойство для установки/получения состояния неудачной отправки чека.

---

#### is_receipt_write_to_swap

Свойство для установки/получения состояния записи чека во временное хранилище.

---

#### is_receipt_full

Свойство для установки/получения состояния заполненности чека.

## <a id="logger">Logger.py</a>

[Возврат к содержанию](#content)

Данный файл содержит класс `Logger`, предназначенный для ведения журнала событий программы в виде JSON-файла.

### Назначение

Класс `Logger` предоставляет функционал для записи информации о событиях программы в виде JSON-файла, а также анализа и обработки этих журналов.



### Методы

#### log(log_message: dict, file = __log_file)

* Метод для записи сообщения в журнал. Принимает на вход словарь `log_message` с данными о событии и опциональный аргумент `file` для указания файла журнала.

#### result_log(log_instance)

* Метод для записи информации из экземпляра класса `Log` в журнал.

#### analyze_logs()

* Метод для анализа и обработки журналов. Удаляет записи старше шести месяцев из файла журнала.


### Атрибуты

#### storage

* Атрибут, содержащий экземпляр класса `Storage`.

#### __log_file

* Приватный атрибут, содержащий путь к файлу журнала по умолчанию.

## <a id="registration">Registration.py</a>

[Возврат к содержанию](#content)

В данном файле представлен класс `TerminalRegistration`, который используется для регистрации терминала и получения его идентификатора и имени.

### Назначение

Класс `TerminalRegistration` предоставляет функционал для регистрации терминала в системе и сохранения его идентификатора и имени в локальном файле.



### Методы

#### \_\_init\_\_():

* Конструктор класса. Инициализирует путь к файлу для хранения информации о терминале и ссылку для регистрации, а также загружает информацию о терминале или регистрирует его, если информация отсутствует.

#### \_\_load_terminal_info():

* Приватный метод для загрузки информации о терминале из локального файла. Если файл не существует, вызывает метод регистрации терминала.

#### \_\_register_terminal():

* Приватный метод для регистрации терминала в системе. Посылает запрос на сервер и сохраняет полученный идентификатор и имя терминала в локальном файле.

#### \_\_save_terminal_id(terminal_id, terminal_name):

* Приватный метод для сохранения идентификатора и имени терминала в локальном файле.


### Свойства

#### terminal_id:

* Свойство для доступа к идентификатору зарегистрированного терминала.

#### terminal_name:

* Свойство для доступа к имени зарегистрированного терминала.

## <a id="sessionloader">SessionLoader.py</a>

[Возврат к содержанию](#content)

В данном файле представлен класс `SessionMonitor`, который отвечает за мониторинг состояния сессии на сервере.

### Назначение

Класс `SessionMonitor` предоставляет функционал для проверки состояния сессии на сервере и мониторинга этого состояния.



### Методы

#### \_\_init\_\_():

* Конструктор класса. Устанавливает URL сервера и инициализирует переменную для хранения последнего состояния сессии.

#### check_session_status():

* Метод для проверки состояния сессии на сервере. Отправляет GET-запрос к серверу и возвращает `True` в случае успешного получения данных или код состояния ответа в случае неудачи.

#### monitor_session():

* Метод для бесконечного мониторинга состояния сессии на сервере. Выполняет цикл, в котором вызывает метод `check_session_status()`, обновляет последнее известное состояние сессии и возвращает `True` при обнаружении изменения состояния.

### Атрибуты

#### server_url:

* URL сервера для проверки состояния сессии.

#### last_status:

* Переменная для хранения последнего известного состояния сессии.


# <a id="storage">Storage</a>

[Возврат к содержанию](#content)

Перейдя к файлам в директории storage, мы сосредоточимся на компонентах, отвечающих за хранение и управление данными в приложении. Данные компоненты играют важную роль в обеспечении доступа к различным ресурсам, таким как файлы, конфигурационные данные, ссылки и т. д. Давайте начнем анализ собранных файлов в этой директории, начиная с файла "ReciptModel.py".

## <a id="recipt">ReciptModel.py</a>

[Возврат к содержанию](#content)

В данном файле представлен класс `Recipt`, который представляет временное хранилище данных (чек).

### Назначение

Класс `Recipt` предназначен для временного хранения данных о заказе, таких как ID заказа, время начала и окончания обслуживания, объем напитка, номер бутылки и UID. Также класс предоставляет методы для получения и установки значений этих данных, а также для очистки временного хранилища.



### Импорт
```python
from storage.Storage import Storage
from services.Logger import Logger
from services.Log import Log
import requests
import time
```

### Поля класса

- `logger`: экземпляр класса Logger для логирования событий.
- `storage`: экземпляр класса Storage для доступа к хранилищу данных.
- `log`: экземпляр класса Log для записи логов.
- `_final_order_id`: ID заказа (по умолчанию пустая строка).
- `_start_time`: время начала обслуживания (по умолчанию пустая строка).
- `_end_time`: время окончания обслуживания (по умолчанию пустая строка).
- `_final_volume`: объем насоса (по умолчанию пустая строка).
- `_final_number_of_bottle`: номер бутылки (по умолчанию -1).
- `_final_uid`: UID (по умолчанию пустая строка).
- `_count`: счетчик заполненности чека (по умолчанию 0).
- `_result_count`: количество полей, которые должны быть заполнены (рассчитывается при инициализации).


### Методы

#### \_\_init\_\_():
* Конструктор класса. Инициализирует переменные и получает экземпляр класса `Logger` и `Storage`.

#### clean:
* Метод для очистки всех полей временного хранилища.

#### total_create:
* Метод для формирования модели заказа и сохранения её. Пока закомментирована отправка данных на сервер.

### Свойства:

### get_bottle_number:
Getter для получения номера выбранной бутылки.

---

### get_volume:
Getter для получения времени работы насоса.

---

### start_time:
Getter и setter для времени начала обслуживания.

---

### end_time:
Getter и setter для времени окончания обслуживания.

---

### volume:
Getter и setter для времени работы насоса.

---

### order_id:
Getter и setter для ID заказа.

---

### uid:
Getter и setter для UID.

---

### def total_create():

Этот метод формирует модель чека и отправляет её на сервер. Он выполняет следующие шаги:

1. Проверяет, все ли необходимые поля чека заполнены. Если нет, то метод завершается без отправки данных на сервер.

2. Формирует JSON-объект `json1` с информацией о чеке, включая `uid`, `order_id`, `start_time`, `end_time`, `volume` и название выбранной бутылки.

3. Отправляет запрос на сервер методом `requests.put()`, передавая URL сервера и JSON-объект.

4. Проверяет ответ сервера. Если ответ успешный (код 200), то устанавливает флаг `is_recipt_send_to_bd` объекта `log` в `True`, выполняет очистку всех полей чека и возвращает `1`.

5. Если ответ не успешный, ожидает 5 секунд (чтобы снизить нагрузку на сервер) и повторно отправляет запрос на сервер.

6. Если вторая попытка также не увенчалась успехом, то записывает данные чека в файл "swap" для дальнейшей обработки, устанавливает флаг `is_recipt_write_to_swap` объекта `log` в `True`, выполняет очистку всех полей чека и возвращает `0`.

Таким образом, метод `total_create()` обеспечивает отправку данных чека на сервер с учетом возможных ошибок при обмене данными.

---

### Атрибуты

#### logger
* Экземпляр класса `Logger` для ведения логирования.

#### storage
* Экземпляр класса `Storage` для работы с хранилищем.


## <a id="storage">Рассмотрение файла "Storage.py"</a>

[Возврат к содержанию](#content)

В файле "Storage.py" содержится класс `Storage`, предоставляющий доступ к различным константам, путям к файлам и функциям, связанным с хранением данных и взаимодействием с внешними сервисами. Давайте подробнее изучим каждый из его элементов:

1. **Константы для пинов различных компонентов**:
    * `__button_pins_led`: Словарь с пинами подсветки кнопок.
    * `__button_pins`: Словарь с пинами для взаимодействия с кнопками.
    * `__pump_pins`: Словарь с пинами для управления насосами.
    * `__pump_pins_list`: Список пинов насосов.
    

2. **Словари и константы для времени работы насоса и других данных**:
    * `__times_for_pumps`: Словарь для установки времени работы насоса.
    * `__names_of_vine`: Словарь с наименованиями вин.
    * `__server_url`: URL сервера.
    * Пути к различным файлам:
        * `__path_to_log_file`: Путь к файлу с логами.
        * `__path_to_statistics_file`: Путь к файлу со статистическими данными.
        * `__path_to_swap_file`: Путь к файлу для обмена данными.
        * `__path_to_system_file`: Путь к файлу с логами циклов перезапуска программы.
        * `__path_to_tech_file`: Путь к файлу с технической информацией.
    * `__link_for_registration`: Ссылка на API регистрации в системе.
    * `__link_for_session_control`: Ссылка на API управления сессией.


3. **Методы для получения путей к файлам и других данных**:
    * `get_log_file_path()`: Возвращает путь к файлу с логами.
    * `get_statistics_file_path()`: Возвращает путь к файлу со статистическими данными.
    * `get_swap_file_path()`: Возвращает путь к файлу swap.
    * `get_system_log_file_path()`: Возвращает путь к файлу с логами циклов перезапуска программы.
    * `get_link_for_registration()`: Возвращает ссылку на API регистрации в системе.
    * `get_link_for_session_control()`: Возвращает ссылку на API управления сессией.
    * `get_tech_file_path()`: Возвращает путь к файлу с технической информацией.


4. **Методы для получения информации о компонентах**:
    * `get_volume(volume: str)`: Возвращает количество секунд для работы насоса по типу объема.
    * `get_dispander_pin(number_of_bottle: int)`: Возвращает номер пина нужного насоса по номеру бутылки.
    * `led_pin(number_of_button: int)`: Возвращает ID пина подсветки по номеру кнопки.
    * `button_pin(number_of_button: int)`: Возвращает ID пина кнопки по номеру.
    * `pump_list()`: Возвращает список пинов всех насосов.
    * `get_vine_name(bottle_number)`: Возвращает наименование вина для формирования чека по номеру бутылки.


5. **Методы для управления результатом работы программы**:
    * `result`: Получение результата работы одного цикла программы.
    * `result.setter`: Изменение промежуточного результата.


6. **Статический метод**:
    * `server_url()`: Получение ссылки на сервер.

Этот класс предоставляет удобный доступ к различным константам, путям и функциям, необходимым для работы программы. Он является важным компонентом системы хранения данных и конфигураций.

# <a id="technical_info">Создание файлов в директории `technical_information`</a>

Директория technical_information представляет собой место хранения различных файлов, необходимых для работы программы. 

## <a id="first_start">Первый запуск программы</a>

При первом запуске программы создается директория `technical_information`.

### `terminal_info.json`

В этом файле содержатся регистрационные данные программы. Он создается при первом запуске программы и заполняется данными о программе.

---

### `system_info.json`

Файл содержит информацию о времени работы полного цикла программы, такую как время запуска программы и время её завершения. 
Этот файл создается при первом завершении программы и пересоздается, если файл будет случайно удален.

---

### `swap.json`

В случае, если заказ был сделан, а сервер отключился, информация сохраняется в этом файле для последующей отправки, когда сервер станет онлайн. 
Файл создается автоматически при первом использовании.

---

### `log.json`

Этот файл содержит внутреннюю информацию о процессах и включении внутренних компонентов программы (логи программы). 
Создается автоматически при первом использовании.


## <a id="using_files">Дальнейшее использование файлов</a>

После создания файлов они используются для записи соответствующей информации в процессе работы программы. Если файлы уже существуют, они будут использоваться для записи и чтения данных.


# <a id="end">Завершение проекта</a>

[Возврат к содержанию](#content)

Поздравляем! Вы завершили документацию нашего проекта. Мы надеемся, что данная документация была полезной для понимания структуры, функциональности и особенностей нашего программного продукта.

Если у вас возникнут дополнительные вопросы или требуется помощь, не стесняйтесь обращаться к разработчикам или консультантам.

Благодарим вас за интерес к нашему проекту и желаем успехов в его использовании!

>С уважением,
>**S.N.A. corp**.


