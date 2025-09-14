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

## Line Edit 輸入文字框
label_input = QtWidgets.QLineEdit(w)

# Combo Box 下拉式
sel = QtWidgets.QComboBox(w)
sel.addItems(['test 1','test 2', 'test 3'])

# Text Edit 長文字輸入
textarea = QtWidgets.QTextEdit(w)

# Push Button
btn = QtWidgets.QPushButton(w)
btn.setText('按我按我!!')

layout = QtWidgets.QFormLayout(w)
layout.addRow(label, label_input)
layout.addRow(sel)
layout.addRow(textarea)
layout.addRow(btn)

def go():
    text = label_input.text()
    sel_text = sel.currentText()
    textarea.setText(f'{text} / {sel_text}')

btn.clicked.connect(go)



w.show()
sys.exit(app.exec())