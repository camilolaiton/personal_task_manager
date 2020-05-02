from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
import re

import sys
sys.path.append("../")

from backend.task_manager import task_manager, Task
from datetime import datetime
from custom_item_task import QTaskItem, DateDialog
 
class Window(QDialog):
    def setupUi(self, personal_task_manager, task_manager):
        personal_task_manager.setWindowTitle("Personal Task Manager - Camilo Laiton")
        personal_task_manager.setObjectName("personal_task_manager")
        personal_task_manager.resize(600, 600)

        self.task_manager = task_manager

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(personal_task_manager)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(personal_task_manager)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton(personal_task_manager)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton(personal_task_manager)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        self.pushButton_remove = QtWidgets.QPushButton(personal_task_manager)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_done = QtWidgets.QPushButton(personal_task_manager)
        self.pushButton_done.setObjectName("pushButton_done")
        self.verticalLayout.addWidget(self.pushButton_done)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(personal_task_manager)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
 
        self.retranslateUi(personal_task_manager)
        QtCore.QMetaObject.connectSlotsByName(personal_task_manager)
        self.pushButton_add.clicked.connect(self.add_task)
        self.pushButton_edit.clicked.connect(self.edit_task)
        self.pushButton_remove.clicked.connect(self.remove_task)
        self.pushButton_done.clicked.connect(self.done_task)
        self.pushButton_close.clicked.connect(self.close_window)
 
        self.set_tasks()
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Employee"))
        Dialog.setWindowIcon(QIcon("icon.png"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_edit.setText(_translate("Dialog", "Edit"))
        self.pushButton_remove.setText(_translate("Dialog", "Remove"))
        self.pushButton_done.setText(_translate("Dialog", "Mask as Done"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
    
    @staticmethod
    def create_personalized_task_item(task):
        myQTaskItem = QTaskItem()
        myQTaskItem.setTaskId(task.id)
        myQTaskItem.setTaskInfo(task.task_info)
        myQTaskItem.setTaskDate(task.limit_date)
        myQTaskItem.setTaskOnTime(task)
        myQTaskItem.setTaskIcon("images/task_image.png")

        return myQTaskItem

    def get_task_id_selected_custom_item(self):
        row = self.listWidget.currentRow()
        widget = self.listWidget.itemWidget(self.listWidget.item(row))
        result_re_search = re.findall('([0-9]{1,2})', widget.text_id_task.text())

        return row, int(result_re_search[0])

    def set_tasks(self):
        
        self.listWidget.clear()

        for task_it in self.task_manager.list_of_tasks:
            print(task_it.__str__())

            if not (task_it.done):
                myQTaskItem = Window.create_personalized_task_item(task_it)
                myQListWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
                # Set size hint
                myQListWidgetItem.setSizeHint(myQTaskItem.sizeHint())
                # Add QListWidgetItem into QListWidget
                self.listWidget.addItem(myQListWidgetItem)
                self.listWidget.setItemWidget(myQListWidgetItem, myQTaskItem)

        self.listWidget.setCurrentRow(0)
 
    def add_task(self):
        
        task_info, ok_task_info = QInputDialog.getText(self, "Task edit", "Edit Task Information",
                                        QLineEdit.Normal, "")
        
        if ok_task_info and task_info != None:
            print("{}".format(task_info))
        
        task_description, ok_task_description = QInputDialog.getText(self, "Task edit", "Edit Task Description",
                                        QLineEdit.Normal, "")
        
        if ok_task_description and task_description != None:
            print("{}".format(task_description))

        task_limit_date, ok_task_limit_date = DateDialog.getDateTime()

        if ok_task_limit_date:
            print("{}".format(task_limit_date))

        new_task = Task({"id": len(self.task_manager.list_of_tasks), "task": task_info, "description": task_description, "limit_date": task_limit_date})
        self.task_manager.add_task(new_task)
        self.set_tasks()

    def edit_task(self):
        row_list, real_task_id = self.get_task_id_selected_custom_item()
        gotten_task = self.task_manager.read_task(real_task_id)

        if gotten_task is not None:
            task_info, ok_task_info = QInputDialog.getText(self, "Task edit", "Edit Task Information",
                                              QLineEdit.Normal, gotten_task.task_info)
            
            if not ok_task_info or task_info == None:
                return
            
            task_description, ok_task_description = QInputDialog.getText(self, "Task edit", "Edit Task Description",
                                              QLineEdit.Normal, gotten_task.description)
            
            if not ok_task_description or task_description == None:
                return

            task_limit_date, ok_task_limit_date = DateDialog.getDateTime()

            if not ok_task_limit_date:
                return
            
            gotten_task.task_info = task_info
            gotten_task.description = task_description
            gotten_task.limit_date = task_limit_date
            self.task_manager.update_task(gotten_task.id, gotten_task)
            self.set_tasks()

    def remove_task(self):
        row_list, real_task_id = self.get_task_id_selected_custom_item()
 
        reply = QMessageBox.question(self, "Remove task", "Are you sure you want to remove this task? ",
                QMessageBox.Yes|QMessageBox.No)

        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row_list)
            self.task_manager.delete_task(real_task_id)
            del item
            self.set_tasks()
  
    # def up(self):
    #     row = self.listWidget.currentRow()
    #     if row >= 1:
    #         item = self.listWidget.takeItem(row)
    #         self.listWidget.insertItem(row - 1, item)
    #         self.listWidget.setCurrentItem(item)
 
    # def down(self):
    #     row = self.listWidget.currentRow()
    #     if row < self.listWidget.count() - 1:
    #         item = self.listWidget.takeItem(row)
    #         self.listWidget.insertItem(row + 1, item)
    #         self.listWidget.setCurrentItem(item)
 
    def done_task(self):
        row_list, real_task_id = self.get_task_id_selected_custom_item()

        number_done_tasks, number_undone_tasks = self.task_manager.get_number_done_undone_tasks()

        print(number_done_tasks, number_undone_tasks)

        if (number_undone_tasks):
            modified_task = self.task_manager.read_task(real_task_id)
            modified_task.done = True
            self.task_manager.update_task(real_task_id, modified_task)
            self.set_tasks()
 
    def close_window(self):
        quit()
 
if __name__ == "__main__":
    task_1 = Task({"id": 0, "task": "Read Elon Musk's book", "description": "Descripcion 1", "limit_date": datetime.now()})
    task_2 = Task({"id": 1, "task": "Search Camilo Laiton on Internet", "description": "Descripcion 2", "limit_date": datetime(2021, 10, 3)})
    task_3 = Task({"id": 2, "task": "Finish The Avengers's movie", "description": "Descripcion 3", "limit_date": datetime(2020, 4, 4, 9, 30)})
    task_4 = Task({"id": 3, "task": "Search University of Magdalena on Google", "description": "Descripcion 3", "limit_date": datetime(2020, 5, 4, 9, 30)})

    task_manager_1 = task_manager("")
    task_manager_1.add_task(task_1)
    task_manager_1.add_task(task_2)
    task_manager_1.add_task(task_3)
    task_manager_1.add_task(task_4)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog, task_manager_1)
    Dialog.show()
    sys.exit(app.exec_())