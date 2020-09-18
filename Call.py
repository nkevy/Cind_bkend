import CindAPI as cpi

##########################################
##      Words                           ##
##########################################
# add a word to the Words table 
# check if string is a valid word
# return false if cannot add to words
def words_set(ss = None):
    try:
        cpi.Words.Set(ss)
        return True
    except (cpi.Words.ForbidenError) as error:
        return False

# get a word object from the Words table
# if word not found return None
def words_get(ss = None):
    try:
        return cpi.Words.Get(SS)
    except (cpi.Words.ForbidenError, cpi.Words.WordsError) as error:
        return None

# get most recent word added to Words table 
# if word not found return None
def words_recent():
    try:
        return cpi.Words.Recent()
    except (cpi.Words.WordsErrror) as error:
        return None

# get a list of new words from Words table
# raise error if cannot get word
def words_novellist(size = None):
    try:
        return cpi.Words.Novel(size)
    except (cpi.Words.WordsError) as error:
        return None

# get a list of old words from Words table
# raise error if cannot get word
def words_oldlist(size):
    try:
        return cpi.Words.Old(size)
    except (cpi.Words.WordsError) as error:
        return None

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
    
