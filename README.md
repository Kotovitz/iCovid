## iCovid - засіб візуалізації поширення вірусу SARS-nCov-2
#### v0.9.8rc

Засіб для отримання зведених даних щодо поширення вірусу SARS-nCov-2 в Україні та інших країнах світу.
Присутній функціонал для генерування та оновлення мережевої сторінки.

_Вигляд інтерфейсу у командному рядку._

![Зображення командного рядка](v0_9_8rc_cli.png?raw=true "Вигляд даних з консолі")

_Вигляд інтерфейсу на мережевому ресурсі._

![Зображення мережового ресурсу](v0_9_8rc_web.png?raw=true "Вигляд даних у мережі")

##### Принцип роботи

* Скрипт аналізує перелік мережевих сторінок, що містять інформацію про поширення вірусу в тій чи іншії країні,
або певному регіоні.
* Отримані дані зберігаються в форматі JSON у тій самій папці, що й скрипт.
* Як результат виконання, скрипт виконає виведення даних у термінал.

> За наявності додаткового параметру, скрипт згенерує мережеву сторінку для відображення ортиманих даних у
> зручнішому вигляді. Додатково скрипт може вивантажити згенеровану сторінку на мережевий сервер.


##### Командний інтерфейс
Запуск скрипта виконується командою терміналу:
```sh
./icovid.py
```

Генерування веб-сторінки та її вивантаження ініціюється вказанням прапорця:
```sh
./icovid.py [--web_update | -w]
```

Для отримання додаткової інформації слід увімкнути режим зневадження:
```sh
./icovid.py [--debug | -d]
```
