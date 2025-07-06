# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget
)

import Views.vh1001_View_Styles as vh 

class View_Transactions(QVBoxLayout):
    def __init__(self, transactions:dict ={} , parent=None):
        super().__init__(parent)
        vh.neutralize_layout_style(self)

        if not transactions:
            label = QLabel("No month selected")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label)
        else:
            for category, transaction_items in transactions.items():
                self._create_transactions(category, transaction_items)
        self.addStretch()

    # For each category it creates a group with th title, the sum and all transactions
    def _create_transactions(self, category:str, transactions:list):
        sum_of_transactions = round(sum(x[0] for x in transactions),1)
        if sum_of_transactions == 0:
            return
        # Outer horizontal layout of total group
        horizontal_frame_group = QWidget(); vh.neutralize_widget_style(horizontal_frame_group)
        horizontal_layout_group = QHBoxLayout(); vh.neutralize_layout_style(horizontal_layout_group)
        # Verticals for costs and transactions (inside total group)
        vertical_frame_costs = QWidget(); vh.neutralize_widget_style(vertical_frame_costs)
        vertical_frame_transactions = QWidget(); vh.neutralize_widget_style(vertical_frame_transactions)
        #
        vertical_layout_costs = QVBoxLayout(); vh.neutralize_layout_style(vertical_layout_costs)
        vertical_layout_transactions = QVBoxLayout(); vh.neutralize_layout_style(vertical_layout_transactions)
        #
        vertical_frame_costs.setLayout(vertical_layout_costs)
        vertical_frame_transactions.setLayout(vertical_layout_transactions)
        # Set horizontal group to widget
        horizontal_frame_group.setLayout(horizontal_layout_group)
        horizontal_layout_group.addWidget(vertical_frame_costs)
        horizontal_layout_group.addWidget(vertical_frame_transactions)
        # Add tiles for the category
        label_transaction_title = QLabel(category)
        vertical_layout_costs.addWidget(label_transaction_title)
        #
        label_expense_sum = QLabel(str(sum_of_transactions)+" CHF")
        vertical_layout_transactions.addWidget(label_expense_sum)

        for transaction in transactions:
            label_transaction = QLabel(transaction[1])
            label_cost = QLabel(str(transaction[0])+" CHF")
            vertical_layout_costs.addWidget(label_cost)
            vertical_layout_transactions.addWidget(label_transaction)
        #    
        self.addWidget(horizontal_frame_group)
        # Space (for upcoming widgets afterwards)
        dummy_widget = QWidget(); vh.neutralize_widget_style(dummy_widget)
        dummy_layout = QVBoxLayout(dummy_widget); # Necessary for space
        self.addWidget(dummy_widget)





