import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

QApplication.setStyle('Fusion')
app = QApplication(sys.argv)

window = QMainWindow()
window.show()
window.centerOnScreen()
window.canva.InitDriver()
sys.exit(app.exec_())
