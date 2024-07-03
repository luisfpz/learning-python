import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    # adding button widget - label, boolean
    button = QPushButton("Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_clicked) # calling def

    # self the central widget of the window
    self.setCentralWidget(button)
  
  # def to print when button is clicked
  def the_button_was_clicked(self):
    print("clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()