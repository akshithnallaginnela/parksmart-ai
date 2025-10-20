from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "ParkSmart AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./parksmart.db"
    SECRET_KEY: str = "change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MODEL_PATH: str = "./ml_models/"
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
