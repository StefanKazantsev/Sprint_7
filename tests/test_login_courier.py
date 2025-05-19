from src.courier import CourierClass
import allure
from responses import ApiResponses

class TestLoginCourier:

    @allure.title('курьер может авторизоваться, для авторизации нужно передать все обязательные поля, успешный запрос возвращает id')
    def test_login_courier(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()

        assert status_code == 200 and 'id' in response, ApiResponses.COURIER_AUTH_FAILED

        courier_id = response['id']
        login_pass.delete_courier(courier_id)

        return status_code, response

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_error_fields()

        assert status_code == 404 and  response == ApiResponses.ACCOUNT_NOT_FOUND


    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_non_login_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_login_fields()
        assert status_code == 400


    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    def test_login_courier_non_user(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_user()

        assert status_code == 404 and response == ApiResponses.ACCOUNT_NOT_FOUND
