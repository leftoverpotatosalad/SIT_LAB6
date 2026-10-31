FROM python:3.12-slim
WORKDIR /app
COPY product.py inventory.py inventory_manager.py inventory.json ./
CMD ["python", "-u", "/app/inventory_manager.py"]
