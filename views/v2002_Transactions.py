# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget
)

import Views.vh1001_View_Styles as vh 

class View_Transactions(QHBoxLayout):
    def __init__(self, transactions:list =[] , parent=None):
        super().__init__(parent)
        vh.neutralize_layout_style(self)

        if len(transactions)==0:
            label = QLabel("No month selected")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label)
        else:
            # Create the main categories
            vertical_frame_costs = QWidget(); vh.neutralize_widget_style(vertical_frame_costs)
            vertical_frame_transactions = QWidget(); vh.neutralize_widget_style(vertical_frame_transactions)
            
            vertical_layout_costs = QVBoxLayout(); vh.neutralize_layout_style(vertical_layout_costs)
            vertical_layout_transactions = QVBoxLayout(); vh.neutralize_layout_style(vertical_layout_transactions)

            label_cost_title = QLabel("CHF")
            label_transaction_title = QLabel("Transaction")

            vertical_layout_costs.addWidget(label_cost_title)
            vertical_layout_transactions.addWidget(label_transaction_title)

            vertical_frame_costs.setLayout(vertical_layout_costs)
            vertical_frame_transactions.setLayout(vertical_layout_transactions)

            self.addWidget(vertical_frame_costs)
            self.addWidget(vertical_frame_transactions)

            # Add transactions
            for transaction in transactions:
                label_transaction = QLabel(transaction[0])
                label_cost = QLabel(str(transaction[1]))
                vertical_layout_costs.addWidget(label_cost)
                vertical_layout_transactions.addWidget(label_transaction)

        self.addStretch()



