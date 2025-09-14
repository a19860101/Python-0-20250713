from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉 python')
w.resize(500,400)


# w.setStyleSheet('''
#     font-size: 30px;
#     font-weight: bold;
#     font-style: italic;
# ''')

font = QtGui.QFont()
font.setPointSize(30)
font.setBold(True)
font.setItalic(False)
font.setUnderline(True)

font2 = QtGui.QFont()
font2.setPointSize(10)


#加入label
label1 = QtWidgets.QLabel(w)
label1.setText('hello')
label1.move(50,50)
label1.setFont(font)

label2 = QtWidgets.QLabel(w)
label2.setText('12345')
label2.move(150,50)
label2.setFont(font2)





w.show()
sys.exit(app.exec())