
# Сайт "Куда пойти?"

Учебный проект для курсов web-разработчиков [dvmn](https://dvmn.org).  
Cайт можно посетить, если нажать [сюда](http://137.184.45.165).
Админ-панель для заполнения сайта находится [по этому адресу](http://137.184.45.165/admin/)


## Установка
Понадобится установленный Python 3.8+ и git.

Клонируем репозиторий:
```bash
git@github.com:IlyaG96/where_to_go.git
```
Создайте виртуальное окружение:
```bash
cd where_to_go
python3 -m venv env
```

Активируйте виртуальное окружение и установите все необходимые пакеты. 
```bash
source env/bin/activate
pip install -r requirements.txt
```
Возможно, потребуется обновить pip командой:
```shell
python3 -m pip install --upgrade pip
```
## Вероятные сценарии использования

### Протестировать сайт локально
<details>
<summary>Протестировать сайт локально</summary>

- Создайте файл `.env` в той же папке, что и `manage.py` или заполните прилагающийся `.env.example` и переименуйте его в `.env`:
```shell
SECRET_KEY=paste_your_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
SECRET_KEY - секретный ключ проекта Django.  
DEBUG - режим отладки (стандартно- True).  
ALLOWED_HOSTS - ip адрес вашего сервера. По умолчанию: 127.0.0.1.  

- Создайте базу данных командой:
```shell
python manage.py migrate
```
- создайте суперпользователя (админа). 
```shell
python manage.py createsuperuser
```
- запустите сервер локально.
```shell
python manage.py runserver
```
- Представлен функционал для заполнения сайта данными из файла .json.
```shell
python manage.py load_place -u 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json'
```
На место ссылки подставляйте одну из ссылок, представленных ниже:
- 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json'
- 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Арт-пространство%20«Бункер%20703».json'
- 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Водопад%20Радужный.json'

Можно также загружать информацию из .json файла, расположенного локально:
```shell
python manage.py load_place -p 'full/path/to/your_file.json'
```

В процессе загрузки вы увидите сообщение в консоль с названием места, которое только что появилось на карте.

Больше данных для заполнения сайта [здесь](https://github.com/devmanorg/where-to-go-places).  

Тестовый сайт можно посетить, если нажать [сюда](http://127.0.0.1).  

Админ-панель для заполнения сайта находится [по этому адресу](http://127.0.0.1/admin/).  

</details>