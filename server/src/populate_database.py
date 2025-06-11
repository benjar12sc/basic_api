import csv
import sqlite3

# Map headers to SQLite types
type_map = {
    "Year": "INTEGER",
    "Month": "INTEGER",
    "Supplier": "TEXT",
    "ItemCode": "TEXT",
    "ItemDescription": "TEXT",
    "ItemType": "TEXT",
    "RetailSales": "REAL",
    "RetailTransfers": "REAL",
    "WarehouseSales": "REAL"
}

def create_table(conn, headers):
    # Drop the table if it exists
    conn.execute('DROP TABLE IF EXISTS sales;')

    columns = [f'"{h}" {type_map.get(h, "TEXT")}' for h in headers]
    columns.insert(0, 'id INTEGER PRIMARY KEY AUTOINCREMENT')
    sql = f'CREATE TABLE IF NOT EXISTS sales ({", ".join(columns)});'
    conn.execute(sql)
    conn.commit()


def normalize_header(h):
    return ''.join(word.capitalize() for word in h.strip().split())


conn = sqlite3.connect("../data/sales.db")

with open('../data/Warehouse_and_Retail_Sales.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    normalized_headers = [normalize_header(h) for h in headers]
    create_table(conn, normalized_headers)
    quoted_headers = ', '.join(normalized_headers)
    for row in reader:
        placeholders = ','.join(['?'] * len(row))
        sql = f'INSERT INTO sales ({quoted_headers}) VALUES ({placeholders})'
        conn.execute(sql, row)
    conn.commit()

conn.close()