class AppStatus:
    def __init__(self, name: str, value: int) -> None:
        self.name = name;
        self.value = value;
    
    def __str__(self) -> str:
        return str(self.value);
    
    def __repr__(self) -> str:
        return str(self);
    
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.value == other.value;
    
    def __lt__(self, other) -> bool:
        return self.name < other.name and self.value < other.value;
    
    def __gt__(self, other) -> bool:
        return self.name > other.name and self.value > other.value;
    
    def __neq__(self, other) -> bool:
        return not (self == other);
    

#   DEFAULT AppStatus
APP_SUCCESS     :   AppStatus   =   AppStatus("APP_SUCCESS"     ,   0);
APP_ERROR       :   AppStatus   =   AppStatus("APP_ERROR"       ,  -1);
    