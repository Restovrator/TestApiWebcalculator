"""Методы для проверки ответов наших запросов"""
import json
from requests import Response
from ut import api
from ut.http_methods import Http_methods
from tcping import Ping
import socket
import subprocess, sys

class Checking():



    """Метод для проверки статус кода!"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success! Status code: " + str(response.status_code))
        else:
            print("Failed! Status code: " + str(response.status_code))

    """Метод для проверки корректности выражения"""

    @staticmethod
    def check_json_value(response: Response, field_name, expended_value, statusMessage, check_result):
        check = response.json()
        check_info = check.get(field_name)
        check_statusMessage = check.get(statusMessage)
        check_result = check.get(check_result)
        #print(check_result)
        #print(check_statusMessage)
        if check_info == expended_value and check_result >= -2147483648 <= 2147483647:
            print("Выражение верно")
        else:
            print(check_statusMessage)

    @staticmethod
    def check_URL():
        print(api.base_url)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print ("Успешное создание сокета")
        if api.base_url == "http://localhost:17678":
            port = 17678
            host_ip = "localhost"
            #print(port, host_ip)
        else:
            port = api.manual_port
            host_ip = socket.gethostbyname(api.manual_host)
            #print(port, host_ip)
        s.connect((host_ip, port))
        print("Успешное подключени к серверу!")


    """Проверка методов запроса к доступным"""

    # @staticmethod
    # def check_Request_Methods(): #response: Response, field_name
    #     get_resource = '/option'
    #     get_url = api.base_url + api.api + get_resource
    #     option = Http_methods.options(get_url)
    #     headers = option.headers
    #     #print(headers)
    #     json_header = headers ['Access-Control-Request-Method']
    #     #print (json_header)





# new_option = Checking ()
# new_option = Checking.URL()



