-- Creeate a procedure to add correction for a student
DELIMITER // ;

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN

    DECLARE project INT;

    SELECT COUNT(*) INTO project
    FROM projects
    WHERE name = project_name;

    IF project = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, @project_id, score);
    ELSE
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
    END IF;

END//

DELIMITER ; //
