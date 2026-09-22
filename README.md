# E-commerce Data Pipeline (Olist Dataset)

Portfolio project: xây dựng data pipeline và data warehouse hoàn chỉnh từ dữ liệu thô của Olist (Brazilian E-commerce), phục vụ phân tích doanh thu, vận chuyển và hành vi khách hàng.

## Kiến trúc
Raw CSV (Olist) --> Extract (Python) --> Raw Zone (Postgres)
|
v
Transform (dbt: staging -> marts)
|
v
Star Schema (Postgres DWH)
|
v
Dashboard (Metabase)

Orchestration: Apache Airflow (chạy toàn bộ pipeline theo lịch)

## Tech Stack

- **Extract/Load**: Python (pandas, psycopg2)
- **Storage**: PostgreSQL (Docker)
- **Transform**: dbt-core
- **Orchestration**: Apache Airflow
- **Visualization**: Metabase
- **Modeling approach**: Kimball Star Schema

## Cấu trúc thư mục
├── data/
│ ├── raw/ # Dữ liệu CSV gốc (không commit)
│ └── processed/ # Dữ liệu trung gian nếu cần
├── src/ # Script Python cho extract/load
├── dbt_project/ # dbt models (staging, marts)
├── dags/ # Airflow DAGs
├── docker-compose.yml
├── requirements.md # Câu hỏi phân tích & yêu cầu dự án
└── README.md


## Cách chạy (đang cập nhật theo tiến độ)

1. Clone repo, tạo virtual environment: `python -m venv venv`
2. Cài dependencies: `pip install -r src/requirements.txt`
3. Khởi động Postgres: `docker compose up -d`
4. *(Các bước tiếp theo sẽ bổ sung khi hoàn thành: chạy extract script, dbt run, Airflow DAG, mở Metabase)*

## Trạng thái

🚧 Đang trong giai đoạn setup (Git, Docker, Postgres). Xem tiến độ chi tiết trong commit history.

