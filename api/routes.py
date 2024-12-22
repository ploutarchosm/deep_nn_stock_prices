# api/routes.py
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import os
import pandas as pd
from models.database import SessionLocal, Model, Signal
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter()


UPLOAD_FOLDER = "./data/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Endpoint to upload CSV data
@router.post("/upload")
async def upload_file(file: UploadFile):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filepath, "wb") as f:
            f.write(await file.read())
        return JSONResponse(content={"message": "File uploaded successfully!", "path": filepath})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Endpoint to configure asset and timeframe
@router.post("/configure")
async def configure_asset(asset_pair: str = Form(...), timeframe: str = Form(...)):
    # Store configuration (can be extended with database storage)
    config = {"asset_pair": asset_pair, "timeframe": timeframe}
    return JSONResponse(content={"message": "Configuration saved!", "config": config})
