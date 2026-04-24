SELECT 
    state,
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(*) AS total_orders
FROM orders
GROUP BY state, region
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;