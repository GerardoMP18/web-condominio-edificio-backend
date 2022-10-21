-- procedure link departament_user --

USE gbs_dev_db;

DROP PROCEDURE IF EXISTS sp_add_departament_user;
DELIMITER $$
CREATE PROCEDURE sp_add_departament_user(
    IN id_user    INT,
    IN id_departament INT,
    IN user_created VARCHAR(60),
    IN user_updated VARCHAR(60)
)
BEGIN
    INSERT INTO departament_user (id_user,id_departament,user_created,user_updated)
    VALUE (id_user,id_departament,user_created,user_updated);
END $$
DELIMITER ;
