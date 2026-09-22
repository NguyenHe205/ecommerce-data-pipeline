# Yêu cầu dự án & Câu hỏi phân tích

## Mục tiêu

Xây dựng một data warehouse theo mô hình Star Schema (Kimball) từ dữ liệu Olist E-commerce, giúp trả lời các câu hỏi kinh doanh dưới đây, đồng thời làm nền tảng portfolio thể hiện kỹ năng ETL/ELT, data modeling và orchestration.

## Câu hỏi phân tích cần trả lời

1. Doanh thu thay đổi thế nào theo tháng và theo bang (state) tại Brazil?
2. Thời gian giao hàng trung bình theo từng vùng là bao nhiêu, và nó có tương quan với điểm đánh giá (review score) của khách hàng không?
3. Top 10 category sản phẩm mang lại doanh thu cao nhất là gì?
4. Phương thức thanh toán nào được sử dụng phổ biến nhất, và có khác biệt gì giữa các vùng không?
5. *(Có thể bổ sung thêm khi thiết kế fact/dimension table ở Tuần 3)*

## Nguồn dữ liệu

- Olist Brazilian E-commerce Public Dataset (Kaggle), gồm các bảng: orders, order_items, products, customers, sellers, payments, reviews, geolocation.

## Yêu cầu kỹ thuật

- **Extract**: Đọc dữ liệu CSV thô, nạp vào raw zone trong Postgres, giữ nguyên cấu trúc gốc.
- **Transform**: Dùng dbt để làm sạch (staging layer) và mô hình hóa thành star schema (marts layer) — có fact table và các dimension table tương ứng với câu hỏi phân tích ở trên.
- **Data quality**: Áp dụng dbt tests (not_null, unique, relationships) cho các bảng quan trọng.
- **Orchestration**: Airflow DAG chạy tuần tự extract → load → dbt run → dbt test, có lịch chạy cố định.
- **Visualization**: Dashboard Metabase hiển thị kết quả cho từng câu hỏi phân tích.

## Ngoài phạm vi (Out of scope)

- Xử lý streaming/real-time.
- Triển khai lên cloud (dự án chạy local qua Docker).
- Xử lý dữ liệu ảnh/geolocation chi tiết (bảng geolocation có thể bỏ qua nếu không cần thiết cho câu hỏi phân tích).