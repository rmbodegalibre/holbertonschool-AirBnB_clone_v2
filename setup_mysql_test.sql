-- This script prepares a MySQL server for the project:
-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test is set to hbnb_test_pwd
-- hbnb_test has all privileges on the database hbnb_test_db
-- (and only this database)
-- hbnb_test has SELECT privilege on the database performance_schema
-- (and only this database)
-- If the database hbnb_test_db or the user hbnb_test already exists,
-- this script not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
