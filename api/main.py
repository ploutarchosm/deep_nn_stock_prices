# api/main.py
from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from api.routes import router as api_router
import uvicorn
from models.database import init_db

app = FastAPI(title="Trading Signal API")

# Initialize database
init_db()

# Include routes
app.include_router(api_router)

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
