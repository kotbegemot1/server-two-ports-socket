# простейшая клиент-серверная системы
-------------------------
Присутствует одна сторонняя библиотека loguru.(Версия в файле requirements.txt)

#### 1. Сервер открывает два порта 8000 и 8001:  
  файл: server.py  
  команда: **python3 server.py**
  
#### 2. Клиент подключается к серверу к порту 8000, передает ему свой идентификатор и получает от сервера уникальный код.  
  файл: client.py  
  команда: **python3 client.py**  
  >В командной строке отобразится просьба ввести идентификатор. После введения идентификатора сервер пришлёт на клиент уникальный код.
  
#### 3. Клиент подключается к серверу к порту 8001 и передает произвольное текстовое сообщение, свой идентификатор и код, полученный на шаге 2.  
  файл: client1.py  
  команда: **python3 client1.py**  
  >В командной строке отобразится просьба ввести идентификатор, далее просьба ввести уникальный код, далее ввести сообщение. Если переданный клиентом код не соответствует его уникальному идентификатору сервер возвращает клиенту сообщение об ошибке "Вы ввели неправильный идентификатор или уникальный код",если код и идентификатор переданы правильно, сервер записывает полученное сообщение в лог файл(info.log).

### Тестировалось на linux(ubuntu)
