"""Implements several random-output functions for testing and populating purposes
"""

from random import choice, random, randint, randrange;
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits;
from datetime import datetime;

def getRandomDatetime() -> datetime:
    try:
        dt = datetime(randint(1970,2024),
                      randint(1,12),
                      randint(1,29),
                      );
    except Exception:
        dt = datetime.now();
    finally:
        return dt;

def getRandomString(length: int) -> str:
    string = "";
    
    for i in range(length):
        string += choice(ascii_letters);
    
    return string;

def getRandomDigitString(length: int) -> str:
    string = "";
    
    for i in range(length):
        string += choice(digits);
        
    return string;

if __name__ == '__main__':
    print(getRandomDigitString(10));
    print(getRandomString(10));