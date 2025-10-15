import json
from time import *


class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.status = 'to-do'

        year, month, day = localtime()[0], localtime()[1], localtime()[2]
        hour, minutes = localtime()[3], localtime()[4]
        self.createdAt = f"{year}.{month}.{day}, {hour}:{minutes}"
        self.updatedAt = self.createdAt


    
    def save_task(self):
        '''Функция для преобразования объекта в json формат, который будет хранится в all_tasks.json'''
        return 
    

    def show(self):
        print(f"\nTAKS_ID: {self.task_id}\nDESCRIPTION: {self.description}\nSTATUS: {self.status}\nCREATEDAT: {self.createdAt}\n")

  


# test_task = Task(
#     name = 'test',
#     description = 'something'
# )

# print(test_task.createdAt)