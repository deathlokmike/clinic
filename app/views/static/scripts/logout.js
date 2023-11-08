window.addEventListener("logout", () => logoutUser(), false);

async function logoutUser() {
    const url = "/api/auth/logout";

    await fetch(url, {
        method: 'POST',
    }).then(response => {
        if (response.status === 200) {
            window.location.href = "/login";
        }
    });
}