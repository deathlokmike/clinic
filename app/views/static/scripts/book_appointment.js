function createBubble(text, onClick) {
    let bubble = document.createElement("div");
    bubble.classList.add("px-2", "py-2", "font-semibold", "text-gray-700", "cursor-pointer",
        "bg-white", "rounded-xl", "shadow",
        "transition", "duration-150", "ease-in", "hover:bg-gray-200")
    bubble.innerText = text;
    bubble.addEventListener("click", onClick);
    return bubble;
}

function createDoctorCard(doctor, onClick) {
    let d_name = document.createElement("span");
    let d_experience = document.createElement("span");
    let d_img = document.createElement("img");
    let img_span = document.createElement("span");
    let text_div = document.createElement("span");
    let align_div = document.createElement("div");
    let img_div = document.createElement("div");
    let card = document.createElement("div");

    img_span.classList.add("relative", "p-2", "bg-blue-100", "rounded-full");
    d_name.classList.add("ml-2", "font-semibold", "text-sm", "text-left", "text-black");
    d_experience.classList.add("ml-2", "text-left", "text-sm", "text-gray-500");
    text_div.classList.add("flex", "flex-col")
    img_div.classList.add("flex", "items-center");
    align_div.classList.add("flex", "items-center", "justify-between");
    card.classList.add("w-full", "p-4", "bg-white", "shadow", "rounded-2xl", "cursor-pointer",
        "transition", "duration-150", "ease-in", "hover:bg-gray-200");

    d_img.alt = "doctor_image";
    d_img.width = "36";
    d_img.height = "36";
    d_img.src = "../static/" + doctor.profile_photo_path;

    d_name.innerText = doctor.full_name;
    d_experience.innerText = doctor.experience + " лет опыта";

    text_div.appendChild(d_name);
    text_div.appendChild(d_experience);
    img_span.appendChild(d_img);
    img_div.appendChild(img_span);
    img_div.appendChild(text_div);
    align_div.appendChild(img_div);

    card.appendChild(align_div);
    card.addEventListener("click", onClick);
    return card;
}

function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }
}

class SelectedData {
    constructor() {
        this.date = null;
        this.time = null;
        this.doctorId = null;
    }

    getDateTime() {
        console.log(this.date + "T" + this.time);
        let dateTime = Date.parse(this.date + "T" + this.time);
        return dateTime;
    }
}

class BookAppointment {
    constructor() {
        this.specialization = document.getElementById("specialization");
        this.doctors = document.getElementById("doctors");
        this.dates = document.getElementById("dates");
        this.times = document.getElementById("times");
        this.confirm = document.getElementById("confirm-button");
        this.confirm.addEventListener("click", this.sendToApi.bind(this));

        this.selectedSpecialization = null;
        this.selectedDoctor = null;
        this.selectedDate = null;
        this.selectedTime = null;
        this.data = null;

        this.selectedData = new SelectedData();
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
        document.getElementById("specialization_main").classList.remove("hidden");
        clearElement(this.specialization);
        document.getElementById("doctors_main").classList.add("hidden");
        document.getElementById("dates_main").classList.add("hidden");
        document.getElementById("times_main").classList.add("hidden");
        for (let item of this.data) {
            let bubble = createBubble(item.specialization, () => {
                if (this.selectedSpecialization) {
                    this.selectedSpecialization.classList.remove("ring-green-300", "outline-none", "ring-2", "shadow-md");
                    this.selectedSpecialization.classList.add("hover:bg-gray-200")
                }
                bubble.classList.add("ring-green-300", "outline-none", "ring-2", "shadow-md");
                bubble.classList.remove("hover:bg-gray-200");
                this.selectedSpecialization = bubble;
                this.fillDoctors.bind(this)(item.doctors);
            });
            this.specialization.appendChild(bubble);
        }
    }

    fillDoctors(doctorsList) {
        document.getElementById("doctors_main").classList.remove("hidden");
        clearElement(this.doctors);
        clearElement(this.dates);
        clearElement(this.times);
        document.getElementById("dates_main").classList.add("hidden");
        document.getElementById("times_main").classList.add("hidden");
        this.confirm.classList.add("hidden");
        for (let doctor of doctorsList) {
            let card = createDoctorCard(doctor, () => {
                if (this.selectedDoctor) {
                    this.selectedDoctor.classList.remove("ring-green-300", "outline-none", "ring-2", "shadow-md");
                    this.selectedDoctor.classList.add("hover:bg-gray-200")
                }
                card.classList.add("ring-green-300", "outline-none", "ring-2", "shadow-md");
                card.classList.remove("hover:bg-gray-200");
                this.selectedDoctor = card;
                this.selectedData.doctorId = doctor.id;
                this.fillDates.bind(this)(doctor.free_appointments);
            });
            this.doctors.appendChild(card);
        }
    }

    fillDates(datesList) {
        document.getElementById("dates_main").classList.remove("hidden");
        clearElement(this.dates);
        clearElement(this.times);
        document.getElementById("times_main").classList.add("hidden");
        this.confirm.classList.add("hidden");
        for (let date of datesList) {
            let bubble = createBubble(date.date, () => {
                console.log(date.date);
                if (this.selectedDate) {
                    this.selectedDate.classList.remove("ring-green-300", "outline-none", "ring-2", "shadow-md");
                    this.selectedDate.classList.add("hover:bg-gray-200")
                }
                bubble.classList.add("ring-green-300", "outline-none", "ring-2", "shadow-md");
                bubble.classList.remove("hover:bg-gray-200");
                this.selectedDate = bubble;
                this.selectedData.date = date.date;
                this.fillTimes.bind(this)(date.time);
            });
            this.dates.appendChild(bubble);
        }
    }

    fillTimes(timesList) {
        document.getElementById("times_main").classList.remove("hidden");
        clearElement(this.times);
        this.confirm.classList.add("hidden");
        for (let time of timesList) {
            let bubble = createBubble(time, () => {
                if (this.selectedTime) {
                    this.selectedTime.classList.remove("bring-green-300", "outline-none", "ring-2", "shadow-md");
                    this.selectedTime.classList.add("hover:bg-gray-200")
                }
                bubble.classList.add("ring-green-300", "outline-none", "ring-2", "shadow-md");
                bubble.classList.remove("hover:bg-gray-200");
                this.selectedTime = bubble;
                console.log(time);
                this.selectedData.time = time;
                this.confirm.classList.remove("hidden");
            });
            this.times.appendChild(bubble);
        }
    }

    async sendToApi() {
        const url = "/api/appointments/book";

        let data = {
            doctor_id: this.selectedData.doctorId,
            date_time: this.selectedData.getDateTime.bind(this.selectedData)(),
        };

        await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        }).then(response => {
            if (response.status === 200) {
                window.alert("Успешно");
            } else {
                response.json().then(value => {
                    window.alert("Ошибка");
                })
            }
        });
    }
}
