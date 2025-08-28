SELECT s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Math'
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
