from bottle import route, run, request
import Call as call
import logging
import sys
## define routes for each method in the Cind API


## route for set word to words table
@route('/setword',method='POST')
def words_set_route():
    return call.words_set(request.forms.get('word'))

## route for get word from words table
@route('/getword',method='POST')
def words_get_route():
    return call.words_get(request.forms.get('word'))

## route for get recent word from words table
@route('/recentword')
def words_recent_route():
    return call.words_recent()

## route for get list of novel words from words table
@ route('/novelword',method='POST')
def words_novel_route():
    temp = request.forms.get('size')
    if isinstance(temp,int):
        return call.words_novel(request.forms.get('size'))
    else:
        return ({'Error':'Please send an integer'})

## route for get list of old words from words table
@ route('/oldword',method='POST')
def words_old_route():
    return call.words_old(request.forms.get('size'))

## route for set a memory to memory table
@ route('setmemory', method='POST')
    return call.memory_set(
            request.forms.get('word1'),
            request.forms.get('word2'),
            request.forms.get('decrement'))

## route for get a memory from memory table
@ route('getmemory',method='POST')
    return call.memory_set(
            request.forms.get('word1'),
            request.forms.get('word2'))

## route for get a list of memories from memory table
@ route('getlistmemory',method='POST')
    return call.memory_getlist(
            request.forms.get('word1'),
            requests.forms.get('size'))

## route for get a sleep list, request a sleep
@ route('/sleep',method='POST')
    return call.sleep_list(request.forms.get('size'))

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
