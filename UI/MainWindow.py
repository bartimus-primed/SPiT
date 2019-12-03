from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl
from PySide2.QtQuick import QQuickView


app = QApplication([])
view = QQuickView()
url = QUrl("UI/Main.qml")

view.setSource(url)
view.show()
app.exec_()
