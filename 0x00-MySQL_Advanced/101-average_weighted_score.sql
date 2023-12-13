-- compute and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER // ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS Users,
    (SELECT Users.id, SUM(score * weight) / SUM(weight) AS wAvg
    FROM users AS Users
    JOIN corrections AS Correction ON Users.id=Correction.user_id
    JOIN projects AS Project ON Project.id=C.project_id
    GROUP BY Users.id) AS WA
    SET Users.average_score=WA.wAvg
    WHERE Users.id=WA.id;
END //

DELIMITER ; //