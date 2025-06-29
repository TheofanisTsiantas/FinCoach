from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class ErrorMessageDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Error")
        self.setFixedSize(300, 150)
        self.init_ui(message)

    def init_ui(self, message):
        layout = QVBoxLayout()

        # Label to display the message
        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)

        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        # Add widgets to layout
        layout.addWidget(label)
        layout.addWidget(close_button)

        self.setLayout(layout)

class YesNoDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Warning")
        self.setFixedSize(300, 150)
        self.init_ui(message)

    def init_ui(self, message):
        layout = QVBoxLayout()

        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)

        # Button layout
        button_layout = QHBoxLayout()
        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        yes_button.clicked.connect(self.accept)   # returns QDialog.Accepted
        no_button.clicked.connect(self.reject)    # returns QDialog.Rejected

        button_layout.addWidget(yes_button)
        button_layout.addWidget(no_button)

        layout.addWidget(label)
        layout.addLayout(button_layout)

        self.setLayout(layout)