from concurrent.futures import process
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

        self.ui.pushButtonStart.clicked.connect(self.start)
    
    def start(self):
        self.ui.pushButtonStart.setDisabled(True)

        sweep = ProgressBarUtil(range(7), self.ui.progressBar)

        for s in sweep:
            self.process(s)

        for s in sweep:
            self.process(s)        

        self.ui.pushButtonStart.setEnabled(True)

    def process(self, s):
        print(s)
        time.sleep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())

    