-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS mrk_db;
CREATE USER IF NOT EXISTS 'mrk_user'@'localhost' IDENTIFIED BY 'mrk_pwd';
GRANT ALL PRIVILEGES ON `mrk_db`.* TO 'mrk_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mrk_user'@'localhost';
FLUSH PRIVILEGES;