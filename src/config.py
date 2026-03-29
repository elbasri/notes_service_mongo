from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    mongo_uri: str = Field(..., env='MONGO_URI')
    feature_flag_enabled: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
