from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('哈囉 python')
w.resize(500,400)

w.setStyleSheet('''
    font-size: 16px;
    font-weight: bold;
''')

#加入label
label = QtWidgets.QLabel(w)
label.setText('hello')

label_input = QtWidgets.QLineEdit(w)

sel = QtWidgets.QComboBox(w)
sel.addItems(['test 1','test 2', 'test 3'])

textarea = QtWidgets.QTextEdit(w)

btn = QtWidgets.QPushButton(w)
btn.setText('按我按我!!')

grid = QtWidgets.QGridLayout(w)
grid.addWidget(label, 1, 1)
grid.addWidget(label_input,1, 2)
grid.addWidget(sel,1, 3,)
grid.addWidget(textarea,3,1,1,2)
grid.addWidget(btn,4,1,1,2)


w.show()
sys.exit(app.exec())