from src.util.nr_fileutil import TaskManagerFileAsserter as FileAsserter;
from src.TaskContainer import TaskContainer;
from src.primitives.AppStatus import AppStatus, APP_ERROR, APP_SUCCESS;
import os;
import json;
import logging;

class TaskrApp:
    __slots__ = ['manager', 'container', 'path', 'frontend'];
    
    def __init__(self) -> None:
        #   Assign container object to store tasks
        self.container  = TaskContainer();
        
        #   Invokes the FileAsserter for managing files
        fileAsserter    =   FileAsserter();
        
        #   Get default filepath
        self.path = os.path.join(fileAsserter.TaskManager_DEFAULT_DIR, fileAsserter.TaskManager_DEFAULT_TASKS_FILE);
        
        #   Assert path existence
        st:AppStatus = self.__assert();
        if(not(st)):
            self.abort();
        else:
            #   Load tasks from file
            st = self.__load();
        
    def __assert(self) -> AppStatus:
        """Asserts the existence of the necessary files for the App.
        """
        try:
            with open(self.path, "r") as f:
                self.container.from_dict(json.loads(f.read()));
                return APP_SUCCESS;
        except Exception as e:
                logging.error(f"Couldn't load tasks from JSON file: {e}");
    
    def __load(self) -> AppStatus:
        """Loads the tasks from the tasks file to the Container object

        Returns:
            AppStatus
        """
        try:
            with open(self.path, "r") as f:
                self.container = self.container.from_dict(json.loads(f.read()));
                return APP_SUCCESS;
        except Exception as e:
            logging.error(f"Error loading Taskr task file: {e}\n\nException Type: {e.__class__}");
            return APP_ERROR;
    
    def run(self) -> None:
        status:AppStatus = APP_SUCCESS;
        
        #   Initialize the front-end
        self.frontend = TaskrFrontEnd(self.container);
        self.frontend.present();
        self.frontend.showMenu();
        
        while(status == APP_SUCCESS):
            option, status = self.frontend.select();
            
            if(status == APP_SUCCESS):
                self.frontend.exec(option)
    
    def abort(self):
        """Unspecified error exit"""
        exit(APP_ERROR);


class TaskrFrontEnd:
    def __init__(self, container: TaskContainer) -> None:
        self.container = container;
        
    def present(self) -> None:
        print(f"{"-"*64}\n{"\t"*4}Taskr v. 0.0.1\n\n{"-"*64}");
        
    def showMenu(self) -> None:
        print(" 1.  View all tasks");
        print(" 2.  Get a task");
        print(" 3.  Add a task");
        print(" 4.  Edit a task");
        print(" 5.  Remove a task");
        print(" 6.  Quit");
    
    
    def select(self) -> tuple[str, AppStatus]:
        option = input("\n >  ");
        
        if(int(option) in range(1,7)):
            return (int(option), APP_SUCCESS);
        return (None, APP_ERROR);
    
    
    
    def exec(self, option:int) -> AppStatus:
        if(option == 1):
            self.__printAllTasks();
            return APP_SUCCESS;
                
        elif(option == 2):
            self.__printAllTasks();
            option = input(" >  Select index: ");
            
            if(option > 0 and option-1 < len(self.container)):
                print(self.container[option-1]);
                print(self.container[option-1].to_dict());
                return APP_SUCCESS
            else:
                print(" >  Invalid index for task");
                return APP_ERROR
        else:
            raise NotImplementedError;
            return APP_ERROR;
            
            
    def __printAllTasks(self) -> None:    
        counter = 1;
            
        for task in self.container.tasks:
            print(f"{counter:4d} \t {task}");
            
            
            counter += 1;
if __name__ == '__main__':
    App = TaskrApp();
    
    App.run();
    
    App.close();
    
    