import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui




MEMBER_TIERS = ['Trial Member', 'Full Member', 'Public Guest']

class C5Calculator(QWidget):

    def __init__(self, parent=None):

        super(C5Calculator, self).__init__(parent)

        """Title and Window Icon"""

        self.setWindowTitle('C5 Calculator')

        self.setWindowIcon(QtGui.QIcon('blackhole.png'))

        """Gets Current Blue Book Prices"""
        self.prices = C5Calculator.getPrices()

        """Layout"""
        
        """Sleeper Drone AI Nexus Box"""
        sleeper_drone_ai_nexus_label = QLabel('Sleeper Drone AI Nexus')
        sdan_price = self.prices['Sleeper Drone AI Nexus']
        sleeper_drone_ai_nexus_price = QLabel(f'{sdan_price}')
        sleeper_drone_ai_nexus = QVBoxLayout()
        sleeper_drone_ai_nexus.addWidget(sleeper_drone_ai_nexus_label)
        sleeper_drone_ai_nexus.addWidget(sleeper_drone_ai_nexus_price)

        """Sleeper Data Library"""
        sleeper_data_library_label = QLabel('Sleeper Data Library')
        sdl_price = self.prices['Sleeper Data Library']
        sleeper_data_library_price = QLabel(f'{sdl_price}')
        sleeper_data_library = QVBoxLayout()
        sleeper_data_library.addWidget(sleeper_data_library_label)
        sleeper_data_library.addWidget(sleeper_data_library_price)

        """Neural Network Analzyer"""
        neural_network_analyzer_label = QLabel('Neural Network Analzyer')
        nna_price = self.prices['Neural Network Analyzer']
        neural_network_analyzer_price = QLabel(f'{nna_price}')
        neural_network_analyzer = QVBoxLayout()
        neural_network_analyzer.addWidget(neural_network_analyzer_label)
        neural_network_analyzer.addWidget(neural_network_analyzer_price)


        """Ancient Coordinates Database"""
        ancient_coordinates_database_label = QLabel('Ancient Coordinates Database')
        acd_price = self.prices['Ancient Coordinates Database']
        ancient_coordinates_database_price = QLabel(f'{acd_price}')
        ancient_coordinates_database = QVBoxLayout()
        ancient_coordinates_database.addWidget(ancient_coordinates_database_label)
        ancient_coordinates_database.addWidget(ancient_coordinates_database_price)

        """First Row of the widget"""
        first_row = QHBoxLayout()
        first_row.addLayout(sleeper_drone_ai_nexus)
        first_row.addLayout(sleeper_data_library)
        first_row.addLayout(neural_network_analyzer)
        first_row.addLayout(ancient_coordinates_database)

        """Second row widgets"""

        party_member_count = QComboBox()
        party_member_count.addItems(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'])

        party_member_count_label = QLabel('Party member size')

        party_member_box = QVBoxLayout()
        party_member_box.addWidget(party_member_count_label)
        party_member_box.addWidget(party_member_count)

        """Second Row of the widget"""
        second_row = QHBoxLayout()
        second_row.addLayout(party_member_box)


        """ Main Vert Layout"""
        layout = QVBoxLayout()
        layout.addLayout(first_row)
        layout.addLayout(second_row)

        """Layout Setter"""
        self.setLayout(layout)



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
        #print(price_book)

        return price_book



if __name__ == '__main__':
    app = QApplication(sys.argv)
    c5 = C5Calculator()
    c5.show()
    sys.exit(app.exec_())