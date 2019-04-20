from app import app, db
from flask import render_template, redirect, url_for, session, jsonify, request
from app.models import Post, Categoria, User
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user, logout_user


@app.route("/")
@app.route("/index")
def index():
    logged = google.authorized
    posts = Post.query.all()
    categorias = Categoria.query.all()
    return render_template(
        "index.html",
        posts=posts,
        categorias=categorias,
        logged=logged
    )


@app.route("/sobre")
def sobre():
    logged = google.authorized
    return render_template("sobre.html", logged=logged)


@app.route("/post/<int:post_id>")
def post(post_id):
    logged = google.authorized
    post = Post.query.get(post_id)
    user = User.query.get(post.user_id)
    return render_template("post.html", post=post, user=user, logged=logged)


@app.route("/post/<int:post_id>/getJson")
def postJSON(post_id):
    post = Post.query.get(post_id)
    return jsonify(post.serialize)


@app.route("/meus_posts")
def meus_posts():
    logged = google.authorized
    if logged:
        try:
            resp = google.get("/oauth2/v1/userinfo")
            user_email = resp.json()['email']
            user = db.session.query(User).filter_by(
                email=user_email
            ).first()
            posts = db.session.query(Post).filter_by(
                user_id=user.id
            ).all()
            categorias = Categoria.query.all()
            return render_template(
                "meus_posts.html",
                posts=posts,
                user=user,
                logged=logged,
                categorias=categorias
            )
        except:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route("/meus_posts/create",  methods=['GET', 'POST'])
def post_create():
    # check authorized and get user
    logged = google.authorized
    if not logged:
        redirect(url_for('login'))

    # get user
    try:
        resp = google.get("/oauth2/v1/userinfo")
        user_email = resp.json()['email']
    except:
        return redirect(url_for('login'))

    # context
    categorias = Categoria.query.all()
    user = db.session.query(User).filter_by(email=user_email).first()

    # create a new post
    if request.method == "POST":
        post = Post(
            title=request.form.get('title'),
            body=request.form.get('body'),
            user_id=user.id,
            categoria_id=request.form.get('categoria_id'),
            abstract=request.form.get('abstract'))
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('meus_posts'))
    else:
        return render_template(
            'post_create.html',
            categorias=categorias,
            logged=logged)


@app.route("/meus_posts/edit/<int:post_id>",  methods=['GET', 'POST'])
def post_edit(post_id):
    # check authorized and get user
    logged = google.authorized
    if not logged:
        redirect(url_for('login'))

    # get user
    try:
        resp = google.get("/oauth2/v1/userinfo")
        user_email = resp.json()['email']
    except:
        return redirect(url_for('login'))

    # context
    categorias = Categoria.query.all()
    post = db.session.query(Post).filter_by(id=int(post_id)).first()
    categoria_id = post.categoria_id
    user = db.session.query(User).filter_by(email=user_email).first()

    # create a new post
    if request.method == "POST":
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        post.user_id = user.id
        post.categoria_id = request.form.get('categoria_id')
        post.abstract = request.form.get('abstract')
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('meus_posts'))
    else:
        return render_template(
            'post_edit.html',
            categorias=categorias,
            logged=logged,
            categoria_id=categoria_id,
            post=post
        )


@app.route('/meus_posts/delete/<int:post_id>', methods=['GET', 'POST'])
def post_delete(post_id):
    # check authorized and get user
    logged = google.authorized
    if not logged:
        redirect(url_for('login'))

    # get user
    try:
        resp = google.get("/oauth2/v1/userinfo")
        user_email = resp.json()['email']
    except:
        return redirect(url_for('login'))

    # context
    categorias = Categoria.query.all()
    post = db.session.query(Post).filter_by(id=int(post_id)).first()
    user = db.session.query(User).filter_by(email=user_email).first()

    # create a new post
    if request.method == "POST":
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('meus_posts'))
    else:
        return render_template(
            'post_delete.html',
            categorias=categorias,
            logged=logged,
            post_id=post_id
        )


@app.route("/categoria/<int:categoria_id>")
def categoria(categoria_id):
    logged = google.authorized
    categoria = Categoria.query.get(categoria_id)
    posts = db.session.query(Post).filter_by(
        categoria_id=categoria.id
    ).all()
    return render_template(
        "categoria.html",
        categoria=categoria,
        posts=posts, logged=logged)


@app.route("/contato")
def contato():
    logged = google.authorized
    return render_template('contact.html', logged=logged)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # check user is authorized
    if not google.authorized:
        return redirect(url_for("google.login"))

    # try get data from user
    try:
        resp = google.get("/oauth2/v1/userinfo")
    except:
        return redirect(url_for("google.login"))
    if resp.ok:
        data = resp.json()
        username = data["given_name"]
        email = data["email"]
        social_id = data["id"]
        pic = data["picture"]

        # check user is on database
        user = User.query.filter_by(email=email).first()

        # if user not, register user in database
        if not user:
            user = User(
                username=username,
                email=email,
                social_id=social_id,
                pic=pic
            )
            db.session.add(user)
            db.session.commit()
            print(user.username)

        # login user
        login_user(user)

        # salve data in session
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for("index"))
    else:
        return redirect(url_for("google.login"))


@app.route('/logout')
def logout():
    try:
        token = current_app.blueprints['google'].token["access_token"]
        resp = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        ) # get out from google session
        assert resp.ok, resp.text  
        logout_user()
        session.clear()
        return redirect(url_for('index'))
    except:
        logout_user()
        session.clear()
        return redirect(url_for('index'))
