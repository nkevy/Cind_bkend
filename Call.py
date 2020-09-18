import CindAPI as cpi

# todo: move code to cpi

# check if a string contains forbiden char(s) 
# return False if string can be used
def forbiden(ss = None):
    if ss is None:
        return True
    if not isinstance(ss,str):
        return True
    avoid = [',','.','/','\\','[',']','+','-','=','\'','\"',';',':','?','!','@','#','$',' ','{','}']
    return any(item in ss for item in avoid)

# define an error for forbiden
# thrown by methods checking string input
class ForbidenError(Exception):
    pass

# convert word responce into word obj
# stop rewriteing code
def wordobj(wrd = None):
    if wrd is None:
        return None
    ret = []
    for item in wrd:
        ret.append(str(item))
    return ret

# format a responce list into a list of word objects
# stop rewriting code
def formatwordlist(wrds == None):
    if wrds is None:
        return None 
    ret = []
    for item in wrds:
        ret.append(wordobj(item))
    return ret
    
# add a word to the Words table 
# check if string is a valid word
# raise error if cannot add to words
def words_set(ss = None):
    if forbiden(ss):
        raise ForbidenError
    if not cpi.Words.Set(ss):
        raise Words.WordsError
    return True

# get a word object from the Words table
# check if string is a valid word
# raise error if cannot get word
def words_get(ss = None):
    if forbiden(ss):
        raise ForbidenError
    ret = cpi.Words.Get(ss)
    if not ret:
        raise Words.WordsError
    return wordobj(ret)

# get most recent word added to Words table 
# raise error if connot get word
def words_recent():
    ret = cpi.Words.Recent()
    if not ret:
        raise Words.WordsError
    return wordobj(ret)

# get a list of new words from Words table
# raise error if cannot get word
def words_novellist(size = None):
    ret = cpi.Words.Novel()
    if not ret:
        raise Words.WordsError
    return formatwordlist(ret)

# get a list of old words from Words table
# raise error if cannot get word
def words_oldlist():
    ret = cpi.Words.Old(size = None):
    if not ret:
        raise Words.WordsError
    return formatwordlist(ret)

#############################################
##      Tests                              ##
#############################################

#
# unit testing for words functions
def unit_test_words(wrd):
    try:
        print("test words table functions:")
        print("set the word:"+wrd)
        ret = words_set(wrd)
        print("returned:",end='')
        print(ret)
        print("get the word:"+wrd)
        ret = words_get(wrd)
        print("returned:",end='')
        print(ret)
        print("get recent word:")
        ret = words_recent()
        print("returned:",end='')
        print(ret)
        print("get novel word list:")
        ret = words_novellist()
        print("returned:",end='')
        print(ret)
        print("get old word list:")
        ret = words_oldlist()
        print("returned:",end='')
        print(ret)
    except (Exception, Words.WordsError, ForbidenError) as error:
        logging.basicConfig(filename='unit_test_words.log',logging.DEBUG)
        logging.debug(error)

###########################################
# run tests 
if __name__ == "__main__":
    print("API Testing...")
    unit_test_words('word')
    
