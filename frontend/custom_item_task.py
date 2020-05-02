from PyQt5 import QtGui, QtWidgets, QtCore
from datetime import datetime

class DateDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        # nice widget for editing the date
        self.datetime = QtWidgets.QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QtCore.QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        # OK and Cancel buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def dateTime(self):
        return self.datetime.dateTime()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.toPyDateTime(), result == QtWidgets.QDialog.Accepted)

class QTaskItem (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QTaskItem, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.text_id_task    = QtWidgets.QLabel()
        self.text_task_info  = QtWidgets.QLabel()
        self.text_task_date_limit  = QtWidgets.QLabel()
        self.text_task_on_time  = QtWidgets.QLabel()

        self.textQVBoxLayout.addWidget(self.text_id_task)
        self.textQVBoxLayout.addWidget(self.text_task_info)
        self.textQVBoxLayout.addWidget(self.text_task_date_limit)
        self.textQVBoxLayout.addWidget(self.text_task_on_time)

        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        
        # setStyleSheet
        # self.text_id_task.setStyleSheet('''
        #     color: rgb(0, 0, 255);
        # ''')
        # self.text_task_info.setStyleSheet('''
        #     color: rgb(255, 0, 0);
        # ''')

    def setTaskId (self, id):
        self.text_id_task.setText("Task °{}".format(id))

    def setTaskInfo (self, info):
        self.text_task_info.setText("{}".format(info))
    
    def setTaskDate (self, date):
        self.text_task_date_limit.setText(date.strftime("%a %d %b %y %I:%M %p"))

    def setTaskIcon (self, imagePath):
        pixmap = QtGui.QPixmap(imagePath)
        # pixmap = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        self.iconQLabel.setPixmap(pixmap)

    def setTaskOnTime(self, task):
        taskOnTime = task.check_expired_date(datetime.now())

        if (taskOnTime):
            self.text_task_on_time.setText("On Time!")

            self.text_task_on_time.setStyleSheet('''
                color: rgb(0, 255, 0);
            ''')
        else:
            self.text_task_on_time.setText("Late!")

            self.text_task_on_time.setStyleSheet('''
                color: rgb(255, 0, 0);
            ''')