import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    BASE_URL: str = "https://rahulshettyacademy.com/loginpagePractise/"
    IMPLICIT_WAIT: int = 5
    BROWSER: str = "chrome"

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

def load_settings(env: str = "dev") -> Settings:
    env_file = f".env.{env}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(
            f"[Config] Missing env file: '{env_file}'. "
            f"Make sure '.env.{env}' exists in your project root."
        )
    class DynamicSettings(Settings):
        model_config = SettingsConfigDict(
            env_file=env_file,
            env_file_encoding="utf-8",
            case_sensitive=False,
            extra="ignore",
        )
    return DynamicSettings()