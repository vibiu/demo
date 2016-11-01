from werkzeug.local import LocalProxy
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Dependency:
    """Dependency."""

d = Dependency()

auth = LocalProxy(lambda: d.auth)
check_role = LocalProxy(lambda: d.check_role)
