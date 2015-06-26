from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from application.models import *

from application.routes import app
from application import db

app.config.from_object('Config.DevelopmentConfig')

print(app.config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
