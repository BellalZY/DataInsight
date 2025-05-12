import pandas as pd
import chardet
import oracledb
from sqlalchemy import create_engine, text

# def detect_encoding(file_path):
#     with open(file_path, 'rb') as f:
#         return chardet.detect(f.read(10000))['encoding']

# orders_encoding = detect_encoding("Awesome_Inc_Superstore_Orders.csv")
# returns_encoding = detect_encoding("Awesome_Inc_Superstore Returns.csv")

# orders = pd.read_csv("Awesome_Inc_Superstore_Orders.csv", encoding=orders_encoding)
# returns = pd.read_csv("Awesome_Inc_Superstore Returns.csv", encoding=returns_encoding)

# print("Orders preview:")
# print(orders.head())
# print("Returns preview:")
# print(returns.head())

username = "SYSTEM"
password = "mypassword1"
host = "host.docker.internal"
port = 1521
service_name = "ORCLCDB"

dsn = oracledb.makedsn(host, port, service_name=service_name)
engine = create_engine(f'oracle+oracledb://{username}:{password}@{dsn}', echo=True)

with engine.connect() as conn:
    print("Oracle connection successful!")

# Tables to export
table_names = [
    "DIM_CUSTOMER", "DIM_PRODUCT", "DIM_ORDER", "DIM_DATE", "DIM_RETURN", "FACT_SALES"
]

# Export each to CSV
df = pd.read_sql(f"""SELECT
DBMS_LOB.SUBSTR(dc."Region", 100) AS REGION,
COUNT(fs.SALES_KEY) AS TOTAL_SALES,
COUNT(fs.RETURN_KEY) AS TOTAL_RETURNS,
ROUND(COUNT(fs.RETURN_KEY) * 100.0 / COUNT(fs.SALES_KEY), 2) AS RETURN_RATE_PERCENT
FROM
FACT_SALES fs
JOIN
DIM_CUSTOMER dc ON fs.CUSTOMER_KEY = dc.CUSTOMER_KEY
GROUP BY
DBMS_LOB.SUBSTR(dc."Region", 100)
ORDER BY
RETURN_RATE_PERCENT DESC""", engine)
df.to_csv(f"return_rate_region.csv", index=False)
print(f"Exported return_rate_region.csv with {len(df)} rows")

