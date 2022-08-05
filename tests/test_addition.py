from requests import Response
from utils.api import web_calc_api

""" Сложение двух сумм, проверка на точность """


class test_summ():
    def test_new_summ(self):
        print("Метод: POST")
        result_post: Response = web_calc_api.test_summ_int()
