from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import login_required, current_user
from app.models import Comment, Post
from app import db

bp = Blueprint('comments', __name__)

@bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get('content')
    if content:
        comment = Comment(content=content, user_id=current_user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    else:
        flash('Comment cannot be empty.', 'error')
    
    # Render only the new comment
    return render_template('blog/_comment.html', comment=comment)

@bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        flash('You do not have permission to delete this comment.', 'error')
        return redirect(url_for('blog.post', post_id=comment.post_id))
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('blog.post', post_id=comment.post_id))