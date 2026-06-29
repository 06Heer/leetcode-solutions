# Write your MySQL query statement below
SELECT
    machine_id,
    ROUND(AVG(process_time), 3) AS processing_time
FROM (
    SELECT
        machine_id,
        process_id,
        SUM(
            CASE
                WHEN activity_type = 'end' THEN timestamp
                ELSE -timestamp
            END
        ) AS process_time
    FROM Activity
    GROUP BY machine_id, process_id
) AS t
GROUP BY machine_id;