from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

feed_blueprint = Blueprint('feed', __name__)

@login_required
@feed_blueprint.route('/')
@feed_blueprint.route('/home')
def feed():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('feed.html')