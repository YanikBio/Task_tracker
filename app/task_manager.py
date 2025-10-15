import json
from app.task import Task


class TaskManager:
    def __init__(self):
        self.memory_file = 'all_tasks.json'
        self.all_memory = ''

        self.task_count = 0  # общее кол-во задач
        self.todo_tasks = 0  # количество неначатых задач
        self.in_progress_tasks = 0  # кол-во начатых задач
        self.done_tasts = 0  # кол-во сделанных задач

        self.all_tasks = 0 # все задачи с объетками класса Task

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
                except json.decoder.JSONDecodeError:
                    self.all_memory = []
                    print("Memory file is empty")

        except FileNotFoundError:
            with open(self.memory_file, 'w') as memory_file:
                print("Memory file is created")
                self.all_memory = []


    def add(self, task_name):
        '''Функция для добавления новой Task'''
        task_id = self.task_count + 1
        new_task = Task(task_id, task_name)
        new_task.show()

        with open(self.memory_file, 'w') as memory_file:
            pass


    def update(self):
        ...


    def delite(self):
        ...


    def show(self):
        ...