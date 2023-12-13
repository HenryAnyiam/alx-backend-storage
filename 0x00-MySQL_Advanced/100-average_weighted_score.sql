-- compute and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER // ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE wAvgScore FLOAT;
    
    SET wAvgScore = (SELECT SUM(score * weight)/ SUM(weight)
                        FROM users AS User
                        JOIN corrections AS Correction ON Correction.user_id=Users.id
                        JOIN projects AS Project ON Correction.project_id=Project.id
                        WHERE Users.id=user_id);
    UPDATE users SET average_score = wAvgScore WHERE users.id=user_id;
END //

DELIMITER ; //
