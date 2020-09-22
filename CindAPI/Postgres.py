###############
## Noah Kevy ##
## 2020      ##
###############
import psycopg2 as psy
from .Error import *
import logging 

# qry and return responce
# size allows limit of responce size
# stop rewriting same code
# DO NOT: update data or insert data
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
        logging.basicConfig(filename='cindPostgres.log',level=logging.DEBUG)
        logging.debug(error)
    finally:
        if con is not None:
            con.close



