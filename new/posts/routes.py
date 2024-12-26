from flask import Blueprint, flash, render_template, request, redirect, url_for, abort, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from new import db
from new.models import Post
from new.posts.forms import PostForm
import os

posts = Blueprint('posts', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

# File checking utility function
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to create a new post
@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # The content field contains HTML from Quill.js (with media included)
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('create&update_post.html', title='New Post', form=form, legend="New Post")

# Route to view a specific post
@posts.route('/post/<int:post_id>', methods=['GET'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    media_files = post.media_filename.split(',') if post.media_filename else []  # Split filenames if multiple
    return render_template('post_detail.html', post=post, media_files=media_files)

@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if post.author != current_user:
        abort(403)  # Prevent unauthorized access to update
    
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data  # Content already contains embedded media (no separate media handling)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post_detail', post_id=post.id))
    
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content  # This will be passed to the template

    return render_template('create&update_post.html', title='Update Post', form=form, legend="Update Post")

# Route to delete a post
@posts.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Ensure the current user is the author
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
