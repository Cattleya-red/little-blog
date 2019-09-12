from flask import Flask
from flask import render_template


app = Flask(__name__)


#  添加注释
@app.route('/index')
def index():
    user = {'username': 'Alice'}
    template = render_template('index.html', title='Home', user=user)
    return template


if __name__ == '__main__':
    app.run()
