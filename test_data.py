
import allure


class Urls:

    base_url = "https://qa-scooter.praktikum-services.ru"

    api_create_courier = "/api/v1/courier"
    api_login_courier = "/api/v1/courier/login"
    api_create_order = "/api/v1/orders"
    api_get_order = "/api/v1/orders"
    api_delete_courier = "/api/v1/courier/"
    api_cancel_order = "/api/v1/orders/cancel"

class TestData:

    @staticmethod
    @allure.step('получение тестовых данных заказа')
    def create_order_dto(colour_list):

        payload = {
            "firstName": "Homer",
            "lastName": "Simpson",
            "address": "Moscow, Lubyanka street 25",
            "metroStation": 3,
            "phone": "+7 977 741 02 08",
            "rentTime": 5,
            "deliveryDate": "2021-08-15",
            "comment": "Welcome, my friend",
            "color": colour_list
        }

        return payload
