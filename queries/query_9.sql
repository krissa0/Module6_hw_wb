SELECT DISTINCT sub.name
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE s.fullname = 'Student Name';
