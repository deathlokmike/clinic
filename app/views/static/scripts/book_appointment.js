function getFormattedDate(date) {
    return date;
}

function getFormattedTime(time) {
    return time;
}

function _renderCloseButton(node, mainNode) {
    let navBar = document.getElementById("mobile_nav_bar")
    let body = document.createElement('div');
    let button = document.createElement('button');

    button.setAttribute('type', 'button');
    button.classList.add(
        'py-2',
        'px-4',
        'bg-blue-600',
        'hover:bg-blue-700',
        'focus:ring-blue-500',
        'focus:ring-offset-blue-200',
        'text-white',
        'w-full',
        'transition',
        'ease-in',
        'duration-200',
        'text-center',
        'text-base',
        'font-semibold',
        'shadow-md',
        'focus:outline-none',
        'focus:ring-2',
        'focus:ring-offset-2',
        'rounded-lg'
    );
    button.innerText = 'Закрыть';
    button.onclick = function () {
        clearElement(mainNode);
        navBar.classList.remove("hidden")
    };

    body.classList.add(
        'flex',
        'items-center',
        'justify-between',
        'w-full',
        'gap-4',
        'mt-8');
    body.appendChild(button);

    node.appendChild(body);
}

function _renderTextObject(node, text) {
    textBlock = document.createElement('p');
    textBlock.classList.add(
        'px-6',
        'py-2',
        'text-gray-600',
        'dark:text-gray-100',
        'text-md'
    );
    textBlock.innerText = text;
    node.appendChild(textBlock);
}

function _getColorAndIconPath(isSuccessful) {
    if (isSuccessful) {
        var color = 'text-green-500';
        var path = 'M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z';
    }
    else {
        var color = 'text-red-500';
        var path = 'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z';
    }
    return [color, path];
}

function _renderIcon(node, isSuccessful) {
    var colorPath = _getColorAndIconPath(isSuccessful);
    let iconSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    let iconPath1 = document.createElementNS(
        'http://www.w3.org/2000/svg',
        'path'
    );
    let iconPath2 = document.createElementNS(
        'http://www.w3.org/2000/svg',
        'path'
    );

    iconSvg.setAttribute('fill', 'none');
    iconSvg.setAttribute('viewBox', '0 0 24 24');
    iconSvg.classList.add('w-12', 'h-12', 'm-auto', 'mt-4', colorPath[0]);

    iconPath1.setAttribute('d', 'M0 0h24v24H0z');
    iconPath1.setAttribute('fill', 'none');

    iconPath2.setAttribute('d', colorPath[1]);
    iconPath2.setAttribute('fill', 'currentColor');

    iconSvg.appendChild(iconPath1);
    iconSvg.appendChild(iconPath2);

    node.appendChild(iconSvg);
}

function _getCardFlex(node, text, isSuccessful) {
    let cardFlex = document.createElement('div');
    cardFlex.classList.add(
        'flex',
        'flex-col',
        'justify-between',
        'h-full'
    );
    _renderIcon(cardFlex, isSuccessful);
    _renderTextObject(cardFlex, text);
    _renderCloseButton(cardFlex, node);
    return cardFlex;
}

function _renderCardSize(node, cardFlex) {
    let cardSize = document.createElement('div');
    cardSize.classList.add(
        'w-full',
        'h-full',
        'text-center'
    );
    cardSize.appendChild(cardFlex);
    node.appendChild(cardSize);
}

function _renderCardBody(node, cardFlex) {
    let cardBody = document.createElement('div');
    cardBody.classList.add(
        'w-64',
        'p-4',
        'm-auto',
        'bg-gray-50',
        'shadow-lg',
        'rounded-xl',
        'dark:bg-gray-700');
    _renderCardSize(cardBody, cardFlex);
    node.appendChild(cardBody);
}

function _renderCard(node, cardFlex) {
    let blur = document.createElement('div');
    blur.classList.add(
        'fixed',
        'flex',
        'justify-center',
        'inset-0',
        'bg-gray-600',
        'backdrop-blur-sm',
        'dark:bg-gray-800',
        'dark:bg-opacity-50',
        'bg-opacity-50',
        'overflow-x-hidden',
        'overflow-y-auto',
        'h-full',
        'w-full',
        'top-0',
        'right-0',
        'left-0',
        'z-50');
    _renderCardBody(blur, cardFlex);
    node.appendChild(blur);
}

