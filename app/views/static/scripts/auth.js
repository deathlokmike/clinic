window.addEventListener("login", () => loginUser(), false);
window.addEventListener("register", () => registerUser(), false);


document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const togglePasswordButton = document.getElementById('toggle_password');
    const hiddenIcon = document.querySelector('.toggle-password .hidden');
    const shownIcon = document.querySelector('.toggle-password img:not(.hidden)');

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


async function loginUser() {
    const url = "/api/auth/login";
    const wrongCredentialsSpan = document.getElementById("wrong_credentials");
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    wrongCredentialsSpan.textContent = "";

    await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, password: password }),
    }).then(response => {
        if (response.status === 200) {
            window.location.href = "/me/appointments";
        } else {
            response.json().then(value => {
                wrongCredentialsSpan.textContent = value.detail;
            })
        }
    });
}

async function registerUser() {
    const wrongCredentialsSpan = document.getElementById("wrong_credentials");
    const url = "/api/auth/register";
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    wrongCredentialsSpan.textContent = "";

    await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, password: password }),
    }).then(response => {
        if (response.status === 200) {
            window.location.href = "/login"
        } else {
            response.json().then(value => {
                wrongCredentialsSpan.textContent = value.detail;
            })
        }
    });
}
