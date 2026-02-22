import re

def validate_username(username) -> (bool, str):
    if len(username) < 5 or len(username) > 20:
        return False, 'Имя пользователя должно содержать от 5 до 20 символов'

    if not re.match(r'^[а-яА-Яa-zA-Z0-9_]+$', username):
        return False, 'Имя пользователя может содержать только буквы, цифры и подчеркивания'

    if not re.search(r'[а-яА-ЯA-Za-z]', username):
        return False, 'Имя пользователя должно содержать хотя бы одну букву'

    if username.startswith('_') or username.endswith('_'):
        return False, 'Имя пользователя не может начинаться или заканчиваться подчеркиванием'

    if re.match(r'\d', username):
        return False, 'Имя пользователя не может начинаться на цифру'

    if '__' in username:
        return False, 'Имя пользователя не может содержать последовательные подчеркивания'

    return True, ''


def validate_password(password) -> (bool, str):
    if len(password) < 8 or len(password) > 16:
        return False, 'Пароль должен содержать от 8 до 16 символов'

    if not re.match(r'^[а-яА-Яa-zA-Z0-9!@#$%^&*()_+\-=\[\]{}:"\\/|,.<>?]+$', password):
        return False, 'Пароль может содержать только буквы, цифры и специальные символы'

    if not re.search(r'[а-яА-Яa-zA-Z]', password):
        return False, 'Пароль должен содержать хотя бы одну букву'

    if not re.search(r'\d', password):
        return False, 'Пароль должен содержать хотя бы одну цифру'

    if not re.search(r'[!@#$%^&*()_+\-=\[\]{}:"\\/|,.<>?]', password):
        return False, 'Пароль должен содержать хотя бы один специальный символ'

    if re.match(r'\d', password):
        return False, 'Пароль не может начинаться на цифру'

    if password[0] in '!@#$%^&*()_+-=[]{}:\"\\/|,.<>?':
        return False, 'Пароль не может начинаться со специального символа'

    return True, ''