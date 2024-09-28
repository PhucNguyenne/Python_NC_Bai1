# Sử dụng image Python
FROM python:3.9

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép các file cần thiết vào container
COPY . /app

# Cài đặt các dependencies
RUN pip install -r requirements.txt

# Lệnh chạy ứng dụng
CMD ["python", "GUI.py"]
