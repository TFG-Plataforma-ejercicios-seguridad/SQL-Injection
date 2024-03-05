# Imagen base
FROM python:3.10

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalación de dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia de archivos de la aplicación
COPY . /app/

# Comandos para ejecutar migraciones, recopilación de archivos estáticos, etc.
# Ejemplo:
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Comando de arranque del servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ejercicioSQL.wsgi:application"]
