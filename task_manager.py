from task import Task
from datetime import datetime

class task_manager():

    def __init__(self, tasks_path):
        self.tasks_path = tasks_path
        self.list_of_tasks = []

    def load_tasks(self):
        pass

    def add_task(self, task):
        self.list_of_tasks.append(task)

    def delete_task(self, task_id):
        try:
            self.list_of_tasks.pop(task_id)
        except IndexError:
            print("Non-existent task")

    def read_task(self, task_id):
        try:
            return self.list_of_tasks[task_id]
        except IndexError:
            print("Non-existent task")

    def update_task(self, task):
        pass

    def print_tasks(self):
        
        if not (self.list_of_tasks.__len__()):
            print("No tasks registered!")
        else:
            print("\nList of tasks\n")
            for task in self.list_of_tasks:
                print(task.__str__())

    def get_all_tasks(self):
        return self.list_of_tasks

task_1 = Task({"id": 1, "task": "Leer libro de matematicas", "description": "Descripcion 1", "limit_date": datetime.now()})
task_2 = Task({"id": 2, "task": "Buscar nuevo libro", "description": "Descripcion 2", "limit_date": datetime(2021, 10, 3)})

# task_manager_1 = task_manager("")
# task_manager_1.add_task(task_1)
# task_manager_1.add_task(task_2)
# task_manager_1.print_tasks()
# task_manager_1.delete_task(2)
# task_manager_1.print_tasks()
# print(task_manager_1.read_task(1).__repr__())