-- procedure update user --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_update_user;
DELIMITER $$
CREATE PROCEDURE sp_update_user(
    IN p_id INT,
    IN p_first_name    VARCHAR(50),
    IN p_document_type INT,
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(120),
    IN p_password VARCHAR(40),
    IN p_number_document INT,
    IN p_phone INT,
    IN p_birth_date DATE
)
BEGIN
    UPDATE user
    SET
    first_name = p_first_name,
    id_document_type = p_document_type,
    last_name = p_last_name,
    email = p_email,
    password = p_password,
    number_document = p_number_document,
    phone = p_phone,
    birth_date = p_birth_date
    WHERE id = p_id;
END $$
DELIMITER ;
