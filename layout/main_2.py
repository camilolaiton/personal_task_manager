# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_task.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_personal_task_manager(object):
    def setupUi(self, personal_task_manager):
        personal_task_manager.setObjectName("personal_task_manager")
        personal_task_manager.resize(791, 562)
        personal_task_manager.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.029, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(personal_task_manager)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxTask = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTask.setGeometry(QtCore.QRect(-1, 9, 791, 471))
        self.groupBoxTask.setMaximumSize(QtCore.QSize(791, 471))
        self.groupBoxTask.setObjectName("groupBoxTask")
        self.listWidgetTask = QtWidgets.QListWidget(self.groupBoxTask)
        self.listWidgetTask.setGeometry(QtCore.QRect(0, 20, 791, 451))
        self.listWidgetTask.setMaximumSize(QtCore.QSize(791, 451))
        self.listWidgetTask.setObjectName("listWidgetTask")
        self.createTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.createTaskButton.setGeometry(QtCore.QRect(0, 490, 791, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.createTaskButton.setFont(font)
        self.createTaskButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.111, y1:0.514, x2:1, y2:0, stop:0.0157895 rgba(0, 227, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.createTaskButton.setObjectName("createTaskButton")
        personal_task_manager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(personal_task_manager)
        self.statusbar.setObjectName("statusbar")
        personal_task_manager.setStatusBar(self.statusbar)

        self.retranslateUi(personal_task_manager)
        QtCore.QMetaObject.connectSlotsByName(personal_task_manager)

    def retranslateUi(self, personal_task_manager):
        _translate = QtCore.QCoreApplication.translate
        personal_task_manager.setWindowTitle(_translate("personal_task_manager", "MainWindow"))
        self.groupBoxTask.setTitle(_translate("personal_task_manager", "List of Tasks"))
        self.createTaskButton.setText(_translate("personal_task_manager", "Create Task"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    personal_task_manager = QtWidgets.QMainWindow()
    ui = Ui_personal_task_manager()
    ui.setupUi(personal_task_manager)
    personal_task_manager.show()
    sys.exit(app.exec_())

