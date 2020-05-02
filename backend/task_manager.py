from datetime import datetime

class Task():

    def __init__(self, task_data):
        
        self.id = task_data["id"]
        self.task_info = task_data["task"]
        self.description = task_data["description"]
        self.done = False
        self.limit_date = task_data["limit_date"]
    
    def __repr__(self):
        return {"id": self.id,
                "task": self.task_info,
                "description": self.description,
                "done": self.done,
                "limit_date": self.limit_date
        }
    
    def __str__(self):
        return "\t[+] Number: {}\n\t    Task: {}\n\t    Limit date: {}\n\t    Done: {}\n\t".format(self.id, self.task_info, self.limit_date, self.done)
    
    def check_expired_date(self, date):
        if (self.limit_date > date):
            return True
        return False

    def update_info_task(self, new_task):
        self.task_info = new_task

    def update_limit_date(self, new_limit_date):
        self.limit_date = new_limit_date
    
    def update_description_task(self, new_description):
        self.description = new_description
    
    def set_task_as_done(self):
        self.done = True

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

            new_task_id = 0

            for task_it in range(0, len(self.list_of_tasks)):
                self.list_of_tasks[new_task_id].id = new_task_id
                new_task_id += 1
                
        except IndexError:
            print("Non-existent task")

    def read_task(self, task_id):
        try:
            return self.list_of_tasks[task_id]
        except IndexError:
            print("Non-existent task")

    def update_task(self, task_id, updated_task):
        try:
            self.list_of_tasks[task_id] = updated_task
        except IndexError:
            print("Non-existent task, task {} cannot be replaced!".format(task_id))

    def print_tasks(self):
        
        if not (self.list_of_tasks.__len__()):
            print("No tasks registered!")
        else:
            print("\nList of tasks\n")
            for task in self.list_of_tasks:
                print(task.__str__())

    def get_all_tasks(self):
        return self.list_of_tasks
    
    def get_number_done_undone_tasks(self):
        number_undone_tasks = 0
        number_done_tasks = 0

        for task_it in self.list_of_tasks:
            if (task_it.done):
                number_done_tasks +=1
            else:
                number_undone_tasks +=1
        
        return number_done_tasks, number_undone_tasks

def main():
    task_1 = Task({"id": 1, "task": "Leer libro de matematicas", "description": "Descripcion 1", "limit_date": datetime.now()})
    task_2 = Task({"id": 2, "task": "Buscar nuevo libro", "description": "Descripcion 2", "limit_date": datetime(2021, 10, 3)})
    task_3 = Task({"id": 2, "task": "Buscar nuevo libro", "description": "Descripcion 2", "limit_date": datetime(2019, 10, 3)})

    print(task_3.check_expired_date(datetime.now()))

    task_manager_1 = task_manager("")
    task_manager_1.add_task(task_1)
    task_manager_1.add_task(task_2)
    task_manager_1.print_tasks()
    task_manager_1.delete_task(2)
    task_manager_1.print_tasks()
    print(task_manager_1.read_task(1).__repr__())

if __name__ == "__main__":
    main()