# tkinter 內建
# pip install PyQt6

from PyQt6 import QtWidgets
import sys

# 建立應用程式
app = QtWidgets.QApplication(sys.argv)

# 建立視窗
w = QtWidgets.QWidget()

# 設定標題
w.setWindowTitle('哈囉 python')

# 設定視窗大小
w.resize(500,400)

# 顯示
w.show()

# 執行
sys.exit(app.exec())