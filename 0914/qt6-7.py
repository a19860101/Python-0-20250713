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
def getfile():
    # result = QtWidgets.QFileDialog.getOpenFileName(filter='python(*.py)')
    # result = QtWidgets.QFileDialog.getOpenFileName(filter='JPG(*.jpg);;PNG(*.png)')
    # result = QtWidgets.QFileDialog.getOpenFileName(filter='圖片檔案(*.jpg *.jpeg *.png *.gif *.webp)')
    result = QtWidgets.QFileDialog.getOpenFileNames(filter='圖片檔案(*.jpg *.jpeg *.png *.gif *.webp)')
    print(result)

btn = QtWidgets.QPushButton(w)
btn.setText('選擇檔案')

btn.clicked.connect(getfile)

w.show()
sys.exit(app.exec())