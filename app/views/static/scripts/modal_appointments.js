let bookButton = document.getElementById("btn_book_appointment");
let bookButtonMobile = document.getElementById("btn_book_appointment_mobile")
let declineButton = document.getElementById("decline-button");
let modal = document.getElementById("modal");
let close = document.getElementById("close");
let results = document.getElementById("results");
let navBar = document.getElementById("mobile_nav_bar");


function getBookings() {
    const book = new BookAppointment()
    book.init.bind(book)();
}

bookButton.onclick = function () {
    modal.classList.remove("hidden")
    getBookings();
};

bookButtonMobile.onclick = function () {
    modal.classList.remove("hidden")
    navBar.classList.add("hidden");
    getBookings();
};

close.onclick = function () {
    modal.classList.add("hidden")
    navBar.classList.remove("hidden");
    
};

declineButton.onclick = function () {
    modal.classList.add("hidden")
    navBar.classList.remove("hidden");
};

window.onclick = function (event) {
    if (event.target == modal) {
        modal.classList.add("hidden")
        navBar.classList.remove("hidden");
    }
};