from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from app.api import auth, parking, booking, prediction, payment
from app.database import engine, Base
from app.config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ParkSmart AI API",
    description="AI-Powered Predictive Parking Management System",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.APP_VERSION}

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(parking.router, prefix="/api/parking", tags=["Parking"])
app.include_router(booking.router, prefix="/api/booking", tags=["Booking"])
app.include_router(prediction.router, prefix="/api/prediction", tags=["Prediction"])
app.include_router(payment.router, prefix="/api/payment", tags=["Payment"])

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal server error", "detail": str(exc)})

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
