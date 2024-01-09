import requests
import data
import allure


class TestCreateCourier:

    @allure.title('Проверка успешной регистрации нового курьера c корректными данными')
    def test_create_new_courier_success(self):

        login = data.generate_random_string(10)
        password = data.generate_random_string(10)
        first_name = data.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 201
        assert response.text == data.create_courier_response_text_200

        id = data.login_and_return_id(login, password)
        data.delete_courier(id)

    @allure.title('Проверка того, что нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_fail(self):

        first_courier_login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "login": first_courier_login_password[0],
            "password": first_courier_login_password[1],
            "firstName": first_courier_login_password[2]
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 409
        assert response.text == data.create_courier_response_text_409


    @allure.title('Проверка того, что нельзя зарегистировать курьера, если не все поля заполнены: не заполнено поле логин')
    def test_not_all_fields_filled_no_login_fail(self):

        password = data.generate_random_string(10)
        first_name = data.generate_random_string(10)

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 400
        assert response.text == data.create_courier_response_text_400

    @allure.title('Проверка того, что нельзя зарегистировать курьера, если не все поля заполнены: не заполнено поле пароль')
    def test_not_all_fields_filled_no_password_fail(self):
        login = data.generate_random_string(10)
        first_name = data.generate_random_string(10)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 400
        assert response.text == data.create_courier_response_text_400

    @allure.title(
        'Проверка того, что нельзя зарегистировать курьера, если не все поля заполнены: не заполнено поле Имя')
    def test_not_all_fields_filled_no_password_fail(self):
        login = data.generate_random_string(10)
        password = data.generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 400
        assert response.text == data.create_courier_response_text_400

    @allure.title('Проверка того, что нельзя зарегистрировать нового курьера с уже существующим логином')
    def test_create_courier_with_existing_login_fail(self):

        first_courier_login_password = data.register_new_courier_and_return_login_password()

        password = data.generate_random_string(10)
        first_name = data.generate_random_string(10)

        payload = {
            "login": first_courier_login_password[0],
            "password": password,
            "firstName": first_name
        }

        response = requests.post(data.create_courier_endpoint, data=payload)

        assert response.status_code == 409
        assert response.text == data.create_courier_response_text_409
