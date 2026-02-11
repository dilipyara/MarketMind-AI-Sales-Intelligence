# database.py - In-Memory Storage (No MongoDB Required)
from collections import defaultdict

_store = defaultdict(list)

async def connect_db():
    print("✅ Using in-memory storage (no MongoDB required)")

async def close_db():
    print("🔌 Server stopped")

def get_collection(name: str):
    return _store[name]
