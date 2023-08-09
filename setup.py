__author__ = "Tommy" 
__version__ = '0.1.0' 
__license__ = 'MIT' 


import sys
import signal 

from PyQt5.QtWidgets import QApplication 
from app import MainWindow


if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    
    window = MainWindow()

    sys.exit(app.exec_()); 
