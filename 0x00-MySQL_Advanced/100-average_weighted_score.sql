-- compute and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER // ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE wAvgScore FLOAT;
    
    SET wAvgScore = (SELECT SUM(score * weight)/ SUM(weight)
                        FROM users AS U
                        JOIN corrections AS C ON C.user_id=U.id
                        JOIN projects AS P ON C.project_id=P.id
                        WHERE U.id=user_id);
    UPDATE users SET average_score = wAvgScore WHERE users.id=user_id;
END //

DELIMITER ; //
