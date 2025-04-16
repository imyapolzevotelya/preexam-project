# Python bazaviy image
FROM python:3.10-slim

# Ishchi katalog
WORKDIR /app

# Talablar ro'yxatini nusxalaymiz
COPY requirement.txt .

# Kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirement.txt

# Loyihani ko'chiramiz
COPY . .

# Aiogram botni ishga tushirish
CMD ["python", "pre-exam-project.py"]
