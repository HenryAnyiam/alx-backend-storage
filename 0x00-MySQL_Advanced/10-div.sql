-- Create a divide function

DELIMITER // ;

CREATE FUNCTION SafeDiv (num1 INT, num2 INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN

    DECLARE results FLOAT;

    IF num2 = 0 THEN
        SET results = 0;
    ELSE
        SET results = num1 / num2;
    END IF;

    RETURN results;

END//

DELIMITER ; //
