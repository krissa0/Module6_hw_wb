SELECT s.fullname
FROM students s
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'Group A';
