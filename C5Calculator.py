import sys
import requests
from PyQt5.QtWidgets import *


MEMBER_TIERS = ['Trial Member', 'Full Member', 'Public Guest']

class C5Calculator(QDialog):

    def __init__(self, parent=None):

        super(C5Calculator, self).__init__(parent)

        self.setWindowTitle('C5 Calculator')

       # self.market_prices = C5Calculator.getPrices()


        self.party_size = QSpinBox()

        self.sites_done = QSpinBox()


        party_size_label = QLabel('Party Member Count: ')
        sites_done_label = QLabel('Number of sites done: ')

        layout = QVBoxLayout()
        layout.addWidget(party_size_label)
        layout.addWidget(self.party_size)
        layout.addWidget(sites_done_label)
        layout.addWidget(self.sites_done)


        self.setLayout(layout)



    def checkIfBlueBook(self):

        pass








    @staticmethod
    def getPrices():

        blue_book_ids = [30747, 30745, 30744, 30746]

        blue_book_names = ['Sleeper Drone AI Nexus', 'Sleeper Data Library', 'Neural Network Analyzer',
                           'Ancient Coordinates Database']

        current_prices = []

        items = f"{blue_book_ids[0]},{blue_book_ids[1]},{blue_book_ids[2]},{blue_book_ids[3]}"

        url = f'https://api.evemarketer.com/ec/marketstat/json?typeid={items}&usesystem=30002187'

        response = requests.get(f'{url}')
        json_response = response.json()
        counter = 0

        price_book = {}

        for i in json_response:
            
            new_price = json_response[counter]['buy']['max']
            current_prices.append(new_price)
            price_book[f'{blue_book_names[counter]}'] = float(f'{current_prices[counter]}')
            counter += 1

        """Remove before production"""
        print(price_book)

        return price_book






if __name__ == '__main__':
    app = QApplication(sys.argv)
    c5 = C5Calculator()
    c5.show()
    sys.exit(app.exec_())