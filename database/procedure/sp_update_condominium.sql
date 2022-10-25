-- procedure update condominium --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_update_condominium;
DELIMITER $$
CREATE PROCEDURE sp_update_condominium(
    IN p_id INT,
    IN p_name    VARCHAR(250),
    IN p_ruc BIGINT,
    IN p_phone INT,
    IN p_email VARCHAR(120),
    IN p_address VARCHAR(120),
    IN p_landline INT,
    IN p_description VARCHAR(250),
    IN p_user_created VARCHAR(60),
    IN p_user_updated VARCHAR(60)
)
BEGIN
    UPDATE condominium
    SET
    name = p_name,
    ruc = p_ruc,
    phone = p_phone,
    email = p_email,
    address = p_address,
    landline = p_landline,
    description = p_description,
    user_created = p_user_created,
    user_updated = p_user_updated
    WHERE id = p_id;
END $$
DELIMITER ;
