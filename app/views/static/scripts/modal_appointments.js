var bookButton = document.getElementById("book-button");
var declineButton = document.getElementById("decline-button");
var modal = document.getElementById("modal");
var close = document.getElementById("close");
var results = document.getElementById("results");


function getBookings() {
    const book = new BookAppointment()
    book.init.bind(book)();
}

bookButton.onclick = function () {
    modal.classList.remove("hidden")
    getBookings();
};

close.onclick = function () {
    modal.classList.add("hidden")
};

declineButton.onclick = function () {
    modal.classList.add("hidden")
};

window.onclick = function (event) {
    if (event.target == modal) {
        modal.classList.add("hidden")
    }
};