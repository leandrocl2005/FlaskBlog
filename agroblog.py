from app import app, db
from app.models import Categoria
from app.models import User
from app.models import Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Categoria': Categoria, 'User': User, 'Post': Post}