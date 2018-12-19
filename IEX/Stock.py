import requests


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = {}

    def build_stock(self):
        url = "https://api.iextrading.com/1.0/stock/"
        self.data["book"] = self.__get_book(url)
        self.data["chart"] = self.__get_chart(url)
        self.data["earnings"] = self.__get_earnings()
        self.data["company"] = self.__get_company(url)
        self.data["dividends"] = self.__get_dividends(url)

    def get_average_high(self):
        if len(self.data["chart"]) < 1:
            return
        total = 0
        for value in self.data["chart"]:
            total += int(value['high'])
            print(total)
        return round(total / len(self.data["chart"]), 2)

    def get_high(self):
        if len(self.data["chart"]) < 1:
            return
        high_list = []
        for value in self.data["chart"]:
            high_list.append(value["high"])
        return round(max(high_list), 2)

    def get_average_low(self):
        if len(self.data["chart"]) < 1:
            return
        total = 0
        for value in self.data["chart"]:
            total += value["low"]
        return round(total / len(self.data["chart"]), 2)

    def get_low(self):
        if len(self.data["chart"]) < 1:
            return
        low_list = []
        for value in self.data["chart"]:
            low_list.append(value["low"])
        return round(min(low_list), 2)

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

    def __get_company(self, url):
        response = requests.get(url + self.symbol + "/company")
        if response.status_code == '404':
            print(response.status_code + " Error has occurred")
            return
        return response.json()

    def __get_dividends(self, url):
        response = requests.get(url + self.symbol + "/dividends/1y")
        if response.status_code == '404':
            print(response.status_code + " Error has occurred")
            return
        return response.json()
