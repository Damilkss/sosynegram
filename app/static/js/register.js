const username = document.getElementById('username');
const password = document.getElementById('password');
const confirm = document.getElementById('confirm');

const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');
const confirmError = document.getElementById('confirmError');

username.addEventListener('input', usernameInput);
password.addEventListener('input', passwordInput);
confirm.addEventListener('input', confirmInput);

function usernameInput() {
    const cursorPos = this.selectionStart;
    const oldValue = this.value;

    this.value = this.value.replace(/\s/g, '');
    this.value = this.value.substring(0, 20);

    const newCursorPos = cursorPos - (oldValue.length - this.value.length);
    this.setSelectionRange(newCursorPos, newCursorPos);

    usernameCheck();
}

function passwordInput() {
    const cursorPos = this.selectionStart;
    const oldValue = this.value;

    this.value = this.value.replace(/\s/g, '');
    this.value = this.value.substring(0, 16);

    const newCursorPos = cursorPos - (oldValue.length - this.value.length);
    this.setSelectionRange(newCursorPos, newCursorPos);

    passwordCheck();
    confirmCheck();
}

function confirmInput() {
    const cursorPos = this.selectionStart;
    const oldValue = this.value;

    this.value = this.value.replace(/\s/g, '');
    this.value = this.value.substring(0, 16);

    const newCursorPos = cursorPos - (oldValue.length - this.value.length);
    this.setSelectionRange(newCursorPos, newCursorPos);

    confirmCheck();
}

function usernameCheck() {
    const value = username.value;
    let error = '';

    if (value.length < 5 || value.length > 20) {
        error = 'Имя пользователя должно содержать от 5 до 20 символов';
    } else if (!/^[а-яА-Яa-zA-Z0-9_]+$/.test(value)) {
        error = 'Имя пользователя может содержать только буквы, цифры и подчеркивания';
    } else if (!/[а-яА-Яa-zA-Z]/.test(value)) {
        error = 'Имя пользователя должно содержать хотя бы одну букву';
    } else if (value.startsWith('_') || value.endsWith('_')) {
        error = 'Имя пользователя не может начинаться или заканчиваться подчеркиванием';
    } else if (/^\d/.test(value)) {
        error = 'Имя пользователя не может начинаться на цифру';
    } else if (/__/.test(value)) {
        error = 'Имя пользователя не может содержать последовательные подчеркивания';
    }

    if (error) {
        usernameError.textContent = error;
        usernameError.style.display = 'block';
        username.classList.add('is-invalid');
    } else {
        usernameError.style.display = 'none';
        username.classList.remove('is-invalid');
    }
}

function passwordCheck() {
    const value = password.value;
    let error = '';

    if (value.length < 8 || value > 16) {
        error = 'Пароль должен содержать от 8 до 16 символов';
    } else if (!/[A-Za-z]/.test(value)) {
        error = 'Пароль должен содержать хотя бы одну букву';
    } else if (!/\d/.test(value)) {
        error = 'Пароль должен содержать хотя бы одну цифру';
    } else if (!/[!@#$%^&*()_+\-=[\]{};:"\\|,.<>?]/.test(value)) {
        error = 'Пароль должен содержать хотя бы один специальный символ';
    }

    if (error) {
        passwordError.textContent = error;
        passwordError.style.display = 'block';
        password.classList.add('is-invalid');
    } else {
        passwordError.style.display = 'none';
        password.classList.remove('is-invalid');
    }
}

function confirmCheck() {
    if (confirm.value === '' && password.value === '') {
        confirmError.style.display = 'none';
        confirm.classList.remove('is-invalid');
        return;
    }
    if (password.value !== confirm.value) {
        confirmError.textContent = 'Пароли не совпадают';
        confirmError.style.display = 'block';
        confirm.classList.add('is-invalid');
    } else {
        confirmError.style.display = 'none';
        confirm.classList.remove('is-invalid');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    if (username.classList.contains('is-invalid')) {
        usernameError.style.display = 'block';
    }
    if (password.classList.contains('is-invalid')) {
        passwordError.style.display = 'block';
    }
    if (confirm.classList.contains('is-invalid')) {
        confirmError.style.display = 'block';
    }
});