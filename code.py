from datetime import datetime
class Task:
    def __init__(self,id,title,created_at,done:bool = False):
        self.id = id
        self.title = title
        self.created_at = datetime.now()
        self.done = done

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self,task:Task):
        self.tasks[task.id] = task
    def show_task(self, id):
        if id in self.tasks:
            return self.tasks.get(id)
    def show_all_tasks(self):
        print(self.tasks.values())
    def delete_task(self,id):
        if id in self.tasks:
            del self.tasks[id]
    def update_task(self,id,new_title:str):
        if id in self.tasks:
            self.tasks[id].title = new_title
    def mark_task_as_done(self,id):
        if id in self.tasks:
            self.tasks[id].done = True

manager = TaskManager()
task1 = Task(1,"Study Python",datetime.now())
task2 = Task(2,"Write Code",datetime.now())    
task3 = Task(3,"Test Code",datetime.now())
task4 = Task(4,"Debug Code",datetime.now())
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)     
manager.add_task(task4)
manager.show_all_tasks()
manager.update_task(1,"Study Python and Django")
manager.mark_task_as_done(2)



    


