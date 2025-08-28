SELECT sub.name
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.fullname = 'Student Name' AND t.fullname = 'John Smith';
