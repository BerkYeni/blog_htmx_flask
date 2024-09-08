from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Post

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
    # Implement new post creation logic
    pass

@bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    # Implement post editing logic
    pass

@bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    # Implement post deletion logic
    pass