function renderInfoCard(text, isSuccessful) {
    let modal = document.getElementById('modal');
    modal.classList.add('hidden')
    let cardMain = document.getElementById('card_main');
    clearElement(cardMain);
    let cardFlex = _getCardFlex(cardMain, text, isSuccessful);
    _renderCard(cardMain, cardFlex);
}

function createBubble(text, onClick) {
    let bubble = document.createElement('div');
    bubble.classList.add(
        'px-2',
        'py-2',
        'font-semibold',
        'text-gray-500',
        'cursor-pointer',
        'bg-gray-50',
        'rounded-xl',
        'shadow',
        'transition',
        'duration-150',
        'ease-in',
        'hover:bg-gray-200',
        'dark:text-gray-200',
        'dark:bg-gray-700',
        'dark:hover:bg-gray-500')
    bubble.innerText = text;
    bubble.addEventListener('click', onClick);
    return bubble;
}

function createDoctorCard(doctor, onClick) {
    let d_name = document.createElement('span');
    let d_experience = document.createElement('span');
    let d_img = document.createElement('img');
    let img_span = document.createElement('span');
    let text_div = document.createElement('span');
    let align_div = document.createElement('div');
    let img_div = document.createElement('div');
    let card = document.createElement('div');

    d_img.classList.add(
        'mx-auto',
        'object-cover',
        'rounded-full',
        'h-10',
        'w-10',
        'bg-blue-100'
    );
    img_span.classList.add(
        'relative',
        'block'
    );
    d_name.classList.add(
        'ml-2',
        'font-semibold',
        'text-sm',
        'text-left',
        'text-black',
        'dark:text-gray-200'
    );
    d_experience.classList.add(
        'ml-2',
        'text-left',
        'text-sm',
        'text-gray-500',
        'dark:text-gray-400'
    );
    text_div.classList.add(
        'flex',
        'flex-col')
    img_div.classList.add(
        'flex',
        'items-center');
    align_div.classList.add(
        'flex',
        'place-items-center',
        'justify-start'
    );
    card.classList.add(
        'w-full',
        'p-4',
        'bg-gray-50',
        'shadow',
        'rounded-2xl',
        'cursor-pointer',
        'transition',
        'duration-150',
        'ease-in',
        'hover:bg-gray-200',
        'dark:bg-gray-700',
        'dark:hover:bg-gray-500'
    );

    d_img.alt = 'doctor_image';
    d_img.width = '36';
    d_img.height = '36';
    d_img.src = '../static/' + doctor.personal_data.profile_photo_path;

    d_name.innerText = doctor.personal_data.first_name + ' ' + doctor.personal_data.second_name + ' ' + doctor.personal_data.last_name;
    d_experience.innerText = doctor.experience + ' лет опыта';

    text_div.appendChild(d_name);
    text_div.appendChild(d_experience);
    img_span.appendChild(d_img);
    img_div.appendChild(img_span);
    img_div.appendChild(text_div);
    align_div.appendChild(img_div);

    card.appendChild(align_div);
    card.addEventListener('click', onClick);
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
        let dateTime = Date.parse(this.date + 'T' + this.time);
        return dateTime;
    }
}

class BookAppointment {
    constructor() {
        this.specialization = document.getElementById('specialization');
        this.doctors = document.getElementById('doctors');
        this.dates = document.getElementById('dates');
        this.times = document.getElementById('times');
        confirm = document.getElementById('confirm-button');
        this.confirm = confirm.cloneNode(true);
        confirm.parentNode.replaceChild(this.confirm, confirm);
        this.confirm.addEventListener('click', this.sendToApi.bind(this));

        this.selectedSpecialization = null;
        this.selectedDoctor = null;
        this.selectedDate = null;
        this.selectedTime = null;
        this.data = null;

        this.selectedData = new SelectedData();
    }

