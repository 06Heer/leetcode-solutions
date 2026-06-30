# Write your MySQL query statement below
SELECT
    u.name,
    t.balance
FROM Users u
JOIN
(
    SELECT
        account,
        SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
) t
ON u.account = t.account
WHERE t.balance > 10000;