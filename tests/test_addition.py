from requests import Response
from ut.api import web_calc_api

""" Сложение двух сумм, проверка на точность """


class Test_summ():
    def test_new_summ(self):
        print("\nМетод: POST")
        result_post: Response = web_calc_api.test_summ_int()
