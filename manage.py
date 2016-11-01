#!/usr/bin/env python
# coding: utf-8

from app import create_app, db
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def createall():
    db.create_all()


@manager.command
def dropall():
    db.drop_all()

if __name__ == '__main__':
    manager.run()
