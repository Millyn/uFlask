from project import app
from flask_script import Manager
import gevent.monkey

manager = Manager(app)
gevent.monkey.patch_all()

if __name__ == '__main__':
    manager.run()
