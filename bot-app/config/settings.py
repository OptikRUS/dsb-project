from pydantic_settings import SettingsConfigDict

from .base import AdvancedSettings


class BotSettings(AdvancedSettings):
    """
    Настройки бота
    """
    model_config = SettingsConfigDict(env_prefix='bot_')
