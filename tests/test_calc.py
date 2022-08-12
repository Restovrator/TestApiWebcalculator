from requests import Response
from ut.api import web_calc_api
from ut.checking import Checking

class Test_calc():

    def test_check_URL(self):
        print("\n\nТекущий хост и порт: ")
        Checking.check_URL()

    def test_check_get_state(self):
        print("\n\nМетод: GET\nПроверка состояния сервера ")
        result_get: Response = web_calc_api.test_get_state()
        Checking.check_status_code(result_get, 200)

    def test_check_option(self):
        print("\n\nМетод: OPTION")
        result_option: Response = web_calc_api.option_()
        Checking.check_status_code(result_option, 200)

    def test_check_addition(self):
        print("\n\nМетод: POST")
        result_post: Response = web_calc_api.test_calc_int('5+2')
        Checking.check_json_value(result_post, 'statusCode', 0, 'statusMessage', 'result')
        Checking.check_status_code(result_post, 200)

    def test_check_multiplication(self):
        print("\n\nМетод: POST")
        result_post: Response = web_calc_api.test_calc_int('5*222222222222')
        Checking.check_json_value(result_post, 'statusCode', 0, 'statusMessage', 'result')
        Checking.check_status_code(result_post, 200)

    def test_check_division(self):
        print("\n\nМетод: POST")
        result_post: Response = web_calc_api.test_calc_int('5/2')
        Checking.check_json_value(result_post, 'statusCode', 0, 'statusMessage', 'result')
        Checking.check_status_code(result_post, 200)

    def test_check_remainder(self):
        print("\n\nМетод: POST")
        result_post: Response = web_calc_api.test_calc_int('5%2')
        Checking.check_json_value(result_post, 'statusCode', 0, 'statusMessage', 'result')
        Checking.check_status_code(result_post, 200)
