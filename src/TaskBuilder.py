from primitives.Task import Task, RandomTask;
from primitives.TaskPriority import TaskPriority as Priority;
from datetime import datetime;

class TaskBuilder:
    @staticmethod
    def build(name: str, description: str, priority:str, due_date:str, completed: str) -> Task:
        #   Priority assignment
        #   Accepts both numeric and string values
        #   Numeric
        if(len(priority) == 1):
            priority = Priority.getPriorities()[int(priority)];
        #   String
        else:
            priority = Priority.getPriorityFromName(priority);

        if(due_date):
            due_date = due_date.split("-");
            due_date = datetime(int(due_date[0]), int(due_date[1]), int(due_date[2]));
            
        return Task(name, description, bool(completed), due_date, priority);