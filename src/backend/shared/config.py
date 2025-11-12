from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


cwd = Path.cwd()
if cwd.name == "src":
    cwd = cwd / "backend"
    dotenv_path = cwd / ".env"
else:
    dotenv_path = cwd / ".env"
if not list(cwd.glob(".env")):
    cwd = cwd.parent
    dotenv_path = cwd / ".env"

    if not list(cwd.glob(".env")):
        cwd = cwd.parent
        dotenv_path = cwd / ".env"


class ProjectSettings(BaseSettings):
    project_name: str = "TerminiAlert"
    log_level: str = "DEBUG"
    frontend_base_url: str = "http://localhost:3003"
    backend_base_url: str = "http://localhost:8008"
    backend_prefix: str = ""


class PostgresSettings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int = 5433
    db_database: str

    echo_sql: bool = False

    def create_engine_url(self, async_driver: bool = False) -> str:
        """Generate engine url using pydantic_settings class

        Args:
            settings (Settings): Settings class

        Returns:
            str
        """

        return f"postgresql{"+asyncpg" if async_driver else ""}://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"


class ScraperSettings(BaseSettings):
    scraper_allowed_schemas: list[str] = ["https"]

    manager_wait_time_minutes: int = 5  # How often to run manager iteration (in minutes)
    retry_limit: int = 20  # How many pages to enumerate for each reminder


class NotificationSettings(BaseSettings):
    mailjet_api_key: str
    mailjet_api_secret: str
    from_email: str = "termini@pesko.si"
    from_name: str = "Termini Alert"


class Settings(ProjectSettings, PostgresSettings, ScraperSettings, NotificationSettings):
    model_config = SettingsConfigDict(
        env_file=str(dotenv_path), env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
