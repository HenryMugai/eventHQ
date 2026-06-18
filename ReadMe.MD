eventhq/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── database/
│   ├── db.py
│   ├── schema.sql
│   ├── seed.sql
│   └── migrations/
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── organiser.py
│   ├── event.py
│   ├── category.py
│   ├── ticket_type.py
│   ├── order.py
│   ├── payment.py
│   ├── ticket.py
│   ├── checkin.py
│   ├── notification.py
│   ├── support_request.py
│   ├── audit_log.py
│   └── setting.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── organiser_service.py
│   ├── event_service.py
│   ├── ticket_service.py
│   ├── payment_service.py
│   ├── qr_service.py
│   ├── report_service.py
│   ├── excel_service.py
│   ├── pdf_service.py
│   ├── notification_service.py
│   ├── email_service.py
│   ├── sms_service.py
│   ├── checkin_service.py
│   └── analytics_service.py
│
├── middleware/
│   ├── auth.py
│   ├── admin_required.py
│   ├── organiser_required.py
│   ├── role_permissions.py
│   └── audit_trail.py
│
├── utils/
│   ├── helpers.py
│   ├── validators.py
│   ├── generators.py
│   ├── constants.py
│   └── file_uploads.py
│
├── routes/
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── login.py
│   │   ├── logout.py
│   │   ├── forgot_password.py
│   │   └── profile.py
│   │
│   ├── public/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── events.py
│   │   ├── event_details.py
│   │   ├── checkout.py
│   │   ├── payment.py
│   │   ├── ticket_download.py
│   │   └── verify_ticket.py
│   │
│   ├── admin/
│   │   ├── __init__.py
│   │   ├── dashboard.py
│   │   ├── events.py
│   │   ├── organisers.py
│   │   ├── users.py
│   │   ├── ticket_types.py
│   │   ├── tickets.py
│   │   ├── orders.py
│   │   ├── payments.py
│   │   ├── checkins.py
│   │   ├── reports.py
│   │   ├── exports.py
│   │   ├── categories.py
│   │   ├── support_requests.py
│   │   ├── notifications.py
│   │   ├── settings.py
│   │   └── audit_logs.py
│   │
│   ├── organiser/
│   │   ├── __init__.py
│   │   ├── dashboard.py
│   │   ├── events.py
│   │   ├── attendees.py
│   │   ├── analytics.py
│   │   ├── reports.py
│   │   ├── downloads.py
│   │   ├── support.py
│   │   └── profile.py
│   │
│   └── api/
│       ├── __init__.py
│       ├── payments.py
│       ├── webhooks.py
│       ├── checkins.py
│       ├── verify.py
│       └── analytics.py
│
├── templates/
│   │
│   ├── layouts/
│   │   ├── base.html
│   │   ├── admin_base.html
│   │   └── organiser_base.html
│   │
│   ├── auth/
│   ├── public/
│   ├── admin/
│   └── organiser/
│
├── static/
│   │
│   ├── css/
│   │   ├── auth/
│   │   ├── public/
│   │   ├── admin/
│   │   └── organiser/
│   │
│   ├── js/
│   │   ├── public/
│   │   ├── admin/
│   │   └── organiser/
│   │
│   ├── images/
│   ├── icons/
│   └── qr_codes/
│
├── uploads/
│   ├── banners/
│   ├── organisers/
│   ├── reports/
│   ├── bulk_uploads/
│   ├── exports/
│   └── temp/
│
└── logs/
    ├── application.log
    ├── audit.log
    └── errors.log









DROP DATABASE IF EXISTS eventhq;
CREATE DATABASE eventhq
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE eventhq;


CREATE TABLE roles (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL UNIQUE,
description VARCHAR(255),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO roles (name, description)
VALUES
('admin', 'Platform Administrator'),
('organiser', 'Event Organiser'),
('gate_agent', 'Ticket Scanner');


CREATE TABLE users (
id BIGINT AUTO_INCREMENT PRIMARY KEY,


role_id INT NOT NULL,

first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100),

email VARCHAR(150) UNIQUE NOT NULL,
phone VARCHAR(30),

password_hash VARCHAR(255) NOT NULL,

is_active BOOLEAN DEFAULT TRUE,

last_login DATETIME NULL,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,

CONSTRAINT fk_users_role
    FOREIGN KEY (role_id)
    REFERENCES roles(id)


);


CREATE TABLE organisers (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

user_id BIGINT NOT NULL,

company_name VARCHAR(255) NOT NULL,

contact_person VARCHAR(255),

phone VARCHAR(50),
email VARCHAR(150),

website VARCHAR(255),

address TEXT,

logo VARCHAR(255),

notes TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

CONSTRAINT fk_organiser_user
    FOREIGN KEY (user_id)
    REFERENCES users(id)


);



CREATE TABLE categories (


id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) UNIQUE NOT NULL,

description TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP


);


CREATE TABLE events (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

category_id INT,

organiser_id BIGINT,

event_name VARCHAR(255) NOT NULL,

slug VARCHAR(255) UNIQUE,

short_description VARCHAR(500),

description LONGTEXT,

venue VARCHAR(255),

venue_address TEXT,

google_maps_link VARCHAR(500),

city VARCHAR(100),

country VARCHAR(100) DEFAULT 'Kenya',

banner_image VARCHAR(255),

start_datetime DATETIME NOT NULL,

end_datetime DATETIME NOT NULL,

status ENUM(
    'draft',
    'published',
    'closed',
    'cancelled'
) DEFAULT 'draft',

is_featured BOOLEAN DEFAULT FALSE,

created_by BIGINT NOT NULL,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,

FOREIGN KEY (category_id)
    REFERENCES categories(id),

FOREIGN KEY (organiser_id)
    REFERENCES organisers(id),

FOREIGN KEY (created_by)
    REFERENCES users(id)


);


