# 📹 Sistema de Conteo de Personas con YOLOv8 y OpenCV

Este proyecto realiza el conteo de personas detectadas en un video, utilizando el modelo de detección de objetos **YOLOv8** junto con **OpenCV** para el procesamiento de imágenes y/o Videos.

## 🧱 Estructura actual

Backend
├── app/
│ ├── main.py # Script principal con detección de personas
│ └── yolov8n.pt # Modelo YOLOv8 Nano (descargado automáticamente)

## 🧪 Tecnologías utilizadas

| Herramienta      | Uso principal (main.py)                |
|------------------|----------------------------------------|
| Python 3.10+     | Lenguaje de programación               |
| OpenCV (`cv2`)   | Lectura y visualización de video       |
| Ultralytics (`yolov8`) | Detección de personas con YOLOv8 |
| time (builtin)   | Temporizador para control de impresión |


## ▶️ Cómo ejecutar

1. Instala los paquetes necesarios:

bash main.py
'pip install ultralytics opencv-python'