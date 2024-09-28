from src.primitives.Task import Task, RandomTask;

class TaskContainer:
    """A list-like container for Task objects"""
    def __init__(self) -> None:
        self.tasks = [];
        
    def insert(self, task: Task):
        self.tasks.append(task);
    
    def remove(self, task: Task):
        self.tasks.remove(task);
    
    def edit(self, src: Task, new: Task):
        self.remove(src);
        self.insert(new);
    
    def to_dict(self):
        return {
            "tasks": [task.to_dict() for task in self.tasks]
        };
        
    @staticmethod
    def from_dict(data):
        container = TaskContainer();
        for task_data in data["tasks"]:
            container.add_task(Task.from_dict(task_data));
        return container;
    
    def __str__(self):
        return "\n".join([str(task) for task in self.tasks]);
    
    def __repr__(self):
        return self.__str__();
    
    def __len__(self):
        return len(self.tasks);
    
    def __getitem__(self, index):
        return self.tasks[index];
    
    def __iter__(self):
        return iter(self.tasks);
    
    def __contains__(self, task:Task):
        return task in self.tasks;
    

if __name__ == '__main__':
    container = TaskContainer();
    
    for i in range(0, 11):
        container.insert(RandomTask());
    
    print(len(container));