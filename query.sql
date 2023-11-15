-- Active: 1699656739683@@127.0.0.1@5432@test_db


INSERT INTO roles (id, name)
VALUES
(0, 'Пациент')

INSERT INTO users (id, email, password, role_id) 
VALUES
('f68d50db-f10a-48b4-acb1-8fae183cac3a', 'user1@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('4d527bd4-c872-4e2c-a56f-14260b345a64', 'user2@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('4a7f20f7-e92d-4925-a580-2b965e2da0a6', 'user3@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('bead8e61-68be-4f39-a459-bf6c906b37c1', 'user4@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('98367c58-9574-4c54-ac91-da4c764c75aa', 'user5@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('cb56fdbb-fd02-4fd8-a3d9-3487b54f21cc', 'user6@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('a5c42a22-3fa0-4bf3-b489-5d4fc9d7ea6f', 'user7@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('b6bac282-22ae-4128-8478-7f61c54b6487', 'user8@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('6434ece9-19a9-45fe-ba04-ba8648db5f16', 'user9@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('9a9e283a-eedb-408d-a9ea-7ac4fb1ee1dc', 'user10@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('982eeb52-667c-4acb-9d83-18d7d48f518a', 'user11@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('2a4e3522-f10f-4fdf-a714-3e58f451c92e', 'user12@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('95291318-f3fa-4f0f-b3a0-8908bfe391b6', 'user13@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('3c1fcb41-9c78-4f0f-b820-9711ffc87a6f', 'user14@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('395ed07f-f6eb-4e74-867a-ae6498bc2f2f', 'user15@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('d384f677-9f23-46d4-a790-f8f29abb6f3f', 'user16@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('5632918c-135b-4c49-8af5-89ed75158fb1', 'user17@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('b5eaeb53-2cce-4d7c-855b-08920d66d6b7', 'user18@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('e7800146-efbb-4bce-950e-f7fbf33613eb', 'user19@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('73443f74-ef2b-4797-b6af-dc0ff6f525eb', 'user20@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('d9244ec4-dc91-4f0b-b171-6e08f0f60daa', 'user21@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('21f579ae-fcd7-4029-b3cd-1d912fe631a7', 'user22@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('e11d2790-3cf6-44f0-9bc6-ce2c93b7eb7f', 'user23@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('0de0b82a-76ae-4efe-99d2-1e282f332d70', 'user24@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('9e204d2e-01bb-44f8-857f-e74cd864d6b2', 'user25@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('aadb1517-d708-45d2-a9ec-15ad0ab1a81d', 'user26@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('3bf56fac-b27e-485b-82de-a251070ed5a3', 'user27@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('6e4bf18d-01de-4c16-ac03-bfbf16d61b55', 'user28@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('b95ebf53-5483-4506-919e-9992388cb237', 'user29@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('1dd85ba2-132b-496a-8a32-c7428e842417', 'user30@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('90598678-86c2-432d-b7be-05c3343d9d87', 'user31@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('700137e5-b363-444d-88a6-5a260282c2c3', 'user32@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('a2b8f394-a8ea-4105-9900-728972825a49', 'user33@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('f199ad27-6d92-4fc4-8ea7-0d543b5ab2d9', 'user34@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('e6a7c9a3-91a5-476c-a912-ca2ed3b9c814', 'user35@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('34fa3bc1-d570-4abc-a80d-23f23864722f', 'user36@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0),
('ec7cc5d4-fc10-4a63-82dc-2c4f02f9b4a0', 'user37@example.com', '$2b$12$UDtMnHqsnIajX7ofKaRp0.Bu5rSkKGd0dhQ4RlpUgCMXg2mTUtN66', 0);


INSERT INTO personal_data(user_id, first_name, second_name, last_name, birth_day, gender, passport_data, address, phone_number, profile_photo_path)
VALUES
('f68d50db-f10a-48b4-acb1-8fae183cac3a', 'Иван', 'Сергеевич', 'Кузнецов','1990-05-15', true, '5234045678', 'ул. Ленина, д. 123', '79012345678', 'img/users/f68d50db-f10a-48b4-acb1-8fae183cac3a.png'),
('4d527bd4-c872-4e2c-a56f-14260b345a64', 'Мария', 'Егоровна', 'Иванова','1985-09-20', false, '9876543210', 'ул. Гагарина, д. 45', '79123456789', 'img/default_profile_photo.png'),
('4a7f20f7-e92d-4925-a580-2b965e2da0a6', 'Алексей','Дмитриевич', 'Федоров', '1995-02-10', true, '1122334455', 'ул. Пушкина, д. 67', '79234567890', 'img/default_profile_photo.png'),
('bead8e61-68be-4f39-a459-bf6c906b37c1', 'Екатерина','Андреевна', 'Соколова', '1980-12-25', false, '5544332211', 'ул. Жукова, д. 56', '79345678901', 'img/default_profile_photo.png'),
('98367c58-9574-4c54-ac91-da4c764c75aa', 'Павел', 'Иванович', 'Петров','1988-07-08', true, '7654321098', 'ул. Строителей, д. 32', '79456789012', 'img/default_profile_photo.png'),
('cb56fdbb-fd02-4fd8-a3d9-3487b54f21cc', 'Светлана','Александровна', 'Смирнова', '1992-03-12', false, '1111222233', 'ул. Кирова, д. 78', '79567890123', 'img/default_profile_photo.png'),
('a5c42a22-3fa0-4bf3-b489-5d4fc9d7ea6f', 'Денис','Николаевич', 'Романов','1987-11-30', true, '9876543210', 'ул. Лермонтова, д. 14', '79678901234', 'img/default_profile_photo.png'),
('b6bac282-22ae-4128-8478-7f61c54b6487', 'Анна','Игоревна', 'Захарова', '1983-04-05', false, '1122334455', 'ул. Маяковского, д. 98', '79789012345', 'img/default_profile_photo.png'),
('6434ece9-19a9-45fe-ba04-ba8648db5f16', 'Михаил','Артемьевич', 'Денисов', '1991-06-18', true, '5544332211', 'ул. Рабочая, д. 27', '79890123456', 'img/default_profile_photo.png'),
('9a9e283a-eedb-408d-a9ea-7ac4fb1ee1dc', 'Татьяна','Олеговна', 'Мельникова', '1986-10-03', false, '7654321098', 'ул. Садовая, д. 8', '79901234567', 'img/default_profile_photo.png'),
('982eeb52-667c-4acb-9d83-18d7d48f518a', 'Александр','Петрович', 'Герасимов', '1993-08-14', true, '5234045678', 'ул. Центральная, д. 72', '79912345678', 'img/default_profile_photo.png'),
('2a4e3522-f10f-4fdf-a714-3e58f451c92e', 'Ольга','Аннаевна', 'Белякова', '1979-01-22', false, '9876543210', 'ул. Парковая, д. 3', '79923456789', 'img/default_profile_photo.png'),
('95291318-f3fa-4f0f-b3a0-8908bfe391b6', 'Андрей','Сергеевич', 'Фролов', '1984-05-07', true, '1122334455', 'ул. Советская, д. 11', '79934567890', 'img/default_profile_photo.png'),
('3c1fcb41-9c78-4f0f-b820-9711ffc87a6f', 'Евгения','Егоровна', 'Лаврова', '1994-09-16', false, '5544332211', 'ул. Горького, д. 63', '79945678901', 'img/default_profile_photo.png'),
('395ed07f-f6eb-4e74-867a-ae6498bc2f2f', 'Сергей','Дмитриевич', 'Котов', '1982-07-28', true, '7654321098', 'ул. Лесная, д. 41', '79956789012', 'img/default_profile_photo.png'),
('d384f677-9f23-46d4-a790-f8f29abb6f3f', 'Ирина', 'Викторовна', 'Константинова','1990-02-09', false, '5234045678', 'ул. Луговая, д. 17', '79967890123', 'img/default_profile_photo.png'),
('5632918c-135b-4c49-8af5-89ed75158fb1', 'Владимир', 'Артемьевич', 'Тимошенко','1981-04-13', true, '9876543210', 'ул. Мичурина, д. 5', '79978901234', 'img/default_profile_photo.png'),
('b5eaeb53-2cce-4d7c-855b-08920d66d6b7', 'Наталья', 'Евгеньевна', 'Исаева','1987-11-25', false, '1122334455', 'ул. Глинки, д. 29', '79989012345', 'img/default_profile_photo.png'),
('e7800146-efbb-4bce-950e-f7fbf33613eb', 'Дмитрий', 'Игоревич', 'Крылов','1993-10-08', true, '5544332211', 'ул. Колхозная, д. 36', '79990123456', 'img/default_profile_photo.png'),
('73443f74-ef2b-4797-b6af-dc0ff6f525eb', 'Оксана', 'Александровна', 'Шевченко','1988-06-29', false, '7654321098', 'ул. Ленина, д. 71', '79901234567', 'img/default_profile_photo.png'),
('d9244ec4-dc91-4f0b-b171-6e08f0f60daa', 'Иван','Владимирович', 'Сидоров', '1980-03-15', true, '5234045678', 'ул. Ленина, д. 123', '79012345678', 'img/default_profile_photo.png'),
('21f579ae-fcd7-4029-b3cd-1d912fe631a7', 'Мария','Андреевна', 'Браткова', '1985-09-20', false, '9876543210', 'ул. Гагарина, д. 45', '79123456789', 'img/default_profile_photo.png'),
('e11d2790-3cf6-44f0-9bc6-ce2c93b7eb7f', 'Алексей','Анатольевич', 'Костин', '1990-02-10', true, '1122334455', 'ул. Пушкина, д. 67', '79234567890', 'img/default_profile_photo.png'),
('0de0b82a-76ae-4efe-99d2-1e282f332d70', 'Екатерина','Егоровна', 'Тихонова', '1983-12-25', false, '5544332211', 'ул. Жукова, д. 56', '79345678901', 'img/default_profile_photo.png'),
('9e204d2e-01bb-44f8-857f-e74cd864d6b2', 'Павел','Никитович', 'Гусев', '1992-07-08', true, '7654321098', 'ул. Строителей, д. 32', '79456789012', 'img/default_profile_photo.png'),
('aadb1517-d708-45d2-a9ec-15ad0ab1a81d', 'Светлана', 'Марковна', 'Антонова','1991-03-12', false, '1111222233', 'ул. Кирова, д. 78', '79567890123', 'img/default_profile_photo.png'),
('3bf56fac-b27e-485b-82de-a251070ed5a3', 'Денис','Геннадьевич', 'Воробьев', '1986-11-30', true, '9876543210', 'ул. Лермонтова, д. 14', '79678901234', 'img/default_profile_photo.png'),
('6e4bf18d-01de-4c16-ac03-bfbf16d61b55', 'Анна', 'Артемьевна', 'Лебедь','1995-04-05', false, '1122334455', 'ул. Маяковского, д. 98', '79789012345', 'img/default_profile_photo.png'),
('b95ebf53-5483-4506-919e-9992388cb237', 'Михаил', 'Степанович', 'Фомин','1980-10-03', true, '5234045678', 'ул. Центральная, д. 72', '79890123456', 'img/default_profile_photo.png'),
('1dd85ba2-132b-496a-8a32-c7428e842417', 'Татьяна','Ольговна', 'Тимофеева', '1993-01-22', false, '9876543210', 'ул. Парковая, д. 3', '79923456789', 'img/default_profile_photo.png');

INSERT INTO doctors (pd_id, specialization, date_employment, pre_work_experience, resigned)
VALUES
(20,'Хирург', '2017-05-10', 6, false), 
(21,'Терапевт', '2015-08-20', 8, false),
(22,'Хирург', '2016-12-08', 7, false),
(23,'Терапевт', '2019-03-25', 4, false),
(24,'Хирург', '2015-06-10', 8, false),
(25,'Терапевт', '2018-11-12', 5, true),
(26,'Хирург', '2017-09-30', 6, false),
(27,'Терапевт', '2016-04-15', 7, false),
(28,'Хирург', '2015-12-18', 6, false),
(29,'Терапевт', '2019-08-14', 4, false);

INSERT INTO patients(pd_id)
VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19);

INSERT INTO appointments (id, patient_id, doctor_id, date_time, status)
VALUES
(1, 1, 1, '2023-11-19 10:00:00', 0),
(2, 2, 2, '2023-10-19 10:00:00', 1),
(3, 1, 3, '2023-11-19 10:00:00', 2),
(4, 3, 4, '2023-10-20 10:00:00', 2),
(5, 1, 5, '2023-11-19 10:00:00', 3);

INSERT INTO schedule (start_time, end_time)
SELECT 
    date::timestamp + interval '8 hours' as start_time,
    date::timestamp + interval '17 hours' as end_time
FROM 
    generate_series('2023-11-01'::date, '2023-11-30'::date, '1 day') date
WHERE 
    EXTRACT(ISODOW FROM date) < 6


INSERT INTO schedule (start_time, end_time) 
SELECT date::timestamp + interval '8 hours' as start_time, 
date::timestamp + interval '17 hours' as end_time 
FROM generate_series('2023-11-15'::date, '2023-11-30'::date, '1 day') date 
WHERE EXTRACT(ISODOW FROM date) < 6