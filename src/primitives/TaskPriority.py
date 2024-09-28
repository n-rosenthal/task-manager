from enum import Enum;


class TaskPriority(Enum):
    """TaskPriority is a enumeration of possible values for task priorities:
        -   0,  lowest priority;
        -   1,  low priority;
        -   2,  medium priority;
        -   3,  high priority;
        -   4,  highest priority;
        -   5,  urgent priority;
    """
    LOWEST = 0,
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3,
    HIGHEST = 4,
    URGENT = 5
    
    @staticmethod
    def getUnicode(priority) -> str:
        if(priority == TaskPriority.LOWEST):
            return "⏬️";
        elif(priority == TaskPriority.LOW):
            return "🔽";
        elif(priority == TaskPriority.MEDIUM):
            return "🔼";
        elif(priority == TaskPriority.HIGH):
            return "⏫";
        elif(priority == TaskPriority.HIGHEST):
            return "🔺";
        elif(priority == TaskPriority.URGENT):
            return "🔺🔺🔺";
        else:
            return "⏬️";
        
    @staticmethod
    def getPriorities() -> list:
        return [TaskPriority.LOWEST, TaskPriority.LOW, TaskPriority.MEDIUM, TaskPriority.HIGH, TaskPriority.HIGHEST, TaskPriority.URGENT];
    
    @staticmethod
    def getPriorityFromName(name: str):
        for p in TaskPriority.getPriorities():
            if(name == p.name):
                return p;
        return TaskPriority.LOWEST;
    
    @property
    def name(self) -> str:
        return str(self).split(".")[1];
    
    def __lt__(self, other):
        return self.value < other.value;