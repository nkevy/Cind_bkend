import CindAPI as cpi
import logging

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
    except (cpi.Error.ForbidenError) as error:
        return False

# get a word object from the Words table
# if word not found return None
def words_get(ss = None):
    try:
        return cpi.Words.Get(ss)
    except (cpi.Error.ForbidenError, cpi.Error.WordsError) as error:
        return None

# get most recent word added to Words table 
# if word not found return None
def words_recent():
    try:
        return cpi.Words.Recent()
    except (cpi.Error.WordsErrror) as error:
        return None

# get a list of new words from Words table
# raise error if cannot get word
def words_novellist(size = None):
    try:
        return cpi.Words.Novel(size)
    except (cpi.Error.WordsError) as error:
        return None

# get a list of old words from Words table
# raise error if cannot get word
def words_oldlist(size = None):
    try:
        return cpi.Words.Old(size)
    except (cpi.Error.WordsError) as error:
        return None

#############################################
##      Tests                              ##
#############################################
#
# unit testing for words functions
def unit_test_words(wrd,num):
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
        ret = words_novellist(num)
        print("returned:",end='')
        print(ret)
        print("get old word list:")
        ret = words_oldlist(num)
        print("returned:",end='')
        print(ret)
    except (cpi.Error.WordsError, cpi.Error.ForbidenError) as error:
        logging.basicConfig(filename='unit_test_words.log', level=logging.DEBUG)
        logging.debug(error)

###########################################
# run tests 
if __name__ == "__main__":
    print("API Testing...")
    unit_test_words('word',2)
    
