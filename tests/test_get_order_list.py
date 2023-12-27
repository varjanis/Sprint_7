import requests
import data
import allure

class TestGetOrderList:

    @allure.title('Проверка запроса списка существующих заказов')
    def test_get_order_list_success(self):

        data.create_new_order()

        order_list = requests.get(data.order_endpoint)

        assert order_list.status_code == 200
        assert 'orders' in order_list.text