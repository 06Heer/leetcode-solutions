# Write your MySQL query statement below
SELECT
    employee_id,
    department_id
FROM (
    SELECT
        employee_id,
        department_id,
        primary_flag,
        COUNT(*) OVER (PARTITION BY employee_id) AS dept_count
    FROM Employee
) AS e
WHERE dept_count = 1
   OR primary_flag = 'Y';