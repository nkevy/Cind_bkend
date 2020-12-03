from bottle import route, run, request, response
import Call as call
import logging
import sys

## enable CORS responses 
def cors(func):
    def wrapper(*args,**kwargs):
        response.set_header('Access-Control-Allow-Origin','*')
        return func(*args,**kwargs)
    return wrapper


## route for set word to words table
@route('/setword',method='POST')
@cors
def words_set_route():
    w = str(request.json['word'])
    call.words_set(w)
    print(w)
    return call.words_get(w)

## route for get word from words table
@route('/getword',method='POST')
@cors
def words_get_route():
    return call.words_get(str(request.json['word']))

## route for get recent word list from begging of list to index
@route('/recentwords',method='POST')
@cors
def words_recent_route():
    return call.words_recentlist(request.json['length'])

## route for get list of novel words from words table
@ route('/novelwords',method='POST')
@cors
def words_novel_route():
    return call.words_novellist(request.json['length'])

## route for get list of old words from words table
@ route('/oldwords',method='POST')
@cors
def words_old_route():
    return call.words_oldlist(int(request.json['length']))

## route for set a memory to memory table
@ route('/setmemory', method='POST')
@cors
def memory_set_route():
    src = request.json['src']
    dst = request.json['dst']
    dec = bool(request.json['decrement'])
    call.memory_set(src, dst, dec)
    return call.memory_get(src,dst)

## route for get a memory from memory table
@ route('/getmemory',method='POST')
@cors
def memory_get_route():
    return call.memory_get(
            str(request.json['src']),
            str(request.json['dst']))

## route for get a list of memories from memory table
@ route('/getlistmemory',method='POST')
@cors
def memory_getlist_route():
    return call.memory_getlist(
            str(request.json['word']),
            int(request.json['length']))

## route for get a sleep list, request a sleep
@ route('/sleep',method='POST')
@cors
def sleep_route():
    return call.sleep_list(int(request.json['length']))

# todo: write routes for all api calls
if __name__ == '__main__':
    if len(sys.argv)>1:
        try:
            run(host='localhost', port=int(sys.argv[1]), debug=True, reloader=True)
        except (Exception) as error:
            logging.basicConfig(filename='servererror.log',level=logging.DEBUG)
            logging.debug(error)
        exit(0)
    else:
        print('[USAGE] $python3 Server.py <Port number as argument>')
