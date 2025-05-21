from fastapi import FastAPI
from detector import iniciar_procesamiento, obtener_datos
import uvicorn

app = FastAPI()

iniciar_procesamiento()

@app.get("/conteo")
def obtener_conteo():
    return obtener_datos()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)