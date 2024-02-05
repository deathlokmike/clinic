window.addEventListener("DOMContentLoaded", () => onLoaded(), false);


function onLoaded() {
    let btnConfirm = document.getElementById("btn_confirm");
    btnConfirm.addEventListener("click", sendPersonalData);
}

function showError(text) {
    let errorMessageBlock = document.getElementById("error_message_block");
    let errorMessageSpan = document.getElementById("error_message_text");
    errorMessageSpan.textContent = text;
    errorMessageBlock.classList.remove('hidden');
}

async function sendPersonalData() {
    const url = "/api/users/update_fullname";
    let firstName = document.getElementById("pd_first_name").value;
    let secondName = document.getElementById("pd_second_name").value;
    let lastName = document.getElementById("pd_last_name").value;

    if (firstName.length === 0 || lastName.length === 0) {
        let requiredFirstNameMessage = document.getElementById("required_field_first");
        let requiredLastLNameMessage = document.getElementById("required_field_last");
        requiredFirstNameMessage.classList.remove("hidden");
        requiredLastLNameMessage.classList.remove("hidden");
        return;
    }

    let response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(
            {
                first_name: firstName,
                second_name: secondName,
                last_name: lastName,
            }),
    })
    if (response.status === 200) {
        window.location.href = "/me";
    }
    else if (response.status === 422) {
        showError("Неверный формат данных")
    }
    else {
        let error_text = await response.json();
        showError(error_text.detail);
    }
}