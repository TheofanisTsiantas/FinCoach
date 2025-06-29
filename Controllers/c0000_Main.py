# Imports of libraries
import sys
import os

# Important --> Append root directory to path
APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(APP_PATH)

# Imports of custom modules
from Controllers.c1000_Controllers import Controllers

#
if __name__ == "__main__":
    Controllers()
