from dataclasses import dataclass;
from datetime import datetime

from src.primitives.TaskPriority import TaskPriority as Priority;

@dataclass
class Task:
    """A Task is a data object responsible for modelling tasks.
    """
    name        :str;
    description :str;
    completed   :bool       =   False;
    dueDate     :datetime   =   None;
    priority    :Priority   =   Priority.LOW;
    CALENDAR_UNICODE:str    =   r"📅";
    
    @staticmethod
    def fromDict(data:dict) -> None:
        if(data["due_date"]):
            return Task(
                data["name"],
                data["description"],
                data["completed"],
                datetime.strptime(data["due_date"], "%Y-%m-%d"),
                Priority.getPriorityFromName(data["priority"]),
            );
        else:
            return Task(
                data["name"],
                data["description"],
                data["completed"],
                data["due_date"],
                Priority.getPriorityFromName(data["priority"]),
            );
        
    def to_dict(self):
        if(self.dueDate):        
            return {
                "name": self.name,
                "description": self.description,
                "priority": self.priority.name,
                "due_date": datetime.strftime(self.dueDate, "%Y-%m-%d"),
                "completed": self.completed,
            };
        else:
            return{
                "name": self.name,
                "description": self.description,
                "priority": self.priority.name,
                "due_date": None,
                "completed": self.completed,
            };
    
    def __eq__(self, other) -> bool:
        return (self.name == other.name) and (self.description == other.description);
    
    def __str__(self) -> str:
        repr:str = "";
        
        if(self.completed):
            repr += " - [x] ";
        else:
            repr += " - [ ] ";
        
        try:
            repr += f"{self.priority.getUnicode(self.priority)} [{self.name}] {self.description}";
        except AttributeError:
            print(f"AttributeError: {self.priority}");
        
        
        if(self.dueDate):
            return repr + f" {self.CALENDAR_UNICODE} {self.dueDate}";
        return repr;

class RandomTask(Task):
    """RandomTask class implementation for testing purposes
    """    
    def __init__(self):
        from util.nr_random import getRandomString, getRandomDigitString, getRandomDatetime;
        from random         import choice;
        
        
        name        :str=getRandomString(6);
        description :str=getRandomString(10);
        completed   :bool=choice([True, False]);
        dueDate     :datetime=getRandomDatetime();
        priority    :Priority=choice([Priority.LOWEST, Priority.LOW, Priority.MEDIUM, Priority.HIGH, Priority.HIGHEST, Priority.URGENT]);
        super().__init__(name, description, completed, dueDate, priority);
    