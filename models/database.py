# models/database.py
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")  # e.g., "mongodb+srv://username:password@cluster.mongodb.net/dbname"
DB_NAME = os.getenv("DB_NAME", "trading_signals")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
models_collection = db["models"]
signals_collection = db["signals"]

# Model Schema
def insert_model(asset_pair, timeframe, model_path):
    model = {
        "asset_pair": asset_pair,
        "timeframe": timeframe,
        "model_path": model_path,
        "created_at": datetime.utcnow()
    }
    result = models_collection.insert_one(model)
    return str(result.inserted_id)


# Signal Schema
def insert_signal(asset_pair, timeframe, prediction, stop_loss, take_profit):
    signal = {
        "asset_pair": asset_pair,
        "timeframe": timeframe,
        "prediction": prediction,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "created_at": datetime.utcnow()
    }
    result = signals_collection.insert_one(signal)
    return str(result.inserted_id)


def get_signals(asset_pair, timeframe):
    signals = signals_collection.find({"asset_pair": asset_pair, "timeframe": timeframe})
    return list(signals)

