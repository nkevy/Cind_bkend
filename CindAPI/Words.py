###############
## Noah Kevy ##
## 2020      ##
###############
import logging 
import psycopg2 as psy

# add a word to the Words table in the Mind
# return false if err
def Add(wrd = None):
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
            cur.execute(qry,wrd)
            check = cur.fetchone()
            print(check)
            if check is None:
                cur.execute(add_new)
            else:
                cur.execute(add_old)
            cur.close()
            con.commit()
        except (Exception, psy.DatabaseError) as error:
            logging.basicConfig(filename='cindapi.log',level=logging.DEBUG)
            logging.debug(error)
        finally:
            if con is not None:
                con.close()


