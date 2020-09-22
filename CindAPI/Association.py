###############
## Noah Kevy ##
## 2020      ##
###############
from .Error import *
from .Postgres import *
import psycopg2 as psy
import logging 


# Association object is an association of two words
# fields: 
#   src,    string
#   dst,    string
#   rank,   float 
class Association:
    def __init__(self, w1: str, w2: str, r: float):
        self.src = w1
        self.dst = w2
        self.rank = r

# return an assosciation object
def assoobj(asso = None):
    if asso is None:
        raise AssociationError
    return Association(asso[0], asso[1], asso[2])

# return a list os association objects
def formatassolist(assolist = None):
    if assolist is None:
        raise AssociationError
    ret = []
    for item in assolist:
        ret.append(assoobj(item))
    return ret

# set an associate of two words from the Association table in mind
# if association exists update the rank
# raise an error if unable to add
def Set(w1: str, w2, decrement = False):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select "+ w2 +" from association where qiword=\'"+ w1 +"\';"
    rank = dbq(qry)
    if rank is None:
        rank = 0.05
    else:
        rank = float(rank)-0.05 if (decrememt) else float(rank)+0.05
    inscol = "alter table association add column "+ w2 +" decimal(5,2);"
    insrank = "insert into association (qiword,"+ w2 +") values(\'"+ w1 +"\',"+ rank +");"
    try: 
        con = psy.connect(
            host = "localhost",
            database = "mind",
            user = "postgres",
            password = "dirty")
        cur = con.cursor()
        cur.execute(inscol)
        cur.execute(insrank)
        cur.close()
        con.commit()
    except (Exception, psy.DatabaseError) as error:
        logging.basicConfig(filename='cindwords.log',level=logging.DEBUG)
        logging.debug(error)
    finally:
        if con is not None:
            con.close()

# get rank of an association from the Association table in mind
# raise an error if unable to get
def Rank(w1: str , w2: str):
    if forbiden(w1) or forbiden(w2):
        raise ForbidenError
    qry = "select "+ w2 +" from association where qiword=\'"+ w1 +"\';"
    check = dbq(qry)
    if check is None:
        raise AssociationError
    return float(check)

# get an association from the Assosciation table in mind
# raise an error if unable to add
def Get(w1):
    if forbiden(w1):
        raise ForbidenError
    qry = "select * from "
    return 
