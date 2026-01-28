from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

@app.get("/weather")
async def get_weather():
    return {"weather": "sunny",
            "temperature": "25°C"
            }
