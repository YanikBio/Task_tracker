import json
from time import *


class Task:
    def __init__(self, task_id, description, status='', createdAt='', updatedAt=''):
        self.task_id = task_id
        self.description = description

        if not status:     
            self.status = 'to-do'
        else:
            self.status = status

        year, month, day = localtime()[0], localtime()[1], localtime()[2]
        hour, minutes = localtime()[3], localtime()[4]
        # проверка для update уже имеющихся задач
        if not createdAt:
            self.createdAt = f"{year}.{month}.{day}, {hour}:{minutes}"
        else: 
            self.createdAt = createdAt
        
        if not updatedAt:
            self.updatedAt = self.createdAt
        else:
            self.updatedAt = updatedAt


    
    def to_json(self):
        '''Функция для преобразования объекта в json формат, который будет хранится в all_tasks.json'''
        json_task = [{
            "task_id": self.task_id,
            "description": self.description,
            "status": self.status,
            "created": self.createdAt,
            "updated": self.updatedAt
        }]
        return json_task
    
    
    def update_description(self, new_description):
        self.description = new_description
    

    def update_time(self):
        year, month, day = localtime()[0], localtime()[1], localtime()[2]
        hour, minutes = localtime()[3], localtime()[4]
        self.updatedAt = f"{year}.{month}.{day}, {hour}:{minutes}"
    

    def show(self):
        print(f"\nTAKS_ID: {self.task_id}\nDESCRIPTION: {self.description}\nSTATUS: {self.status}\nCREATEDAT: {self.createdAt}\n")

  


# test_task = Task(
#     name = 'test',
#     description = 'something'
# )

# print(test_task.createdAt)