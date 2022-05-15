from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quote
from ..models import User,Post,Comment,Subscribe
from .forms import UpdateProfile,PostForm,UpdatePostForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
from datetime import datetime
import bleach


#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote()
    posts = Post.get_all_posts()
    title = "Home _ Welcome to family news Hub"
    return render_template('index.html',title = title,quote=quote,posts=posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Post.query.filter_by(user_id = user.id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route("/post/<int:id>", methods = ["POST", "GET"])
def post(id):
    post = Post.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(post_id = id).all()
    comment_form = CommentForm()
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, comment_on = datetime.now(),comment_by = comment_alias,post_id = id)
        new_comment.save_comment()
        return redirect(url_for("main.post", id = post.id))

    return render_template("blog.html",post = post,comments = comments,comment_form = comment_form,comment_count = comment_count)

@main.route("/post/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    post = Post.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.post", id = post.id))

@main.route("/post/<int:id>/<int:comment_id>/favourite")
@login_required
def fav_comment(id, comment_id):
    post = Post.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    comment.count_likes = 1
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.post', id = post.id))

@main.route("/post/<int:id>/update", methods = ["POST", "GET"])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id = id).first()
    edit_form = UpdatePostForm()

    if edit_form.validate_on_submit():
        post.post_title = edit_form.post_title.data
        edit_form.post_title.data = ""
        post.post_content = edit_form.post_content.data
        edit_form.post_content.data = ""

        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.post", id = post.id))

    return render_template("edit_blog.html", post = post,edit_form = edit_form)

@main.route("/post/new", methods = ["POST", "GET"])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.post_title.data
        post_form.post_title.data = ""
        post_content = bleach.clean(post_form.post_content.data, 
                                    tags = bleach.sanitizer.ALLOWED_TAGS + ["h1", "h2", "h3", "h4",
                                                                            "h5", "h6", "p", "span",
                                                                            "div", "br", "em", "strong"
                                                                            "i", "blockquote", "hr", "a"
                                                                            "ul", "ol", "li"])
        post_form.post_content.data = ""
        new_post = Post(post_title = post_title,post_content = post_content,posted_at = datetime.now(),post_by = current_user.username,user_id = current_user.id)
        new_post.save_post()
        
    return render_template("new_blog.html",post_form = post_form)

@main.route("/profile/<int:id>/<int:post_id>/delete")
@login_required
def delete_post(id, post_id):
    user = User.query.filter_by(id = id).first()
    post = Post.query.filter_by(id = post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("main.profile", id = user.id))
