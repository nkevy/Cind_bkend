###############
## Noah Kevy ##
## 2020      ##
###############
import logging 
import psycopg2 as psy

# define error type MemoriesError
# thrown when using Memory.py
class MemoriesError(Exception):
    def __init__(self, expression = None, message = "Memory error"):
        self.expression = expression
        self.message = message

# define error type WordsError
# thrown when using Words.py
class WordsError(Exception):
    def __init__(self, expression = None, message = "Words error"):
        self.expression = expression
        self.message = message

# define error type SleepError
# thrown when using Sleep.py
class SleepError(Exception):
    def __init__(self, expression = None, message = "Sleep Error"):
        self.expression = expression
        self.message = message

# define an error for forbiden
# thrown by methods checking string input
class ForbidenError(Exception):
    def __init__(self, expression = None, message = "Forbiden error string not valid"):
        self.expression = expression
        self.message = message

# check if a string contains forbiden char(s) 
# raise tyoe error
def forbiden(ss = None):
    if ss is None:
        raise TypeError
    if not isinstance(ss,str):
        raise TypeError
    avoid = [',','.','/','\\','[',']','+','-','=','\'','\"',';',':','?','!','@','#','$',' ','{','}','<','>']
    return any(item in ss for item in avoid)

#EOF
