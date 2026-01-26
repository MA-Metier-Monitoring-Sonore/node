"""Logging utilities for the application."""

import datetime
from src.enums.log_level import LogLevel

class Logger:
    """Simple logger service."""

    @staticmethod
    def log(level: LogLevel, message: str):
        """Log message with level."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}][{level.value}] {message}")

    @staticmethod
    def debug(message: str):
        """Log debug message."""
        Logger.log(LogLevel.DEBUG, message)

    @staticmethod
    def info(message: str):
        """Log info message."""
        Logger.log(LogLevel.INFO, message)

    @staticmethod
    def warning(message: str):
        """Log warning message."""
        Logger.log(LogLevel.WARNING, message)

    @staticmethod
    def error(message: str):
        """Log error message."""
        Logger.log(LogLevel.ERROR, message)

    @staticmethod
    def critical(message: str):
        """Log critical message."""
        Logger.log(LogLevel.CRITICAL, message)
