import pytest
import requests
import json
import data
import allure

class TestCreateOrder:

    @allure.title('Проверка создания нового заказа с корректными данными')
    @pytest.mark.parametrize('first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color',
                    [
                         [data.generate_random_name(), data.generate_random_lastname(),
                          data.generate_random_address(), data.choose_random_metrostation(),
                          data.generate_random_phone(), data.choose_random_renttime(),
                          data.choose_random_deliverydate(), data.generate_random_comment(), ['BLACK']],
                         [data.generate_random_name(), data.generate_random_lastname(),
                          data.generate_random_address(), data.choose_random_metrostation(),
                          data.generate_random_phone(), data.choose_random_renttime(),
                          data.choose_random_deliverydate(), data.generate_random_comment(), ['GRAY']],
                         [data.generate_random_name(), data.generate_random_lastname(),
                          data.generate_random_address(), data.choose_random_metrostation(),
                          data.generate_random_phone(), data.choose_random_renttime(),
                          data.choose_random_deliverydate(), data.generate_random_comment(), ['GRAY', 'BLACK']],
                         [data.generate_random_name(), data.generate_random_lastname(),
                          data.generate_random_address(), data.choose_random_metrostation(),
                          data.generate_random_phone(), data.choose_random_renttime(),
                          data.choose_random_deliverydate(), data.generate_random_comment(), '']
                  ]
                     )
    def test_create_new_order_all_fields_filled_one_color_success(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color):

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }

        json_payload = json.dumps(payload)

        response = requests.post(data.order_endpoint, data=json_payload)

        assert response.status_code == 201
        assert "track" in response.text