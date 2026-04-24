import pandas as pd
import mysql.connector

# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='P@ssw0rd!',
    database='superstore'
)

cursor = conn.cursor()

# --- Clear existing empty table ---
cursor.execute("TRUNCATE TABLE orders")

# --- Load cleaned CSV ---
df = pd.read_csv('outputs/superstore_mysql.csv')

# --- Rename columns to match MySQL table ---
df.columns = [
    'order_id', 'order_date', 'ship_date', 'ship_mode',
    'customer_id', 'customer_name', 'segment', 'country',
    'city', 'state', 'postal_code', 'region', 'product_id',
    'category', 'sub_category', 'product_name', 'sales',
    'quantity', 'discount', 'profit', 'days_to_ship',
    'year', 'month'
]

# --- Insert rows ---
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO orders (
            order_id, order_date, ship_date, ship_mode,
            customer_id, customer_name, segment, country,
            city, state, postal_code, region, product_id,
            category, sub_category, product_name, sales,
            quantity, discount, profit, days_to_ship,
            year, month
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s
        )
    """, (
        row['order_id'], row['order_date'], row['ship_date'],
        row['ship_mode'], row['customer_id'], row['customer_name'],
        row['segment'], row['country'], row['city'], row['state'],
        row['postal_code'], row['region'], row['product_id'],
        row['category'], row['sub_category'], row['product_name'],
        row['sales'], row['quantity'], row['discount'],
        row['profit'], row['days_to_ship'], row['year'], row['month']
    ))

# --- Commit and close ---
conn.commit()
cursor.close()
conn.close()

print(f"Done. {len(df)} rows loaded into MySQL.")