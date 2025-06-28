# The main hosting window

# Imports of libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,QMenuBar,QMessageBox,QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import pyqtSlot

# Imports of custom modules
from v1001_menu import Menu
from v2000_W_Main_Frame import W_Main_Frame


class Start_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fin Coach v1.0")
        self._init_size()

        main_frame = W_Main_Frame(self)
        self.setCentralWidget(main_frame)


        # Create the central widget and layout
#        central_widget = QWidget()
#        layout = QVBoxLayout()
#        label = QLabel("Click File -> New to see the message box")
#        layout.addWidget(label)
#        central_widget.setLayout(layout)
#        self.setCentralWidget(central_widget)
        
        application_menu = Menu(self)
        self.show()

    def _init_size(self):
        screen = QApplication.primaryScreen()
        geomerty = screen.geometry()
        width = geomerty.width()
        height = geomerty.height()
        self.resize(int(width/1.2), height//2)






def main():
    app = QApplication(sys.argv)
    app.setApplicationName("My App")
    window = Start_Window()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
