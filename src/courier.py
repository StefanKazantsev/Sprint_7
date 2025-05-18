import requests
import allure
from test_data import Urls
from helpers import DataHelpers

class CourierClass:

    @allure.step('регистрация нового курьера')
    def register_new_courier_and_return_login_password(self):
        dto_payload = DataHelpers()
        login_pass_name = dto_payload.login_pass_name_courier_dto()
        requests.post(f'{Urls.base_url}{Urls.api_create_courier}', data=login_pass_name)

        return login_pass_name

    @allure.step('удаление курьера')
    def delete_courier(self, courier_id):
        requests.delete(f'{Urls.base_url}{Urls.api_delete_courier}{courier_id}')

    @allure.step('авторизация курьера')
    def login_courier(self):

        autorization_courier = self.register_new_courier_and_return_login_password()

        payload = {
            "login": autorization_courier['login'],
            "password": autorization_courier['password']
        }
        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        return response.status_code, response.json()

    @allure.step('авторизация с неправильными данными курьера')
    def login_courier_error_fields(self):

        failed_authorization_courier = self.register_new_courier_and_return_login_password()
        failed_authorization_courier2 = self.register_new_courier_and_return_login_password()

        payload = {
            "login": failed_authorization_courier['login'],
            "password": failed_authorization_courier2['password']
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        return response.status_code, response.json()

    @allure.step('авторизация курьера с отсутствием 1ого обязательного поля')
    def login_courier_non_login_fields(self):

        blank_field_authorization_courier = self.register_new_courier_and_return_login_password()

        payload = {
            "password": blank_field_authorization_courier['password']
        }
        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        return response.status_code, response.json()

    @allure.step('авторизоваться под несуществующим пользователем')
    def login_courier_non_user(self):

        dto_payload = DataHelpers()
        login_pass_name = dto_payload.login_pass_name_courier_dto()

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=login_pass_name)
        return response.status_code, response.json()

    @allure.step('регистрация нового курьера')
    def register_new_courier_and_return_lp(self):
        dto_payload = DataHelpers()
        login_pass_name = dto_payload.login_pass_name_courier_dto()
        response = requests.post(f'{Urls.base_url}{Urls.api_create_courier}', data=login_pass_name)

        return response.status_code, response.json()
