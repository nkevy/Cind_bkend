###############
## Noah Kevy ##
## 2020      ##
###############
import logging 
import psycopg2 as psy

# define error type WordsError
# thrown by encapusulation of Words.py
class WordsError(Exception):
    pass

# set a word to the Words table in the Mind
# return false if err
def Set(wrd = None):
        if wrd is None:
            return False
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
            return True
        except (Exception, psy.DatabaseError) as error:
            logging.basicConfig(filename='cindapierror.log',level=logging.DEBUG)
            logging.debug(error)
        finally:
            if con is not None:
                con.close()

# qry and return responce
# size allows limit of responce size
# stop rewriting same code
# DO NOT: update data or insert data
def dbq(qry = None, size = None)
    if qry is None:
        return None
    con = None
    try:
        con = psy.connect(
            host = "localhost",
            database = "mind",
            user = "postgres",
            password = "dirty")
        cur = con.cursor()
        cur.execute(qry)
        if size is None:
            return cur.fetchone()
        ret = []
        ret.append(cur.fetchall())
        if len(ret) > size:
            return ret[0:size]
        else:
            return ret
    except (Exception, psy.DatabaseError) as error:
        logging.basicConfig(filename='cindapierror.log',level=logging.DEBUG)
        logging.debug(error)
    finally:
        if con is not None:
            con.close


# get word info from Words table in the Mind
# return false if err
def Get(wrd = None):
        if wrd is None:
                return False
        qry = "select * from words where lect=\'"+str(wrd)+"\';"
        check = dbq(qry)
        if check is None:
                return False
        return check

# get the most recent word info from Words table in the Mind
# return false if err
def Recent():
    # todo: add a time variable to recal a specific time
    # todo: time should be aproximate
    qry = "select * from words where clock=(select MAX(clock) from words);"
    check = dbq(qry)
    if check is None:
        return False
    return check

# get all new words from Words table in Mind
# most recently used words first
# return false if err
def Novel():
    # todo: decide how many to return, 10 for now
    qry = "select * from words where new=True order by clock;"
    check = dbq(qry,10)
    if check is None:
        return False
    return check

# get all old words
# most recently used words first
# return false if err
def Old():
    # todo: decide how many to return, 10 for now
    qry = "select * from words where old=True order by clock;"
    check = dbq(qry,10)
    if check is None
        return False
    return check
#EOF
