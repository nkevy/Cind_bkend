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

# define an error for forbiden
# thrown by methods checking string input
class ForbidenError(Exception):
    pass

# check if a string contains forbiden char(s) 
# raise tyoe error
def forbiden(ss = None):
    if ss is None:
        raise TypeError
    if not isinstance(ss,str):
        raise TypeError
    avoid = [',','.','/','\\','[',']','+','-','=','\'','\"',';',':','?','!','@','#','$',' ','{','}']
    return any(item in ss for item in avoid)

# convert word responce into word obj
# stop rewriteing code
def wordobj(wrd = None):
    if wrd is None:
        raise TypeError
    ret = []
    for item in wrd:
        ret.append(str(item))
    return ret

## format a responce list into a list of word objects
# stop rewriting code
def formatwordlist(wrds == None):
    if wrds is None:
        raise TypeError
    ret = []
    for item in wrds:
        ret.append(wordobj(item))
    return ret
    
# set a word to the Words table in the Mind
# rasie type error is wrd is not a string
# log error if cannot insert into words table
def Set(wrd = None):
        if wrd is None:
            raise TypeError
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

# qry and return responce
# size allows limit of responce size
# stop rewriting same code
# DO NOT: update data or insert data
def dbq(qry = None, size = None)
    if qry is None:
        raise TypeError
    con = None
    try:
        con = psy.connect(
            host = "localhost",
            database = "mind",
            user = "postgres",
            password = "dirty")
        cur = con.cursor()
        cur.execute(qry)
        if size is None or size is 1:
            ret = wordobj(cur.fetchone())
            return ret
        ret = []
        ret.append(cur.fetchall())
        if len(ret) > size:
            return formatwordlist(ret[0:size])
        return formatwordslist(ret)
    except (Exception, TypeError, psy.DatabaseError) as error:
        logging.basicConfig(filename='cindwords.log',level=logging.DEBUG)
        logging.debug(error)
    finally:
        if con is not None:
            con.close


# get word info from Words table in the Mind
# raise type error if wrd is not a string
# raise words error if result not found
def Get(wrd = None):
        if wrd is None:
            raise TypeError
        if forbiden(wrd):
            raise ForbidenError
        qry = "select * from words where lect=\'"+str(wrd)+"\';"
        check = dbq(qry)
        if check is None:
            raise WordsError
        return check

# get the most recent word info from Words table in the Mind
# return false if err
def Recent():
    # todo: add a time variable to recal a specific time
    # todo: time should be aproximate
    qry = "select * from words where clock=(select MAX(clock) from words);"
    check = dbq(qry)
    if check is None:
        raise WordsError 
    return check

# get all new words from Words table in Mind
# most recently used words first
# raise words error if result not found
def Novel(size = None):
    qry = "select * from words where new=True order by clock;"
    check = dbq(qry,size)
    if check is None:
        raise WordsError
    return check

# get all old words
# most recently used words first
# return false if err
def Old(size = None):
    qry = "select * from words where old=True order by clock;"
    check = dbq(qry,size)
    if check is None
        raise WordsError
    return check
#EOF
