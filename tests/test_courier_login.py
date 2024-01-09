import requests
import data
import allure


class TestCourierLogin:

    @allure.title('Проверка, что курьер может войти в систему, если вводит корректные данные')
    def test_courier_login_correct_data_success(self):

        login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "login": login_password[0],
            "password": login_password[1]
        }

        response = requests.post(data.courier_login_endpoint, data=payload)
        id = response.json()['id']

        assert response.status_code == 200
        assert "id" in response.text

        data.delete_courier(id)

    @allure.title('Проверка, что курьер не может войти в систему, если не заполнено поле логин')
    def test_courier_login_loginfield_not_filled_fail(self):
        login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "password": login_password[1]
        }

        response = requests.post(data.courier_login_endpoint, data=payload)

        assert response.status_code == 400
        assert response.text == data.login_courier_response_text_400

    @allure.title('Проверка, что курьер не может войти в систему, если не заполнено поле пароль')
    def test_courier_login_password_not_filled_fail(self):

        login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "login": login_password[0]
        }

        response = requests.post(data.courier_login_endpoint, data=payload)

        assert response.status_code == 400
        assert response.text == data.login_courier_response_text_400

    @allure.title('Проверка, что курьер не может войти в систему, если введен неверный логин')
    def test_courier_login_wrong_login_fail(self):

        login = data.generate_random_string(10)

        login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": login_password[1]
        }

        response = requests.post(data.courier_login_endpoint, data=payload)

        assert response.status_code == 404
        assert response.text == data.login_courier_response_text_404

    @allure.title('Проверка, что курьер не может войти в систему, если введен неверный пароль')
    def test_courier_login_wrong_password_fail(self):

        password = data.generate_random_string(10)

        login_password = data.register_new_courier_and_return_login_password()

        payload = {
            "login": login_password[0],
            "password": password
        }

        response = requests.post(data.courier_login_endpoint, data=payload)

        assert response.status_code == 404
        assert response.text == data.login_courier_response_text_404

    @allure.title('Проверка, что курьер не может войти в систему, если введен несуществующий логин')
    def test_courier_login_user_doesnt_exist_fail(self):

        login = data.generate_random_string(10)
        password = data.generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(data.courier_login_endpoint, data=payload)

        assert response.status_code == 404
        assert response.text == data.login_courier_response_text_404