INSERT INTO tickets_client (full_name, email, phone, created_at) VALUES
('Иванов Иван Иванович', 'ivanov@example.com', '+79001234567', CURRENT_TIMESTAMP),
('Петров Петр Петрович', 'petrov@example.com', '+79007654321', CURRENT_TIMESTAMP),
('Смирнова Анна Олеговна', 'smirnova@example.com', '+79005554433', CURRENT_TIMESTAMP);

INSERT INTO tickets_ticketstatus (name) VALUES
('Новая'),
('В обработке'),
('Ожидает ответа'),
('Закрыта');

INSERT INTO tickets_ticketpriority (name) VALUES
('Низкий'),
('Средний'),
('Высокий');

INSERT INTO tickets_ticketcategory (name) VALUES
('Техническая проблема'),
('Вопрос по оплате'),
('Жалоба'),
('Консультация');

INSERT INTO tickets_channel (name) VALUES
('Веб-форма'),
('Email'),
('Телефон'),
('Чат');

INSERT INTO tickets_role (name) VALUES
('Агент поддержки'),
('Менеджер'),
('Администратор');

INSERT INTO tickets_department (name) VALUES
('Техническая поддержка'),
('Клиентский сервис'),
('Финансовый отдел');

INSERT INTO tickets_user (role_id, department_id, full_name, email) VALUES
(1, 1, 'Алексеева Ольга Викторовна', 'alekseeva@support.local'),
(1, 2, 'Морозов Дмитрий Павлович', 'morozov@support.local'),
(2, 2, 'Васильев Сергей Николаевич', 'vasiliev@support.local');