CREATE TABLE ticket_types (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

event_id BIGINT NOT NULL,

name VARCHAR(100) NOT NULL,

description TEXT,

price DECIMAL(12,2) DEFAULT 0,

quantity INT NOT NULL,

sold INT DEFAULT 0,

max_per_order INT DEFAULT 10,

sales_start DATETIME,

sales_end DATETIME,

is_active BOOLEAN DEFAULT TRUE,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (event_id)
    REFERENCES events(id)
    ON DELETE CASCADE


);


CREATE TABLE orders (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

order_reference VARCHAR(100)
    UNIQUE NOT NULL,

event_id BIGINT NOT NULL,

customer_name VARCHAR(255) NOT NULL,

customer_email VARCHAR(150),

customer_phone VARCHAR(50),

total_amount DECIMAL(12,2) DEFAULT 0,

order_status ENUM(
    'pending',
    'paid',
    'cancelled',
    'refunded'
) DEFAULT 'pending',

source ENUM(
    'online',
    'bulk_upload',
    'manual'
) DEFAULT 'online',

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (event_id)
    REFERENCES events(id)


);


CREATE TABLE payments (

id BIGINT AUTO_INCREMENT PRIMARY KEY,

order_id BIGINT NOT NULL,

transaction_reference VARCHAR(255),

payment_method ENUM(
    'mpesa',
    'pesapal',
    'cash',
    'bank'
),

amount DECIMAL(12,2),

payment_status ENUM(
    'pending',
    'paid',
    'failed',
    'refunded'
) DEFAULT 'pending',

paid_at DATETIME,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (order_id)
    REFERENCES orders(id)


);


CREATE TABLE tickets (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

order_id BIGINT,

event_id BIGINT NOT NULL,

ticket_type_id BIGINT NOT NULL,

ticket_number VARCHAR(100)
    UNIQUE NOT NULL,

qr_code VARCHAR(255),

attendee_name VARCHAR(255) NOT NULL,

attendee_email VARCHAR(150),

attendee_phone VARCHAR(50),

status ENUM(
    'valid',
    'used',
    'cancelled',
    'refunded'
) DEFAULT 'valid',

ticket_source ENUM(
    'online',
    'bulk_upload',
    'complimentary',
    'manual'
) DEFAULT 'online',

issued_at DATETIME DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (order_id)
    REFERENCES orders(id),

FOREIGN KEY (event_id)
    REFERENCES events(id),

FOREIGN KEY (ticket_type_id)
    REFERENCES ticket_types(id)


);


CREATE TABLE checkins (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

ticket_id BIGINT NOT NULL,

scanned_by BIGINT,

scan_time DATETIME DEFAULT CURRENT_TIMESTAMP,

notes TEXT,

FOREIGN KEY (ticket_id)
    REFERENCES tickets(id),

FOREIGN KEY (scanned_by)
    REFERENCES users(id)


);


CREATE TABLE support_requests (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

organiser_id BIGINT NOT NULL,

event_id BIGINT,

subject VARCHAR(255),

message TEXT,

status ENUM(
    'open',
    'in_progress',
    'resolved',
    'closed'
) DEFAULT 'open',

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (organiser_id)
    REFERENCES organisers(id),

FOREIGN KEY (event_id)
    REFERENCES events(id)


);


CREATE TABLE notifications (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

user_id BIGINT NOT NULL,

title VARCHAR(255),

message TEXT,

is_read BOOLEAN DEFAULT FALSE,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (user_id)
    REFERENCES users(id)

);


CREATE TABLE audit_logs (


id BIGINT AUTO_INCREMENT PRIMARY KEY,

user_id BIGINT,

module_name VARCHAR(100),

action_taken VARCHAR(255),

record_id BIGINT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (user_id)
    REFERENCES users(id)


);


CREATE TABLE settings (


id INT AUTO_INCREMENT PRIMARY KEY,

setting_key VARCHAR(100)
    UNIQUE NOT NULL,

setting_value TEXT,

updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP


);


INSERT INTO categories (name) VALUES
('Conference'),
('Workshop'),
('Training'),
('Expo'),
('Festival'),
('Concert'),
('Church Event'),
('Corporate Event'),
('Sports'),
('Community Event');



INSERT INTO users (
role_id,
first_name,
last_name,
email,
password_hash
)
VALUES (
1,
'System',
'Administrator',
'[admin@eventhq.com](mailto:admin@eventhq.com)',
'$2b$12$CHANGE_THIS_HASH'
);



CREATE INDEX idx_events_status
ON events(status);

CREATE INDEX idx_events_start_date
ON events(start_datetime);

CREATE INDEX idx_orders_status
ON orders(order_status);

CREATE INDEX idx_payments_status
ON payments(payment_status);

CREATE INDEX idx_tickets_number
ON tickets(ticket_number);

CREATE INDEX idx_tickets_event
ON tickets(event_id);

CREATE INDEX idx_checkins_ticket
ON checkins(ticket_id);


