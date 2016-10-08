from flask import Blueprint, render_template

mod = Blueprint('example', __name__, url_prefix='/example')


@mod.route('/')
def index():
    return 'Hello World'


@mod.route('/html')
def test():
    return render_template('example/html.html')
