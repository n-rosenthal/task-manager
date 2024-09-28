"""nr_fileutil_20240927 (TaskManagerFileAsserter)
"""

import os;
import json;

class FileAsserter:
    """Asserts the existence of files and directories necessary for running an application.
    """
    def __init__(self) -> None:
        pass;
    
    def chkFile(self, file: str) -> bool:
        """Returns True if `file` exists.
        """
        if(os.path.exists(file)):
            return True;
        return False;
    
    def assertDir(self, dir:str) -> int:
        """Asserts that `dir` exists.

        Args:
            dir (str): directory's path

        Returns:
            int:    0,  if `dir` already existed
                    1,  if it was necessary to create `dir`
                    2,  if an error occurred
        """
        if(os.path.exists(dir)):
            return 0;
        else:
            try:
                os.mkdir(dir);
                return 1;
            except Exception as e:
                print(e);
            finally:
                return 2;
    
    def assertFile(self, file: str) -> int:
        """Asserts that `file` exists.

        Args:
            file (str): file's path

        Returns:
            int:    0,  if `file` already existed
                    1,  if it was necessary to create `file`
                    2,  if an error occurred
        """
        if(not self.chkFile(file)):
            try:
                with open(os.path(file), "w") as f:
                    pass;
                return 1;
            except Exception as e:
                print(e);
            finally:
                return 2;
        return 0;
    
class TaskManagerFileAsserter(FileAsserter):
    TaskManager_DEFAULT_DIR:str         =   ".taskr";
    TaskManager_DEFAULT_TASKS_FILE:str  =   ".tasks.json";
    
    
    def __init__(self) -> None:
        super().__init__();
        
        if(not self.chkFile(self.TaskManager_DEFAULT_DIR)):
            self.assertDir(self.TaskManager_DEFAULT_DIR);
        
        if(not self.chkFile(os.path.join(self.TaskManager_DEFAULT_DIR, self.TaskManager_DEFAULT_TASKS_FILE))):
            self.assertFile(os.path.join(self.TaskManager_DEFAULT_DIR, self.TaskManager_DEFAULT_TASKS_FILE));
    
    def assertFile(self, file: str) -> int:
        try:
            with open(os.path.join(file), "w") as f:
                f.write(json.dumps({"tasks": []}));
                return 0;
        except Exception as e:
            print(e);
            return 1;
        
    @property
    def path(self) -> str:
        return os.path.join(self.TaskManager_DEFAULT_DIR, self.TaskManager_DEFAULT_TASKS_FILE);
        
if __name__ == '__main__':
    fasserter = TaskManagerFileAsserter();