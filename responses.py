class ApiResponses:
    SUCCESS_RESPONSE = {'ok': True}
    LOGIN_ALREADY_USED = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    INSUFFICIENT_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_AUTH_FAILED = "Курьер не может авторизоваться или id не найден"