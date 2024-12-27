# api/main.py
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from models.database import db  # Ensures MongoDB connection is ready

# Load environment variables
load_dotenv()

app = FastAPI(title="Trading Signal API")

@app.get("/")
def root():
    return {"message": "Trading Signal API is running"}

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
