-- procedure update departament --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_update_departament;
DELIMITER $$
CREATE PROCEDURE sp_update_departament(
    IN p_id INT,
    IN p_number_departament    INT,
    IN p_id_district INT,
    IN p_id_building INT,
    IN p_number_bedrooms INT,
    IN p_floor INT,
    IN p_description VARCHAR(250),
    IN p_status VARCHAR(42),
    IN p_user_created VARCHAR(120),
    IN p_user_updated VARCHAR(120)
)
BEGIN
    UPDATE departament
    SET
    number_departament = p_number_departament,
    id_district = p_id_district,
    id_building = p_id_building,
    number_bedrooms = p_number_bedrooms,
    floor = p_floor,
    description = p_description,
    status = p_status,
    user_created = p_user_created,
    user_updated = p_user_updated
    WHERE id = p_id;
END $$
DELIMITER ;
