# main.py - FastAPI Entry Point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import campaign, pitch, lead, market, persona, report, predict, compete, strategy, multimodal
from database import connect_db, close_db
import uvicorn

app = FastAPI(
    title="GenAI Sales & Marketing Intelligence API",
    description="AI-powered platform for sales and marketing teams using Groq LLM",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(campaign.router, prefix="/api/campaign", tags=["Campaign Generation"])
app.include_router(pitch.router, prefix="/api/pitch", tags=["Sales Pitch"])
app.include_router(lead.router, prefix="/api/lead", tags=["Lead Scoring"])
app.include_router(market.router, prefix="/api/market", tags=["Market Analysis"])
app.include_router(persona.router, prefix="/api/persona", tags=["Customer Persona"])
app.include_router(report.router, prefix="/api/report", tags=["Performance Reports"])
app.include_router(predict.router, prefix="/api/predict", tags=["Predictive Insights"])
app.include_router(compete.router, prefix="/api/compete", tags=["Competitive Intel"])
app.include_router(strategy.router, prefix="/api/strategy", tags=["Business Strategy"])
app.include_router(multimodal.router, prefix="/api/multimodal", tags=["Multimodal Content"])

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

@app.get("/")
async def root():
    return {"message": "GenAI Sales & Marketing Intelligence Platform is running 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
