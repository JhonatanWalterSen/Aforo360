import os
import cv2
import time
import threading
from ultralytics import YOLO

# Inicializar modelo
model = YOLO("yolov8n.pt")

# Ruta del video
ruta_actual = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(ruta_actual, '../assets/video_cafeteria.mp4')
cap = cv2.VideoCapture(video_path)

# Variables globales
conteo_actual = 0
estado_video = "procesando"

def procesar_video():
    global conteo_actual, estado_video
    anterior_conteo = -1  # Valor inicial imposible para forzar primer cambio

    while True:
        ret, frame = cap.read()
        if not ret:
            estado_video = "fin"
            print("✅ Fin del video.")
            break

        # Detectar personas
        results = model(frame, classes=[0], verbose=False)
        detections = results[0].boxes
        nuevo_conteo = len(detections)

        # Solo actualizar si el conteo cambió
        if nuevo_conteo != anterior_conteo:
            conteo_actual = nuevo_conteo
            anterior_conteo = nuevo_conteo
            print(f"👥 Cambio detectado → Personas ahora: {conteo_actual}")

        # Espera corta para evitar saturar la CPU
        time.sleep(0.1)

# Hilo para correr en segundo plano
def iniciar_procesamiento():
    hilo = threading.Thread(target=procesar_video, daemon=True)
    hilo.start()

# Función que lee el conteo actual desde el backend
def obtener_datos():
    return {
        "estado": estado_video,
        "personas": conteo_actual
    }