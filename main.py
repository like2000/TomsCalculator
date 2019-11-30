import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

from windows import mainwindow


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Create window
        # =============
        self.setGeometry(300, 300, 550, 550)
        self.setWindowTitle("Tom's Calculator - v0.1")
        with open("resources/application_stylesheet.qss", "r") as fh:
            self.setStyleSheet(fh.read())

        # Create toolbar
        # ==============
        exitAct = QtWidgets.QAction(QtGui.QIcon.fromTheme("window-close"), 'Exit', self)
        exitAct.triggered.connect(QtWidgets.qApp.quit)
        exitAct.setShortcut('Ctrl+Q')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        # Fun
        # ===
        # self.ui.verticalLayout.insertWidget(0, Image('resources/riccati.jpeg', 200))

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ApplicationWindow()
    sys.exit(app.exec_())
