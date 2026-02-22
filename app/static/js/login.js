const username = document.getElementById('username');
const password = document.getElementById('password');

const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');

username.addEventListener('input', usernameInput);
password.addEventListener('input', passwordInput);

function usernameInput() {
    const cursorPos = this.selectionStart;
    const oldValue = this.value;

    this.value = this.value.replace(/\s/g, '');
    this.value = this.value.substring(0, 20);

    const newCursorPos = cursorPos - (oldValue.length - this.value.length);
    this.setSelectionRange(newCursorPos, newCursorPos);

    username.classList.remove('is-invalid');
    usernameError.style.display = 'none';
}

function passwordInput() {
    const cursorPos = this.selectionStart;
    const oldValue = this.value;

    this.value = this.value.replace(/\s/g, '');
    this.value = this.value.substring(0, 16);

    const newCursorPos = cursorPos - (oldValue.length - this.value.length);
    this.setSelectionRange(newCursorPos, newCursorPos);

    password.classList.remove('is-invalid');
    passwordError.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    if (username.classList.contains('is-invalid')) {
        usernameError.style.display = 'block';
    }
    if (password.classList.contains('is-invalid')) {
        passwordError.style.display = 'block';
    }
});