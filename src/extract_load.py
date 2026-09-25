import os
import pandas as pd
from db_connection import get_engine

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
SCHEMA = "raw"

# Map tên file CSV -> tên bảng trong raw schema
FILES = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "category_translation",
}

def create_schema(engine):
    with engine.connect() as conn:
        conn.exec_driver_sql(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA};")
        conn.commit()

def load_csv_to_table(engine, filename, table_name):
    path = os.path.join(RAW_DIR, filename)
    if not os.path.exists(path):
        print(f"[SKIP] Không tìm thấy file: {filename}")
        return

    print(f"[LOAD] {filename} -> {SCHEMA}.{table_name}")
    df = pd.read_csv(path)
    df.to_sql(
        table_name,
        engine,
        schema=SCHEMA,
        if_exists="replace",   # replace = ghi đè mỗi lần chạy, phù hợp giai đoạn dev
        index=False,
    )
    print(f"[OK] {table_name}: {len(df)} dòng")

def main():
    engine = get_engine()
    create_schema(engine)
    for filename, table_name in FILES.items():
        load_csv_to_table(engine, filename, table_name)
    print("Hoàn tất extract & load vào raw zone.")

if __name__ == "__main__":
    main()