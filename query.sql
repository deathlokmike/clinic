-- Active: 1700866669137@@127.0.0.1@5432@clinic_db


INSERT INTO roles (id, name)
VALUES
(0, 'Пациент'),
(1, 'Врач')

INSERT INTO personal_data(first_name, second_name, last_name, birth_day, gender, passport_data, address, phone_number, profile_photo_path)
VALUES
('Иван', 'Сергеевич', 'Кузнецов','1990-05-15', true, '5234045678', 'ул. Ленина, д. 123', '79012345678', 'img/users/f68d50db-f10a-48b4-acb1-8fae183cac3a.png'),
('Мария', 'Егоровна', 'Иванова','1985-09-20', false, '9876543210', 'ул. Гагарина, д. 45', '79123456789', 'img/default_profile_photo.png'),
('Алексей','Дмитриевич', 'Федоров', '1995-02-10', true, '1122334455', 'ул. Пушкина, д. 67', '79234567890', 'img/default_profile_photo.png'),
('Екатерина','Андреевна', 'Соколова', '1980-12-25', false, '5544332211', 'ул. Жукова, д. 56', '79345678901', 'img/default_profile_photo.png'),
('Павел', 'Иванович', 'Петров','1988-07-08', true, '7654321098', 'ул. Строителей, д. 32', '79456789012', 'img/default_profile_photo.png'),
('Светлана','Александровна', 'Смирнова', '1992-03-12', false, '1111222233', 'ул. Кирова, д. 78', '79567890123', 'img/default_profile_photo.png'),
('Денис','Николаевич', 'Романов','1987-11-30', true, '9876543210', 'ул. Лермонтова, д. 14', '79678901234', 'img/default_profile_photo.png'),
('Анна','Игоревна', 'Захарова', '1983-04-05', false, '1122334455', 'ул. Маяковского, д. 98', '79789012345', 'img/default_profile_photo.png'),
('Михаил','Артемьевич', 'Денисов', '1991-06-18', true, '5544332211', 'ул. Рабочая, д. 27', '79890123456', 'img/default_profile_photo.png'),
('Татьяна','Олеговна', 'Мельникова', '1986-10-03', false, '7654321098', 'ул. Садовая, д. 8', '79901234567', 'img/default_profile_photo.png');

INSERT INTO users (id, email, password, role_id, pd_id)
VALUES
('f68d50db-f10a-48b4-acb1-8fae183cac3a', 'user1@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 1),
('4d527bd4-c872-4e2c-a56f-14260b345a64', 'user2@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 2),
('4a7f20f7-e92d-4925-a580-2b965e2da0a6', 'user3@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 3),
('bead8e61-68be-4f39-a459-bf6c906b37c1', 'user4@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 4),
('98367c58-9574-4c54-ac91-da4c764c75aa', 'user5@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 5),
('cb56fdbb-fd02-4fd8-a3d9-3487b54f21cc', 'user6@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 6),
('a5c42a22-3fa0-4bf3-b489-5d4fc9d7ea6f', 'user7@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 7),
('b6bac282-22ae-4128-8478-7f61c54b6487', 'user8@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 8),
('6434ece9-19a9-45fe-ba04-ba8648db5f16', 'user9@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 9),
('9a9e283a-eedb-408d-a9ea-7ac4fb1ee1dc', 'user10@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 1, 10);


INSERT INTO doctors (user_id, specialization, date_employment, pre_work_experience, resigned)
VALUES
('f68d50db-f10a-48b4-acb1-8fae183cac3a','Хирург', '2017-05-10', 6, false), 
('4d527bd4-c872-4e2c-a56f-14260b345a64','Терапевт', '2015-08-20', 8, false),
('4a7f20f7-e92d-4925-a580-2b965e2da0a6','Хирург', '2016-12-08', 7, false),
('bead8e61-68be-4f39-a459-bf6c906b37c1','Терапевт', '2019-03-25', 4, false),
('98367c58-9574-4c54-ac91-da4c764c75aa','Хирург', '2015-06-10', 8, false),
('cb56fdbb-fd02-4fd8-a3d9-3487b54f21cc','Терапевт', '2018-11-12', 5, true),
('a5c42a22-3fa0-4bf3-b489-5d4fc9d7ea6f','Хирург', '2017-09-30', 6, false),
('b6bac282-22ae-4128-8478-7f61c54b6487','Терапевт', '2016-04-15', 7, false),
('6434ece9-19a9-45fe-ba04-ba8648db5f16','Хирург', '2015-12-18', 6, false),
('9a9e283a-eedb-408d-a9ea-7ac4fb1ee1dc','Терапевт', '2019-08-14', 4, false);

INSERT INTO appointments (id, patient_id, doctor_id, date_time, status)
VALUES
(1, 1, 1, '2023-11-19 10:00:00', 0),
(2, 2, 2, '2023-10-19 10:00:00', 1),
(3, 1, 3, '2023-11-19 10:00:00', 2),
(4, 3, 4, '2023-10-20 10:00:00', 2),
(5, 1, 5, '2023-11-19 10:00:00', 3);
    