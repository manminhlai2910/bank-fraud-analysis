select * from fraud limit 50


-- Fraud rate by transaction type
SELECT 
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN is_fraud='true' THEN 1 ELSE 0 END) AS fraud_count,
    ROUND(
        SUM(CASE WHEN is_fraud='true' THEN 1 ELSE 0 END)::numeric / COUNT(*) * 100, 
        2
    ) AS fraud_rate_pct
FROM fraud
GROUP BY 1
ORDER BY 3 DESC;

-- Average transaction amount
select is_fraud, round(avg(amount),2) as avg_amt,
round(a)