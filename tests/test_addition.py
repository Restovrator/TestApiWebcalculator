from requests import Response
from ut.api import web_calc_api
from ut.checking import Checking
import asyncio
import pytest

class Test_summ():

    @pytest.mark.asyncio
    async def test_check_URL(self):
        print("\nТекущий хост и порт: ")
        Checking.check_URL()

    @pytest.mark.asyncio
    async def test_check_get_state(self):
        print("\nМетод: GET\nПроверка состояния сервера ")
        result_option: Response = web_calc_api.test_get_state()
        Checking.check_status_code(result_option, 200)

    @pytest.mark.asyncio
    async def test_check_option(self):
        print("\nМетод: OPTION")
        result_option: Response = web_calc_api.option_()
        Checking.check_status_code(result_option, 200)

    @pytest.mark.asyncio
    async def test_check_calc_int(self, result_option=200):
        print("\nМетод: POST")
        result_post: Response = web_calc_api.test_calc_int()
        Checking.check_json_value(result_post, 'statusCode', 0, 'statusMessage', 'result')
        Checking.check_status_code(result_option, 200)

