import json
from time import *


class Task:
    def __init__(self, description):
        self.id = self._creatID()
        self.description = description
        self.status = 'to-do'

        year, month, day = localtime()[0], localtime()[1], localtime()[2]
        hour, minutes = localtime()[3], localtime()[4]
        self.createdAt = f"{year}.{month}.{day}, {hour}:{minutes}"
        self.updatedAt = self.createdAt


    def _successfully_task_create(self):
        pass


    def _creatID(self):
        return 1
  


test_task = Task(
    name = 'test',
    description = 'something'
)

print(test_task.createdAt)