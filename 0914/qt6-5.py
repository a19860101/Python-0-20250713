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
label.move(50,50)

## Line Edit 輸入文字框
label_input = QtWidgets.QLineEdit(w)
label_input.move(50,100)

# Combo Box 下拉式
sel = QtWidgets.QComboBox(w)
sel.addItems(['test 1','test 2', 'test 3'])
sel.move(50,150)

# Text Edit 長文字輸入
textarea = QtWidgets.QTextEdit(w)
textarea.move(50,200)

# Push Button
btn = QtWidgets.QPushButton(w)
btn.setText('按我按我!!')
btn.move(300,300)

def go():
    text = label_input.text()
    sel_text = sel.currentText()
    textarea.setText(f'{text} / {sel_text}')

btn.clicked.connect(go)



w.show()
sys.exit(app.exec())