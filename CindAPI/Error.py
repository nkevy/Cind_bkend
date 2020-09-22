###############
## Noah Kevy ##
## 2020      ##
###############
import logging 
import psycopg2 as psy

# define error type AssociationError
# thrown when using Association.py
class AssociationError(Exception):
    def __init__(self, expression = None, message = "Association error"):
        self.expression = expression
        self.message = message

# define error type WordsError
# thrown when using Words.py
class WordsError(Exception):
    def __init__(self, expression = None, message = "words error"):
        self.expression = expression
        self.message = message

# define an error for forbiden
# thrown by methods checking string input
class ForbidenError(Exception):
    def __init__(self, expression = None, message = "forbiden error string not valid"):
        self.expression = expression
        self.message = message

# check if a string contains forbiden char(s) 
# raise tyoe error
def forbiden(ss = None):
    if ss is None:
        raise TypeError
    if not isinstance(ss,str):
        raise TypeError
    avoid = [',','.','/','\\','[',']','+','-','=','\'','\"',';',':','?','!','@','#','$',' ','{','}']
    return any(item in ss for item in avoid)

#EOF
