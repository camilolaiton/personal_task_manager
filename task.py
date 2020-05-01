
from datetime import datetime

class Task():

    def __init__(self, task_data):
        
        self.id = task_data["id"]
        self.task = task_data["task"]
        self.description = task_data["description"]
        self.done = False
        self.limit_date = task_data["limit_date"]
    
    def check_expired_date(self, date):
        if (self.limit_date < date):
            return True
        return False

    def update_limit_date(self, new_limit_date):
        self.limit_date = new_limit_date
    
    def update_description_task(self, new_description):
        self.description = new_description
    
    def set_task_as_done(self):
        self.done = True

    def __repr__(self):
        return {"id": self.id,
                "task": self.task,
                "description": self.description,
                "done": self.done,
                "limit_date": self.limit_date
        }
    
    def __str__(self):
        return "\t[+] Number: {}\n\t    Task: {}\n\t    Limit date: {}\n".format(self.id, self.task, self.limit_date)

# task_1 = Task({"id": 1, "task": "prueba", "description": "esta es una description", "limit_date": datetime.now()})
# print(task_1.limit_date)
# print(task_1.check_expired_date(datetime(2010, 5, 30)))