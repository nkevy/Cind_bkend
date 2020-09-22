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
class memory:
    def __init__(self, w1: str, w2: str, r: float):
        self.src = w1
        self.dst = w2
        self.rank = r
    def __str__(self):
        return "{} {} {}".format(self.src, self.dst, self.rank)

# return a memory object
def memobj(mem = None):
    if mem is None:
        raise MemoriesError
    return memory(mem[0], mem[1], float(mem[2]))

# return a list os memory objects
def formatmemlist(memlist = None):
    if memlist is None:
        raise MemoriesError
    ret = []
    for item in memlist:
        print(item)
        ret.append(memobj(item))
    return ret

# set an associate of two words from the Memory table in mind
# if memory exists update the rank
# raise an error if unable to add
def Set(w1: str, w2, decrement = False):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select dyad from memory where src=\'"+ w1 +"\' and dst=\'"+ w2 +"\';"
    ins = ""
    rank = dbq(qry)[0]
    if rank is None:
        ins = "insert into memory(src,dst,dyad) values(\'"+ w1 +"\',\'"+ w2 +"\',0.05);"
    else:
        rank = float(rank)-0.05 if (decrement) else float(rank)+0.05
        ins = "update memory set dyad="+str(rank)+" where src=\'"+w1+"\' and dst=\'"+w2+"\';"
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
        return True
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
    qry = "select dyad from memory where src=\'"+w1+"\' and dst=\'"+w2+"\';"
    check = dbq(qry)
    if check is None:
        raise MemoriesError
    temp = [w1,w2,check[0]]
    return memobj(temp)

# get all memory associated with the word from the Memory table in mind
# raise an error if unable to add
def GetList(w1: str, size=None):
    if forbiden(w1):
        raise ForbidenError
    qry = "select * from memory where src=\'"+w1+"\' order by dyad;"
    check = dbq(qry,size)
    if check is None:
        raise MemoriesError
    if not isinstance(check,list):
        return memobj(check)
    return formatmemlist(check)
#EOF
