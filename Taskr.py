from src.util.nr_fileutil import TaskManagerFileAsserter as FileAsserter;
from src.TaskContainer import TaskContainer;
from src.primitives.AppStatus import AppStatus, APP_ERROR, APP_SUCCESS;
import os;
import json;
import logging;

class TaskrApp:
    __slots__ = ['manager', 'container', 'path'];
    
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
    
    def abort(self):
        """Unspecified error exit"""
        exit(APP_ERROR);
    
     
        
if __name__ == '__main__':
    App = TaskrApp();
    
    App.run();
    
    App.close();
    
    