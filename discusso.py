from app import app, db
from app.models import User, Post, Reply, Post_BC, Reply_BC

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Reply': Reply, 'Post_BC':Post_BC, 'Reply_BC':Reply_BC}

