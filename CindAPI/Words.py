###############
## Noah Kevy ##
## 2020      ##
###############
from .Error import *
from .Postgres import *
import psycopg2 as psy
import logging 

class word:
    def __init__(self, w: str, c: str, n:str, o:str):
        self.value = w
        self.clock = c
        self.new = bool(n)
        self.old = bool(o)
    def __str__(self):
        return "{} {} {} {}".format(self.value, self.clock, self.new, self.old)

# convert word responce into word obj
# stop rewriteing code
def wordobj(wrd = None):
    if wrd is None:
        raise TypeError
    return word(wrd[0], wrd[1], wrd[2], wrd[3])

## format a responce list into a list of word objects
# stop rewriting code
def formatwordlist(wrds = None):
    if wrds is None:
        raise TypeError
    ret = []
    for item in wrds:
        ret.append(wordobj(item))
    return ret
    
# set a word to the Words table in the Mind
# rasie type error is wrd is not a string
# log error if cannot insert into words table
def Set(wrd: str):
        if forbiden(wrd):
            raise ForbidenError
        qry = "select clock from words where lect=\'"+str(wrd)+"\';"
        add_new = "insert into words(lect,clock,new,old) values(\'"+str(wrd)+"\',CURRENT_TIMESTAMP,true,false) returning clock;"
        add_old = "update words set clock=CURRENT_TIMESTAMP where lect=\'"+str(wrd)+"\';"
        con = None
        try: 
            con = psy.connect(
                host = "localhost",
                database = "mind",
                user = "postgres",
                password = "dirty")
            cur = con.cursor()
            cur.execute(qry)
            check = cur.fetchone()
            if check is None:
                cur.execute(add_new)
            else:
                cur.execute(add_old)
            cur.close()
            con.commit()
        except (Exception, psy.DatabaseError) as error:
            logging.basicConfig(filename='cindwords.log',level=logging.DEBUG)
            logging.debug(error)
        finally:
            if con is not None:
                con.close()

# get word info from Words table in the Mind
# raise type error if wrd is not a string
# raise words error if result not found
def Get(wrd: str):
        if forbiden(wrd):
            raise ForbidenError
        qry = "select * from words where lect=\'"+str(wrd)+"\';"
        check = dbq(qry)
        if check is None:
            raise WordsError("get none")
        return wordobj(check)

# get the most recent word info from Words table in the Mind
# return false if err
def Recent():
    # todo: add a time variable to recal a specific time
    # todo: time should be aproximate
    qry = "select * from words where clock=(select MAX(clock) from words);"
    check = dbq(qry)
    if check is None:
        raise WordsError("recent none") 
    return wordobj(check)

# get all new words from Words table in Mind
# most recently used words first
# raise words error if result not found
def Novel(size = None):
    qry = "select * from words where new=True order by clock;"
    check = dbq(qry,size)
    if check is None or len(check) == 0:
        raise WordsError("novel none")
    if not isinstance(check,list):
        return wordobj(check)
    return formatwordlist(check)

# get all old words
# most recently used words first
# return false if err
def Old(size = None):
    qry = "select * from words where old=True order by clock;"
    check = dbq(qry,size)
    if check is None or len(check) == 0:
        raise WordsError("old none")
    if not isinstance(check,list):
        return wordobj(check)
    return formatwordlist(check)
#EOF
