-- SP for the create new condominium --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_condominium;
DELIMITER $$
CREATE PROCEDURE sp_add_condominium(
    IN name    VARCHAR(250),
    IN ruc BIGINT,
    IN phone INT,
    IN email VARCHAR(120),
    IN address VARCHAR(120),
    IN landline INT,
    IN description VARCHAR(250),
    IN user_created VARCHAR(60),
    IN user_updated VARCHAR(60)
)
BEGIN
    INSERT INTO condominium (name,ruc,phone,email,address,landline,description,user_created,user_updated)
    VALUE (name,ruc,phone,email,address,landline,description,user_created,user_updated);
END $$
DELIMITER ;
