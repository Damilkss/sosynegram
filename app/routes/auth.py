from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user

from app.models import User, data_base
from app.utils.validator import validate_username, validate_password

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm = request.form.get('confirm', '').strip()

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('register.html',
                                   username_error='Пользователь с таким именем уже существует',
                                   username_value=username)

        is_valid_username, username_error = validate_username(username)
        if not is_valid_username:
            return render_template('register.html',
                                   username_value=username,
                                   username_error=username_error)

        is_valid_password, password_error = validate_password(password)
        if not is_valid_password:
            return render_template('register.html',
                                   username_value=username,
                                   password_error=password_error)

        if password != confirm:
            return render_template('register.html',
                                   username_value=username,
                                   confirm_password_error='Пароли не совпадают')

        try:
            new_user = User()
            new_user.set_username(username)
            new_user.set_password(password)
            data_base.session.add(new_user)
            data_base.session.commit()

            login_user(new_user)
            return redirect(url_for('feed.feed'))

        except Exception as exception:
            data_base.session.rollback()
            return render_template('register.html',
                                   username_value=username,
                                   general_error=f'Ошибка при регистрации: {str(exception)}')

    return render_template('register.html')



@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            return render_template('login.html',
                                   general_error='Пожалуйста, заполните все поля',
                                   username_value=username)
        try:
            user = User.query.filter_by(username=username).first()

            if user:
                if user.check_password(password):
                    login_user(user)
                    return redirect(url_for('feed.feed'))
                else:
                    return render_template('login.html',
                                           password_error='Неверный пороль',
                                           username_value=username)
            else:
                return render_template('login.html',
                                       username_error='Неизвестный пользователь',
                                       username_value=username)

        except Exception as exception:
            return render_template('login.html',
                                   username_error=f'Ошибка при входе: {str(exception)}',
                                   username_value=username)

    return render_template('login.html')


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.feed'))