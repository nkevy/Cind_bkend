from .Error import *
from .Words import Novel
from .Postgres import dbupdate
import logging


# change the status of words from new to old
# impacts the words found by the Novel function
# use periodicaly
def sleep(dream: int):
    try:
        wordlist = Novel(size = dream)
        if len(wordlist) == 1:
            raise SleepError
        ins = "update words set new=False, old=True where lect=\'{}\';"
        ins_cat = ""
        for w in wordlist:
            ins_cat = ins_cat + ins.format(w.value)
        dbupdate(ins_cat)
        ins = "insert into memory (src,dst,dyad) values(\'{}\',\'{}\',0.05);"
        ins_cat = ""
        for i in range(1,len(wordlist)):
            ins_cat = ins_cat + ins.format(wordlist[i-1].value,wordlist[i].value)
        print(ins_cat)
        dbupdate(ins_cat)
        return wordlist
    except (WordsError, SleepError) as error:
        raise SleepError("no novel words, cant sleep not tired")


