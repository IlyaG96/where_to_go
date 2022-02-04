
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

### Добавить администратора
<details>

<summary>Добавить администратора</summary>

Войдите в админ-панель от имени суперпользователя.  
Слева на панели "Пользователи и группы", около кнопки "пользователь", нажмите "добавить".    
После того, как пользователь будет создан, не забудьте дать ему права для добавления новых точек на карту.   
Пример:  

![](https://downloader.disk.yandex.ru/preview/44aaf98f5b6bcb6fc5c0093bea45cd0c069cec95071d7e8d4dd2d79182e218fd/61fd1655/fkn8lihf7uOgXlJMEejJWLfZfz7HTIqaw6zRp7V63sDCRlsrvtbZbR9fXckAQvYG04JB5NR5759RjgqKYRjB4Q%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-02-04%20%D0%B2%2019.02.48.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)
</details>
