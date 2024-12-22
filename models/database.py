# models/database.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime

# Database URL
DATABASE_URL = "sqlite:///./trading_signals.db"  # Replace with PostgreSQL in production

# Initialize DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Model for storing trained LSTM models
class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True, index=True)
    asset_pair = Column(String, index=True)
    timeframe = Column(String)
    model_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Model for storing predictions and signals
class Signal(Base):
    __tablename__ = "signals"
    id = Column(Integer, primary_key=True, index=True)
    asset_pair = Column(String, index=True)
    timeframe = Column(String)
    prediction = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


# Create Tables
def init_db():
    Base.metadata.create_all(bind=engine)
