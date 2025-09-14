from PyQt6 import QtWidgets
import random
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.setWindowTitle('樂透自動選號機')
w.resize(500,400)
w.setStyleSheet('''
    font-size: 24px
''')

lotto = QtWidgets.QPushButton(w)
super_lotto = QtWidgets.QPushButton(w)
result = QtWidgets.QTextEdit(w)

lotto.setText('大樂透')
super_lotto.setText('威力彩')

layout = QtWidgets.QFormLayout(w)
layout.addRow(lotto)
layout.addRow(super_lotto)
layout.addRow(result)



def generate_lotto():
    r = random.sample(range(1,50),6)
    result_txt = ','.join(str(i) for i in r)
    result.setText(f'您的大樂投選號結果為\n{result_txt}\n特別號為\n{r[-1]}')

def generate_super_lotto():
    one = random.sample(range(1,39),6)
    two = random.sample(range(1,9),1)
    one_txt = ','.join(str(i) for i in one)
    two_txt = two[0]
    result.setText(f'您的威力彩選號結果為第一區\n{one_txt}\n第二區為\n{two_txt}')

lotto.clicked.connect(generate_lotto)
super_lotto.clicked.connect(generate_super_lotto)

w.show()
sys.exit(app.exec())