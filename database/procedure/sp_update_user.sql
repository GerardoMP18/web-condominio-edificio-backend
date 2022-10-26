-- procedure update user --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_update_user;
DELIMITER $$
CREATE PROCEDURE sp_update_user(
    IN p_id INT,
    IN p_first_name    VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_id_document_type INT,
    IN p_number_document INT,
    IN p_email VARCHAR(120),
    IN p_password VARCHAR(40),
    IN p_phone INT,
    IN p_birth_date DATE,
    IN p_id_role SMALLINT
)
BEGIN
    UPDATE user
    SET
    first_name = p_first_name,
    last_name = p_last_name,
    id_document_type = p_id_document_type,
    number_document = p_number_document,
    email = p_email,
    password = p_password,
    phone = p_phone,
    birth_date = p_birth_date,
    id_role = p_id_role
    WHERE id = p_id;
END $$
DELIMITER ;
