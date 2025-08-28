SELECT ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE t.fullname = 'Bob Lee' AND s.fullname = 'Student Name';
