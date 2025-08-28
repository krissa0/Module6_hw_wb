SELECT s.fullname, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'Group B' AND sub.name = 'Chemistry';