    async init() {
        const url = '/api/appointments/available';
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
                    alert('Произошла ошибка: ' + value.detail);
                })
            }
        });
    }

    fillSpecialization() {
        document.getElementById('specialization_main').classList.remove('hidden');
        clearElement(this.specialization);
        document.getElementById('doctors_main').classList.add('hidden');
        document.getElementById('dates_main').classList.add('hidden');
        document.getElementById('times_main').classList.add('hidden');
        for (let item of this.data) {
            let bubble = createBubble(item.specialization, () => {
                if (this.selectedSpecialization) {
                    this.selectedSpecialization.classList.remove(
                        'ring-green-300',
                        'outline-none',
                        'ring-2',
                        'shadow-md'
                    );
                    this.selectedSpecialization.classList.add('hover:bg-gray-200')
                }
                bubble.classList.add(
                    'ring-green-300',
                    'outline-none',
                    'ring-2',
                    'shadow-md'
                );
                bubble.classList.remove('hover:bg-gray-200');
                this.selectedSpecialization = bubble;
                this.fillDoctors.bind(this)(item.doctors);
            });
            this.specialization.appendChild(bubble);
        }
    }

    fillDoctors(doctorsList) {
        document.getElementById('doctors_main').classList.remove('hidden');
        clearElement(this.doctors);
        clearElement(this.dates);
        clearElement(this.times);
        document.getElementById('dates_main').classList.add('hidden');
        document.getElementById('times_main').classList.add('hidden');
        this.confirm.classList.add('hidden');
        for (let doctor of doctorsList) {
            let card = createDoctorCard(doctor, () => {
                if (this.selectedDoctor) {
                    this.selectedDoctor.classList.remove(
                        'ring-green-300',
                        'outline-none',
                        'ring-2',
                        'shadow-md'
                    );
                    this.selectedDoctor.classList.add('hover:bg-gray-200')
                }
                card.classList.add(
                    'ring-green-300',
                    'outline-none',
                    'ring-2',
                    'shadow-md');
                card.classList.remove('hover:bg-gray-200');
                this.selectedDoctor = card;
                this.selectedData.doctorId = doctor.id;
                this.fillDates.bind(this)(doctor.free_appointments);
            });
            this.doctors.appendChild(card);
        }
    }

    fillDates(datesList) {
        document.getElementById('dates_main').classList.remove('hidden');
        clearElement(this.dates);
        clearElement(this.times);
        document.getElementById('times_main').classList.add('hidden');
        this.confirm.classList.add('hidden');
        for (let date of datesList) {
            let bubble = createBubble(date.date, () => {
                if (this.selectedDate) {
                    this.selectedDate.classList.remove(
                        'ring-green-300',
                        'outline-none',
                        'ring-2',
                        'shadow-md'
                    );
                    this.selectedDate.classList.add('hover:bg-gray-200')
                }
                bubble.classList.add(
                    'ring-green-300',
                    'outline-none',
                    'ring-2',
                    'shadow-md'
                );
                bubble.classList.remove('hover:bg-gray-200');
                this.selectedDate = bubble;
                this.selectedData.date = date.date;
                this.fillTimes.bind(this)(date.time);
            });
            this.dates.appendChild(bubble);
        }
    }

    fillTimes(timesList) {
        document.getElementById('times_main').classList.remove('hidden');
        clearElement(this.times);
        this.confirm.classList.add('hidden');
        for (let time of timesList) {
            let bubble = createBubble(time, () => {
                if (this.selectedTime) {
                    this.selectedTime.classList.remove(
                        'bring-green-300',
                        'outline-none',
                        'ring-2',
                        'shadow-md'
                    );
                    this.selectedTime.classList.add('hover:bg-gray-200')
                }
                bubble.classList.add(
                    'ring-green-300',
                    'outline-none',
                    'ring-2',
                    'shadow-md'
                );
                bubble.classList.remove('hover:bg-gray-200');
                this.selectedTime = bubble;
                this.selectedData.time = time;
                this.confirm.classList.remove('hidden');
            });
            this.times.appendChild(bubble);
        }
    }


    async sendToApi() {
        const url = '/api/appointments/book';

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
                renderInfoCard('Успешно', true);
            } else {
                response.json().then(value => {
                    renderInfoCard('Ошибка', false);
                })
            }
        });
    }
}
