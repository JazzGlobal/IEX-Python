import requests


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = {}

    def build_stock(self):
        url = "https://api.iextrading.com/1.0/stock/"
        self.data["book"] = self.__get_book(url)
        self.data["chart"] = self.__get_chart(url)
        self.data["earnings"] = self._get_earnings()

    def __get_book(self, url):
        response = requests.get(url + self.symbol + '/book')
        if response.status_code == '404':
            print(response.status_code + " Error has occurred")
            return
        return response.json()

    def __get_chart(self, url):
        response = requests.get(url + self.symbol + '/chart/1y')
        if response.status_code == '404':
            print(response.status_code + " Error has occurred")
            return
        return response.json()

    def __get_earnings(self, url):
        response = requests.get(url + self.symbol + "/earnings")
        if response.status_code == '404':
            print(response.status_code + " Error has occurred")
            return
        return response.json()
