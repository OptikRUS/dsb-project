from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import Field, field_validator


class BotSettings(BaseSettings):
    """
    Настройки бота
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="BOT_"
    )
    bot_token: str = Field(alias="BOT_TOKEN")


bot_settings = BotSettings()


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="DATABASE_"
    )
    user: str
    password: str
    host: str = "localhost"
    name: str
    port: str


class DataBaseConnections(BaseSettings):
    default: str = Field("postgres://{user}:{password}@{host}:{port}/{name}")

    @field_validator("default")
    def generate_db_url(cls, db_url: str):
        return db_url.format(**PostgresSettings().model_dump())


class TortoiseSettings(BaseSettings):
    generate_schemas: bool = Field(True, env="TORTOISE_GENERATE_SCHEMAS")
    add_exception_handlers: bool = Field(True, env="DATABASE_EXCEPTION_HANDLERS")


class Settings(BaseSettings):
    BOT: BotSettings = BotSettings()
    DATABASE: DataBaseConnections = DataBaseConnections()
    TORTOISE: TortoiseSettings = TortoiseSettings()


settings = Settings()



