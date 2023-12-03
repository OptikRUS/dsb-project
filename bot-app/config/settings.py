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
