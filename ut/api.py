from ut.http_methods import Http_methods

""" Создание базового URL адреса для подключение к хосту """
base_host = "http://localhost"
base_port = 17678
manual_host = None
manual_port = None
if manual_host == None and manual_port == None:
    base_url = base_host + ':' + str(base_port)
    print(base_url)
else:
    base_url = manual_host + ':' + str(manual_port)
    print(base_url)

api = "/api"  # ресурс
json_date = {
    "x": 4,
    "y": 2
}

""" Методы для тестирования Калькулятора на localhost """


class web_calc_api():
    """ Метод для проверки состояния сервера """

    @staticmethod
    def test_get_state():
        get_resource = "/state"
        get_url = base_url + api + get_resource
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    """ Метод для сложения двух целых чисел """

    @staticmethod
    def test_calc_int():
        post_resource = "/addition"  # Сложение
        post_url = base_url + api + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_date)
        print(result_post.json())
        return result_post

    """Метод для вывода заголовка"""

    @staticmethod
    def option_():
        get_resource = "/state"
        get_url = base_url + api + get_resource
        option = Http_methods.options(get_url)
        print(option.headers)
        return option
