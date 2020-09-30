import requests 
import logging
## test the routes set in Server.py 

HOST = 'http://127.0.0.1:8080'
HEADER = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}

## test the set word route /setword
def test_route_set_word(wrd: str):
    r = requests.post(
            url = HOST + '/setword',
            data = {'word' : wrd}, 
            headers = HEADER)
    return (r.status_code,r.json())

## test the get word route /getword
def test_route_get_word(wrd: str):
    r = requests.post(
            url = HOST + '/getword',
            data = {'word' : wrd},
            headers = HEADER)
    return (r.status_code,r.json())

## test the get recent word route /recentword
def test_route_recent_word():
    r = requests.post(
            url = HOST + '/recentword')
    return (r.status_code,r.json())

## test the get novel word route /novelword
def test_route_novel_word():
    r = requests.post(
            url = HOST + '/novelword',
            data = {'size' : 5},
            headers = HEADER)
    return (r.status_code,r.json())

## test the get old word route /oldword
def test_route_old_word():
    r = requests.post(
            url = HOST + '/oldword',
            data = {'size' : 5},
            headers = HEADER)
    return (r.status_code,r.json())

## test the set memory route /setmemory
def test_route_set_memory(wrd1: str, wrd2: str, dec: bool):
    r = requests.post(
            url = HOST + '/setmemory',
            data = {'word1' : wrd1, 'word2' : wrd2, 'decrement' : dec},
            headers = HEADER)
    return (r.status_code,r.json())

## test the get memory route /getmemory
def test_route_get_memory(wrd1: str, wrd2: str):
    r = requests.post(
            url = HOST + '/getmemory',
            data = {'word1' : wrd1, 'word2' : wrd2},
            headers = HEADER)
    return (r.status_code,r.json())

## test the get list memory route /getlistmemory
def test_route_get_list_memory(wrd1: str):
    r = requests.post(
            url = HOST + '/getlistmemory',
            data = {'word1' : wrd1, 'size' : 5},
            headers = HEADER)
    return (r.status_code,r.json())

## test the sleep route /sleep
def test_route_sleep():
    r = requests.post(
            url = HOST + '/sleep',
            data = {'size' : 5},
            headers = HEADER)
    return (r.status_code,r.json())


###################################
##      unit tests               ##
###################################

## unit test for word routes
def unit_test_word():
    print(test_route_set_word('summary'))
    print(test_route_get_word('summary'))
    print(test_route_recent_word())
    print(test_route_novel_word())
    print(test_route_old_word())

## unit test for memory routes
def unit_test_memory():
    print(test_route_set_word('leg'))
    print(test_route_set_word('foot'))
    print(test_route_set_word('knee'))
    print(test_route_set_memory('leg','foot',False))
    print(test_route_set_memory('leg','knee',False))
    print(test_route_get_memory('leg','foot'))
    print(test_route_get_list_memory('leg'))

## unit test for sleep route
def unit_test_sleep():
    print(test_route_set_word('jump'))
    print(test_route_set_word('dance'))
    print(test_route_set_word('run'))
    print(test_route_sleep())

###################################
## run unit tests                ##
###################################
if __name__=="__main__":
    unit_test_word()
    unit_test_memory()
    unit_test_sleep()



