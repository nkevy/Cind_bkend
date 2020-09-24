###############
## Noah Kevy ##
## 2020      ##
###############
import psycopg2 as psy
from .Error import *
import logging 


# update database with sql insert or update
# return False if Error
# stop rewriting code
def dbupdate(ins:str):
    con = None
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
        logging.basicConfig(filename='cindpostgres.log',level=logging.DEBUG)
        logging.debug(error)
        return False
    finally:
        if con is not None:
            con.close()



# qry and return responce or None if error
# argument size allows limit of responce size
# stop rewriting code
def dbq(qry: str, size = None):
    con = None
    try:
        con = psy.connect(
            host = "localhost",
            database = "mind",
            user = "postgres",
            password = "dirty")
        cur = con.cursor()
        cur.execute(qry)
        if size is None or size == 1:
            ret = cur.fetchone()
            return ret
        ret = cur.fetchall()
        if len(ret) > size:
            return ret[0:size]
        return ret
    except (Exception, TypeError, psy.DatabaseError) as error:
        logging.basicConfig(filename='cindpostgres.log',level=logging.DEBUG)
        logging.debug(error)
        return None
    finally:
        if con is not None:
            con.close



