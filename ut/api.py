from ut.http_methods import Http_methods
""" Методы для тестирования Калькулятора на localhost """

base_url = "http://localhost:5413"  # базовый URL
api = "/api"  # ресурс


class web_calc_api():
    """ Метод для сложения двух целых чисел """
    @staticmethod
    def test_summ_int():
        json_date = {
            "x": 2, 
            "y": 2
        }
        post_summ = "/addition"  # Сложение
        post_url = base_url + api + post_summ
        print(post_url)
        result_post = Http_methods.post(post_url, json_date)
        print(result_post.json())
        return result_post