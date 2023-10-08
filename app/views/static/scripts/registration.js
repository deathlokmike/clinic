document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password_field');
    const repeatPasswordInput = document.getElementById('repeat_password_field');
    const togglePasswordButton = document.getElementById('toggle_password');
    const hiddenIcon = document.querySelector('.toggle-password .hidden');
    const shownIcon = document.querySelector('.toggle-password img:not(.hidden)');

    togglePasswordButton.addEventListener('click', function () {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            repeatPasswordInput.type = 'text';
            shownIcon.classList.add('hidden');
            hiddenIcon.classList.remove('hidden');
        } else {
            passwordInput.type = 'password';
            repeatPasswordInput.type = 'password';
            hiddenIcon.classList.add('hidden');
            shownIcon.classList.remove('hidden');
        }
    });
});
