from flask import Flask
from flask import render_template


app = Flask(__name__)


#  添加注释
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alice'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    template = render_template('index.html', title='Home', user=user, posts=posts)
    return template


if __name__ == '__main__':
    app.run()
