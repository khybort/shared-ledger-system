from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "postgres"
    DB_NAME: str = "ledger_db"
    DB_PASSWORD: str = "ledger"
    DB_PORT: int = 5432
    DB_USER: str = "ledger"
    FASTAPI_HOST: str = "localhost"
    FASTAPI_PORT: int = 8000
    DATABASE_URL: str = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    class Config:
        env_file = ".env"


settings = Settings()
