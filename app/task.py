import json
from time import *


class Task:
    def __init__(self, task_id, description, status='', createdAt='', updatedAt=''):
        self._task_id = task_id
        self._description = description

        if not status:     
            self._status = 'todo'
        else:
            self._status = status

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
    

    @property
    def status(self):
        return self._status
    

    @property
    def task_id(self):
        return self._task_id
    

    @property
    def description(self):
        return self._description
    
    
    def update_description(self, new_description):
        self._description = new_description


    def update_status(self, new_status):
        self._status = new_status
    

    def update_time(self):
        year, month, day = localtime()[0], localtime()[1], localtime()[2]
        hour, minutes = localtime()[3], localtime()[4]
        self.updatedAt = f"{year}.{month}.{day}, {hour}:{minutes}"
    

    def show(self):
        print(f"\nTAKS_ID: {self.task_id}\nDESCRIPTION: {self.description}\nSTATUS: {self.status}\nCREATEDAT: {self.createdAt}\nUPDATEDAT: {self.updatedAt}\n")
