"""User."""
from flask_restaction import abort
from app import model
from app.dependency import db


class User:
    """User.

    $shared:
        userinfo:
            id?int: id
            username?str: username
    """

    def get(self, username):
        """Get user info by username.

        $input:
            username?str: username
        $output: "@userinfo"
        $error:
            404.NotFound: not found
        """
        user = model.User.query.filter_by(username=username).first()
        if user:
            return user
        abort(404, 'not found')

    def post(self, username, password):
        """Post user info.

        $input:
            username?str: username
            password?str: password
        $output: "@userinfo"
        """
        user = model.User.query.filter_by(username=username).first()
        if user:
            abort(400, 'user all ready exist')
        user = model.User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user
