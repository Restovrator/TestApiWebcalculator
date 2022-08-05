import requests


""" Список HTTP методов """


class Http_methods:
    headers = {
        'Content-Type':  'application/json'
    }
    cookie = ""
    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def options(url):
        result = requests.options(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result
