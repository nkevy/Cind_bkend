import CindAPI as cpi
import logging
import json


##########################################
## help convert to json                 ##
##########################################
def to_json(ll: list):
    ret = []
    for i in ll:
        ret.append(i.json())
    return ret

# not used 
def success_json(bvalue: bool, data = None):
    if data is None:
        return json.dumps([{'success' : bvalue}])
    return json.dumps([{'success' : bvalue}] + data)
##########################################
##      Words                           ##
##########################################
# add a word to the Words table 
# return json 
def words_set(ss: str):
    try:
        cpi.Words.Set(ss)
        return json.dumps([{'success' : True}])
    except (cpi.Error.ForbidenError) as error:
        return json.dumps({'success' : False})

# get a word object from the Words table
# put word object in list format 
# if return json
def words_get(ss: str):
    try:
        ret = to_json(cpi.Words.Get(ss))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.ForbidenError, cpi.Error.WordsError) as error:
        return json.dumps({'success' : False})

# get recent words added to Words table 
# cut list from beginning to index arg
# return json
def words_recentlist(size = None):
    try:
        ret = to_json(cpi.Words.Recent(size))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.WordsError) as error:
        return json.dumps([{'success' : False}])

# get a list of new words from Words table
# return json
def words_novellist(size = None):
    try:
        ret = to_json(cpi.Words.Novel(size))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.WordsError) as error:
        return json.dumps([{'success' : False}])

# get a list of old words from Words table
# return json
def words_oldlist(size = None):
    try:
        ret = to_json(cpi.Words.Old(size))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.WordsError) as error:
        return json.dumps([{'success' : False}])

#############################################
##      Memory                             ##
#############################################

# add a memory to the Memory table  
# return json
def memory_set(w1:str, w2:str, decrement=False):
    try:
        cpi.Memory.Set(w1,w2,decrement)
        return json.dumps([{'success' : True}])
    except (cpi.Error.ForbidenError) as error:
        return json.dumps([{'success' : False}])

# get a memory from the Memory table
# put memory object in list format
# return json
def memory_get(w1:str, w2:str):
    try:
        ret = to_json(cpi.Memory.Get(w1,w2))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.MemoriesError) as error:
        return json.dumps([{'success' : False}])

# get a list of memories from the Memory table
# return json
def memory_getlist(w1: str,size = None):
    try: 
        ret = to_json(cpi.Memory.GetList(w1,size))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.MemoriesError) as error:
        return json.dumps([{'success' : False}])

#############################################
##      Sleep                              ##
#############################################

# request sleep
# return None if cannot sleep
# return dream if slept
def sleep_list(dreamsize: int):
    try:
        ret = to_json(cpi.Sleep.sleep(dreamsize))
        return json.dumps([{'success' : True}] + ret)
    except (cpi.Error.SleepError) as error:
        return json.dumps([{'success' : False}])


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
        ret = words_recentlist(num)
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
    unit_test_words('sun is ',2)
    unit_test_words('rain',2)
    unit_test_memory('warm ','sunny',30,False)
    unit_test_sleep(30)
    
