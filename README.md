## 📹 Sistema de Conteo de Personas con YOLOv8 y OpenCV

Este proyecto realiza el conteo de personas detectadas en un video, utilizando el modelo de detección de objetos **YOLOv8** junto con **OpenCV** para el procesamiento de imágenes y/o Videos.

### 🧱 Estructura actual

Backend
├── app/
│ ├── main.py ← Aquí está tu backend FastAPI
│ ├── detector.py ← Aquí está tu lógica con YOLO y threading
│ └── yolov8n.pt # Modelo YOLOv8 Nano (descargado automáticamente)

### 🧪 Tecnologías utilizadas

| Herramienta      |  (detector.py)            |
|------------------|----------------------------------------|
| Python 3.10+     | Lenguaje de programación               |
| OpenCV (`cv2`)   | Lectura y visualización de video       |
| Ultralytics (`yolov8`) | Detección de personas con YOLOv8 |
| time (builtin)   | Temporizador para control de impresión |


| Herramienta      |  (main.py)   |
|------------------|---------------------------|
| FastAPI    | para la API REST.               |
| Uvicorn   | para ejecutar el servidor.       |

### ▶️ Cómo ejecutar

1. Instala los paquetes necesarios:

bash detector.py
'pip install ultralytics opencv-python'

bash main.py
'pip install fastapi uvicorn'