-- procedure create departament --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_departament;
DELIMITER $$
CREATE PROCEDURE sp_add_departament(
    IN number_departament    INT,
    IN id_district SMALLINT,
    IN id_building INT,
    IN number_bedrooms INT,
    IN floor INT,
    IN description VARCHAR(250),
    IN status VARCHAR(42),
    IN user_created VARCHAR(120),
    IN user_updated VARCHAR(120)
)
BEGIN
    INSERT INTO departament (number_departament,id_district,id_building,number_bedrooms,floor,description,status,user_created,user_updated)
    VALUE (number_departament,id_district,id_building,number_bedrooms,floor,description,status,user_created,user_updated);
END $$
DELIMITER ;
