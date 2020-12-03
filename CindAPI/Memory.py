###############
## Noah Kevy ##
## 2020      ##
###############
from .Error import *
from .Postgres import *
import psycopg2 as psy
import logging 


######################################################################
# back end functions to support the memory table in the mind database 
# all functions should return a list of memory objects
# or
# return None (no return statment)
######################################################################

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

    def json(self):
        return {'word1' : self.src, 'word2' : self.dst, 'rank' : self.rank}

# create a memory object from a sql response 
def memoryobj(mem = None):
    if mem is None:
        raise TypeError
    return memory(mem[0], mem[1], float(mem[2]))

# create a list of memory objects from a list of sql responces
def formatmemorylist(memlist = None):
    if memlist is None:
        raise TypeError
    ret = []
    for item in memlist:
        ret.append(memoryobj(item))
    return ret
##############################################################

# set an associate of two words from the Memory table in mind
# if memory exists update the rank
# raise an error if unable to add
def Set(w1: str, w2, decrement = False):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select dyad from memory where src=\'{}\' and dst=\'{}\';".format(w1,w2)
    ins = ""
    rank = dbq(qry)
    if rank is None:
        ins = "insert into memory(src,dst,dyad) values(\'{}\',\'{}\',0.05);".format(w1,w2)
        ins = ins+"update words set new=False, old=True where lect=\'{}\' or lect=\'{}\';".format(w1,w2)
    else:
        rank = rank[0]
        rank = float(rank)-0.05 if (decrement) else float(rank)+0.05
        ins = "update memory set dyad={} where src=\'{}\' and dst=\'{}\';".format(str(rank),w1,w2)
    if not dbupdate(ins):
        raise MemoriesError("set of memory failed")

# get a memory from the Memory table in mind
# raise an error if unable to get
def Get(w1: str , w2: str):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select dyad from memory where src=\'{}\' and dst=\'{}\';".format(w1,w2)
    check = dbq(qry)
    if check is None:
        raise MemoriesError("get of memory error, query returned none")
    temp = [w1,w2,check[0]]
    # return a list containing a single memory object
    return [memoryobj(temp)]

# get all memory associated with the word from the Memory table in mind
# raise an error if unable to add
def GetList(w1: str, size=None):
    if forbiden(w1):
        raise ForbidenError
    qry = "select * from memory where src=\'{}\' order by dyad;".format(w1)
    check = dbq(qry,size)
    if check is None:
        raise MemoriesError("get list of memories error, query returned none")
    if not isinstance(check,list):
        return [memoryobj(check)]
    return formatmemorylist(check)
#EOF
