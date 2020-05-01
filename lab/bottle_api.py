import bottle
from bottle import route, run, request


@route('/', method='GET')
def homepage():
    return 'Hello world!'


@route('/events/:id', method='GET')
def get_event(id):
    return dict(name='Event ' + str(id))


@route('/result', method='POST')
def result_submit():
    result = request.POST.get('result', '').strip()
    print(result)
    # write result to file
    fileName = "Result.json"
    f = open(fileName + ".json", "w")
    f.write(result)
    return {'success': True}


bottle.debug(True)
run()

# http://www.onbiron.com.tr/python-ile-cevik-web-service-gelistirme/