import requests
from ut.logger import Logger


""" Список HTTP методов """


class Http_methods:
    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body)
        Logger.add_response(result)
        return result

    @staticmethod
    def options(url):
        Logger.add_request(url, method="OPTION")
        result = requests.options(url)
        Logger.add_response(result)
        return result
