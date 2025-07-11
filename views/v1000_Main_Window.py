# The main hosting window

# Imports of libraries
from PyQt5.QtWidgets import QApplication, QMainWindow

# Imports of custom modules
from Views.v1100_menu import Menu
from Views.v1100_Main_Frame import View_Main_Frame

class View_Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fin Coach v1.0")
        self._init_size()

        self.main_frame = View_Main_Frame()
        self.setCentralWidget(self.main_frame)
        
        application_menu = Menu(self)
        self.show()

    def _init_size(self):
        screen = QApplication.primaryScreen()
        geomerty = screen.geometry()
        width = geomerty.width()
        height = geomerty.height()
        self.resize(int(width/1.2), height//2)