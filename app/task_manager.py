import json
from app.task import Task


class TaskManager:
    def __init__(self):
        self.memory_file = 'all_tasks.json'
        self.all_memory = ''

        self.task_count = 0  # общее кол-во задач
        self.todo_tasks = 0  # количество неначатых задач
        self.in_progress_tasks = 0  # кол-во начатых задач
        self.done_tasks = 0  # кол-во сделанных задач

        self.last_id = 0

        self.all_tasks = [] # все задачи с объетками класса Task

        try:
            with open(self.memory_file, 'r') as memory_file:
                '''
                Здесь будет происходит считывание или создание памяти и считывание кол-ва задач, которые имеются в загашнике,
                сразу же определятся:
                - общее кол-во имеющихся задач
                - кол-во неначатых задач
                - кол-во начатых задач
                - кол-во законченых задач
                - список всех задач (в json формате, который будет поступать в функцию show() и показывать всё это пользователю)
                '''
                
                try:
                    self.all_memory = json.load(memory_file)
                    '''Всё буду хранить в виде объектов'''
                    for task in self.all_memory:
                        self.all_tasks.append(
                            Task(
                                task_id=task['task_id'],
                                description=task['description'],
                                status=task['status'],
                                createdAt=task['created'],
                                updatedAt=task['updated']
                            )
                        )
                        
                    self.task_count = len(self.all_tasks)  # забираем значение и берём все значения 
                    self.last_id = self.all_tasks[-1].task_id # забираю последнее значение id

                except json.decoder.JSONDecodeError:
                    self.all_memory = []
                    print("Memory file is empty")

        except FileNotFoundError:
            with open(self.memory_file, 'w') as memory_file:
                print("Memory file is created")
                memory_file.write('[]')
                self.all_memory = []

    
    def create_memory(self):
        '''Создаём новую память записывая снова всё в json'''
        self.all_memory = []
        for task in self.all_tasks:
            self.all_memory = self.all_memory + task.to_json()


    def remember(self):
        '''Функция для запоминания новой памяти'''
        with open(self.memory_file, 'w') as memory_file:
            json.dump(self.all_memory, memory_file, indent=4)


    def add(self, task_name):
        '''Функция для создания новой Task'''
        task_id = self.last_id + 1
        new_task = Task(task_id, task_name)
        new_task.show()

        json_new_task = new_task.to_json()
        self.all_memory = self.all_memory + json_new_task

        self.remember()


    def update(self, task_id, new_description):
        for task in self.all_tasks:
            if task.task_id == task_id:
                task.update_description(new_description)
                task.update_time()

                self.create_memory()
                self.remember()
                return
         
        else:
            print("NO TASK with such ID")


    def change_status(self, new_status, task_id):
        new_status = new_status.replace("mark-", "")
        for task in self.all_tasks:
            if task.task_id == task_id:
                task.update_status(new_status)
                task.show()
                
                self.create_memory()
                self.remember()
                return
        else:
            print("No task with such ID")
            
                

    def delite(self, task_id):
        for task in self.all_tasks:
            if task.task_id == task_id:
                self.all_tasks.remove(task)
                
                self.create_memory()
                self.remember()
                return
        else:
            print("NO TASK with such ID")
        
    

    def show_list(self, task_status=''):
        if task_status:
            for task in self.all_tasks:
                if task.status == task_status:
                    task.show()
        else:
            for task in self.all_tasks:
                task.show()
        



        