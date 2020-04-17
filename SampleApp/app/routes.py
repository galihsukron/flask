from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Galih'}
    return '''
<html>
    <head>
        <title>Home Page - My Website</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
