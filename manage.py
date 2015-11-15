# manage.py


import os
import unittest
import coverage

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from project import app, db
from project.user.models import User


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(
        branch=True,
        include='project/*',
        omit=['*/__init__.py', '*/config/*']
    )
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    cov.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    cov.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(first_name='Admin', last_name='',
                        email='admin@example.com', password='admin',
                        admin=True))
    db.session.commit()


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()