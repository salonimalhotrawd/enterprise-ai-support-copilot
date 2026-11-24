
"""
Title: Application Configuration Manager
Author: Saloni Malhotra
Date: 24-11-2026
Filename: settings.py

Description:
    Centralized configuration manager for Enterprise AI
    Support Copilot.

    Responsibilities:
    - Load environment variables from .env.
    - Read application configuration from config.json.
    - Validate configurations using Pydantic.
    - Support Google Gemini and OpenAI providers.
    - Provide centralized access to application settings.
"""

import json
import os

from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field, SecretStr


# ==================================================
# 1. PROJECT PATH CONFIGURATION
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_FILE = PROJECT_ROOT / "config" / "config.json"

ENV_FILE = PROJECT_ROOT / ".env"


# ==================================================
# 2. LOAD ENVIRONMENT VARIABLES
# ==================================================

load_dotenv(dotenv_path=ENV_FILE)


# ==================================================
# 3. LLM CONFIGURATION MODELS
# ==================================================

class LLMModels(BaseModel):
    """Supported models for each LLM provider."""

    google: str

    openai: str


class LLMConfig(BaseModel):
    """Configuration for LLM providers."""

    provider: Literal["google", "openai"]

    models: LLMModels

    temperature: float = Field(ge=0, le=2)


# ==================================================
# 4. EMBEDDING CONFIGURATION
# ==================================================

class EmbeddingConfig(BaseModel):
    """Configuration for embedding generation."""

    provider: Literal["sentence-transformers"]

    model: str


# ==================================================
# 5. RAG CONFIGURATION
# ==================================================

class RAGConfig(BaseModel):
    """Configuration for the RAG pipeline."""

    chunk_size: int = Field(gt=0)

    chunk_overlap: int = Field(ge=0)

    retrieval_k: int = Field(gt=0)


# ==================================================
# 6. VECTOR DATABASE CONFIGURATION
# ==================================================

class VectorStoreConfig(BaseModel):
    """Configuration for ChromaDB."""

    provider: Literal["chroma"]

    persist_directory: str

    collection_name: str


# ==================================================
# 7. DATABASE CONFIGURATION
# ==================================================

class DatabaseConfig(BaseModel):
    """Configuration for SQLite database."""

    type: Literal["sqlite"]

    path: str


# ==================================================
# 8. APPLICATION CONFIGURATION
# ==================================================

class ApplicationConfig(BaseModel):
    """General application configuration."""

    name: str

    environment: Literal["development", "production"]

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


# ==================================================
# 9. MAIN APPLICATION CONFIGURATION
# ==================================================

class AppConfig(BaseModel):
    """Combines all application configurations."""

    llm: LLMConfig

    embeddings: EmbeddingConfig

    rag: RAGConfig

    vector_store: VectorStoreConfig

    database: DatabaseConfig

    application: ApplicationConfig


# ==================================================
# 10. SETTINGS MODEL
# ==================================================

class Settings(BaseModel):
    """Stores validated application settings and secrets."""

    app: AppConfig

    google_api_key: SecretStr | None = None

    openai_api_key: SecretStr | None = None


# ==================================================
# 11. LOAD APPLICATION SETTINGS
# ==================================================

def load_settings() -> Settings:
    """
    Load application configuration from config.json
    and API credentials from .env.

    Returns:
        Settings: Validated application settings.

    Raises:
        FileNotFoundError: If config.json is missing.
        ValueError: If JSON configuration is invalid.
    """

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_FILE}"
        )

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config_data = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON configuration: {error}"
        ) from error

    settings_data = {
        "app": config_data,
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "openai_api_key": os.getenv("OPENAI_API_KEY")
    }

    return Settings.model_validate(settings_data)


# ==================================================
# 12. INITIALIZE APPLICATION SETTINGS
# ==================================================

settings = load_settings()


# ==================================================
# 13. GET SELECTED LLM API KEY
# ==================================================

def get_llm_api_key() -> str:
    """
    Retrieve the API key for the selected LLM provider.

    Returns:
        str: API key for the configured provider.

    Raises:
        RuntimeError: If the selected provider's key is missing.
    """

    provider = settings.app.llm.provider

    api_keys = {
        "google": settings.google_api_key,
        "openai": settings.openai_api_key
    }

    api_key = api_keys[provider]

    if api_key is None or not api_key.get_secret_value().strip():

        raise RuntimeError(
            f"{provider} API key is missing. "
            f"Please configure it in your .env file."
        )

    return api_key.get_secret_value()


# ==================================================
# 14. GET SELECTED LLM MODEL
# ==================================================

def get_llm_model() -> str:
    """
    Retrieve the model name for the selected provider.

    Returns:
        str: Configured LLM model name.
    """

    llm_config = settings.app.llm

    return getattr(
        llm_config.models,
        llm_config.provider
    )


# ==================================================
# 15. GET APPLICATION CONFIGURATION
# ==================================================

def get_app_config() -> AppConfig:
    """
    Return the complete validated application configuration.

    Returns:
        AppConfig: Application configuration.
    """

    return settings.app
