import logging
import os
from datetime import datetime


class Logger:
    """Custom logger for the framework"""

    @staticmethod
    def get_logger(name):
        """
        Create and return a logger instance

        Args:
            name (str): Name for the logger

        Returns:
            logging.Logger: Configured logger instance
        """
        # Create logs directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Configure logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Create file handler with timestamp in filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_handler = logging.FileHandler(f"logs/test_run_{timestamp}.log")
        file_handler.setLevel(logging.INFO)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger