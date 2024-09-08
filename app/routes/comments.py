from flask import Blueprint, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import Comment, Post
from app import db

bp = Blueprint('comments', __name__)

@bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    # Implement comment creation logic
    pass

@bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    # Implement comment deletion logic
    pass