from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉 python')
w.resize(500,400)
w.setStyleSheet('background: pink; font-size: 36px;')

#加入label
label1 = QtWidgets.QLabel(w)
label1.setText('hello')
label1.move(50,50)
# label1.setGeometry(100,100,200,200)
# label1.setStyleSheet('background: blue; font-size: 16px; color: red')

label1.setStyleSheet('''
    color: red;
    padding: 15px;
    background: blue;
''')


w.show()
sys.exit(app.exec())