import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui.test import Ui_MainWindow
from progress_bar_util import ProgressBarUtil


class MainWindow(QMainWindow):
    is_stopped = False

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.pushButtonStart.clicked.connect(self.process)
    
    def process(self):
        self.ui.pushButtonStart.setDisabled(True)
        
        for p in ProgressBarUtil(range(7), self.ui.progressBar):
            time.sleep(0.5)

        self.ui.pushButtonStart.setEnabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())

    