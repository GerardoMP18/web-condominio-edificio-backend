-- SP for the create new user

use gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_user;
DELIMITER $$
CREATE PROCEDURE sp_add_user(
    IN first_name    VARCHAR(50),
    IN document_type INT,
    IN last_name VARCHAR(50),
    IN email VARCHAR(120),
    IN password VARCHAR(40),
    IN number_document INT,
    IN phone INT,
    IN birth_date DATE
)
BEGIN
    INSERT INTO user (first_name,id_document_type,last_name,email,password,number_document,phone,birth_date)
    VALUE (first_name,document_type,last_name,email,password,number_document,phone,birth_date);
END $$
DELIMITER ;
