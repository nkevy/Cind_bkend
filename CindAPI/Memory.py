###############
## Noah Kevy ##
## 2020      ##
###############
from .Error import *
from .Postgres import *
import psycopg2 as psy
import logging 


# Memory object is an memory of two words
# fields: 
#   src,    string
#   dst,    string
#   rank,   float 
class Memory:
    def __init__(self, w1: str, w2: str, r: float):
        self.src = w1
        self.dst = w2
        self.rank = r

# return a memory object
def memobj(mem = None):
    if mem is None:
        raise MemoryError
    return Memory(mem[0], mem[1], mem[2])

# return a list os memory objects
def formatmemlist(memlist = None):
    if mem is None:
        raise MemoryError
    ret = []
    for item in assolist:
        ret.append(memobj(item))
    return ret

# set an associate of two words from the Memory table in mind
# if memory exists update the rank
# raise an error if unable to add
def Set(w1: str, w2, decrement = False):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select rank from memory where src=\'"+ w1 +"\' and dst=\'"+ w2 +"\';"
    ins = ""
    rank = dbq(qry)
    if rank is None:
        ins = "insert into memory(src,dst,rank) values(\'"+ w1 +"\',\'"+ w2 +"\',0.05);"
    else:
        rank = float(rank)-0.05 if (decrememt) else float(rank)+0.05
        ins = "update memory set rank="+rank+" where src=\'"+w1+"\' and dst=\'"+w2+"\';"
    try: 
        con = psy.connect(
            host = "localhost",
            database = "mind",
            user = "postgres",
            password = "dirty")
        cur = con.cursor()
        cur.execute(ins)
        cur.close()
        con.commit()
    except (Exception, psy.DatabaseError) as error:
        logging.basicConfig(filename='cindwords.log',level=logging.DEBUG)
        logging.debug(error)
    finally:
        if con is not None:
            con.close()

# get a memory from the Memory table in mind
# raise an error if unable to get
def Get(w1: str , w2: str):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select rank from memory where src=\'"+w1+"\' and dst=\'"+w2+"\';"
    check = dbq(qry)
    if check is None:
        raise MemoryError
    return memobj(w1,w2,check)

# get all memory associated with the word from the Memory table in mind
# raise an error if unable to add
def GetList(w1: str, size=None):
    if forbiden(w1):
        raise ForbidenError
    qry = "select * from memory where src=\'"+w1+"\' order by rank;"
    check = dbq(qry,size)
    if check is None:
        raise MemoryError
    return formatmemlist(check)
