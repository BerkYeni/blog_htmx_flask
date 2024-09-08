from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Post
from app import db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post.html', post=post)

@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.post', post_id=post.id))
    return render_template('blog/create_post.html')

@bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have permission to edit this post.', 'error')
        return redirect(url_for('blog.post', post_id=post.id))
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.post', post_id=post.id))
    return render_template('blog/edit_post.html', post=post)

@bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have permission to delete this post.', 'error')
        return redirect(url_for('blog.post', post_id=post.id))
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('blog.index'))