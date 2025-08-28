SELECT s.fullname, g.grade, g.date_of
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'Group C' AND sub.name = 'History'
AND g.date_of = (
    SELECT MAX(date_of)
    FROM grades g2
    JOIN students s2 ON g2.student_id = s2.id
    WHERE s2.group_id = gr.id AND g2.subject_id = sub.id
);

