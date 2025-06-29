# Imports of libraries
import sys
import os
from PyQt5.QtWidgets import QApplication

# Important --> Append root directory to path
APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(APP_PATH)

# Imports of custom modules
from views.v1000_Start_Window import Start_Window

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("My App")
    window = Start_Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
