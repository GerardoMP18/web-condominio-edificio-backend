-- procedure update building --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_update_building;
DELIMITER $$
CREATE PROCEDURE sp_update_building(
    IN p_id INT,
    IN p_id_condominium INT,
    IN p_name_building    VARCHAR(120),
    IN p_ruc BIGINT,
    IN p_phone INT,
    IN p_email VARCHAR(120),
    IN p_description VARCHAR(250),
    IN p_floor SMALLINT,
    IN p_address VARCHAR(120),
    IN p_user_created VARCHAR(60),
    IN p_user_updated VARCHAR(60)
)
BEGIN
    UPDATE building
    SET
    id_condominium = p_id_condominium,
    name_building = p_name_building,
    ruc = p_ruc,
    phone = p_phone,
    email = p_email,
    description = p_description,
    floor = p_floor,
    address = p_address,
    user_created = p_user_created,
    user_updated = p_user_updated
    WHERE id = p_id;
END $$
DELIMITER ;
