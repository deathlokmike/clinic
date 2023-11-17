function createBubble(text, onClick) {
    let bubble = document.createElement("div");
    bubble.classList.add("px-2", "py-2", "font-semibold", "text-gray-700", "bg-gray-100", "rounded-xl")
    bubble.innerText = text;
    bubble.addEventListener("click", onClick);
    return bubble;
}

function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }
}

class BookAppointment {
    constructor() {
        this.specialization = document.getElementById("specialization");
        this.doctors = document.getElementById("doctors");
        this.dates = document.getElementById("dates");
        this.times = document.getElementById("times");
        this.confirm = document.getElementById("confirm-button");

        this.selectedSpecialization = null;
        this.selectedDoctor = null;
        this.selectedDate = null;
        this.selectedTime = null;
        this.data = null;
    }

    async init() {
        const url = "/api/appointments/available";
        await fetch(url, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        }).then(response => {
            if (response.status === 200) {
                response.json().then(value => {
                    this.data = value;
                    this.fillSpecialization.bind(this)();
                })

            } else {
                response.json().then(value => {
                    alert("Произошла ошибка: " + value.detail);
                })
            }
        });
    }

    fillSpecialization() {
        clearElement(specialization);
        for (let item of this.data) {
            let bubble = createBubble(item.specialization, () => {
                if (this.selectedSpecialization) {
                    this.selectedSpecialization.classList.remove("selected");
                }
                bubble.classList.add("selected");
                this.selectedSpecialization = bubble;
                this.fillDoctors.bind(this)(item.doctors);
            });
            this.specialization.appendChild(bubble);
        }
    }

    fillDoctors(doctorsList) {
        clearElement(this.doctors);
        clearElement(this.dates);
        clearElement(this.times);
        this.confirm.classList.add("hidden");
        for (let doctor of doctorsList) {
            let bubble = createBubble(doctor.full_name + " (" + doctor.experience + " лет опыта)", () => {
                if (this.selectedDoctor) {
                    this.selectedDoctor.classList.remove("selected");
                }
                bubble.classList.add("selected");
                this.selectedDoctor = bubble;
                this.fillDates.bind(this)(doctor.free_appointments);
            });
            this.doctors.appendChild(bubble);
        }
    }

    fillDates(datesList) {
        clearElement(this.dates);
        clearElement(this.times);
        this.confirm.classList.add("hidden");
        for (let date of datesList) {
            let bubble = createBubble(date.date, () => {
                if (this.selectedDate) {
                    this.selectedDate.classList.remove("selected");
                }
                bubble.classList.add("selected");
                this.selectedDate = bubble;
                this.fillTimes.bind(this)(date.time);
            });
            this.dates.appendChild(bubble);
        }
    }

    fillTimes(timesList) {
        clearElement(this.times);
        this.confirm.classList.add("hidden");
        for (let time of timesList) {
            let bubble = createBubble(time, () => {
                if (this.selectedTime) {
                    this.selectedTime.classList.remove("selected");
                }
                bubble.classList.add("selected");
                this.selectedTime = bubble;
                this.confirm.classList.remove("hidden");
            });
            this.times.appendChild(bubble);
        }
    }
}





// // Функция для отправки данных на api
// function sendToApi() {
//     // Предположим, что api - это адрес, куда нужно отправить данные
//     let api = "...";
//     // Создаем объект с данными
//     let data = {
//         specialization: selectedSpecialization.innerText,
//         doctor: selectedDoctor.innerText,
//         date: selectedDate.innerText,
//         time: selectedTime.innerText
//     };
//     // Создаем запрос
//     let xhr = new XMLHttpRequest();
//     xhr.open("POST", api, true);
//     xhr.setRequestHeader("Content-Type", "application/json");
//     // Отправляем запрос с данными в формате JSON
//     xhr.send(JSON.stringify(data));
//     // Обрабатываем ответ
//     xhr.onload = function () {
//         if (xhr.status == 200) {
//             // Если все успешно, выводим сообщение
//             alert("Ваша запись подтверждена!");
//         } else {
//             // Если что-то пошло не так, выводим ошибку
//             alert("Произошла ошибка: " + xhr.statusText);
//         }
//     };
// }

// Добавляем обработчик клика на кнопку подтверждения
// confirm.addEventListener("click", sendToApi);

// Заполняем элемент облачками со специализациями при загрузке страницы
