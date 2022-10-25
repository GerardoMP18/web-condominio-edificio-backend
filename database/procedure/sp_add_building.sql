-- procedure create new building --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_building;
DELIMITER $$
CREATE PROCEDURE sp_add_building(
    IN id_condominium INT,
    IN name_building    VARCHAR(120),
    IN ruc BIGINT,
    IN phone INT,
    IN email VARCHAR(120),
    IN description VARCHAR(250),
    IN floor SMALLINT,
    IN address VARCHAR(120),
    IN user_created VARCHAR(60),
    IN user_updated VARCHAR(60)
)
BEGIN
    INSERT INTO building (id_condominium,name_building,ruc,phone,email,description,floor,address,user_created,user_updated)
    VALUE (id_condominium,name_building,ruc,phone,email,description,floor,address,user_created,user_updated);
END $$
DELIMITER ;
