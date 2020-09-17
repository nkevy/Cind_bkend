import CindAPI as cpi

# check if a string contains forbiden char(s) 
# return False if string can be used
def forbiden(ss = None):
    if ss is None:
        return True
    if not isinstance(ss,str):
        return True
    avoid = [',','.','/','\\','[',']','+','-','=','\'','\"',';',':','?','!','@','#','$',' ','{','}']
    return any(item in ss for item in avoid)

# add a word to the Words table 
# check if string is a valid word
# return error if cannot add to words
def words_set(ss = None):
    if forbiden(ss):
        return False
    # todo: add handeling of a False return
    if not cpi.Words.Set(ss):
        return False
    return True

# get a word object from the Words table
# check if string is a valid word
# return error if cannot get word
def words_get(ss = None):
    # todo: add handling of false return
    if forbiden(ss):
        return False
    ret = cpi.Words.Get(ss)
    if not ret:
        return False
    wordobj = []
    for item in ret:
        wordobj.append(str(item))
    return wordobj
#
# unit testing for words functions
def unit_test_words(wrd):
    print("test words table functions:")
    print("set the word:"+wrd)
    ret = words_set(wrd)
    print("returned:",end=' ')
    print(ret)
    print("get the word:"+wrd)
    ret = words_get(wrd)
    print("returned:",end=' ')
    print(ret)


if __name__ == "__main__":
    print("API Testing...")
    unit_test_words('word')
    
