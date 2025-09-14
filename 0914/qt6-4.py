from PyQt6 import QtWidgets, QtGui
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
label1 = QtWidgets.QLabel(w)
label1.setText('hello')
label1.move(50,50)

## Line Edit 輸入文字框
label_input = QtWidgets.QLineEdit(w)
label_input.move(50,100)
label_input.setStyleSheet('''
    color: red;
''')

# Combo Box 下拉式
sel = QtWidgets.QComboBox(w)
# sel.addItem('test 1')
# sel.addItem('test 2')
# sel.addItem('test 3')
sel.addItems(['test 1','test 2', 'test 3'])

# Text Edit 長文字輸入
textarea = QtWidgets.QTextEdit(w)
textarea.move(50,200)

# Push Button
btn = QtWidgets.QPushButton(w)
btn.setText('按我按我!!')
btn.move(300,300)
btn.setStyleSheet('''
    background: red;
    color: yellow;
    padding: 8px;
    border-radius: 8px;
''')




w.show()
sys.exit(app.exec())