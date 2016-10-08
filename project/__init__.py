from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()
db.init_app(app)


@app.errorhandler(404)
def error_404(error):
    return render_template('error/404.html'), 404


from project.views import example

app.register_blueprint(example.mod)
