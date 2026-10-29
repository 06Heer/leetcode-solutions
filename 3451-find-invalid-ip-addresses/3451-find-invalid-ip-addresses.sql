# Write your MySQL query statement below
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE ip NOT REGEXP '^([0-9]{1,3}\\.){3}[0-9]{1,3}$'
   OR ip REGEXP '(^|\\.)(0[0-9]+)(\\.|$)'
   OR ip REGEXP '(^|\\.)([2][5][6-9]|[3-9][0-9]{2}|[0-9]{4,})(\\.|$)'
GROUP BY ip
HAVING COUNT(*) > 0
ORDER BY invalid_count DESC, ip DESC;