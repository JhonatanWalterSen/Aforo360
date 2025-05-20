import os                  # Módulo para manejar rutas del sistema operativo
import cv2                 # OpenCV, para manejo de video e imágenes
import time                # Módulo para medir tiempo (temporizadores)
from ultralytics import YOLO  # Importa YOLOv8 desde Ultralytics para detección de objetos

# Cargar el modelo YOLOv8 preentrenado (versión ligera)
model = YOLO("yolov8n.pt")  # También puedes usar 'yolov8s.pt' para más precisión

# Obtener la ruta absoluta del archivo actual (main.py)
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Unir la ruta con el nombre del archivo de video
video_path = os.path.join(ruta_actual, '../assets/video_cafeteria.mp4')

# Intentar abrir el video
cap = cv2.VideoCapture(video_path)

# Verificar si el video se abrió correctamente
if not cap.isOpened():
    print("❌ Error: No se pudo abrir el video.")
    print("Ruta usada:", video_path)
    exit()  # Terminar el programa si falla

# Guardar el tiempo inicial (para control de impresión cada cierto tiempo)
last_time = time.time()

# Bucle para leer y procesar el video fotograma por fotograma
while True:
    ret, frame = cap.read()  # Leer un fotograma

    if not ret:
        print("✅ Fin del video.")  # Si no se pudo leer (fin del video), salir del bucle
        break

    # Ejecutar el modelo YOLO en el fotograma actual, solo detectando personas (clase 0)
    results = model(frame, classes=[0], verbose=False)

    # Obtener las cajas detectadas del primer resultado
    detections = results[0].boxes

    # Contar cuántas personas fueron detectadas
    count = len(detections)

    # Obtener el tiempo actual
    current_time = time.time()

    # Si ha pasado al menos 2 segundos desde la última impresión
    if current_time - last_time >= 2:
        print(f"⏱️ {int(current_time - last_time)}s → 👥 Personas detectadas: {count}")
        last_time = current_time  # Reiniciar el temporizador

    # Dibujar las cajas de detección sobre el fotograma
    annotated_frame = results[0].plot()

    # Mostrar el video con anotaciones en una ventana llamada "Detección de personas"
    cv2.imshow("Detección de personas", annotated_frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el recurso del video y cerrar ventanas al finalizar
cap.release()
cv2.destroyAllWindows()
