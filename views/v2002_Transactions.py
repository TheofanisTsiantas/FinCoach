# The view of the months list

from PyQt5.QtWidgets import (
    QLabel,
    QGridLayout
)

from PyQt5.QtCore import Qt

import Views.vh1001_View_Styles as vh 

class View_Transactions(QGridLayout):
    def __init__(self, transactions:dict ={} , parent=None):
        super().__init__(parent)
        vh.neutral_layout_style(self)

        if not transactions:
            label = QLabel("No month selected")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label,0, 0, alignment=Qt.AlignTop)
        else:
            rowpos = [0] # To enable pass by reference
            for category, transaction_items in transactions.items():
                self._create_transactions(category, transaction_items, rowpos)

    # For each category it a grid group with th title, the sum and all transactions
    def _create_transactions(self, category:str, transactions:list, rowpos):
        # If the sum of transactions is zero, omit the category
        sum_of_transactions = round(sum(x[0] for x in transactions),1)
        if sum_of_transactions == 0:
            return
        # Add category and transactions
        label_title = QLabel(category)
        vh.add_label_left_padding_style(label_title)
        self.addWidget(label_title,rowpos[0], 0)
        label_sum = QLabel(str(sum_of_transactions)+" CHF")
        vh.add_label_left_padding_style(label_sum)
        self.addWidget(label_sum,rowpos[0], 1)
        rowpos[0] += 1
        for i, transaction in enumerate(transactions):
            label_transaction = QLabel(transaction[1])
            vh.add_label_left_padding_style(label_transaction)
            label_cost = QLabel(str(transaction[0])+" CHF")
            vh.add_label_left_padding_style(label_cost)
            self.addWidget(label_cost,rowpos[0], 0)
            self.addWidget(label_transaction,rowpos[0], 1)
            rowpos[0] += 1
        self.addWidget(QLabel(),rowpos[0], 0)
        rowpos[0] += 1
        return







