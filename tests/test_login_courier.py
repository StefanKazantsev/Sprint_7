from src.courier import CourierClass
import allure

class TestLoginCourier:

    def check_courier_login(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()

        assert status_code == 200 and 'id' in response, "Курьер не может авторизоваться или id не найден"

        courier_id = response['id']
        login_pass.delete_courier(courier_id)

        return status_code, response

    @allure.title('курьер может авторизоваться')
    def test_login_courier(self):

        self.check_courier_login()

    @allure.title('для авторизации нужно передать все обязательные поля')
    def test_login_courier_all_fields(self):

        self.check_courier_login()

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_error_fields()

        assert status_code == 404 and  response == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_non_login_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_login_fields()
        assert status_code == 400


    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    def test_login_courier_non_user(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_user()

        assert status_code == 404 and response == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('успешный запрос возвращает id')
    def test_login_courier_ok_id(self):

        status_code, response = self.check_courier_login()
        assert status_code == 200 and 'id' in response, "Успешный запрос не вернул id"