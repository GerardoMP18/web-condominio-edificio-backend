-- SP for the create new user --

use gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_user;
DELIMITER $$
CREATE PROCEDURE sp_add_user(
    IN first_name    VARCHAR(50),
    IN last_name VARCHAR(50),
    IN id_document_type INT,
    IN number_document INT,
    IN email VARCHAR(120),
    IN password VARCHAR(40),
    IN phone INT,
    IN birth_date DATE,
    IN id_role SMALLINT
)
BEGIN
    INSERT INTO user (first_name,last_name,id_document_type,number_document,email,password,phone,birth_date,id_role)
    VALUE (first_name,last_name,id_document_type,number_document,email,password,phone,birth_date,id_role);
END $$
DELIMITER ;
