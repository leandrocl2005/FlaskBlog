from app import app, db
from app.models import Categoria, User, Post
from data import categorias, users, posts


for categoria in categorias:
    c = Categoria()
    c.id = categoria['id']
    c.name = categoria['name']
    c.slug = categoria['slug']
    c.css_class = categoria['css_class']
    db.session.add(c)
db.session.commit()

for user in users:
    u = User()
    u.id = user['id']
    u.username = user['username']
    u.email = user['email']
    u.social_id = user['social_id']
    u.bio = user['bio']
    u.pic = user['pic']
    db.session.add(u)
db.session.commit()

for post in posts:
    p = Post()
    p.id = post['id']
    p.title = post['title']
    p.body = post['body']
    p.user_id = post['user_id']
    p.categoria_id = post['categoria_id']
    p.publish_date = post['publish_date']
    p.pic = post['pic']
    p.abstract = post['abstract']
    p.featured = post['featured']
    p.start_page = post['start_page']
    db.session.add(p)
db.session.commit()
