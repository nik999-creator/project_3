from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

app = QApplication([])

win = QWidget()
win.resize(600, 600)
win.setWindowTitle('girl')
win.show()

label_p = QLabel('')
label_p.setFixedSize(500, 500)
label_p.hide()
pixmapimage = QPixmap('girl.jpg')
w, h = label_p.width(), label_p.height()
pixmapimage = pixmapimage.scaled(300, 300, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

field_text = QTextEdit()

list_country_label = QLabel("Список країн")
list_country = QListWidget()

w = QVBoxLayout()
w.addWidget(label_p)

w.addWidget(list_country)

win.setLayout(w)



app.exec()