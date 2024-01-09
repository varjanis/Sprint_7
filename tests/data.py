import random
import string
import requests
import json

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

order_endpoint = BASE_URL + 'api/v1/orders/'
courier_login_endpoint = BASE_URL + 'api/v1/courier/login'
create_courier_endpoint = BASE_URL + 'api/v1/courier/'
delete_courier_endpoint = BASE_URL + 'api/v1/courier/'

create_courier_response_text_200 = '{"ok":true}'
create_courier_response_text_409 = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
create_courier_response_text_400 = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

login_courier_response_text_400 = '{"code":400,"message":"Недостаточно данных для входа"}'
login_courier_response_text_404 = '{"code":404,"message":"Учетная запись не найдена"}'




def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass



def choose_random_metrostation():
    stations_list = ['Александровский сад', 'Арбатская', 'Библиотека имени Ленина', 'Воробьёвы горы', 'Выставочная',
                     'Деловой центр', 'Достоевская', 'Китай-город', 'Кузнецкий мост', 'Лубянка', 'Маяковская',
                     'Новослободская', 'Охотный ряд', 'Парк культуры', 'Площадь Революции', 'Пролетарская',
                     'Пушкинская', 'Савёловская', 'Серпуховская', 'Театральная', 'Третьяковская', 'Трубная',
                     'Тургеневская', 'Улица 1905 года', 'Фрунзенская', 'Черкизовская', 'Чистые пруды', 'Чкаловская']
    random_metrostation = random.choice(stations_list)
    return random_metrostation


def choose_random_renttime():
    rent_time = ['1', '2', '3', '4', '5', '6', '7']
    random_renttime = random.choice(rent_time)
    return random_renttime


def choose_random_deliverydate():
    random_day = random.randint(1, 31)
    random_deliverydate = f'2024-01-{random_day}'
    return random_deliverydate


def generate_random_phone():
    area_code = str(random.randint(961, 978))
    local_number = ''.join(str(random.randint(0, 9)) for i in range(6))
    random_number = f'+7{area_code}{local_number}'
    return random_number


def generate_random_address(length=10):
    letters = string.ascii_lowercase
    numbers = random.randint(1, 99)
    address_string = ''.join(random.choice(letters) for i in range(length))
    random_string = f'{address_string}, {numbers}'
    return random_string


def generate_random_comment(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_lastname(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_name(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_new_order():
    payload = {
        "firstName": generate_random_name(),
        "lastName": generate_random_lastname(),
        "address": generate_random_address(),
        "metroStation": choose_random_metrostation(),
        "phone": generate_random_phone(),
        "rentTime": choose_random_renttime(),
        "deliveryDate": choose_random_deliverydate(),
        "comment": generate_random_comment(),
        "color": ['GRAY']
    }

    json_payload = json.dumps(payload)

    response = requests.post(order_endpoint, data=json_payload)

    return response


def delete_courier(id):

    response = requests.delete(delete_courier_endpoint+str(id))

    if response.status_code == 200:
        print('После окончания тестирования курьер удалён')
    else:
        print('Не получилось удалить курьера')


def login_and_return_id(login, password):

    response = requests.post(courier_login_endpoint, data={'login': login, 'password': password})

    if response.status_code == 200:
        return response.json()['id']
    else:
        print('Ошибка логина')


