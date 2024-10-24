# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
