import CindAPI as cpi
import logging

##########################################
##      Words                           ##
##########################################
# add a word to the Words table 
# return false if cannot add to words
def words_set(ss: str):
    try:
        cpi.Words.Set(ss)
        return True
    except (cpi.Error.ForbidenError) as error:
        return False

# get a word object from the Words table
# if word not found return None
def words_get(ss: str):
    try:
        return cpi.Words.Get(ss)
    except (cpi.Error.ForbidenError, cpi.Error.WordsError) as error:
        return None

# get most recent word added to Words table 
# return None if get fails
def words_recent():
    try:
        return cpi.Words.Recent()
    except (cpi.Error.WordsErrror) as error:
        return None

# get a list of new words from Words table
# return None if get fails
def words_novellist(size = None):
    try:
        return cpi.Words.Novel(size)
    except (cpi.Error.WordsError) as error:
        return None

# get a list of old words from Words table
# return None if get fails
def words_oldlist(size = None):
    try:
        return cpi.Words.Old(size)
    except (cpi.Error.WordsError) as error:
        return None

#############################################
##      Memory                             ##
#############################################

# add a memory to the Memory table  
# return false if cannot add word
def memory_set(w1:str, w2:str, decrement=False):
    try:
        return cpi.Memory.Set(w1,w2,decrement)
    except (cpi.Error.ForbidenError) as error:
        return False

# get a memory from the Memory table
# return None if get fails
def memory_get(w1:str, w2:str):
    try:
        return cpi.Memory.Get(w1,w2)
    except (cpi.Error.MemoriesError) as error:
        return None

# get a list of memories from the Memory table
# return none if get fails
def memory_getlist(w1: str,size = None):
    try: 
        return cpi.Memory.GetList(w1,size)
    except (cpi.Error.MemoriesError) as error:
        return None

#############################################
##      Sleep                              ##
#############################################

# request sleep
# return None if cannot sleep
# return dream if slept
def sleep_list(dreamsize: int):
    try:
        return cpi.Sleep.sleep(dreamsize) 
    except (cpi.Error.SleepError) as error:
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

#
# unit testing for memory functions
def unit_test_memory(wrd1,wrd2,num,decrement):
    try:
        print("test memory table functions:")
        print("set a memory: "+wrd1+" "+wrd2)
        ret = memory_set(wrd1,wrd2,decrement)
        print("returned:",end='')
        print(ret)
        print("get a memory: "+wrd1+" "+wrd2)
        ret = memory_get(wrd1,wrd2)
        print("returned:",end='')
        print(ret)
        print("get a list of memories: "+wrd1)
        ret = memory_getlist(wrd1,num)
        print("returned:",end='')
        print(ret)
    except (cpi.Error.MemoriesError, cpi.Error.ForbidenError) as error:
        logging.basicConfig(filename='unit_test_memory.log', level=logging.DEBUG)
        logging.debug(error)

#
# unit testing for sleep functions
def unit_test_sleep(num):
    try:
        print("test sleep functions")
        print("sleep with dream size: "+str(num))
        ret = sleep_list(num)
        print("returned:",end='')
        print(ret)
    except (cpi.Error.WordsError) as error:
        logging.basicConfig(filename='unit_test_sleep.log',level=logging.DEBUG)
        logging.debug(error)

###########################################
# run tests 
if __name__ == "__main__":
    print("API Testing...")
    unit_test_words('H',2)
    unit_test_words('I',2)
    unit_test_memory('H','I',30,False)
    unit_test_sleep(30)
    
