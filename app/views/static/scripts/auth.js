window.addEventListener("login", () => loginUser(), false);
window.addEventListener("register", () => registerUser(), false);


document.addEventListener('DOMContentLoaded', function () {
    let passwordInput = document.getElementById('password');
    let togglePasswordButton = document.getElementById('toggle_hide_password');
    let hiddenIcon = document.getElementById('img_hide');
    let shownIcon = document.getElementById('img_show');

    togglePasswordButton.addEventListener('click', function () {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            shownIcon.classList.add('hidden');
            hiddenIcon.classList.remove('hidden');
        } else {
            passwordInput.type = 'password';
            hiddenIcon.classList.add('hidden');
            shownIcon.classList.remove('hidden');
        }
    });
});

function showError(text) {
    let errorMessageBlock = document.getElementById("error_message_block");
    let errorMessageSpan = document.getElementById("error_message_text");
    errorMessageSpan.textContent = text;
    errorMessageBlock.classList.remove('hidden');
}


async function auth(url) {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, password: password }),
    })
    if (response.status === 200) {
        window.location.href = "/me";
    }
    else if (response.status === 422) {
        showError("Неверный формат почты")
    }
    else {
        let error_text = await response.json();
        showError(error_text.detail);
    }
}


async function loginUser() {
    let url = "/api/auth/login";
    await auth(url);
}


async function registerUser() {
    const url = "/api/auth/register";
    await auth(url);
}
