#!/usr/bin/env python
# coding: utf-8

from app import create_app, db
from flask_script import Manager, Shell
from simple_migrate import MigrateCommand

app = create_app()


def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('shell', Shell(make_context=make_shell_context))

    @manager.command
    def createall():
        db.create_all()

    @manager.command
    def dropall():
        db.drop_all()
    manager.run()
