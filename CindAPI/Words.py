###############
## Noah Kevy ##
## 2020      ##
###############
import logging 
import psycopg2 as psy

# set a word to the Words table in the Mind
# return false if err
def Set(wrd = None):
        if wrd is None:
            return False
        qry = "select clock from words where lect=\'"+str(wrd)+"\';"
        add_new = "insert into words(lect,clock,new,old) values(\'"+str(wrd)+"\',CURRENT_TIMESTAMP,true,false) returning clock;"
        add_old = "update words set clock=CURRENT_TIMESTAMP, new=true, old=false where lect=\'"+str(wrd)+"\';"
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

# get word info from Words table in the Mind
# return false if err
def Get(wrd = None):
        if wrd is None:
                return False
        qry = "select * from words where lect=\'"+str(wrd)+"\';"
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
                    return False
            return check
        except (Exception, psy.DatabaseError) as error:
            logging.basicConfig(filename='cindapierror.log',level=logging.DEBUG)
            logging.debug(error)
        finally:
            if con is not None:
                con.close()

#EOF
