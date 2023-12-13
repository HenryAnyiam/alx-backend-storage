-- Create view for students who need meetings

CREATE VIEW need_meeting AS
SELECT * FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
