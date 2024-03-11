[![SWUbanner](https://github.com/vshymanskyy/StandWithUkraine/blob/main/badges/StandWithUkraine.svg)](http://stand-with-ukraine.pp.ua/)
[![SWUbanner](https://github.com/vshymanskyy/StandWithUkraine/blob/main/badges/RussianWarship.svg)](http://stand-with-ukraine.pp.ua/)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.github.com/v00g100skr/3834111d448e497c81a139b69756835c/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)


Репозиторій містить файли прошивки JAAM. JAAM це прошивка для ESP32, що дозволяє за допомогою розміщених на мапі України адресних світлодіодів відображати таку інформацію: повітряні тривоги, погода, візуальні зображення накшталт прапору України. Крім цього, є окремий диспей, який може відображати потончий час, погоду та сервісні повідомлення.

<img src="https://github.com/v00g100skr/ukraine_alarm_map/blob/master/img/map-alerts.jpg" width="400"/><img src="https://github.com/v00g100skr/ukraine_alarm_map/blob/master/img/map-weather.jpg" width="400"/><img src="https://github.com/v00g100skr/ukraine_alarm_map/blob/master/img/map-flag.jpg" width="400"/>



Вітаю Вас в репозіторії проєкту JAAM - Just another alerts map :-)

<img src="https://github.com/v00g100skr/ukraine_alarm_map/blob/master/img/front-full.png" width="600"/>


[WIKI по прошивці](https://github.com/v00g100skr/ukraine_alarm_map/wiki)

[Багтрекер](https://github.com/v00g100skr/ukraine_alarm_map/issues)

[Питання та пропозиції](https://github.com/v00g100skr/ukraine_alarm_map/discussions)

-->> [ТЕЛЕГРАМ КАНАЛ ПРОЕКТУ](https://t.me/jaam_project) <<--

-->> [ПОРТАЛ ДАНИХ](http://alerts.net.ua) <<--

Прошивка використовує бібліотеку **_NeoPixelBus_** (останню версію брати [тут](https://github.com/Makuna/NeoPixelBus))

Прошивка використовує _**async**_ в роботі, що дозволяє запускати декілька процесів одночасно і швидше реагувати на зміни

Прошивка використовує _**власний сервер даних**_ [alerts.net.ua](http://alerts.net.ua/) для отримування даних про тривоги і погоду

Прошивка використовує _**Websockets**_ для коннекта з сервером даних, що дозволяє майже миттєво отримувати оновлення даних

### Прошивка має такі можливості: 
 - режим відображення повітряних тривог на базі офіційного API https://www.ukrainealarm.com/
 - режим відображення погоди за даними сайту https://openweathermap.org/
 - режим прапора України
 - режим випадкових кольорів
 - режим лампи
 - режим offline - мапа не відображає нічого

### Для отримання даних не треба мати ключі для API тривог або openweathermap - все вже є в нашому API

Мапа може бути обладнана _**дисплеєм**_ (128 * 32 SSD1306 та 128 * 64 SSD1306). 

### Режим дисплея вмикається окремо через налаштування:
 - поточний час
 - погода
 - технічна інформація мапи
 - дані з датчика температури і вологості
 - також є сервісні сповіщення при старті мапи, при проблемних ситуаціях з мапою та процессі перемикання режимів

### Мапа має _**вбудований web-сервер**_ 
для керування налаштуваннями. Сторінка керування знаходиться за адресою [alarmmap.local](http://alarmmap.local) (або по IP). Також доступна сервісна сторінка  [alarmmap.local:8080](http://alarmmap.local:8080), де можна змініти WiFi налаштуванння, перезавантажити мапу або перепрошити, якшо у вас є готовий зібраний файл прошивки і ви не хочете використовувати Arduino IDE

### Всі _**налаштування зберігаються у внутрішній пам'яті**_
Відновлюються після перезавантаження та після перепрошивки мапи (якшо не вказувати примусове очищення) 

### Мапа інтегрується в сервіс _**home assistant**_ 
HA бачить мапу як окремий прилад розумного будинку і має можливість керувати мапою

### Мапа може бути обладнана _**сенсорною кнопкою**_ ttp223 (на платі jaam кнопка вже є)
Є підтримка довгого натиснення на кнопку - можна встановити додатковий режим
Кнопка дозволяє перемикати всі наявні режими в мапі: 
 - саму мапу (тривога, погода, прапор, лампа, вимкнено)
 - дисплей (годинник, погода, тех. інформація, мікроклімат (при наявності датчика температури/вологості), вимкнено)

Список можливих дій на кнопці:
 - "Вимкнено"
 - "Перемикання режимів мапи"
 - "Перемикання режимів дисплея"
 - "Увімк./Вимк. мапу"
 - "Увімк./Вимк. дисплей"
 - "Увімк./Вимк. мапу та дисплей"
 - "Увімк./Вимк. нічний режим"
 - "Перезавантаження пристрою" (доступно тількі для довгого натискання)

### Мапа підтримує певний рівень кастомізацій:
 - загальна яскравість
 - яскравість на основі часу (нічний режим зі зниженою яскравістю)
 - яскравість на основі даних датчика освітлення (якщо встановлений, підтримується аналоговий фоторезистор та цифровий датчик BH1750)
 - можливість окремого світлодіода для Києва, або замість Київської області, чи обидна одночасно (дана кастомізація потребує окремого світлодіода в позиції 8 перед Київською областю, загальна довжина стрічкі збільшиться з 25 до 26 світлодіодів). Також є комбінований режим "Київ-Киівська область" для одного діода, що показує тривогу якщо вона є в Києві або області
 - можливість підсвічування нових тривог та відбоїв тривог певний час іншим кольором
 - можливість окремо і незалежно виставити яскравість різних зон тривог відносно одна одної
 - можливість окремо і незалежно виставити кольори різних зон тривог відносно одна одної
 - можливість окремо і незалежно виставити колір домашнього регіону
 - в налаштуваннях можна увімкнути та вимкнути звукове сповіщення (при наявності динаміка "buzzer") для різних подій, як-от початок та скасування тривоги, запуск мапи, щогодинні сповіщення, звуки в режимі "Хвилина мовчання"
 - є змога обрати канал розповсюдження нових версій прошивки PRODUCTION (стабільні прошивки, що готові для щоденного користування), або BETA (прошивки доступні одразу після додавання нових функцій, можуть містити помилки та виводити мапу з ладу, використовувати обережно!)

### Для плати jaam окремо є функціонал сервісних світлодіодів на задній панелі:
 - наявність живлення
 - підключення до WiFi
 - підключення до сервера даних
 - підключення до home assistant

### Мапа може оновлювати прошивку через веб інтерфейс, або кнопкою, якщо нова прошивка доступна


[![CodeQL](https://github.com/v00g100skr/ukraine_alarm_map/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/v00g100skr/ukraine_alarm_map/actions/workflows/github-code-scanning/codeql)

[![GitHub version](https://img.shields.io/github/release/v00g100skr/ukraine_alarm_map.svg)](https://github.com/v00g100skr/ukraine_alarm_map/releases/latest)
[![GitHub commits](https://img.shields.io/github/commit-activity/t/v00g100skr/ukraine_alarm_map.svg)](https://github.com/v00g100skr/ukraine_alarm_map/commits/master)
[![GitHub issues](https://img.shields.io/github/issues/v00g100skr/ukraine_alarm_map.svg)](https://github.com/v00g100skr/ukraine_alarm_map/issues)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.github.com/v00g100skr/3834111d448e497c81a139b69756835c/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)


[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://vshymanskyy.github.io/StandWithUkraine)




