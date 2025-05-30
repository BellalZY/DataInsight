SELECT DBMS_LOB.SUBSTR(dc."Customer Name", 100) AS CUSTOMER_NAME,
       SUM(fs.SALES_AMOUNT) AS TOTAL_REVENUE
FROM FACT_SALES fs
JOIN DIM_CUSTOMER dc ON fs.CUSTOMER_KEY = dc.CUSTOMER_KEY
GROUP BY DBMS_LOB.SUBSTR(dc."Customer Name", 100)
ORDER BY TOTAL_REVENUE DESC
FETCH FIRST 10 ROWS ONLY;

SELECT
    dd.YEAR,
    TO_CHAR(dd.FULL_DATE, 'MM') AS MONTH,
    SUM(fs.SALES_AMOUNT) AS MONTHLY_SALES
FROM FACT_SALES fs
JOIN DIM_DATE dd ON fs.DATE_KEY = dd.DATE_KEY
GROUP BY dd.YEAR, TO_CHAR(dd.FULL_DATE, 'MM')
ORDER BY dd.YEAR, TO_CHAR(dd.FULL_DATE, 'MM');


SELECT 
    TO_CHAR(dp."Category") AS CATEGORY,
    SUM(fs.PROFIT) AS TOTAL_PROFIT
FROM FACT_SALES fs
JOIN DIM_PRODUCT dp ON fs.PRODUCT_KEY = dp.PRODUCT_KEY
GROUP BY TO_CHAR(dp."Category")
ORDER BY TOTAL_PROFIT DESC;



SELECT fs.SHIP_MODE,
       COUNT(*) AS NUM_SHIPPED
FROM FACT_SALES fs
GROUP BY fs.SHIP_MODE
ORDER BY NUM_SHIPPED DESC;


SELECT 
    DBMS_LOB.SUBSTR(dp."Sub-Category", 50) AS SUB_CATEGORY,
    SUM(fs.SALES_AMOUNT) AS TOTAL_SALES,
    SUM(fs.PROFIT) AS TOTAL_PROFIT
FROM FACT_SALES fs
JOIN DIM_PRODUCT dp ON fs.PRODUCT_KEY = dp.PRODUCT_KEY
GROUP BY DBMS_LOB.SUBSTR(dp."Sub-Category", 50)
ORDER BY TOTAL_SALES DESC;


SELECT 
    dd.YEAR,
    DBMS_LOB.SUBSTR(dd.MONTH, 20) AS MONTH,
    SUM(fs.SALES_AMOUNT) AS MONTHLY_SALES
FROM FACT_SALES fs
JOIN DIM_DATE dd ON fs.DATE_KEY = dd.DATE_KEY
GROUP BY dd.YEAR, DBMS_LOB.SUBSTR(dd.MONTH, 20)
ORDER BY dd.YEAR, DBMS_LOB.SUBSTR(dd.MONTH, 20);
